# Used the following demo: https://github.com/iver56/audiomentations/blob/main/demo/demo.py

import glob, os
from audiomentations.core.audio_loading_utils import load_sound_file

if __name__ == "__main__":
    os.chdir("resources/commands")

    for file in glob.glob("*.wav"):
        # load sound file
        samples, sampelRate = load_sound_file(file)
        if len(samples.shape) == 2 and samples.shape[0] > samples.shape[1]:
            samples = samples.transpose()
        
        print(
            "Transforming {} with shape {}".format(
                file.name, str(samples.shape)
            )
        )
        
        
        # put background noise to file

        for i in range(1, 10):
            
                    

