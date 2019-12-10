import xml.etree.ElementTree as ET
import requests
from requests.auth import HTTPBasicAuth
import subprocess
import time
import os

def main():
	try:
	    H_180_A = subprocess.getoutput("./skedul.sh b 180 'port a l anglais' A")
	    H_180_R = subprocess.getoutput("./skedul.sh b 180 'port a l anglais' R")
	    H_217_A = subprocess.getoutput("./skedul.sh b 217 'vitry RER' A")
	    H_25_A = subprocess.getoutput("./skedul.sh b 25 'Duras' R")
	    H_323_R = subprocess.getoutput("./skedul.sh b 323 'Gambetta' R")
	    H_125_A = subprocess.getoutput("./skedul.sh b 125 'Gambetta' A")
	    H_125_R = subprocess.getoutput("./skedul.sh b 125 'Gambetta' R")
	    r = requests.get('https://api.transilien.com/gare/87545293/depart', auth=HTTPBasicAuth('tnhtn1120', 'C35XsX9ya'))
	    H_RER_C = ET.fromstring(r.content)
	except ValueError:
	    print("Error")


	os.system('clear')
	print("=============================================(4)=")
	print("--------------------- RER C -----------------(4)=\n")

	for element in H_RER_C.findall('train'):
	    print(element.find('date').text, end=' | ')
	    print(element.find('miss').text)

	print("\n=================================================")

	print("---------------- PORT A L'ANGLAIS -----------(1)-")
	print(H_180_A)
	print(H_180_R)
	print("-------------------- DURAS ------------------(3)-")
	print(H_25_A)
	print("------------------ VITRY RER ----------------(4)-")
	print(H_217_A)
	print("------------------- GAMBETTA ---------------(17)-")
	print(H_323_R)
	print(H_125_A)
	print(H_125_R)

	print("=================================================\n")

	for i in range(0, 48):
	    print('.',end='', flush=True)
	    time.sleep(0.5)
