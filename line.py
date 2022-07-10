import display
import system
import utime

display.drawFill(0x000000)
display.flush()
for i in range(200):
    display.drawPixel(i, i+2, 0xff00ff)
    display.flush()
    utime.sleep(0.06)
    
utime.sleep(3)
system.home()
