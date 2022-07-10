import display

while True:
    
        
    def home_press(pressed):
        if pressed:
            system.home()
            
    buttons.attach(buttons.BTN_HOME, home_press)
    
    display.drawFill(0xff0000)
    display.flush()
    time.sleep(1)
    display.drawFill(0x0000ff)
    display.flush()
    time.sleep(1)

