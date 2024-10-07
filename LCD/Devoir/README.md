# Devoir LCD-DHT11

## Explications du code 
Le système surveille en continu la température et l'humidité ambiantes, et ajuste le comportement de la LED et du buzzer en fonction d'une température de référence réglée par le potentiomètre. Plusieurs bibliothèques sont utilisées : lcd1602 pour l'affichage sur écran LCD via I2C, utime pour la gestion du temps, machine pour interagir avec les périphériques matériels (I2C, ADC, PWM, Timer, GPIO), et dht11 pour lire les valeurs de température et d'humidité. La LED est connectée à la broche GPIO 20 et sert de retour visuel. Le buzzer est connecté à la broche GPIO 18 via PWM pour la sortie sonore. Le potentiomètre est connecté à la broche ADC 0 et permet de définir la température de référence (Vset). Le capteur DHT11 est connecté à la broche GPIO 16 pour mesurer la température et l'humidité. 
Un écran LCD 16x2 est utilisé pour afficher la température, l'humidité et des messages d'alerte comme "ALARM" lorsque la température dépasse une certaine limite. 
Le code inclut une routine d'interruption avec un timer pour basculer l'état de la LED à des intervalles réguliers. Si la température ambiante dépasse de plus de 3°C la température de référence, une alarme sonore est déclenchée via le buzzer, et un message d'alerte est affiché sur l'écran LCD. Le programme fonctionne en boucle infinie, lisant en continu la température et l'humidité du capteur DHT11, ainsi que la valeur du potentiomètre pour ajuster la température de référence. 
Il compare ensuite la température ambiante avec cette référence et adapte le comportement du système en conséquence.


## ChartFlow Diagramme
![image](https://github.com/user-attachments/assets/5e6725c6-cd55-4284-8f87-3d19dff9bb39)
