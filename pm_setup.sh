apt-get update
apt-get dist-upgrade -y
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password password pm_django'
debconf-set-selections <<< 'mysql-server-5.5 mysql-server/root_password_again password pm_django'
apt-get install -y mysql-server python-pip libmysqlclient-dev python-dev yui-compressor
mysql -u root -ppm_django <<< 'create database project_management'
pip install "django<1.5"
pip install "django-pipeline"
pip install -U "distribute"
pip install "mysql-python"
pip install "django-grappelli<2.5.0"
pip install "django-html5"
python /vagrant/project_management/manage.py syncdb --noinput
python /vagrant/project_management/manage.py loaddata /vagrant/project_management/initial_data.json
python /vagrant/project_management/manage.py collectstatic --noinput
