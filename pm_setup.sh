# pm_setup.sh: shell script to provision vagrant vm's
# Copyright (C) 2013 Jerome Rasky
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/license/>.
#
# Contact the author of this software at <jerome@rasky.co>.

apt-get update
apt-get dist-upgrade -y
apt-get install -y python-pip
pip install --upgrade "django<1.5"
pip install --upgrade "django-pipeline"
pip install --upgrade "distribute"
pip install --upgrade "django-grappelli<2.5.0"
pip install --upgrade "django-html5"
pip install --upgrade "django-haystack"
pip install --upgrade "whoosh"
pip install --upgrade "django-widget-tweaks"
pip install --upgrade "django_select2"
python /vagrant/project_management/manage.py syncdb --noinput
python /vagrant/project_management/manage.py loaddata /vagrant/project_management/initial_data.json
python /vagrant/project_management/manage.py rebuild_index --noinput
python /vagrant/project_management/manage.py collectstatic --link --noinput
