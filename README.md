# Olist

## Installation
- Installer un environnement virtuel :

    - Windows :

    `py -m venv .env`

    - Linux ou Mac OS :

    `python3 -m venv .env` ou `python -m venv .env`

- Lancer l'environnement virtuel :

    - Windows :

    `.env\Scripts\activate`

    - Linux ou Mac OS :

    `source .env/bin/activate`

- Installer les différents packages (Django, ...) :

    `pip install -r requirements.txt`

- Créer la base de données sur PostgreSQL :

    - Paramètres de configuration :

        - Name : Olist
        - User : postgres
        - Password : 0000

- Effectuer les premières migrations :

    - Windows :

    `py manage.py makemigrations`

    `py manage.py migrate`

    - Linux ou Mac OS :

    `python3 manage.py makemigrations` ou `python manage.py makemigrations`

    `python3 manage.py migrate` ou `python manage.py migrate`

- Lancer le serveur Django

    - Vérifier que l'environnement virtuel est lancé et que vous êtes bien dans le dossier `src` :

        - Windows :

        `py manage.py runserver`

        - Linux ou Mac OS :

        `python3 manage.py runserver` ou `python manage.py runserver`