import RPi.GPIO as GPIO
import time
import subprocess
from threading import Thread


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    thread_button_1 = Thread(target = button_check, args = (18,"sounds/nanbaptiste.wav"))
    thread_button_2 = Thread(target = button_check, args = (14,"sounds/tuvoispas.mp3"))
    thread_button_3 = Thread(target = button_check, args = (15,"sounds/jsuistresnet.mp3"))

    thread_button_1.start()
    thread_button_2.start()
    thread_button_3.start()

def button_check(gpio_number, sound_path):
    GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        r = GPIO.input(gpio_number)
        if r == False:
            cmd = "play -q " + sound_path + " -t alsa"

            Thread(target = subprocess.run, args = (cmd.split(),)).start()
            time.sleep(0.5)

def print_news(gpio_number):
    GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    while True:
        r = GPIO.input(gpio_number)
        if r == False:
            cmd = "play -q " + sound_path + " -t alsa"

            Thread(target = subprocess.run, args = (cmd.split(),)).start()
            time.sleep(0.5)
