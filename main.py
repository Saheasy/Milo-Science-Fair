from picographics import PicoGraphics, DISPLAY_PICO_DISPLAY,  PEN_P4
from pimoroni import RGBLED,Button
import machine 
import time 
display = PicoGraphics(display=DISPLAY_PICO_DISPLAY, pen_type=PEN_P4, rotate=0)

display.set_backlight(0.25)
display.set_font("bitmap8")
WIDTH, HEIGHT = display.get_bounds()


button_a = Button(12)
button_b = Button(13)
button_x = Button(14)
button_y = Button(15)

led = machine.Pin(25, machine.Pin.OUT)
rgb = RGBLED(6, 7, 8)
rgb.set_rgb(0,10,0) 
motor = machine.PWM(machine.Pin(2))
motor.freq(1000)
WHITE = display.create_pen(255, 255, 255)
BLACK = display.create_pen(0, 0, 0)
CYAN = display.create_pen(0, 255, 255)
MAGENTA = display.create_pen(255, 0, 255)
YELLOW = display.create_pen(255, 255, 0)
GREEN = display.create_pen(0, 255, 0)


# sets up a handy function we can call to clear the screen
def clear():
    display.set_pen(BLACK)
    display.clear()
    display.update()


# set up
clear()

state = "idle"

while True:
    if button_a.read():
        state = "a"
        clear()
    elif button_b.read():
        state = "b"
        clear()
    elif button_x.read():
        state = "x"
        clear()
    elif button_y.read():
        state = "y"
        clear()
    
    if state == "x": 
        rgb.set_rgb(0,10,10)
        motor.duty_u16(230 * 230)
        display.set_pen(WHITE)
        display.text("State: Half Speed", 10, 10, 240, 3)
        display.text("A: On", 10, 45, 240, 3)
        display.text("X: On(Half Speed)", 10, 80, 240, 3)
        display.text("B&Y: Off", 10, 115, 240, 3)
        display.update()

    elif state == "idle":
        rgb.set_rgb(10,10,0) 
        motor.duty_u16(0 * 0)
        display.set_pen(GREEN)
        display.text("State: Idle", 10, 10, 240, 3)
        display.text("A: On", 10, 45, 240, 3)
        display.text("X: On(Half Speed)", 10, 80, 240, 3)
        display.text("B&Y: Off", 10, 115, 240, 3)
        display.update()
    
    elif state == "a":
        rgb.set_rgb(0,10,0) 
        motor.duty_u16(255 * 255)
        display.set_pen(WHITE)
        display.text("State: Full Speed", 10, 10, 240, 3)
        display.text("A: On", 10, 45, 240, 3)
        display.text("X: On(Half Speed)", 10, 80, 240, 3)
        display.text("B&Y: Off", 10, 115, 240, 3)
        display.update()
    elif state == "y" or state == "b":
        rgb.set_rgb(10,0,0) 
        motor.duty_u16(0 * 0)
        display.set_pen(WHITE)
        display.text("State: Off", 10, 10, 240, 3)
        display.text("A: On", 10, 45, 240, 3)
        display.text("X: On(Half Speed)", 10, 80, 240, 3)
        display.text("B&Y: Off", 10, 115, 240, 3)
        display.update()
    time.sleep(0.1)  # this number is how frequently the Pico checks for button presses