import RPi.GPIO as GPIO
import time
from sys import argv

while True:
	target_sensor_1 = open("/var/www/data.json", 'w')
	target_sensor_2 = open("/var/www/data.json", 'a')
	GPIO.setmode(GPIO.BCM)
	TRIG = 23
	ECHO = 24
	TRIGtwo = 20
	ECHOtwo = 21
	spot1 = False
	spot2 = False

	print "Distance measurement in progress"

	GPIO.setup(TRIG,GPIO.OUT)
	GPIO.setup(ECHO,GPIO.IN)

	GPIO.setup(TRIGtwo,GPIO.OUT)
	GPIO.setup(ECHOtwo,GPIO.IN)

	GPIO.output(TRIGtwo, False)
	print "Waiting for Sensor 2 to Settle"	

	GPIO.output(TRIG, False)
	print "Waiting for Sensor 1 to Settle"

	time.sleep(2)

	GPIO.output(TRIG, True)
	time.sleep(0.00001)
	GPIO.output(TRIG, False)

	#sensor 2
	





	#sensor 1

	while GPIO.input(ECHO)==0:
		pulse_start = time.time()

	while GPIO.input(ECHO)==1:
		pulse_end = time.time()

	pulse_duration = pulse_end - pulse_start
	distance = pulse_duration * 17150
	distance = round(distance, 2)

	print "Distance1:",distance,"cm"
	#hello = str(distance)
	if distance < 50:
		spot1 = True
		#target_sensor_1.write("[{ \"number\":\"1\", \"timeparked\": \"0\", \"timevacant\": \"8\", \"vacant\": false},")
	if distance > 100:
		spot1 = False
		#target_sensor_1.write("[{ \"number\":\"1\", \"timeparked\": \"0\", \"timevacant\": \"10\", \"vacant\": true},")		
				
	




	GPIO.output(TRIGtwo, True)
	time.sleep(0.00001)
	GPIO.output(TRIGtwo, False)

	#sensor 2
	while GPIO.input(ECHOtwo)==0:
		pulse_start_two = time.time()

	while GPIO.input(ECHOtwo)==1:
		pulse_end_two = time.time()

	pulse_duration_two = pulse_end_two - pulse_start_two

	distance_two = pulse_duration_two * 17150

	distance_two = round(distance_two, 2)
	print "Distance2:", distance_two, "cm"
	#hello_two = str(distance_two)
	if distance_two < 50:
		spot2 = True
		#target_sensor_2.write("{ \"number\":\"2\", \"timeparked\": \"0\", \"timevacant\": \"11\", \"vacant\": false}]")
	if distance_two > 100:
		spot2 = False
		#target_sensor_2.write("{ \"number\":\"2\", \"timeparked\": \"0\", \"timevacant\": \"6\", \"vacant\": true}]")	
	
	
	# both true
	if spot1 and spot2:
		target_sensor_1.write("[{ \"number\":\"1\", \"timeparked\": \"0\", \"timevacant\": \"8\", \"vacant\": false}, { \"number\":\"2\", \"timeparked\": \"0\", \"timevacant\": \"11\", \"vacant\": false}]")

	# spot1 = false, spot2 = true
	if (not spot1) and spot2:
		target_sensor_1.write("[{ \"number\":\"1\", \"timeparked\": \"0\", \"timevacant\": \"10\", \"vacant\": true}, { \"number\":\"2\", \"timeparked\": \"0\", \"timevacant\": \"11\", \"vacant\": false}]")
	# spot1 = true, spot2 = false
	if spot1 and (not spot2):
		target_sensor_1.write("[{ \"number\":\"1\", \"timeparked\": \"0\", \"timevacant\": \"8\", \"vacant\": false}, { \"number\":\"2\", \"timeparked\": \"0\", \"timevacant\": \"6\", \"vacant\": true}]")
	if (not spot1) and (not spot2):
		target_sensor_1.write("[{ \"number\":\"1\", \"timeparked\": \"0\", \"timevacant\": \"10\", \"vacant\": true}, { \"number\":\"2\", \"timeparked\": \"0\", \"timevacant\": \"6\", \"vacant\": true}]")
	


	
	GPIO.cleanup()
