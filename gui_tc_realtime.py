import xml.etree.ElementTree as ET
import requests
from requests.auth import HTTPBasicAuth
import subprocess
import datetime
import time
import os
import re

def main():
	move_cursor(0,0)
	gui_tc()

	for i in range(0, 28):
		move_cursor(i, 48)
		print("|")

	move_cursor(0, 49)
	nadine()
	meteo()

	move_cursor(28, 0)
	print("="*80)
	for i in range(0, 80):
	    print('.',end='', flush=True)
	    time.sleep(0.2)

def move_cursor(y, x):
	os.system("tput cup " + str(y) + " " + str(x))

def get_weather(id):
	switch={
		0:'Soleil',
		1:'Peu nuageux',
		2:'Ciel voilé',
		3:'Nuageux',
		4:'Très nuageux',
		5:'Couvert',
		6:'Brouillard',
		7:'Brouillard givrant',
		10:'Pluie faible',
		11:'Pluie modérée',
		12:'Pluie forte',
		13:'Pluie faible verglaçante',
		14:'Pluie modérée verglaçante',
		15:'Pluie forte verglaçante',
		16:'Bruine',
		20:'Neige faible',
		21:'Neige modérée',
		22:'Neige forte',
		30:'Pluie et neige mêlées faibles',
		31:'Pluie et neige mêlées modérées',
		32:'Pluie et neige mêlées fortes',
		40:'Averses de pluie locales et faibles',
		41:'Averses de pluie locales',
		42:'Averses locales et fortes',
		43:'Averses de pluie faibles',
		44:'Averses de pluie',
		45:'Averses de pluie fortes',
		46:'Averses de pluie faibles et fréquentes',
		47:'Averses de pluie fréquentes',
		48:'Averses de pluie fortes et fréquentes',
		60:'Averses de neige localisées et faibles',
		61:'Averses de neige localisées',
		62:'Averses de neige localisées et fortes',
		63:'Averses de neige faibles',
		64:'Averses de neige',
		65:'Averses de neige fortes',
		66:'Averses de neige faibles et fréquentes',
		67:'Averses de neige fréquentes',
		68:'Averses de neige fortes et fréquentes',
		70:'Averses de pluie et neige mêlées localisées et faibles',
		71:'Averses de pluie et neige mêlées localisées',
		72:'Averses de pluie et neige mêlées localisées et fortes',
		73:'Averses de pluie et neige mêlées faibles',
		74:'Averses de pluie et neige mêlées',
		75:'Averses de pluie et neige mêlées fortes',
		76:'Averses de pluie et neige mêlées faibles et nombreuses',
		77:'Averses de pluie et neige mêlées fréquentes',
		78:'Averses de pluie et neige mêlées fortes et fréquentes',
		100:'Orages faibles et locaux',
		101:'Orages locaux',
		102:'Orages fort et locaux',
		103:'Orages faibles',
		104:'Orages',
		105:'Orages forts',
		106:'Orages faibles et fréquents',
		107:'Orages fréquents',
		108:'Orages forts et fréquents',
		120:'Orages faibles et locaux de neige ou grésil',
		121:'Orages locaux de neige ou grésil',
		122:'Orages locaux de neige ou grésil',
		123:'Orages faibles de neige ou grésil',
		124:'Orages de neige ou grésil',
		125:'Orages de neige ou grésil',
		126:'Orages faibles et fréquents de neige ou grésil',
		127:'Orages fréquents de neige ou grésil',
		128:'Orages fréquents de neige ou grésil',
		130:'Orages faibles et locaux de pluie et neige mêlées ou grésil',
		131:'Orages locaux de pluie et neige mêlées ou grésil',
		132:'Orages fort et locaux de pluie et neige mêlées ou grésil',
		133:'Orages faibles de pluie et neige mêlées ou grésil',
		134:'Orages de pluie et neige mêlées ou grésil',
		135:'Orages forts de pluie et neige mêlées ou grésil',
		136:'Orages faibles et fréquents de pluie et neige mêlées ou grésil',
		137:'Orages fréquents de pluie et neige mêlées ou grésil',
		138:'Orages forts et fréquents de pluie et neige mêlées ou grésil',
		140:'Pluies orageuses',
		141:'Pluie et neige mêlées à caractère orageux',
		142:'Neige à caractère orageux',
		210:'Pluie faible intermittente',
		211:'Pluie modérée intermittente',
		212:'Pluie forte intermittente',
		220:'Neige faible intermittente',
		221:'Neige modérée intermittente',
		222:'Neige forte intermittente',
		230:'Pluie et neige mêlées',
		231:'Pluie et neige mêlées',
		232:'Pluie et neige mêlées',
		235:'Averses de grêle',
	}

	return switch.get(id, "Invalid Weather")

def print_49(n, s):
	move_cursor(n, 49)
	print(s)

	return n+1

def meteo():
	n = 10

	api = "https://api.meteo-concept.com/api/"
	token = "82caf19ff0ff78534e4ca42c6695a2c53b770ea9bb4404cbf0f826c45bd03d32"
	param = "&insee=94081"

	#=====================================================
	n = print_49(n, (" AUJOURD'HUI ").center(30, "_"))
	route = "ephemeride/0"
	request = api + route + "?token=" + token + param
	res = requests.get(request)
	n = print_49(n, res)
	'''
	ephemeride = res.json()["ephemeride"]

	n = print_49(n, "sunrise: " + ephemeride["sunrise"])
	n = n = print_49(n, n, "sunset: " + ephemeride["sunset"])
	n = print_49(n, "day duration: " + ephemeride["duration_day"])
	n = print_49(n, "moon age: " + str(ephemeride["moon_age"]))
	n = print_49(n, "moon phase: " + ephemeride["moon_phase"])

	#====================================================
	route = "forecast/daily/0"
	param = "&insee=94081"
	request = api + route + "?token=" + token + param
	res = requests.get(request)
	forecast = res.json()['forecast']

	n = print_49(n, "\n" + get_weather(forecast["weather"]))

	n = print_49(n, str(forecast["tmin"]) + "-" + str(forecast["tmax"]) + "°C")
	n = print_49(n, forecast["sun_hours"])
	n = print_49(n, "Vitesse du vent (v): " + str(forecast["wind10m"]))
	n = print_49(n, "Probablite de pluie (p)" + str(forecast["probarain"]))

	#======================================================
	route = "forecast/daily/0/periods"
	request = api + route + "?token=" + token + param
	res = requests.get(request)
	forecast = res.json()['forecast']


	for f, day_step in zip(forecast, ["nuit", "matin", "apres midi", "soir"]):
		n = print_49(n, (" " + day_step + " ").center(30, "-"))
		n = print_49(n, "p: " + str(f["probarain"]) + "%")
		n = print_49(n, re.sub("(.{30})", "\\1\n", get_weather(f["weather"]), 0, re.DOTALL))
	'''


def nadine():
	n = 0
	n = print_49(n, "="*10 + "[" + "nadine".center(10) +"]" + "="*9)

	n = print_49(n, "in dev")

def gui_tc():
	H_180_A = subprocess.getoutput("./skedul.sh b 180 'port a l anglais' A")
	H_180_R = subprocess.getoutput("./skedul.sh b 180 'port a l anglais' R")
	H_217_A = subprocess.getoutput("./skedul.sh b 217 'vitry RER' A")
	H_25_A = subprocess.getoutput("./skedul.sh b 25 'Duras' R")
	H_323_R = subprocess.getoutput("./skedul.sh b 323 'Gambetta' R")
	H_125_A = subprocess.getoutput("./skedul.sh b 125 'Gambetta' A")
	H_125_R = subprocess.getoutput("./skedul.sh b 125 'Gambetta' R")
	r_C_ALL = requests.get('https://api.transilien.com/gare/87545293/depart', auth=HTTPBasicAuth('tnhtn1120', 'C35XsX9ya'))

	r_C_BNF = requests.get('https://api.transilien.com/gare/87545293/depart/87328328', auth=HTTPBasicAuth('tnhtn1120', 'C35XsX9ya'))
	r_C_CHS = requests.get('https://api.transilien.com/gare/87545293/depart/87545285', auth=HTTPBasicAuth('tnhtn1120', 'C35XsX9ya'))
	H_C_BNF = ET.fromstring(r_C_BNF.content)
	H_C_CHS = ET.fromstring(r_C_CHS.content)


	os.system('clear')

	print("="*13 + "[" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).center(20) + "]" + "="*13)
	print("-"*14 + " GARE VITRY RER C ".center(20,"-") + "-"*9 + "-(1)-")
	print("VERS BNF".center(24) + "|" + "VERS CHOISY".center(23))

	i=0
	for E_C_BNF, E_C_CHS in zip(H_C_BNF.findall('train'), H_C_CHS.findall('train')):
		if i < 5:
			print((E_C_BNF.find('date').text + ' ' + E_C_BNF.find('miss').text).center(24), end='|')
			print((E_C_CHS.find('date').text + ' ' + (E_C_CHS.find('miss').text)).center(23))
		i+=1

	if i < 5:
		print('\n' * (5 - i))

	print("-"*14 + " PORT A L'ANGLAIS ".center(20,"-") + "-"*7 + "-(180)-")
	print(H_180_A)
	print(H_180_R)
	print("-"*14 + " DURAS ".center(20,"-") + "-"*8 + "-(25)-")
	print(H_25_A)
	print("-"*14 + " VTRY RER ".center(20,"-") + "-"*7 + "-(217)-")
	print(H_217_A)
	print("-"*14 + " GAMBETTA ".center(20,"-") + "-"*7 + "-(323)-")
	print(H_323_R)
	print("-"*14 + " GAMBETTA ".center(20,"-") + "-"*7 + "-(125)-")
	print(H_125_A)
	print(H_125_R)
