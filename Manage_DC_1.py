import twitter
import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)

  
CurrentStatus=GPIO.input(17)
if CurrentStatus == 0:
	print ("Currently Server is OFF")
elif CurrentStatus == 1: 	
	print ("Currently Server is ON")

APP_KEY = ''  #CONSUMER KEY
APP_SECRET = ''  #CONSUMER SECRET
OAUTH_TOKEN = ''  #ACCESS TOKEN 
OAUTH_TOKEN_SECRET = ''  #ACCESS TOKEN SECRET


auth = twitter.OAuth(
    consumer_key=APP_KEY,
    consumer_secret=APP_SECRET,
    token=OAUTH_TOKEN,
    token_secret=OAUTH_TOKEN_SECRET
)

stream = twitter.stream.TwitterStream(auth=auth, domain='userstream.twitter.com')




for msg in stream.user():
	if 'direct_message' in msg:
		print msg['direct_message']['text']

		cur_msg_default = msg['direct_message']['text']
		cur_msg = cur_msg_default.lower()

		CurrentStatus=GPIO.input(17)

		if cur_msg == "serveron":
			
			if CurrentStatus == 0:
				print("Turning Server On")
				GPIO.output(17,1)
				
			else:
				print("Server is already ON. No Action Performed")
			
		elif cur_msg == "serveroff":
			if CurrentStatus == 1:
				print("Turning Server Off")
				GPIO.output(17,0)
				time.sleep(2)
				print("Turned Off Server Successfully")
				
			else:
				print("Server is already Off. No Action Performed")

		elif cur_msg == "reboot":

			if CurrentStatus == 1:
				print("Turning Server Off")
				GPIO.output(17,0)
				print("Turned Off Server Successfully")
				print("Turning Server back On")
				time.sleep(2)	
				GPIO.output(17,1)
				time.sleep(2)
				print("Server back On")
			else:
				print("Turning Server On. It was in OFF state earlier.")	
				GPIO.output(17,1)
				time.sleep(2)
				print("Server back On")	

		else:
			print("Unknown command. Please try again!")
	