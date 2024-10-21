import neopixel
from utime import sleep
import utime
from machine import I2C, Pin, ADC
import machine
import random

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
colors = [BLACK, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

# Initialisation du capteur sonor
Ssensor = ADC(1)

# Valeurs de référence pour les battements
RefNoise = 0
Vbattement = 3000

# Prise de valeurs pour le démarrage du premier temps
LastTime = utime.ticks_ms()

def SoundSensorAverage():
    # Faire une moyenne sur 10 valeur avec 10ms d'interval
        # Cette méthode permet de supprimer le buit
    global Mnoise
    Mnoise = 0
    for i in range (1000):
        noise = Ssensor.read_u16()
        Mnoise = Mnoise + noise
        utime.sleep_us(1)
        
    Mnoise = Mnoise/1000
    return Mnoise

while True:
    
    noise = SoundSensorAverage() #Besoin d'une moyenne car capteur très instable
    
    if abs(noise - RefNoise) > Vbattement:  # Comparaison de l'écart - Si il y a eu un battement
        #Prise de du temps actuels
        CurrentTime = utime.ticks_ms()
        
        #Temps écoulé depuis le battement précédent
        VTime = CurrentTime - LastTime
        
        # vérifier que l'interval entre les deux est assez grand (limiter les sons parasites)
        if VTime > 300:
            # Calculer le BPM en fonction du délai
            BPM = 60000/VTime
            print(BPM)
            # Actualiser 'LastTime'
            LastTime = CurrentTime
        
        # Prendre une couleur au hasard
        random_color = random.choice(colors)
        # Appliquer la couleur choisie à la LED NeoPixel
        Neopixel.fill(random_color)
        Neopixel.write()
        
        # Actualiser la valeur de référence
        RefNoise = noise
    utime.sleep_ms(50)
    

