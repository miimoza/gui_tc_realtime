import RPi.GPIO as GPIO
import time
import subprocess
from threading import Thread


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    thread_button_1 = Thread(button_check, args=[18])

    thread_button_1.start()

button_check(BUTTON_PIN):
    GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        r = GPIO.input(BUTTON_PIN)
        if r == False:
            subprocess.run("play -q sounds/nanbaptiste.wav".split())
