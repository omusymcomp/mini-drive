import RPi.GPIO as GPIO
import time

IN1 = 13
IN2 = 0
NSLP = 12
D2 = 27
D3 = 22

GPIO.setmode(GPIO.BCM)
for i in [IN1, IN2, NSLP, D2, D3]:
 GPIO.setup(i, GPIO.OUT)
 GPIO.output(i, GPIO.LOW)

def acc():
 GPIO.output(IN1, GPIO.HIGH)
 GPIO.output(IN2, GPIO.LOW)
 GPIO.output(NSLP, GPIO.HIGH)

def slp():
 GPIO.output(NSLP, GPIO.LOW)

def beake():
 GPIO.output(IN1, GPIO.LOW)
 GPIO.output(IN2, GPIO.LOW)

def led(no, flag):
 if flag:
  GPIO.output(no, GPIO.HIGH)
 else:
  GPIO.output(no, GPIO.LOW)


acc()
time.sleep(2)





