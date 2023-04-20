import os
import librosa.display
import numpy as np
import pandas as pd

all_data = []

data_path_dict = {
    0: ["resources/commands/undefined/" + file_path for file_path in os.listdir("resources/commands/undefined/")],
    1: ["resources/commands/hey_bmw/" + file_path for file_path in os.listdir("resources/commands/hey_bmw/")],
    2: ["resources/commands/stop/" + file_path for file_path in os.listdir("resources/commands/stop/")]
}

for class_label, list_of_files in data_path_dict.items():
    for single_file in list_of_files:
        audio, sample_rate = librosa.load(single_file)
        mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfcc_processed = np.mean(mfcc.T, axis=0)
        all_data.append([mfcc_processed, class_label])
    print(f"Info: Succesfully Preprocessed Class Label {class_label}")

df = pd.DataFrame(all_data, columns=["feature", "class_label"])

df.to_pickle("resources/audio_data.csv")
