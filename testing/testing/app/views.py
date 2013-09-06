# -*- coding: utf-8 -*-
# Copyright (c) 2013 by Pablo Martín <goinnn@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this programe.  If not, see <http://www.gnu.org/licenses/>.
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from testing.app.models import Title, Chunk, Alert, Panel


def index(request):
    extra_fields = False
    if 'inplaceeditform_extra_fields' in settings.INSTALLED_APPS:
        extra_fields = True
    alerts = Alert.objects.all()
    panels = Panel.objects.all()
    title = get_object_or_404(Title, key="title")
    alert_title = get_object_or_404(Title, key="alert_title")
    panel_title = get_object_or_404(Title, key="panel_title")
    well_title = get_object_or_404(Title, key="well_title")
    chunk_content = get_object_or_404(Chunk, key="content")
    chunk_well_content = get_object_or_404(Chunk, key="well_content")
    return render_to_response('app/index.html',
                              {'alerts': alerts,
                               'panels': panels,
                               'title': title,
                               'chunk_content': chunk_content,
                               'alert_title': alert_title,
                               'panel_title': panel_title,
                               'well_title': well_title,
                               'chunk_well_content': chunk_well_content,
                               'extra_fields': extra_fields},
                              context_instance=RequestContext(request))
