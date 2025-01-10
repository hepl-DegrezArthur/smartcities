# ESP32-CAM Version 2

## Description

Cette deuxième version de la carte **ESP32-CAM** apporte plusieurs améliorations significatives pour optimiser ses performances et son utilisation.  

### Nouveautés

- **Nouveau régulateur LDO**  
  Implémentation d'un régulateur offrant des performances améliorées, particulièrement adaptées à l'utilisation du Wi-Fi.  

- **Pont diviseur pour ADC2**  
  Intégration d'un pont diviseur pour convenir à la plage de tension de l'ADC.  

- **Modifications de connectique**  
  Ajustements pour améliorer la compatibilité et simplifier les branchements.  

- **Nouveau logo**  
  Mise à jour du design pour meilleur rendu.

Note : Toutes les connexions sont indiquées sur le PCB (à l'aide de texte ou de schémas) afin d'éviter toute erreur. 

# Remarques Techniques


## Problème de Pins sur l'ESP32-CAM

- Deux pins de l'ESP32-CAM ont été coupées en raison de problèmes techniques :  
  - **Pin 1 (GND)** : Bien que censée être une masse, cette pin provoquait des erreurs et des chutes de tension lors de son utilisation.  
  - **Autre pin** : Coupée par erreur lors des manipulations.  

Ces ajustements ont été nécessaires pour éviter les dysfonctionnements et garantir la stabilité de la carte.

## Améliorations Proposées

- **LED IR** :  
  Actuellement connectée directement à une sortie IO de l'ESP32, la LED IR ne bénéficie que d'un courant d'environ **20 mA**, ce qui est insuffisant pour une luminosité optimale.  
  - **Proposition** : Intégrer un système basé sur un MOSFET pour augmenter le courant disponible, offrant ainsi plus de courant à la LED IR.

