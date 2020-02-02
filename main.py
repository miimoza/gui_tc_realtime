import subprocess
import importlib
import gui_tc_realtime
import nadine
import nanbaptiste
import meteo
import display
import time
from threading import Thread


while True:
	subprocess.check_call(["git","pull"])
	importlib.reload(gui_tc_realtime)
	importlib.reload(nadine)
	importlib.reload(meteo)
	importlib.reload(display)
		print("test3")
	importlib.reload(nanbaptiste)

	print("test")
	button_thread = Thread(target = nanbaptiste.main())
	button_thread.start()

	print("test2")

	gui_tc_realtime.main()
	nadine.main()
	meteo.main()

	display.move_cursor(28, 0)
	print("="*80)
	for i in range(0, 80):
	    print('.',end='', flush=True)
	    time.sleep(0.2)
