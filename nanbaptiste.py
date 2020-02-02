import RPi.GPIO as GPIO
import time
import pyaudio
import wave
import os
import subprocess

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    BUTTON1_PIN=18
    GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        r = GPIO.input(BUTTON1_PIN)
        if r == False:
            print("bouton pressax")
            playsound("sounds/nanbaptiste.wav")
            subprocess.run("play sounds/nanbaptiste.wav".split())


def playsound(path):
    chunk = 1024
    f = wave.open( path,"rb")
    p = pyaudio.PyAudio()
    stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                    channels = f.getnchannels(),
                    rate = f.getframerate(),
                    output = True)

    data = f.readframes(chunk)
    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()


main()
