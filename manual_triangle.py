import display


#added a feature to show triangle being drawn with time.sleep(0.06)
display.drawFill(0x000000)
display.flush()

for i in range(200):
    display.drawPixel(i, i+2, 0xff00ff)
    display.flush()
    time.sleep(0.06)
    
x = 200

while x > 1:
    display.drawPixel(x,202,0xff00ff)
    display.flush()
    time.sleep(0.06)
    x-=1

x=202

while x > 1:
    display.drawPixel(1,x,0xff00ff)
    display.flush()
    time.sleep(0.06)
    x -= 1
   

