# ADC - PWM

Cette partie conciste à apprendre à utiliser les convertisseurs analogique/numérique et à utiliser le PWM :

## Explications du code 
Le script commence par importer des bibliothèques nécessaires. utime est utilisé pour les temporisations, comme sleep(), tandis que machine permet d'interagir avec le matériel, notamment les broches GPIO, la modulation de largeur d'impulsion (PWM) pour le buzzer, les temporisateurs (Timer) et la lecture de valeurs analogiques (ADC).

Il initialise ensuite le buzzer sur la broche GPIO 18 et configure un ADC sur la broche 1 pour lire un potentiomètre, qui contrôle le volume. Deux variables sont définies : NWait, qui détermine le temps d'attente entre les notes, et VPot, qui fixe le volume initial.

Une fonction d'interruption appelée routine est définie pour mettre à jour VPot en lisant régulièrement la valeur du potentiomètre. Cette interruption est défini sur un timer qui attend 10ms avant de déclencher l'interruption.

Le code définit des fonctions pour chaque note musicale (DO, RE, MI, FA, SOL, LA, SI). Chacune de ces fonctions configure la fréquence du buzzer pour la note correspondante, définit le volume à partir de VPot, joue la note pendant une durée spécifiée, puis éteint le buzzer.

La fonction BirthdaySong() joue les notes dans l'ordre pour la chanson "Joyeux Anniversaire", en insérant des pauses entre les notes. De manière similaire, MarioSong() joue une séquence de notes inspirée de Mario.

Enfin, une boucle infinie est mise en place pour jouer alternativement les deux chansons, avec une pause d'une seconde entre chaque répétition. Cela permet de jouer des mélodies simples en utilisant un buzzer et un potentiomètre pour ajuster le volume. Les fonctions de notes sont conçues de manière modulaire pour faciliter l'ajout de nouvelles mélodies à l'avenir.

## FlowChart Diagramme
![image](https://github.com/user-attachments/assets/4ac526fb-3340-475b-ba2b-d14a999872ad)

