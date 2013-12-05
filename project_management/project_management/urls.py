# urls.py: deployment-specific URLs, including some required for the tasks submodule
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
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import tasks.urls

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^', include(tasks.urls, namespace="tasks"))
)
