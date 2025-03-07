import RPi.GPIO as GPIO
from . import pi,MOTD,PWM,NSLP

#Duty比の変更
def set_duty(rate):
    pi.ChangeDutyCycle(rate)

#ショートブレーキ(あまり効果ないかも)
def brake(): 
    GPIO.output(PWM, GPIO.LOW)

#モーターへの出力を入れたり切ったり
def sleep(l=True):
    if l:
        GPIO.output(NSLP, GPIO.LOW)
    else:
        GPIO.output(NSLP, GPIO.HIGH)

def cleanup():
    GPIO.cleanup()
