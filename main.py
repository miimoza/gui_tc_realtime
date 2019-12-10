import subprocess
import importlib
import gui_tc_realtime

while True:
	subprocess.check_call(["git","pull"])
	importlib.reload(gui_tc_realtime)
	gui_tc_realtime.main()
