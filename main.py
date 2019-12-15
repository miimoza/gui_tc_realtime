import subprocess
import importlib
import gui_tc_realtime
import nadine
import meteo
import display
import time

while True:
	subprocess.check_call(["git","pull"])
	importlib.reload(gui_tc_realtime)
	importlib.reload(nadine)
	importlib.reload(meteo)
	importlib.reload(display)

	for i in range(0, 28):
		display.move_cursor(i, 48)
		print("|")

	gui_tc_realtime.main()
	nadine.main()
	meteo.main()

	display.move_cursor(28, 0)
	print("="*80)
	for i in range(0, 80):
	    print('.',end='', flush=True)
	    time.sleep(0.2)
