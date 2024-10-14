import neopixel
from utime import sleep
from machine import I2C, Pin, ADC
import machine
import utime

# Initialisation de la LED RGB
Led = machine.Pin.board.GP18
Neopixel = neopixel.NeoPixel(Led, 1)

# Création de tuples pour les couleurs de la LED
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
COLORS = (RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE)

# Initialisation du capteur de lumière
Lsensor = ADC(0)

# Initialisation du capteur sonor
Ssensor = ADC(1)

Mnoise = 0

def SensorAverage():
    # Faire une moyenne sur 10 valeur avec 10ms d'interval
        # Cette méthode permet de supprimer le buit
    global Mnoise
    Mnoise = 0
    for i in range (1000):
        noise = Ssensor.read_u16()
        Mnoise = Mnoise + noise
        utime.sleep_us(1)
        
    Mnoise = Mnoise/1000
    print(Mnoise)
    

while True:
    
    SensorAverage()
    
    light = Lsensor.read_u16()
    if light < 30000 or Mnoise > 9000:
        Neopixel.fill(WHITE)
        Neopixel.write()
    else:
        Neopixel.fill(RED)
        Neopixel.write()
    sleep(0.1)

    
