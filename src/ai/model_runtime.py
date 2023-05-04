import sounddevice as sd
from scipy.io.wavfile import write
import librosa
import numpy as np
from tensorflow.keras.models import load_model

from src.tcpClient.client import sendWakeCommand

fs = 44100
seconds = 2
filename = "prediction.wav"
class_names = ["Wake Word NOT Detected", "Wake Word Detected"]

model = load_model("saved_model/WWD.h5")


def start_prediction(event):
    while True:
        if not event.is_set():
            continue

        print("Say something...")
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()

        if not event.is_set():
            continue

        write(filename, fs, myrecording)

        audio, sample_rate = librosa.load(filename)
        mfcc = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfcc_processed = np.mean(mfcc.T, axis=0)

        prediction = model.predict(np.expand_dims(mfcc_processed, axis=0))

        if prediction[:, 0] < 0.95:
            print(f"Wake Word Detected for (STOP)")
            sendWakeCommand()
            print(prediction)

        else:
            print(f"Wake Word NOT Detected")
            print(prediction)