import machine
import time

PIR = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)
PIR.irq(trigger=machine.Pin.IRQ_RISING, handler=PIR_handler)                     # Configuration de l'interruption sur changement d'état de la pin x
def PIR_handler(pin):                                                            # Fonction d'interruption
    #Code d'interruption ici

wake_up = machine.Pin(4, mode=machine.Pin.IN)                                    # Définir le réveil sur la pin 4
machine.PinWake.wake_on_pin(wake_up, level=machine.PinWake.HIGH)                 # Activer le wake up de l'ESP32 depuis l'hardware sur la PIN4

print("Le deep sleep va être activé...")                                         
time.sleep(2)      
machine.deepsleep()                                                              #Actvier le deep sleep

