import numpy as np
from typing import Tuple, List

from deepmd.env import tf
from deepmd.env import global_cvt_2_ener_float, MODEL_VERSION, GLOBAL_TF_FLOAT_PRECISION
from deepmd.env import op_module
from deepmd.utils.graph import load_graph_def
from .model import Model
from .model_stat import make_stat_input, merge_sys_stat

class TensorModel(Model) :
    """Tensor model.

    Parameters
    ----------
    tensor_name
            Name of the tensor.
    descrpt
            Descriptor
    fitting
            Fitting net
    typeebd
            Type embedding net
    type_map
            Mapping atom type to the name (str) of the type.
            For example `type_map[1]` gives the name of the type 1.
    data_stat_nbatch
            Number of frames used for data statistic
    data_stat_protect
            Protect parameter for atomic energy regression
    """
    def __init__ (
            self, 
            tensor_name : str,
            descrpt, 
            fitting,
            typeebd=None,
            type_map : List[str] = None,
            data_stat_nbatch : int = 10,
            data_stat_protect : float = 1e-2,
    )->None:
        """
        Constructor
        """
        self.model_type = tensor_name
        # descriptor
        self.descrpt = descrpt
        self.rcut = self.descrpt.get_rcut()
        self.ntypes = self.descrpt.get_ntypes()
        # fitting
        self.fitting = fitting
        # type embedding
        self.typeebd = typeebd
        # other params
        if type_map is None:
            self.type_map = []
        else:
            self.type_map = type_map
        self.data_stat_nbatch = data_stat_nbatch
        self.data_stat_protect = data_stat_protect
    
    def get_rcut (self) :
        return self.rcut

    def get_ntypes (self) :
        return self.ntypes

    def get_type_map (self) :
        return self.type_map

    def get_sel_type(self):
        return self.fitting.get_sel_type()

    def get_out_size (self) :
        return self.fitting.get_out_size()

    def data_stat(self, data):
        all_stat = make_stat_input(data, self.data_stat_nbatch, merge_sys = False)
        m_all_stat = merge_sys_stat(all_stat)        
        self._compute_input_stat (m_all_stat, protection = self.data_stat_protect)
        self._compute_output_stat(all_stat)

    def _compute_input_stat(self, all_stat, protection = 1e-2) :
        self.descrpt.compute_input_stats(all_stat['coord'],
                                         all_stat['box'],
                                         all_stat['type'],
                                         all_stat['natoms_vec'],
                                         all_stat['default_mesh'], 
                                         all_stat)
        if hasattr(self.fitting, 'compute_input_stats'):
            self.fitting.compute_input_stats(all_stat, protection = protection)

    def _compute_output_stat (self, all_stat) :
        if hasattr(self.fitting, 'compute_output_stats'):
            self.fitting.compute_output_stats(all_stat)

    def build (self, 
               coord_, 
               atype_,
               natoms,
               box, 
               mesh,
               input_dict,
               frz_model = None,         
               suffix = '', 
               reuse = None):

        if input_dict is None:
            input_dict = {}
        with tf.variable_scope('model_attr' + suffix, reuse = reuse) :
            t_tmap = tf.constant(' '.join(self.type_map), 
                                 name = 'tmap', 
                                 dtype = tf.string)
            t_st = tf.constant(self.get_sel_type(), 
                               name = 'sel_type',
                               dtype = tf.int32)
            t_mt = tf.constant(self.model_type, 
                               name = 'model_type', 
                               dtype = tf.string)
            t_ver = tf.constant(MODEL_VERSION,
                                name = 'model_version',
                                dtype = tf.string)
            t_od = tf.constant(self.get_out_size(), 
                               name = 'output_dim', 
                               dtype = tf.int32)

        natomsel = sum(natoms[2+type_i] for type_i in self.get_sel_type())
        nout = self.get_out_size()

        coord = tf.reshape(coord_, [-1, natoms[1] * 3])
        atype = tf.reshape(atype_, [-1, natoms[1]])
        input_dict['nframes'] = tf.shape(coord)[0]

        # type embedding if any
        if self.typeebd is not None:
            type_embedding = self.typeebd.build(
                self.ntypes,
                reuse=reuse,
                suffix=suffix,
            )
            input_dict['type_embedding'] = type_embedding
            input_dict['atype'] = atype_

        if frz_model == None:
            dout \
                = self.descrpt.build(coord_,
                                     atype_,
                                     natoms,
                                     box,
                                     mesh,
                                     input_dict,
                                     suffix = suffix,
                                     reuse = reuse)
            dout = tf.identity(dout, name='o_descriptor')
        else:
            tf.constant(self.rcut,
                name = 'descrpt_attr/rcut',
                dtype = GLOBAL_TF_FLOAT_PRECISION)
            tf.constant(self.ntypes,
                name = 'descrpt_attr/ntypes',
                dtype = tf.int32)
            feed_dict = self.descrpt.get_feed_dict(coord_, atype_, natoms, box, mesh)
            return_elements = [*self.descrpt.get_tensor_names(), 'o_descriptor:0']
            imported_tensors \
                = self._import_graph_def_from_frz_model(frz_model, feed_dict, return_elements)
            dout = imported_tensors[-1]
            self.descrpt.pass_tensors_from_frz_model(*imported_tensors[:-1])

        rot_mat = self.descrpt.get_rot_mat()
        rot_mat = tf.identity(rot_mat, name = 'o_rot_mat'+suffix)

        output = self.fitting.build (dout, 
                                     rot_mat,
                                     natoms,
                                     input_dict,
                                     reuse = reuse, 
                                     suffix = suffix)
        framesize = nout if "global" in self.model_type else natomsel * nout
        output = tf.reshape(output, [-1, framesize], name = 'o_' + self.model_type + suffix)

        model_dict = {self.model_type: output}

        if "global" not in self.model_type:
            gname = "global_"+self.model_type
            atom_out = tf.reshape(output, [-1, natomsel, nout])
            global_out = tf.reduce_sum(atom_out, axis=1)
            global_out = tf.reshape(global_out, [-1, nout], name="o_" + gname + suffix)
            
            out_cpnts = tf.split(atom_out, nout, axis=-1)
            force_cpnts = []
            virial_cpnts = []
            atom_virial_cpnts = []

            for out_i in out_cpnts:
                force_i, virial_i, atom_virial_i \
                    = self.descrpt.prod_force_virial(out_i, natoms)
                force_cpnts.append      (tf.reshape(force_i,       [-1, 3*natoms[1]]))
                virial_cpnts.append     (tf.reshape(virial_i,      [-1, 9]))
                atom_virial_cpnts.append(tf.reshape(atom_virial_i, [-1, 9*natoms[1]]))

            # [nframe x nout x (natom x 3)]
            force = tf.concat(force_cpnts, axis=1, name="o_force" + suffix)
            # [nframe x nout x 9]
            virial = tf.concat(virial_cpnts, axis=1, name="o_virial" + suffix)
            # [nframe x nout x (natom x 9)]
            atom_virial = tf.concat(atom_virial_cpnts, axis=1, name="o_atom_virial" + suffix)

            model_dict[gname] = global_out
            model_dict["force"] = force
            model_dict["virial"] = virial
            model_dict["atom_virial"] = atom_virial

        return model_dict

    def _import_graph_def_from_frz_model(self, frz_model, feed_dict, return_elements):
        graph, graph_def = load_graph_def(frz_model)
        return tf.import_graph_def(graph_def, input_map = feed_dict, return_elements = return_elements, name = "")

    def init_variables(self,
                       graph : tf.Graph,
                       graph_def : tf.GraphDef,
                       model_type : str = "original_model",
                       suffix : str = "",
    ) -> None:
        """
        Init the embedding net variables with the given frozen model

        Parameters
        ----------
        graph : tf.Graph
            The input frozen model graph
        graph_def : tf.GraphDef
            The input frozen model graph_def
        model_type : str
            the type of the model
        suffix : str
            suffix to name scope
        """
        if model_type == 'original_model':
            self.descrpt.init_variables(graph, graph_def, suffix=suffix)
            self.fitting.init_variables(graph, graph_def, suffix=suffix)
            tf.constant("original_model", name = 'model_type', dtype = tf.string)
        elif model_type == 'compressed_model':
            self.fitting.init_variables(graph, graph_def, suffix=suffix)
            tf.constant("compressed_model", name = 'model_type', dtype = tf.string)
        else:
            raise RuntimeError("Unknown model type %s" % model_type)


class WFCModel(TensorModel):
    def __init__(self, *args, **kwargs) -> None:
        TensorModel.__init__(self, 'wfc', *args, **kwargs)


class DipoleModel(TensorModel):
    def __init__(self, *args, **kwargs) -> None:
        TensorModel.__init__(self, 'dipole', *args, **kwargs)


class PolarModel(TensorModel):
    def __init__(self, *args, **kwargs) -> None:
        TensorModel.__init__(self, 'polar', *args, **kwargs)


class GlobalPolarModel(TensorModel):
    def __init__(self, *args, **kwargs) -> None:
        TensorModel.__init__(self, 'global_polar', *args, **kwargs)
