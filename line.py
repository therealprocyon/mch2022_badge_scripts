import display


display.drawFill(0x000000)
display.flush()
for i in range(200):
    display.drawPixel(i, i+2, 0xff00ff)
    display.flush()

