import pyaudio


def start_recording():
    FRAMES_PER_BUFFER = 3200
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    p = pyaudio.PyAudio()

    # starts recording
    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER
    )

    stream.start_stream()
    return stream, p


def stop_recording(stream, p):
    stream.stop_stream()
    stream.close()
    p.terminate()
