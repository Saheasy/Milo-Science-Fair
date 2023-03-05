
import machine 
import time 

pwm = machine.PWM(machine.Pin(2))
#pwm.freq(1000)
'''
pin = machine.Pin(2, machine.Pin.OUT)
pin.value(1)
time.sleep(2)
pin.value(0)
#pwm.freq(0) '''
# Fade the LED in and out a few times.

duty = 00
pwm.duty_u16(duty * duty)