import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.cleanup()
GPIO.setup("P8_14",GPIO.OUT)
GPIO.setup("P8_12",GPIO.OUT)
GPIO.setup("P8_16",GPIO.OUT)
GPIO.setup("P8_18",GPIO.OUT)
GPIO.setup("P8_17",GPIO.OUT)
GPIO.setup("P8_15",GPIO.OUT)
GPIO.setup("P8_13",GPIO.OUT)
GPIO.setup("P8_11",GPIO.OUT)
GPIO.setup("P9_24",GPIO.OUT)
GPIO.setup("P9_15",GPIO.OUT)
GPIO.setup("P9_13",GPIO.OUT)
GPIO.setup("P9_11",GPIO.OUT)
GPIO.setup("P9_12",GPIO.OUT)
GPIO.setup("P9_14",GPIO.OUT)
GPIO.setup("P9_16",GPIO.OUT)
GPIO.setup("P9_23",GPIO.OUT)

GPIO.output("P8_11",GPIO.HIGH) #red
GPIO.output("P9_11",GPIO.HIGH) #red
GPIO.output("P9_23",GPIO.HIGH) #red

while(True):

	GPIO.output("P8_12",GPIO.HIGH) #green
	GPIO.output("P8_14",GPIO.HIGH) #green
	time.sleep(5)
	GPIO.output("P8_12",GPIO.LOW) #green
	GPIO.output("P8_14",GPIO.LOW) #green
	GPIO.output("P8_16",GPIO.HIGH) #YELLOW
	time.sleep(2)
	GPIO.output("P8_16",GPIO.LOW) #YELLOW
	GPIO.output("P8_18",GPIO.HIGH) #RED on
	GPIO.output("P8_11",GPIO.LOW) #red off
	GPIO.output("P8_15",GPIO.HIGH) #green
	GPIO.output("P8_17",GPIO.HIGH) #green
	time.sleep(5)
	GPIO.output("P8_15",GPIO.LOW) #green
	GPIO.output("P9_17",GPIO.LOW) #green
	GPIO.output("P8_13",GPIO.HIGH) #YELLOW
	time.sleep(2)
	GPIO.output("P8_13",GPIO.LOW) #YELLOW
	GPIO.output("P8_11",GPIO.HIGH) #RED on
	GPIO.output("P9_11",GPIO.LOW) #red off
	GPIO.output("P9_24",GPIO.HIGH) #green
	GPIO.output("P9_15",GPIO.HIGH) #green
	time.sleep(5)
	GPIO.output("P9_24",GPIO.LOW) #green
	GPIO.output("P9_15",GPIO.LOW) #green
	GPIO.output("P9_13",GPIO.HIGH) #YELLOW
	time.sleep(2)
	GPIO.output("P9_13",GPIO.LOW) #YELLOW
	GPIO.output("P9_11",GPIO.HIGH) #RED on
	GPIO.output("P9_23",GPIO.LOW) #red off
	GPIO.output("P9_12",GPIO.HIGH) #green
	GPIO.output("P9_14",GPIO.HIGH) #green
	time.sleep(5)
	GPIO.output("P9_12",GPIO.LOW) #Green
	GPIO.output("P9_14",GPIO.LOW) #Green
	GPIO.output("P9_16",GPIO.HIGH) #YELLOW
	time.sleep(2)
	GPIO.output("P9_16",GPIO.LOW) #YELLOW
	GPIO.output("P9_23",GPIO.HIGH) #RED on
	


