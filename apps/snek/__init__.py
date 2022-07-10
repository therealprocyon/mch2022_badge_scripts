import display
import buttons
import mascot
import system


def home_press(pressed):
    if pressed:
        system.home()
            
buttons.attach(buttons.BTN_HOME, home_press)

display.drawFill(0x000000)
display.drawText(10,10,"Hack The Planet!!!", display.GREEN, "roboto_regular18")
display.flush()

while True:
    def on_action_btn(pressed):
        if pressed:
            display.drawFill(display.BLACK)
            display.drawPng(100,100,mascot.snek)
            display.flush()
           
    buttons.attach(buttons.BTN_A, on_action_btn)
    buttons.detach(buttons.BTN_A)
    def on_action(pressed):
        if pressed:
            display.drawFill(display.BLACK)
            display.drawText(10,10,"Hack The Planet!!!", display.GREEN, "roboto_regular18")
            display.flush()
    buttons.attach(buttons.BTN_A, on_action)
    buttons.detach(buttons.BTN_A)
