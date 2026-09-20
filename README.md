\# Intégration et Déploiement — TP Docker



Ce dépôt contient l'ensemble des travaux pratiques du module

\*\*Intégration et Déploiement\*\*, organisés par dossier.



\## Structure du dépôt



TP\_Docker/

├── ex1\_containers/      # Manipulation de base des conteneurs

├── ex2\_nginx/           # Création d'un serveur web avec Docker

├── ex3\_flask/           # Déploiement d'une application Python Flask

└── ex4\_flask\_mongo/     # Utilisation de docker compose (Flask + MongoDB)



\## Tâches réalisées



| TP | Objectif | Statut |

|----|----------|--------|

| Ex 1 | Commandes Docker de base (pull, run, ps, rm, rmi) | à faire |

| Ex 2 | Lancer Nginx dans un conteneur avec mappage de port | à faire |

| Ex 3 | Dockeriser une application Flask avec un Dockerfile | à faire |

| Ex 4 | Orchestrer Flask + MongoDB avec docker compose | à faire |



\## Comment exécuter



Chaque dossier contient son propre Readme.md avec les commandes détaillées.



Pour le TP4 (Flask + MongoDB) :



&#x20;   cd TP\_Docker/ex4\_flask\_mongo

&#x20;   docker compose up -d --build

&#x20;   curl http://localhost:5000/health



