import display

while True:
    display.drawFill(0xff0000)
    display.flush()
    time.sleep(1)
    display.drawFill(0x0000ff)
    display.flush()
    time.sleep(1)

