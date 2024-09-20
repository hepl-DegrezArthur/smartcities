#Librairies
import machine
import utime


#Define
LED = machine.Pin(18,machine.Pin.OUT)
Button=machine.Pin(16,machine.Pin.IN)
Delai=0.5

count=0

#Main
while 1:
    if Button.value() == 1:
        count=count+1
        utime.sleep(0.2)
    elif count==2:
        count=0
        utime.sleep(0.2)
    LED.value(count)
