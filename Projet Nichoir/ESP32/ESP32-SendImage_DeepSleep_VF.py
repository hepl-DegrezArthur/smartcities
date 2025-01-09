import esp32
import machine
from machine import Pin, ADC
import time
import camera
import network
from umqtt.simple import MQTTClient

# Configuration des broches
LED = machine.Pin(12, machine.Pin.OUT)  # LED sur GPIO 12

wake1 = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)

# Désactiver le Wi-Fi pour éviter les conflits avec l'ADC2
wifi = network.WLAN(network.STA_IF)
wifi.active(False)
# Configuration de l'ADC sur la broche IO13
ADC_IN = ADC(Pin(13))
ADC_IN.atten(ADC.ATTN_11DB)  # Plage 0-3.3V
ADC_IN.width(ADC.WIDTH_12BIT)  # Résolution de 12 bits (0-4095)
ResistanceM = 300000
ResistanceV = 200000

# Configuration du réveil par interruption externe (EXT0)
esp32.wake_on_ext0(pin=wake1, level=esp32.WAKEUP_ANY_HIGH)

# Temps maximum avant un réveil du Deep Sleep
SLEEP_DURATION_MS = 60 * 1000  # 60 secondes

# Paramètres réseau Wi-Fi
ssid = 'Proximus-Home-3890'
password = 'whn3ajbkbpjre'

# Paramètres du serveur Mosquitto
mqtt_broker = "192.168.1.9"
mqtt_port = 1883
mqtt_user = 'RaspberryAD'
mqtt_pass = 'RaspberryAD'
topic_Photos = "ProjetNichoir_Photos"
topic_Batterie = "ProjetNichoir_Batterie"

# Se connecter au réseau Wi-Fi
def connect_to_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            time.sleep(1)

# Publier un message sur un topic avec authentification
def publish_message(ToSend, topic):
    try:
        client = MQTTClient(client_id="esp32_client", server=mqtt_broker, port=mqtt_port, user=mqtt_user, password=mqtt_pass)
        client.connect()
        if isinstance(ToSend, (int, float)):
            ToSend = str(ToSend)
        client.publish(topic, ToSend)
        client.disconnect()
    except:
        pass

# Prendre une photo et envoyer le niveau de batterie
def TakeAndSendPhotoAndBat(TauxBatterie):
    try:
        publish_message(TauxBatterie, topic_Batterie)

        # Prendre une photo
        LED.value(1)
        camera.init()
        img = camera.capture()
        LED.value(0)
        camera.deinit()

        # Publier la photo
        publish_message(bytearray(img), topic_Photos)
    except:
        pass


# Lecture de la valeur brute de l'ADC
ADC_IN_Value = ADC_IN.read()
# Conversion en tension (en volts)
MesureVoltage = (ADC_IN_Value * 3.3) / 4095
# Calcul de la tension réelle
RealVoltage = MesureVoltage * ((ResistanceM + ResistanceV) / ResistanceM)
# Calcul du pourcentage de batterie
TauxBatterie = max(0, min(100, int(((RealVoltage - 3) / (4.4 - 3)) * 100)))


wifi.active(True)
connect_to_wifi()
time.sleep(2)

TakeAndSendPhotoAndBat(TauxBatterie)
time.sleep(1)

# Mettre l'ESP32 en Deep Sleep
machine.deepsleep(SLEEP_DURATION_MS)
