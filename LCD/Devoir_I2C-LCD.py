# Librairies
from lcd1602 import LCD1602
from utime import sleep
from machine import I2C, Pin, ADC, PWM, Timer
from dht11 import *

# Define
LED = machine.Pin(20,machine.Pin.OUT)

RAS = ADC(0)

buzzer = PWM(Pin(18))
NWait = 0.07	#Attente pour couper les notes 
VPot = 1000		#Volume au démarrage du programme

dht = DHT(16)
temp, humid = dht.readTempHumid()

i2c = I2C(1, scl=Pin(7), sda=Pin(6), freq=400000)  # I2C conf pin
d = LCD1602(i2c, 2, 16)                            # Data info
d.display()

# Routine d'interruption pour le pot
def routine(timer):
    LED.value(not LED.value())	#toggle l'état de la LED

timer = Timer()
#timer.init(period=125, mode=Timer.PERIODIC, callback=routine)


#Fonctions
def AffichageV():
    d.print('SET : '+str(Vset))
    d.setCursor(0, 1)
    d.print('Ambient : '+str(Vtemp))


while True:
    sleep(0.1)
    d.clear()
    d.setCursor(0, 0)
    Vset = RAS.read_u16()
    Vset = ((Vset/65535)*20)+15
    Vset = round (Vset,2)
    Vtemp, humid = dht.readTempHumid()
    
    if Vset > Vtemp and Vset < Vtemp+3:
        AffichageV()
        timer.deinit()
        buzzer.deinit()
        sleep(0.01)
        timer.init(period=125, mode=Timer.PERIODIC, callback=routine)
        sleep(0.01)
        
    elif Vset > Vtemp+3:
        timer.deinit()
        sleep(0.01)
        timer.init(period=100, mode=Timer.PERIODIC, callback=routine)
        sleep(0.01)
        buzzer.freq(1047)
        buzzer.duty_u16(1000)
        d.clear()
        d.setCursor(0, 0)
        d.print('ALARM')
        
    else:
        AffichageV()
        timer.deinit()
        buzzer.deinit()
        LED.value(0)
        
    sleep(0.1)
        
        

