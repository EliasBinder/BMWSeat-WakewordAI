import numpy as np

from keras import models


from src.helpers.audio_helper import record_audio, terminate
from src.helpers.tf_helper import preprocess_audiobuffer

# !! Modify this in the correct order
commands = ['stop']

loaded_model = models.load_model("../../saved_model")

def predict_mic():
    audio = record_audio()
    spec = preprocess_audiobuffer(audio)
    prediction = loaded_model(spec)
    label_pred = np.argmax(prediction, axis=1)
    command = commands[label_pred[0]]
    print("Predicted label:", command)
    return command

if __name__ == "__main__":
    while True:
        command = predict_mic()
        """if command == "stop":
            terminate()
            break"""