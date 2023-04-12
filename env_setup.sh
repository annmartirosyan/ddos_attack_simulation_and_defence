#!/bin/bash

sudo apt update
sudo apt install nginx
sudo ufw enable
sudo ufw allow "Nginx HTTP"
sudo ufw allow "OpenSSH"
systemctln status nginx
sudo apt install python3-pip
sudo pip install virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/Devel
source /usr/local/bin/virtualenvwrapper.sh
workon
mkvirtualenv wagtailbakerydemo
git clone https://github.com/wagtail/bakerydemo.git
cd bakerydemo/
pip install -r requirements/development.txt
cp bakerydemo/settings/local.py.example bakerydemo/settings/local.py
touch .env
./manage.py migrate
./manage.py load_initial_data
./manage.py runserver
pip install gunicorn
cd /etc/nginx/sites-available/
nano django.conf
# add the content of django.conf located in this repository
nginx -t
sudo ln django.conf /etc/nginx/sites-enabled/
cd ../sites-enabled/
sudo service nginx restart
sudo service nginx status
sudo apt update && sudo apt install supervisor
sudo systemctl status supervisor
cd /etc/supervisor/
cd /etc/supervisor/conf.d/
nano gunicorn.conf
# add the content of gunicorn.conf located in this repository
sudo mkdir /var/log/gunicorn
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status
sudo ufw allow 80
sudo ufw status
sudo nginx -t
sudo service nginx restart
sudo service nginx status
history >> history.txt

