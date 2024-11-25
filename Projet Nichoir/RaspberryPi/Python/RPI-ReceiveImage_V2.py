import os
import paho.mqtt.client as mqtt
from PIL import Image
import io
import time

# Paramètres du broker MQTT
mqtt_broker = "192.168.1.26"
mqtt_port = 1883
mqtt_topic_Photos = "ProjetNichoir_Photos"  # Topic pour les photos
mqtt_topic_Batterie = "ProjetNichoir_Batterie"  # Topic pour la batterie

# Identifiants pour la connexion
mqtt_user = "RaspberryAD"
mqtt_pass = "RaspberryAD"

# Répertoire pour stocker les photos
photo_directory = "/var/www/html/nichoir"
max_photos = 50  # Nombre maximum de photos autorisées dans le répertoire

# Variables globales
image_data = bytearray()
battery_level = 100  # Niveau de batterie par défaut

# Fonction pour trouver le numéro de la prochaine image
def get_next_image_number():
    # Liste les fichiers dans le répertoire
    existing_files = [f for f in os.listdir(photo_directory) if f.startswith("P") and f.endswith(".jpg")]
    # Trier les fichiers par numéro
    existing_files.sort(key=lambda x: int(x.split('_')[0][1:]))
    if existing_files:
        last_file = existing_files[-1]
        last_number = int(last_file.split('_')[0][1:])
        return last_number + 1
    return 1

# Fonction pour limiter le nombre de photos dans le dossier
def manage_photo_limit():
    # Liste les fichiers dans le répertoire
    existing_files = [f for f in os.listdir(photo_directory) if f.startswith("P") and f.endswith(".jpg")]
    # Trier les fichiers par numéro croissant
    existing_files.sort(key=lambda x: int(x.split('_')[0][1:]))
    # Supprimer les fichiers si le nombre dépasse la limite
    while len(existing_files) > max_photos:
        oldest_file = os.path.join(photo_directory, existing_files.pop(0))
        os.remove(oldest_file)
        print(f"Photo supprimée : {oldest_file}")

# Fonction appelée lorsqu'un message est reçu
def on_message(client, userdata, msg):
    global image_data, battery_level

    if msg.topic == mqtt_topic_Photos:
        # Ajouter les données du message reçu à l'image
        image_data.extend(msg.payload)
        print(f"Morceau reçu, taille totale actuelle : {len(image_data)} octets")

    elif msg.topic == mqtt_topic_Batterie:
        try:
            # Mettre à jour le niveau de batterie
            battery_level = int(msg.payload.decode())
            print(f"Niveau de batterie mis à jour : {battery_level}%")
        except ValueError:
            print("Erreur : Impossible de convertir le niveau de batterie")

# Fonction pour traiter et stocker l'image
def process_and_store_image():
    global image_data

    try:
        # Convertir les données en image en utilisant un flux mémoire (BytesIO)
        image_stream = io.BytesIO(image_data)
        image = Image.open(image_stream)

        # Vérifier et créer le répertoire si nécessaire
        if not os.path.exists(photo_directory):
            os.makedirs(photo_directory)

        # Obtenir le numéro de la prochaine image
        next_image_number = get_next_image_number()
        image_name = f"P{next_image_number}_{battery_level}.jpg"
        image_path = os.path.join(photo_directory, image_name)

        # Sauvegarder l'image
        image.save(image_path)
        print(f"Image sauvegardée : {image_path}")

        # Gérer la limite des photos
        manage_photo_limit()

    except Exception as e:
        print("Erreur lors de l'interprétation de l'image :", e)

    # Réinitialiser les données après traitement
    image_data.clear()

# Fonction appelée lors de la connexion au broker
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connecté au broker MQTT avec succès")
        client.subscribe([(mqtt_topic_Photos, 0), (mqtt_topic_Batterie, 0)])  # S'abonner aux topics
        print(f"Abonné aux topics '{mqtt_topic_Photos}' et '{mqtt_topic_Batterie}'")
    else:
        print("Échec de la connexion, code de retour :", rc)

# Configuration du client MQTT
client = mqtt.Client("image_receiver")
client.username_pw_set(mqtt_user, mqtt_pass)  # Configuration des identifiants
client.on_connect = on_connect
client.on_message = on_message

# Connexion au broker MQTT
print("Connexion au broker MQTT...")
client.connect(mqtt_broker, mqtt_port)

# Boucle d'attente des messages avec traitement périodique de l'image
try:
    client.loop_start()
    while True:
        # Traiter et afficher l'image toutes les secondes si des données sont disponibles
        time.sleep(1)
        if image_data:
            process_and_store_image()
except KeyboardInterrupt:
    print("Déconnexion du client MQTT")
    client.loop_stop()
    client.disconnect()
