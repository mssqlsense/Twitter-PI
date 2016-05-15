import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

  
CurrentStatus=GPIO.input(17)
print CurrentStatus




if CurrentStatus == 1:
	print("Light is already ON")
	GPIO.output(17,0)

else:
	print("Turning Light ON")
	GPIO.output(17,1)

