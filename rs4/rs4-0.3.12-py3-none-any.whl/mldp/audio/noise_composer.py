# Noise data from:
#    https://github.com/MycroftAI/Precise-Community-Data/blob/master/not-wake-words/noises/noises-20190814-elt.tar.gz

from . import feature
from glob import glob
import numpy as np
import os
from random import shuffle

class NoiseData:
    def __init__(self, noise_folder, sr = 16000):
        self.noise_data = [
            feature.load (file, sr) [0]
            for file in glob (os.path.join(noise_folder, '*.wav'))
        ]
        self.noise_data_id = 0
        self.noise_pos = 0
        self.repeat_count = 0

    def get_fresh_noise(self, n) -> np.ndarray:
        noise_audio = np.empty(0)
        while len(noise_audio) < n:
            noise_source = self.noise_data[self.noise_data_id]
            noise_chunk = noise_source[self.noise_pos:self.noise_pos + n - len(noise_audio)]
            self.noise_pos += n - len(noise_audio)
            if self.noise_pos >= len(noise_source):
                self.noise_pos = 0
                self.noise_data_id += 1
                if self.noise_data_id >= len(self.noise_data):
                    self.noise_data_id = 0
                    shuffle (self.noise_data)
                    self.repeat_count += 1
                    if self.repeat_count == 100:
                        print ('Warning: Repeating noise 100+ times. Add more to prevent '
                              'overfitting.')
            noise_audio = np.concatenate([noise_audio, noise_chunk])
        return noise_audio

    def compose (self, audio, noise_ratio) -> np.ndarray:
        noise_data = self.get_fresh_noise(len(audio))
        audio_volume = feature.get_volume (audio)
        noise_volume = feature.get_volume (noise_data)        
        adjusted_noise = audio_volume * noise_data / noise_volume
        return noise_ratio * adjusted_noise + (1.0 - noise_ratio) * audio

def create (noise_folder, sr = 16000):
    return NoiseData (noise_folder, sr)
