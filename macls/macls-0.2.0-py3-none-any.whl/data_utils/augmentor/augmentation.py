"""Contains the data augmentation pipeline."""

import json
import os
import random

from macls.data_utils.augmentor.volume_perturb import VolumePerturbAugmentor
from macls.data_utils.augmentor.shift_perturb import ShiftPerturbAugmentor
from macls.data_utils.augmentor.speed_perturb import SpeedPerturbAugmentor
from macls.data_utils.augmentor.noise_perturb import NoisePerturbAugmentor
from macls.data_utils.augmentor.spec_augment import SpecAugmentor
from macls.data_utils.augmentor.spec_sub import SpecSubAugmentor
from macls.data_utils.augmentor.resample import ResampleAugmentor
from macls.utils.logger import setup_logger

logger = setup_logger(__name__)


class AugmentationPipeline(object):
    """Build a pre-processing pipeline with various augmentation models.Such a
    data augmentation pipeline is oftern leveraged to augment the training
    samples to make the model invariant to certain types of perturbations in the
    real world, improving model's generalization ability.

    The pipeline is built according the the augmentation configuration in json
    string, e.g.
    
    .. code-block::
    [
      {
        "type": "noise",
        "params": {
          "min_snr_dB": 10,
          "max_snr_dB": 50,
          "noise_manifest_path": "dataset/manifest.noise"
        },
        "prob": 0.5
      },
      {
        "type": "speed",
        "params": {
          "min_speed_rate": 0.9,
          "max_speed_rate": 1.1,
          "num_rates": 3
        },
        "prob": 1.0
      },
      {
        "type": "shift",
        "params": {
          "min_shift_ms": -5,
          "max_shift_ms": 5
        },
        "prob": 1.0
      },
      {
        "type": "volume",
        "params": {
          "min_gain_dBFS": -15,
          "max_gain_dBFS": 15
        },
        "prob": 1.0
      },
      {
        "type": "specaug",
        "params": {
          "W": 0,
          "warp_mode": "PIL",
          "F": 10,
          "n_freq_masks": 2,
          "T": 50,
          "n_time_masks": 2,
          "p": 1.0,
          "adaptive_number_ratio": 0,
          "adaptive_size_ratio": 0,
          "max_n_time_masks": 20,
          "replace_with_zero": true
        },
        "prob": 1.0
      }
    ]
    This augmentation configuration inserts two augmentation models
    into the pipeline, with one is VolumePerturbAugmentor and the other
    SpeedPerturbAugmentor. "prob" indicates the probability of the current
    augmentor to take effect. If "prob" is zero, the augmentor does not take
    effect.

    :param augmentation_config: Augmentation configuration in json string.
    :type augmentation_config: str
    """

    def __init__(self, augmentation_config):
        self._augmentors, self._rates = self._parse_pipeline_from(augmentation_config, aug_type='audio')
        self._spec_augmentors, self._spec_rates = self._parse_pipeline_from(augmentation_config, aug_type='feature')

    def transform_audio(self, audio_segment):
        """Run the pre-processing pipeline for data augmentation.

        Note that this is an in-place transformation.
        
        :param audio_segment: Audio segment to process.
        :type audio_segment: AudioSegmenet|SpeechSegment
        """
        for augmentor, rate in zip(self._augmentors, self._rates):
            if random.random() < rate:
                augmentor.transform_audio(audio_segment)

    def transform_feature(self, spec_segment):
        """spectrogram augmentation.

        Args:
            spec_segment (np.ndarray): audio feature, (D, T).
        """
        for augmentor, rate in zip(self._spec_augmentors, self._spec_rates):
            if random.random() < rate:
                spec_segment = augmentor.transform_feature(spec_segment)
        return spec_segment

    def _parse_pipeline_from(self, config_json, aug_type):
        """Parse the config json to build a augmentation pipelien."""
        try:
            configs = []
            configs_temp = json.loads(config_json)
            for config in configs_temp:
                if config['aug_type'] != aug_type: continue
                logger.info('数据增强配置：%s' % config)
                configs.append(config)
            augmentors = [self._get_augmentor(config["type"], config["params"]) for config in configs]
            rates = [config["prob"] for config in configs]
        except Exception as e:
            raise ValueError("Failed to parse the augmentation config json: %s" % str(e))
        return augmentors, rates

    def _get_augmentor(self, augmentor_type, params):
        """Return an augmentation model by the type name, and pass in params."""
        if augmentor_type == "volume":
            return VolumePerturbAugmentor(**params)
        elif augmentor_type == "shift":
            return ShiftPerturbAugmentor(**params)
        elif augmentor_type == "speed":
            return SpeedPerturbAugmentor(**params)
        elif augmentor_type == "resample":
            return ResampleAugmentor(**params)
        elif augmentor_type == "noise":
            return NoisePerturbAugmentor(**params)
        elif augmentor_type == "specaug":
            return SpecAugmentor(**params)
        elif augmentor_type == "specsub":
            return SpecSubAugmentor(**params)
        else:
            raise ValueError("Unknown augmentor type [%s]." % augmentor_type)
