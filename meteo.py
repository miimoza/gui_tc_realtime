import display
import requests
import re

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

def main():
	display.move_cursor(15, 49)
	meteo()

def meteo():
	n = 15


	#n = display.print_n(49, n, "="*10 + "[" + " METEO ".center(10) +"]" + "="*9)

	api = "https://api.meteo-concept.com/api/"
	token = "82caf19ff0ff78534e4ca42c6695a2c53b770ea9bb4404cbf0f826c45bd03d32"
	param = "&insee=94081"

	'''
	#=====================================================
	n = display.print_n(49, n, (" AUJOURD'HUI ").center(30, "_"))
	route = "ephemeride/0"
	request = api + route + "?token=" + token + param
	res = requests.get(request)
	n = display.print_n(49, n, res)

	ephemeride = res.json()["ephemeride"]

	n = display.print_n(49, n, "sunrise: " + ephemeride["sunrise"])
	n = display.print_n(49, n, "sunset: " + ephemeride["sunset"])
	n = display.print_n(49, n, "day duration: " + ephemeride["duration_day"])
	n = display.print_n(49, n, "moon age: " + str(ephemeride["moon_age"]))
	n = display.print_n(49, n, "moon phase: " + ephemeride["moon_phase"])

	#====================================================
	route = "forecast/daily/0"
	param = "&insee=94081"
	request = api + route + "?token=" + token + param
	res = requests.get(request)
	forecast = res.json()['forecast']

	n = display.print_n(49, n, "\n" + get_weather(forecast["weather"]))

	n = display.print_n(49, n, str(forecast["tmin"]) + "-" + str(forecast["tmax"]) + "°C")
	n = display.print_n(49, n, forecast["sun_hours"])
	n = display.print_n(49, n, "Vitesse du vent (v): " + str(forecast["wind10m"]))
	n = display.print_n(49, n, "Probablite de pluie (p)" + str(forecast["probarain"]))

	#======================================================
	route = "forecast/daily/0/periods"
	request = api + route + "?token=" + token + param
	res = requests.get(request)
	forecast = res.json()['forecast']


	for f, day_step in zip(forecast, ["nuit", "matin", "apres midi", "soir"]):
		n = display.print_n(49, n, (" " + day_step + " ").center(30, "-"))
		n = display.print_n(49, n, "p: " + str(f["probarain"]) + "%")
		n = display.print_n(49, n, re.sub("(.{30})", "\\1\n", get_weather(f["weather"]), 0, re.DOTALL))

'''
