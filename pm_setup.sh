# pm_setup.sh: shell script to provision vagrant vm's

apt-get update
apt-get dist-upgrade -y
apt-get install -y python-pip
pip install --upgrade "django" "django-pipeline" "distribute" "django-grappelli" "django-html5" "django-haystack" "whoosh" "django-widget-tweaks" "django_select2" "python-dateutil"
python /vagrant/project_management/manage.py syncdb --noinput
python /vagrant/project_management/manage.py loaddata /vagrant/project_management/initial_data.json
python /vagrant/project_management/manage.py rebuild_index --noinput
python /vagrant/project_management/manage.py collectstatic --link --no-post-process --noinput
