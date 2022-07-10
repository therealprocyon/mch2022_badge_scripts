import system
import time
import display
import buttons
import esp32

def home_press(pressed):
    if pressed:
        system.home()
            
buttons.attach(buttons.BTN_HOME, home_press)

while True:
    display.drawFill(0x000000)
    raw_temp = esp32.raw_temperature
    raw_temp_celsius = (raw_temp -32) / 1.8
    display.drawText(10,10,"Internal temperature is: {} \nCelsius".format(raw_temp_celsius), display.GREEN, "roboto_regular18")
    time.sleep(10)

    
