# Librairies
import machine
import utime

# Définition
LED = machine.Pin(18, machine.Pin.OUT)
Button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Variables
count = 0
i=1

# Fonction d'interruption
def button_handler(pin):
    global i
    i += 1
    if i==6:
        i=1

# Configuration de l'interruption sur changement d'état
Button.irq(trigger=machine.Pin.IRQ_RISING, handler=button_handler)

while True:
    while i==1:
        LED.toggle()
        utime.sleep(0.2)
    while i==2:
        LED.toggle()
        utime.sleep(0.5)
    while i==3:
        LED.toggle()
        utime.sleep(0.5)
        LED.toggle()
        utime.sleep(0.1)
        LED.toggle()
        utime.sleep(0.5)
    while i==4:
        LED.toggle()
        utime.sleep(0.5)
        for y in range (10):
            LED.toggle()
            utime.sleep(0.1)
        LED.toggle()
        utime.sleep(0.5)
    while i==5:
        LED.value(0)
        
