import RPi.GPIO as GPIO

#ピン番号の指定(BCM)
LED1 = 2     #blue
LED2 = 20    #green
LED3 = 21    #orange
LED4 = 3     #red
MOTD = 6     #回転方向指定
PWM = 12      #PWM
NSLP = 13    #スリープ指定

list = [LED1, LED2, LED3, LED4, MOTD, PWM, NSLP]

#GPIOの初期化
GPIO.setmode(GPIO.BCM)
for i in list:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)
pi = GPIO.PWM(PWM, 1000)    #1kHzでpwm制御
pi.start(0)
GPIO.output(NSLP, GPIO.HIGH)


from .drive import (
    set_duty,
    brake,
    cleanup,
    sleep,
)

from .data import (
    acc_x,
    acc_y,
    acc_z,
    mag_x,
    mag_y,
    mag_z,
    gyr_x,
    gyr_y,
    gyr_z,
    mot_in,
    mot_out,
    A0,
    A1,
    A2,
    A3,
    A4,
    A5,
    LED_out,
)
