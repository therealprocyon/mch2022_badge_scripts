# Simple house drawing program using quadrilaterals
# Will be improved in the future :)
import display,system,time,buttons

for i in range(320):
    display.drawQuad(0,0,i,0,i,120,0,120,0x10fadd)
    display.flush()

for i in range(320):
    display.drawQuad(0,120,i,120,i,240,0,240,0x0ddd12)
    display.flush()

for i in range(107,157):
    display.drawQuad(107,100,i,100,i,140,107,140,0xeea20a)
    display.flush()

for i in range(104,160):
    display.drawQuad(132,80,133,80,i,100,160,100,0xff0a0a)
    display.flush()
