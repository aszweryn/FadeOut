import time
from subprocess import Popen, PIPE, call
import subprocess

amount = '6%-'

def check_master():

	#using a subprocess to call amixer
	sub = Popen(['amixer', '-D', 'pulse', 'sget', 'Master', amount], stdout = PIPE)
	output = sub.communicate()[0]

	#slicing a strict to extract the volume value
	volume = str(output).split('[')[1].split(']')[0]
	return volume



vol = check_master()

#main loop
while 1:

	#type conversion, so the volume can be decreased
	#addressng all possible cases
	if len(vol) == 4:
		temp = int(vol[:3]) - 2
	elif len(vol) == 3:
		temp = int(vol[:2]) - 2
	elif len(vol) == 2:
		temp = int(vol[:1]) - 1


	#when the volume reaches 0, iniciate shutdown
	if temp <= 0:
		
		cmd = ["shutdown", "now"]
		proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)

		break 


	#converting back to string, so the command can be executed
	vol = str(str(temp) + "%")


	#setting a lower volume
	call(["amixer", "-D", "pulse", "-q", "sset", "Master", vol])


	#change time in the brackets to change the pace of volume decrease
	time.sleep(0.2)
