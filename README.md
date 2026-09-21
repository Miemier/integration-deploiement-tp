# Intégration et Déploiement — TP Docker



Ce dépôt contient l'ensemble des travaux pratiques du module

*\*Intégration et Déploiement\*\*, organisés par dossier.



## Structure du dépôt



TP\_Docker/

├── ex3\_containers/      # Manipulation de base des conteneurs

├── ex4\_nginx/           # Création d'un serveur web avec Docker

├── ex5\_flask/           # Déploiement d'une application Python Flask

└── ex6\_flask\_mongo/     # Utilisation de docker compose (Flask + MongoDB)



## Tâches réalisées


| Exercice  | Objectif                                            | Statut    |
|-----|-----------------------------------------------------|-----------|
| Ex3 | Commandes Docker de base (pull, run, ps, rm, rmi)   | ✅ terminé |
| Ex4 | Lancer Nginx dans un conteneur avec mappage de port | ✅ terminé |
| Ex5 | Dockeriser une application Flask avec un Dockerfile | ✅ terminé |
| Ex6 | Orchestrer Flask + MongoDB avec docker compose      | ✅ terminé |




## Comment exécuter



Chaque dossier contient son propre Readme.md avec les commandes détaillées.

Pour tester l'ex6 (Flask + MongoDB avec Docker Compose) :

``` powershell
cd TP_Docker/ex6
docker compose up -d --build
```

Application : http://localhost:5000

Vérification connexion BDD : http://localhost:5000/db-check




## Auteur

**Mengyi YANG**

MIAGE IPM FI

22208372