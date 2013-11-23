# shell script to provision vagrant vm's

apt-get update
apt-get dist-upgrade -y
apt-get install -y python-pip libmysqlclient-dev python-dev yui-compressor
pip install "django<1.5"
pip install "django-pipeline"
pip install "distribute"
pip install "django-grappelli<2.5.0"
pip install "django-html5"
python /vagrant/project_management/manage.py syncdb --noinput
python /vagrant/project_management/manage.py loaddata /vagrant/project_management/initial_data.json
python /vagrant/project_management/manage.py collectstatic --noinput
