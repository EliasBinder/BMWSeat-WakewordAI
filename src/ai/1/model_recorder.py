import sounddevice as sd
from scipy.io.wavfile import write

def record_background_sound(save_path, n_times=50):
    input("To start recording your background sounds press Enter: ")
    for i in range(n_times):
        fs = 44100
        seconds = 2

        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        sd.wait()
        write(save_path + str(i) + ".wav", fs, myrecording)
        print(f"Currently on {i+1}/{n_times}")


print("Recording the Background sounds:\n")
record_background_sound("resources/commands/undefined/", n_times=100)
