import RPi.GPIO as GPIO
import time

IN1 = 13
IN2 = 0
NSLP = 12
D1 = 17
D2 = 27
D3 = 22
D4 = 23

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

import pygame

f,w = True, True
while w:
 try:
  led(D3, True)
  pygame.init()
  pygame.joystick.init()
  joystick = pygame.joystick.Joystick(0)
  joystick.init()
  break
 except Exception as e:
  print("Controller not conected...")
  GPIO.cleanup()
  exit()

w = True
noLB = 5
noRB = 4

while w:
 print('waiting...')
 for event in pygame.event.get():
  if joystick.get_button(0):
   print('connected')
   w = False
 if f:
  led(D3, True)
  f = False
 else:
  led(D3, False)
  f = True
 time.sleep(0.5)
print('connected!!!')
led(D3, False)
led(D2, True)
time.sleep(0.5)
led(D2, False)


GPIO.cleanup()




