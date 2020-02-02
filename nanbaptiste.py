import RPi.GPIO as GPIO
import time
import subprocess
from threading import Thread


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    thread_button_1 = Thread(target = button_check, args = (18,))

    thread_button_1.start()

def button_check(gpio_number):
    GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        r = GPIO.input(gpio_number)
        if r == False:
            cmd = "play -q sounds/nanbaptiste.wav".split()
            Thread(target = subprocess.run, args = (cmd,)).start()
            sleep(0.1)
