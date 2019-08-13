#!/bin/sh
systemctl stop my_flask_web
sudo yum -y install python-pip
pip install virtualenv
cd /demos/form
virtualenv .venv
source .venv/bin/activate
pip install -U setuptools
pip install gunicorn
pip install greenlet
pip install gevent
pip install setproctitle
pip install -r requirements.txt
cp my_flask_web.service /usr/lib/systemd/system
systemctl daemon-reload
systemctl enable my_flask_web
systemctl start my_flask_web