import machine
import time

# Définir le pin qui servira pour l'interruption
interrupt_pin = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)  # GPIO 4 avec pull-up

# Fonction à exécuter lors de l'interruption
def handle_interrupt(pin):
    print("Interruption détectée sur le pin :", pin)

# Configurer l'interruption sur front descendant
interrupt_pin.irq(trigger=machine.Pin.IRQ_FALLING, handler=handle_interrupt)

# Mettre en place le réveil de l'ESP32 à partir du deep sleep
wake_up = machine.Pin(4, mode=machine.Pin.IN)
machine.PinWake.wake_on_pin(wake_up, level=machine.PinWake.LOW)

# Mettre l'ESP32 en mode sommeil profond
print("Entrée en deep sleep...")
time.sleep(2)  # Petite pause pour voir le message avant de dormir
machine.deepsleep()

