import logging
import json
import numpy as np
import deepmd
from typing import Callable
from typing import Tuple, List, Dict, Any
from functools import lru_cache
from scipy.special import comb
from deepmd.env import tf
from deepmd.env import op_module
from deepmd.common import ACTIVATION_FN_DICT
from deepmd.utils.graph import get_tensor_by_name
from deepmd.utils.errors import GraphWithoutTensorError
from deepmd.descriptor import Descriptor

log = logging.getLogger(__name__)


def replace_model_params_with_pretrained_model(jdata: Dict[str, Any], pretrained_model: str):
    """Replace the model params in input script according to pretrained model.

    Parameters
    ----------
    jdata: Dict[str, Any]
        input script
    pretrained_model: str
        filename of the pretrained model
    """
    # Get the input script from the pretrained model
    try:
        t_jdata = get_tensor_by_name(pretrained_model, 'train_attr/training_script')
    except GraphWithoutTensorError as e:
        raise RuntimeError(
            "The input frozen pretrained model: %s has no training script, "
            "which is not supported to perform finetuning. "
            "Please use the model pretrained with v2.1.5 or higher version of DeePMD-kit." % input
        ) from e
    pretrained_jdata = json.loads(t_jdata)

    # Check the model type
    assert pretrained_jdata['model']['descriptor']['type'] in ['se_atten'] and \
           pretrained_jdata['model']['fitting_net']['type'] in ['ener'], \
           "The finetune process only supports models pretrained with 'se_atten' descriptor and 'ener' fitting_net!"

    # Check the type map
    pretrained_type_map = pretrained_jdata['model']['type_map']
    cur_type_map = jdata['model'].get("type_map", [])
    out_line_type = []
    for i in cur_type_map:
        if i not in pretrained_type_map:
            out_line_type.append(i)
    assert not out_line_type, "{} type(s) not contained in the pretrained model! " \
                              "Please choose another suitable one.".format(str(out_line_type))
    if cur_type_map != pretrained_type_map:
        log.info("Change the type_map from {} to {}.".format(str(cur_type_map), str(pretrained_type_map)))
        jdata['model']['type_map'] = pretrained_type_map

    # Change model configurations
    log.info("Change the model configurations according to the pretrained one...")
    for config_key in ['type_embedding', 'descriptor', 'fitting_net']:
        if config_key not in jdata['model'].keys() and config_key in pretrained_jdata['model'].keys():
            log.info("Add the '{}' from pretrained model: {}.".format(
                config_key, str(pretrained_jdata['model'][config_key])))
            jdata['model'][config_key] = pretrained_jdata['model'][config_key]
        elif config_key == 'type_embedding' and \
                config_key in jdata['model'].keys() and config_key not in pretrained_jdata['model'].keys():
            # 'type_embedding' can be omitted using 'se_atten' descriptor, and the activation_function will be None.
            cur_para = jdata['model'].pop(config_key)
            if 'trainable' in cur_para and not cur_para['trainable']:
                jdata['model'][config_key] = {'trainable': False, 'activation_function': 'None'}
                log.info("The type_embeddings from pretrained model will be frozen.")
        elif config_key in jdata['model'].keys() and config_key in pretrained_jdata['model'].keys() and \
                jdata['model'][config_key] != pretrained_jdata['model'][config_key]:
            target_para = pretrained_jdata['model'][config_key]
            cur_para = jdata['model'][config_key]
            # keep some params that are irrelevant to model structures (need to discuss) TODO
            if 'trainable' in cur_para.keys():
                target_para['trainable'] = cur_para['trainable']
            log.info("Change the '{}' from {} to {}.".format(config_key, str(cur_para), str(target_para)))
            jdata['model'][config_key] = target_para

    return jdata, cur_type_map
