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
import display

def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    thread_button_1 = Thread(target = wrapper, args = (18,play_random_baptiste))
    thread_button_2 = Thread(target = wrapper, args = (14,print_news))
    thread_button_3 = Thread(target = wrapper, args = (15,print_news))

    thread_button_1.start()
    thread_button_2.start()
    thread_button_3.start()
    print("[button_wrapper] Launch Thread function")

def wrapper(gpio_number, function):
    GPIO.setup(gpio_number, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    while True:
        r = GPIO.input(gpio_number)
        if r == False:
            function()


def play_random_baptiste():
    print("====super baptiste===")
    sounds_list = glob.glob("/home/pi/gui_tc_realtime/sounds/*.mp3")
    print(sounds_list)
    print(len(sounds_list))
    index = random.randint(0, len(sounds_list) - 1)
    print("rand:" + str(index))
    print(sounds_list[index])


    cmd = "play -q " + sounds_list[index] + " -t alsa"

    Thread(target = subprocess.run, args = (cmd.split(),)).start()
    time.sleep(0.5)



def print_news():
    os.system('clear')

    news_data = getToday("ile-de-france", "val-de-marne")
    print("cool ces news dis donc..")
    print("news_data size:" + str(len(news_data)))
    print("n[0]", news_data[0], "[1]", news_data[1])
    print("n[0]0", news_data[0][0], "[1]0", news_data[1][0])


    n = 0
    width = 47
    n_max = 26
    for i in range(0, len(news_data)):
        n = display.breakline_n(49, n, width, n_max, "[" + news_data[0][i] + "] " + news_data[1][i])



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

def getNews(region, departement = "", city = ""):
    request = "https://faitsdivers365.fr/" + region + "/" + departement + "/" + city + "/"

    html_doc = requests.get(request)
    soup = BeautifulSoup(html_doc.text, "html.parser")

    dates = soup.find_all('span', {'class': 'mh-meta-date updated'})
    posts = soup.find_all('a', {'class': 'mh-thumb-icon'})

    return {"dates":dates, "posts":posts};
