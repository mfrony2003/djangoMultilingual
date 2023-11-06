py -m venv venv
python.exe -m pip install --upgrade pip
pip install django
django-admin  startproject conf .
mkdir apps
cd apps
pip freeze > requirements.txt
django-admin startapp multilungualSite