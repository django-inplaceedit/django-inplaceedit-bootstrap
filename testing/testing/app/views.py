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
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from testing.app.models import Chunk, Alert, Panel, ListGroup


def index(request):
    return render_to_response('app/index.html',
                              {},
                              context_instance=RequestContext(request))
