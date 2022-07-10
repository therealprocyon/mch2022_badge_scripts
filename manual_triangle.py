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
    utime.sleep(0.02)

x = 200

while x > 1:
    display.drawPixel(x,202,0xff00ff)
    display.flush()
    utime.sleep(0.02)
    x-=1

x=202

while x > 1:
    display.drawPixel(1,x,0xff00ff)
    display.flush()
    utime.sleep(0.02)
    x -= 1

utime.sleep(10)
system.home()
