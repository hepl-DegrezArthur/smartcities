import machine
import time
import camera
import network
from umqtt.simple import MQTTClient

print("starting...")

# Configuration des broches
LED = machine.Pin(12, machine.Pin.OUT)  # LED sur GPIO 4
pir = machine.Pin(15, machine.Pin.IN)  	# PIR sur GPIO 15

# Créer un objet ADC pour GPIO 2
adc = machine.ADC(machine.Pin(13))
adc.width(machine.ADC.WIDTH_12BIT)  # Résolution de 12 bits (0-4095)
adc.atten(machine.ADC.ATTN_11DB)    # Réglage d'atténuation pour gérer jusqu'à 3.3V

# Configurer l'interruption sur le PIR
pir.irq(trigger=machine.Pin.IRQ_RISING, handler=lambda pin: print("Interruption GPIO détectée"))

# Configurer le réveil sur l'interruption externe (EXT0)
pir = machine.Pin(15, machine.Pin.IN)  # Pin 15 as input (for PIR sensor)
pir.irq(trigger=machine.Pin.IRQ_RISING, handler=lambda pin: machine.deepsleep())  # Wake up from deep sleep on PIR signal

# Temps maximum avant un réveil du Deep Sleep
SLEEP_DURATION_MS = 10 * 1000  # 10 secondes pour test

# Paramètres réseau Wi-Fi
ssid = 'WiFi-2.4-74AC'
password = 'wea42cus35ywe'

# Paramètres du serveur Mosquitto
mqtt_broker = "192.168.1.59"
mqtt_port = 1883
mqtt_user = 'RaspberryAD'
mqtt_pass = 'RaspberryAD'
topic_Photos = "ProjetNichoir_Photos"
topic_Batterie = "ProjetNichoir_Batterie"

# Se connecter au réseau Wi-Fi
def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('Connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            time.sleep(1)
    print('Network connected:', sta_if.ifconfig())

# Publier un message sur un topic avec authentification
def publish_message(ToSend, topic):
    try:
        client = MQTTClient(client_id="esp32_client", server=mqtt_broker, port=mqtt_port, user=mqtt_user, password=mqtt_pass)
        client.connect()
        if isinstance(ToSend, (int, float)):
            ToSend = str(ToSend)
        client.publish(topic, ToSend)
        client.disconnect()
    except Exception as e:
        print("Erreur lors de la publication MQTT :", e)

def create_white_image(width, height):
    # Crée une image blanche de dimensions données
    image = bytearray(width * height * 3)  # Image en RGB
    for i in range(len(image)):
        image[i] = 255  # Chaque pixel est blanc (255, 255, 255 en RGB)
    return image

def TakeAndSendPhotoAndBat():
    try:
        BatLevel = 32
        publish_message(BatLevel, topic_Batterie)

        # Prendre une photo
        LED.value(1)
        camera.init()
        img = camera.capture()
        LED.value(0)
        camera.deinit()

        # Publier la photo
        publish_message(bytearray(img), topic_Photos)
    except Exception as e:
        print("Erreur lors de la prise ou de l'envoi de la photo :", e)

def TakeAndSendBat():
    try:
        BatLevel = 32
        publish_message(BatLevel, topic_Batterie)

        # Créer une image blanche
        img = create_white_image(320, 240)  # Dimensions standard (320x240)
        publish_message(img, topic_Photos)
    except Exception as e:
        print("Erreur lors de la création ou de l'envoi de l'image blanche :", e)

# Programme principal
connect_to_wifi()
time.sleep(2)

# Identifier la raison du réveil
wake_reason = machine.reset_cause()

TakeAndSendPhotoAndBat()
time.sleep(1)

# Mettre l'ESP32 en Deep Sleep
print("Mise en sommeil pour 10 secondes ou interruption GPIO...")
machine.deepsleep(SLEEP_DURATION_MS)

