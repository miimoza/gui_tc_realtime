import RPi.GPIO as GPIO
import time
import subprocess
from threading import Thread
import glob
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import random
import os


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    thread_button_1 = Thread(target = play_random_baptiste, args = (18,))
    thread_button_2 = Thread(target = print_news, args = (14,))
    thread_button_3 = Thread(target = print_news, args = (15,))

    thread_button_1.start()
    thread_button_2.start()
    thread_button_3.start()
    print("[button_wrapper] Launch Thread function")

def play_random_baptiste(gpio_number):
    GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    sounds_list = glob.glob("/home/pi/gui_tc_realtime/sounds/*.mp3")
    print(sounds_list)
    sound_path = sounds_list[random.randint(0, sounds_list.size() - 1)]

    while True:
        r = GPIO.input(gpio_number)
        if r == False:
            cmd = "play -q " + sound_path + " -t alsa"

            Thread(target = subprocess.run, args = (cmd.split(),)).start()
            time.sleep(0.5)

def print_news(gpio_number):
    os.system('clear')
    print("cool ces news dis donc..")
    news_data = getToday("ile-de-france", "val-de-marne")
    for date, post in news_data:
        print("[" + date + "] " + post)


def getToday(region, departement = "", city = ""):
    res = getNews(region, departement, city)
    posts_bs, dates_bs = res["posts"], res["dates"]

    posts, dates = [], []
    i = 0;
    d0 = datetime.strptime(dates_bs[0].text, '%H:%M')
    while (i < len(posts_bs) and datetime.strptime(dates_bs[i].text, '%H:%M') <= d0):
        dates.append(dates_bs[i].text)
        posts.append(posts_bs[i]['title'])
        i+=1

    return (dates, posts)
