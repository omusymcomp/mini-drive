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
pi = GPIO.PWM(IN1, 5000)    #5kHzでpwm制御
pi.start(0)
GPIO.output(NSLP, GPIO.HIGH)

#Duty比の変更
def set_duty(rate):
    pi.ChangeDutyCycle(rate)

#ショートブレーキ(あまり効果ないかも)
def brake(): 
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)

#モーターへの出力を入れたり切ったり
def sleep(l=True):
    if l:
        GPIO.output(NSLP, GPIO.LOW)
    else:
        GPIO.output(NSLP, GPIO.HIGH)

def cleanup():
    GPIO.cleanup()