import xml.etree.ElementTree as ET
import requests
from requests.auth import HTTPBasicAuth
import subprocess
import datetime
import time
import os

def main():
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

	print("="*13 + "[" + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")).center(20) + "]" + "="*13, end='|\n')
	print("-"*14 + " GARE VITRY RER C ".center(20,"-") + "-"*9 + "-(1)-", end='|\n')
	print("VERS BNF".center(24) + "|" + "VERS CHOISY".center(23), end='|\n')

	i=0
	for E_C_BNF, E_C_CHS in zip(H_C_BNF.findall('train'), H_C_CHS.findall('train')):
		if i < 5:
			print((E_C_BNF.find('date').text + ' ' + E_C_BNF.find('miss').text).center(24), end='|')
			print((E_C_CHS.find('date').text + ' ' + (E_C_CHS.find('miss').text)).center(23), end='|\n')
		i+=1

	if i < 5:
		print('\n' * (5 - i))

	print("-"*14 + " PORT A L'ANGLAIS ".center(20,"-") + "-"*9 + "-(1)-", end='|\n')
	print("-"*14 + " 180 ".center(20,"-") + "-"*9 + "-(1)-", end='|\n')
	print(H_180_A.ljust(48), end='|\n')
	print(H_180_R.ljust(48), end='|\n')
	print("-"*14 + " DURAS ".center(20,"-") + "-"*9 + "-(1)-", end='|\n')
	print("-"*14 + " 25 ".center(20,"-") + "-"*9 + "-(1)-", end='|\n')
	print(H_25_A.ljust(48), end='|\n')
	print("-"*14 + " VTRY RER ".center(20,"-") + "-"*9 + "-(1)-", end='|\n')
	print("-"*14 + " 217 ".center(20,"-") + "-"*9 + "-(1)-", end='|\n')
	print(H_217_A.ljust(48), end='|\n')
	print("-"*14 + " GAMBETTA ".center(20,"-") + "-"*9 + "-(1)-", end='|\n')
	print("-"*14 + " 323 ".center(20,"-") + "-"*9 + "-(1)-", end='|\n')
	print(H_323_R.ljust(48), end='|\n')
	print("-"*14 + " 125 ".center(20,"-") + "-"*9 + "-(1)-", end='|\n')
	print(H_125_A.ljust(48), end='|\n')
	print(H_125_R.ljust(48), end='|\n')
	print("="*48, end='|\n')

	for i in range(0, 48):
	    print('.',end='', flush=True)
	    time.sleep(0.5)
	print()
