import RPi.GPIO as GPIO
from . import pwm1,MOTD,PWM,NSLP

#Duty比の変更
def set_duty(rate):
    if not -100 <= rate <= 100:
        raise Exception('Duty rate must be between -100 and 100.')
        return  # Exit the function after raising the exception
    if rate < 0:
        GPIO.output(MOTD, GPIO.HIGH)
        rate = -rate
    else:
        GPIO.output(MOTD, GPIO.LOW)
    pwm1.ChangeDutyCycle(rate)

#ショートブレーキ(あまり効果ないかも)
def brake(flag=True):
    if flag:
        GPIO.output(MOTD, GPIO.LOW)
    else:
        GPIO.output(MOTD, GPIO.HIGH) 

#モーターへの出力を入れたり切ったり
def sleep(l=True):
    if l:
        GPIO.output(NSLP, GPIO.LOW)
    else:
        GPIO.output(NSLP, GPIO.HIGH)

def cleanup():
    GPIO.cleanup()
