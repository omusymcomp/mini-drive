import RPi.GPIO as GPIO

#ピン番号の指定
D1 = 17
D2 = 27
D3 = 22
D4 = 23
IN1 = 13
IN2 = 0
NSLP = 12

list = [D1, D2, D3, D4, IN1, IN2, NSLP]

#GPIOの初期化
GPIO.setmode(GPIO.BCM)
for i in list:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.LOW)
pi = GPIO.PWM(IN1, 5000)    #5kHzでpwm制御
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
