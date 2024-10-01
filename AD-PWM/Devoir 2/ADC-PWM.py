# Librairies
from utime import sleep
from machine import Pin, PWM, Timer, ADC


# Define
buzzer = PWM(Pin(18))
Pot = ADC(1)

NWait = 0.07	#Attente pour couper les notes 
VPot = 1000		#Volume au démarrage du programme


# Routine d'interruption pour le pot
def routine(timer):
    global VPot
    VPot = Pot.read_u16()

timer = Timer()
timer.init(period=10, mode=Timer.PERIODIC, callback=routine)
    

# Notes définies
def DO(delai):
    buzzer.freq(1047)
    buzzer.duty_u16(VPot)
    sleep(delai)
    buzzer.freq(10)
    buzzer.duty_u16(1)

def RE(delai):
    buzzer.freq(1175)
    buzzer.duty_u16(VPot)
    sleep(delai)
    buzzer.freq(10)
    buzzer.duty_u16(1)

def MI(delai):
    buzzer.freq(1319)
    buzzer.duty_u16(VPot)
    sleep(delai)
    buzzer.freq(10)
    buzzer.duty_u16(1)

def FA(delai):
    buzzer.freq(1397)
    buzzer.duty_u16(VPot)
    sleep(delai)
    buzzer.freq(10)
    buzzer.duty_u16(1)

def SOL(delai):
    buzzer.freq(1568)
    buzzer.duty_u16(VPot)
    sleep(delai)
    buzzer.freq(10)
    buzzer.duty_u16(1)

def LA(delai):
    buzzer.freq(1760)
    buzzer.duty_u16(VPot)
    sleep(delai)
    buzzer.freq(10)
    buzzer.duty_u16(1)

def SI(delai):
    buzzer.freq(1976)
    buzzer.duty_u16(VPot)
    sleep(delai)
    buzzer.freq(10)
    buzzer.duty_u16(1)
    
def SOL2(delai):
    buzzer.freq(1661)
    buzzer.duty_u16(VPot)
    sleep(delai)
    buzzer.freq(10)
    buzzer.duty_u16(1)
    
def Nope(delai):
    buzzer.freq(10)
    buzzer.duty_u16(1)
    sleep(delai)

# Version améliorée de la chanson "Joyeux Anniversaire"
def BirthdaySong():
    SOL(0.3)  # Happy (G)
    Nope(NWait)
    SOL(0.3)  # Birthday (G)
    Nope(NWait)
    LA(0.3)   # To (A)
    Nope(NWait)
    SOL(0.3)  # You (G)
    Nope(NWait)
    DO(0.3)   # Happy (C)
    Nope(NWait)
    SI(0.8)   # Birthday (B)
    Nope(NWait)
    SOL(0.3)  # Happy (G)
    Nope(NWait)
    SOL(0.3)  # Birthday (G)
    Nope(NWait)
    LA(0.3)   # To (A)
    Nope(NWait)
    SOL(0.3)  # You (G)
    Nope(NWait)
    RE(0.3)   # Happy (D)
    Nope(NWait)
    DO(0.7)   # Birthday (C)
    Nope(NWait)
    SOL(0.3)  # Happy (G)
    Nope(NWait)
    SOL(0.3)  # Birthday (G)
    Nope(NWait)
    SOL2(0.3) # Dear (G#)
    Nope(NWait)
    MI(0.3)   # Friend's (E)
    Nope(NWait)
    DO(0.3)   # Name (C)
    Nope(NWait)
    SI(0.3)   # Happy (B)
    Nope(NWait)
    LA(0.3)   # Birthday (A)
    Nope(NWait)
    FA(0.3)   # Happy (F)
    Nope(NWait)
    FA(0.3)   # Birthday (F)
    Nope(NWait)
    MI(0.3)   # To (E)
    Nope(NWait)
    DO(0.3)   # You (C)
    Nope(NWait)
    RE(0.3)   # Happy (D)
    Nope(NWait)
    DO(0.7)   # Birthday (C)
    Nope(NWait)
    
def MarioSong():
    # Phrase 1
    MI(0.15)
    Nope(NWait)
    MI(0.15)
    Nope(NWait)
    MI(0.15)
    Nope(NWait)
    DO(0.15)
    Nope(NWait)
    MI(0.15)
    Nope(NWait)
    SOL(0.4)
    Nope(NWait)
    

# Main
while True:
    BirthdaySong()
    MarioSong()
    sleep(1)
