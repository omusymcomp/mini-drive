import RPi.GPIO as GPIO
from . import pi,IN1,IN2,NSLP

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
