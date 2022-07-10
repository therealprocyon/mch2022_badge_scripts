import display
import system
import utime
import buttons


def home_press(pressed):
    if pressed:
        system.home()
            
buttons.attach(buttons.BTN_HOME, home_press)


display.drawFill(0x000000)
display.flush()
for i in range(200):
    display.drawPixel(i, i+2, 0xff00ff)
    display.flush()
    utime.sleep(0.06)
    
