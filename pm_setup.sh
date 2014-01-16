# pm_setup.sh: shell script to provision vagrant vm's

apt-get update
apt-get dist-upgrade -y
apt-get install -y python-pip
pip install --upgrade "django"
pip install --upgrade "django-pipeline"
pip install --upgrade "distribute"
pip install --upgrade "django-grappelli"
pip install --upgrade "django-html5"
pip install --upgrade "django-haystack"
pip install --upgrade "whoosh"
pip install --upgrade "django-widget-tweaks"
pip install --upgrade "django_select2"
pip install --upgrade "python-dateutil"
python /vagrant/project_management/manage.py syncdb --noinput
python /vagrant/project_management/manage.py loaddata /vagrant/project_management/initial_data.json
python /vagrant/project_management/manage.py rebuild_index --noinput
python /vagrant/project_management/manage.py collectstatic --link --no-post-process --noinput
