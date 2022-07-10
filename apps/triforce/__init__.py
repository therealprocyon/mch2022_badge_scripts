import display, math, buttons,system


def home_press(pressed):
    if pressed:
        system.home()
            
buttons.attach(buttons.BTN_HOME, home_press)

display.clearMatrix()
display.translate(display.width() / 2, display.height() / 2)

while True:
    display.drawFill(0x000000)
    display.drawTriangle(0,0,30,35,-30,35,0xFFFF00)
    display.drawTriangle(-30,35,0,70,-60,70,0xFFFF00)
    display.drawTriangle(30,35,60,70,0,70,0xFFFF00)
    display.flush()
    time.sleep(0.040)
