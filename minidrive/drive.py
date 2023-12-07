import RPi.GPIO as GPIO

#ピン番号の指定
IN1 = 13
IN2 = 0
NSLP = 12

#GPIOの初期化
GPIO.setmode(GPIO.BCM)
for i in [IN1, IN2, NSLP]:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)
pi = GPIO.PWM(IN1, 100)
pi.start(0)
GPIO.output(NSLP, GPIO.HIGH)

#Duty比の変更
def set_duty(rate):
    pi.ChangeDutyCycle(rate)

#ショートブレーキ
def brake(): 
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

def cleanup():
    GPIO.cleanup()