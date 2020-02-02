import RPi.GPIO as GPIO
import time
import subprocess

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    BUTTON1_PIN=18
    GPIO.setup(BUTTON1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        r = GPIO.input(BUTTON1_PIN)
        if r == False:
            subprocess.run("play -q sounds/nanbaptiste.wav".split())


main()
