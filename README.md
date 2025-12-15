
## Description

Ce projet est un **dashboard de monitoring système en temps réel** qui collecte et affiche des informations détaillées sur les performances et l'état d'un ordinateur.

Le dashboard permet de surveiller :
- Les informations système
- L'utilisation du processeur
- La consommation de la RAM
- L'espace disque disponible
- Les processus les plus gourmands
- Une analyse statistique des fichiers du répertoire Desktop

## Prérequis

- **Python 3.7+** installé

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/ertan-yilzid/AAA
```

### 2. Installer les dépendances Python

Le projet nécessite la bibliothèque `psutil` pour collecter les informations système :

```bash
pip3 install psutil
```

## Utilisation

### Lancer le script de monitoring

1. Ouvrez un terminal dans le répertoire du projet
2. Lancez le script Python :

```bash
python3 monitor.py
```

### Visualiser le dashboard

1. Ouvrez le fichier `index.html` dans votre navigateur web
2. La page se rafraîchit automatiquement toutes les secondes

**Note :** Le script Python doit rester en cours d'exécution pour que les données continuent à être mises à jour.

### Arrêter le monitoring

Pour arrêter le script, utilisez `Ctrl+C` dans le terminal.

## Fonctionnalités

### Informations Système
- Hostname
- Système d'exploitation
- Heure de démarrage
- Durée de fonctionnement
- Utilisateurs
- Adresse IP

### Monitoring CPU
- Nombre de cœurs (physiques et logiques)
- Fréquences (actuelle, minimale, maximale)
- Pourcentage d'utilisation globale
- Barre de progression visuelle

### Monitoring RAM
- Mémoire totale disponible
- Mémoire utilisée et disponible
- Pourcentage d'utilisation
- Barre de progression visuelle

### Monitoring Disque
- Espace total, utilisé et libre
- Pourcentage d'utilisation
- Barre de progression visuelle

### Analyse des Processus
Trois classements distincts des processus :
1. Top 3 CPU
2. Top 3 Memory
3. Top 3 Overall

Pour chaque processus : PID, nom, pourcentage CPU et mémoire

### Analyse de Fichiers
- Répertoire surveillé
- Nombre total de fichiers
- Taille totale du répertoire
- Statistiques par type de fichier (.txt, .py, .pdf, .jpg)
- Pourcentage de chaque type de fichier

## Captures d'écran
Terminal

![alt text](https://github.com/ertan-yilzid/AAA/blob/main/screenshots/terminal.png)

Site

![alt text](https://github.com/ertan-yilzid/AAA/blob/main/screenshots/site.png)

## Auteur

**Challenge Triple A - Projet de Monitoring Système**

@***

