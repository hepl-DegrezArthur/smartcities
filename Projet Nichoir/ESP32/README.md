# Codes du Projet Nichoir

## Description

Ce répertoire contient l'ensemble des codes développés pour la création du **code principal du Nichoir**.  
Vous y trouverez :  
- Tous les codes intermédiaires de développement.  
- Les différentes versions du code principal, permettant de retracer l'évolution du projet.
  

# Remarques Techniques

## Optimisations Disponibles

- **Gestion de la consommation** :  
  Des améliorations peuvent être apportées pour optimiser l'activation des différents composants. L'objectif est d'éviter une consommation simultanée excessive de courant, ce qui pourrait affecter la stabilité de l'ESP32.

- **Gestion des réveils par le capteur IR** :  
  Actuellement, le capteur IR pourrait provoquer de multiples réveils de l'ESP32 en peu de temps, ce qui pourrait entraîner une surconsommation ou simplement trop de photos. Il serait alors possible de mettre en place un mécanisme pour limiter le nombre de réveils sur une période donnée.
