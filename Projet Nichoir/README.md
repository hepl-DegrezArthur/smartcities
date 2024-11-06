# Projet Nichoir

## Objectifs du projet
Ce projet a pour objectif de créer un nichoir intelligent et connecté qui permet de suivre la vie des oiseaux avec un coût accessible et une autonomie énergétique prolongée. 
Les différents objectifs de ce projet sont : 
- Surveiller l'activité dans un nichoir via un système de détection de mouvement et de capture d'image
- Diminuer la consommation pour une autonomie utile pour une longue utilisation
- Publier les données (images) avec une mise en page

## Fonctionnement du système
Détection de mouvement : 
- Un capteur PIR détecte la présence d'oiseaux dans le nichoir
- Lorsqu'un mouvement est détecté, l'ESP32-CAM capture une photo avec un éclairage IR.

Transmission des données : 
- La photo est envoyée au Raspberry Pi via Wi-Fi pour être traitée et stockée en MQTT.
- Le raspberry Pi transmet ensuite les photos vers un serveur cloud afin de pouvoir les visualiser

Niveau de batterie : 
- Mode standby - En absence de mouvement dans le nichoir, le système se réveille une seule fois par jour et envoie le niveau de la batterie en MQTT.
- Mode présence - Lorsque le capteur PIR détecte un mouvement, le niveau de la batterie est associé à chaque photo capturée.

Diagramme représentant le fonctionnement du système : 
![image](https://github.com/user-attachments/assets/c9697f7c-cb90-435d-8cbe-d75e76c01bf4)


