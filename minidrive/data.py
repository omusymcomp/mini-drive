import RPi.GPIO as GPIO
from . import LED1,LED2,LED3,LED4


def acc_x():
    print('acc x')

def acc_y():
    print('acc y')

def acc_z():
    print('acc z')

def mag_x():
    print('mag x')

def mag_y():
    print('mag y')

def mag_z():
    print('mag z')

def gyr_x():
    print('gyr x')

def gyr_y():
    print('gyr y')

def gyr_z():
    print('gyr z')

def mot_in():
    print('aa bat Volts')

def mot_out():
    print('moter power Volts')

def A0():
    print('analog 0')

def A1():
    print('analog 1')

def A2():
    print('analog 2')

def A3():
    print('analog 3')

def A4():
    print('analog 4')

def A5():
    print('analog 5')

def LED_out(flag:bool, No:int):
    if not (type(No) is int):
        raise Exception('Only integer type is allowed for variable No.')
    elif not (type(flag) is bool):
        raise Exception('Only boolian type is allowed for variable flag.')
    if No < 1 or 4 < No:
        raise Exception('Please enter value 1,2,3 or 4 for No.')

    list = [D1,D2,D3,D4]
    No = No - 1
    if flag:
    	GPIO.output(list[No], GPIO.HIGH)
    else:
        GPIO.output(list[No], GPIO.LOW)
