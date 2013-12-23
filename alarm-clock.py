import winsound
import time

def alarm(seconds):	
	time.sleep(seconds)
	winsound.Beep(100,1000)

alarm(int(raw_input("How many seconds until the alarm? ")))