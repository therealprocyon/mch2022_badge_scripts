import display
import system
import utime
import buttons

def home_press(pressed):
    if pressed:
        system.home()
            
buttons.attach(buttons.BTN_HOME, home_press)

display.drawFill(0xfbf80d)

display.drawText(10,10,"CYBER!",0x000000,"permanentmarker22")
display.flush()

