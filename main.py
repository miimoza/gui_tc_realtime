import subprocess
import importlib
import gui_tc_realtime
import nadine
import nanbaptiste
import faits_divers
import meteo
import display
import time


importlib.reload(nanbaptiste)

while True:
	subprocess.check_call(["git","pull"])
	importlib.reload(gui_tc_realtime)
	importlib.reload(nadine)
	importlib.reload(meteo)
	importlib.reload(display)
	importlib.reload(faits_divers)

	nanbaptiste.main()
	gui_tc_realtime.main()
	nadine.main()
	#faits_divers.main()
	meteo.main()

	display.move_cursor(28, 0)
	print("="*80)
	for i in range(0, 80):
	    print('.',end='', flush=True)
	    time.sleep(0.2)
