import RPi.GPIO as GPIO
IN1 = 13
IN2 = 0
NSLP = 12

GPIO.setmode(GPIO.BCM)
for i in [IN1, IN2, NSLP]:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)
pi = GPIO.PWM(IN1, 100)
pi.start(0)
GPIO.output(NSLP, 1)

def set_duty():
    print("set duty")

def short():
    print("short_brake")

def cleanup():
    GPIO.cleanup()