import esp32
import machine
import time
import camera
import network
from umqtt.simple import MQTTClient

# Configuration des broches
LED = machine.Pin(12, machine.Pin.OUT)  # LED sur GPIO 12
wake1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Configuration du réveil par interruption externe (EXT0)
esp32.wake_on_ext0(pin=wake1, level=esp32.WAKEUP_ANY_HIGH)

# Temps maximum avant un réveil du Deep Sleep
SLEEP_DURATION_MS = 60 * 1000  # 60 secondes

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

# Identifier la raison du réveil
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print("Réveillé par une interruption externe GPIO")
else:
    print("Réveillé pour une autre raison")

# Programme principal
connect_to_wifi()
time.sleep(2)

TakeAndSendPhotoAndBat()
time.sleep(1)

# Mettre l'ESP32 en Deep Sleep
print("Mise en sommeil pour 60 secondes ou interruption GPIO...")
machine.deepsleep(SLEEP_DURATION_MS)

