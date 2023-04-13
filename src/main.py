import wave
import pyaudio
from src.hardware.microphone import start_recording, stop_recording
from src.tcpClient.client import setupConnection
from src.udpServer.server import createServer
from scipy.io.wavfile import write


PORT = 5001
PORT_MAINAPPLICATION = 5000

if __name__ == '__main__':

    print('Initializing AI model...')
    # TODO: Initialize AI model
    print('🚀 Starting TCP client on port ' + str(PORT_MAINAPPLICATION) + '...')
    setupConnection(PORT_MAINAPPLICATION)
    print('📡 Starting UDP server on port ' + str(PORT) + '...')
    createServer(PORT)
    """
    print('start audio stream')

    [stream, p] = start_recording()
    filename = '../resources/recordings/test.wav'
    frames = []
    fs = 16000  # Sample rate
    for i in range(0, int(fs / 3200 * 10)):
        data = stream.read(1024)
        frames.append(data)
        print('recording...')

    stop_recording(stream, p)

    print('stop audio stream')
    wf = wave.open(filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    print('wrote to file')
    """
