import xml.etree.ElementTree as ET
import requests
from requests.auth import HTTPBasicAuth
import subprocess
import datetime
import time
import os


def main():
	move_cursor(0,0)
	gui_tc()

	for i in range(0, 32):
		move_cursor(i, 48)
		print("|")

	move_cursor(0, 49)
	nadine()

	move_cursor(32, 0)
	for i in range(0, 80):
	    print('.',end='', flush=True)
	    time.sleep(0.2)

def move_cursor(y, x):
	os.system("tput cup " + str(y) + " " + str(x))

def nadine():
	print("="*10 + "[" + "nadine".center(10) +"]" + "="*10)

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
	print("-"*14 + " VTRY RER ".center(20,"-") + "-"*7 + "-(125)-")
	print(H_217_A)
	print("-"*14 + " GAMBETTA ".center(20,"-") + "-"*7 + "-(125)-")
	print(H_323_R)
	print("-"*14 + " GAMBETTA ".center(20,"-") + "-"*7 + "-(125)-")
	print(H_125_A)
	print(H_125_R)
	print("="*48)

	'''
	for i in range(0, 48):
	    print('.',end='', flush=True)
	    time.sleep(0.5)
	print()
	'''
