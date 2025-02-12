🌡️📊 Système de Monitoring de Température et d’Humidité Basé sur Flask
📝 Présentation
Ce projet est une application web basée sur Flask qui lit les données de température et d'humidité à partir d'un capteur DHT connecté à un Arduino. Les données sont collectées via une communication série et affichées sur une interface web.

⚙️ Fonctionnalités
✅ Lecture des données de température et d'humidité via un capteur DHT.
✅ Affichage des relevés en temps réel sur une interface web.
✅ Utilisation de Flask et Flask-Bootstrap pour un frontend responsive.
✅ Collecte asynchrone des données grâce au threading.
✅ Communication avec le capteur via un port série (COM3, 9600 bauds).

🛠️ Technologies utilisées
🖥️ Python (Flask, Flask-Bootstrap) pour l’application web.
🔌 Arduino C++ pour l’acquisition des données du capteur.
🌡️ Capteur DHT pour les relevés de température et d’humidité.
🔄 Communication série pour le transfert des données.

🚀 Installation et Configuration
📌 Prérequis
🔹 Python 3 installé
🔹 Flask installé (pip install flask flask-bootstrap)
🔹 Arduino avec un capteur DHT

📂 Étapes
1️⃣ Cloner le dépôt
bash
Copy
Edit
git clone <repository-url>
cd <project-folder>
2️⃣ Connecter le matériel
🛠️ Composants matériels :
🖼️ (insérer image du matériel ici)

🔗 Connecter le capteur DHT à la broche 2 de l’Arduino.
🔌 Brancher l’Arduino à l’ordinateur.
3️⃣ Télécharger le code Arduino
🏗️ Ouvrir l’IDE Arduino.
📋 Copier et coller le code Arduino fourni.
🚀 L’envoyer vers la carte Arduino.
4️⃣ Lancer l’application Flask
bash
Copy
Edit
python app.py
5️⃣ Accéder à l’interface web
🌐 Ouvrir un navigateur et aller sur 👉 http://127.0.0.1:5000/

📁 Structure du projet
php
Copy
Edit
├── app.py            # 🖥️ Application Flask  
├── templates/  
│   ├── index.html    # 🎨 Template de l’interface web  
├── static/  
│   ├── styles.css    # 🎨 Feuille de styles CSS (si nécessaire)  
└── arduino_code.ino  # 🔌 Script Arduino pour le capteur  
🛠️ Explication du code Arduino
📌 Utilisation de la bibliothèque DHT.h pour la lecture des données du capteur.
📡 Envoi des données via communication série à intervalles réguliers.
⏳ Temps d’échantillonnage fixé à 3 minutes.

💻 Explication de l’application Flask
🔄 Démarrage d’un thread en arrière-plan pour collecter les données en continu.
🔌 Lecture des données du capteur via la communication série.
📊 Affichage des relevés en direct sur l’interface web.

🔮 Améliorations futures
📂 Stocker les données historiques dans une base de données.
📈 Ajouter des graphiques pour la visualisation des données.
☁️ Déployer l’application sur un serveur cloud.

📜 Licence
🔓 Ce projet est open-source. Vous êtes libre de l'utiliser et de le modifier !

