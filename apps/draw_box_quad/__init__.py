import system,display,time

display.drawFill()
display.flush()
display.drawQuad(0,0,40,0,40,40,0,40,0xbbaabb)
display.flush()
display.drawQuad(40,0,50,10,50,40,40,40,0xbbaa00)
display.flush()

time.sleep(5)
system.home()
