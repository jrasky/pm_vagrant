# shell script to provision vagrant vm's

apt-get update
apt-get dist-upgrade -y
apt-get install -y python-pip libmysqlclient-dev python-dev
pip install --upgrade "django<1.5"
pip install --upgrade "django-pipeline"
pip install --upgrade "distribute"
pip install --upgrade "django-grappelli<2.5.0"
pip install --upgrade "django-html5"
pip install --upgrade "django-haystack"
pip install --upgrade "whoosh"
pip install --upgrade "django-widget-tweaks"
python /vagrant/project_management/manage.py syncdb --noinput
python /vagrant/project_management/manage.py loaddata /vagrant/project_management/initial_data.json
python /vagrant/project_management/manage.py rebuild_index --noinput
python /vagrant/project_management/manage.py collectstatic --noinput
