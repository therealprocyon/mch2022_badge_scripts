import display
import system

display.drawFill(0x000000)
display.flush()
for i in range(200):
    display.drawPixel(i, i+2, 0xff00ff)
    display.flush()
    time.sleep(0.06)
    
time.sleep(3)
system.home()
