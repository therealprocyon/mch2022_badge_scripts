import display
import utime
import buttons
import system


def home_press(pressed):
    if pressed:
        system.home()
            
buttons.attach(buttons.BTN_HOME, home_press)
    
while True:
    
        

    display.drawFill(0xff0000)
    display.flush()
    utime.sleep(1)
    display.drawFill(0x0000ff)
    display.flush()
    utime.sleep(1)
