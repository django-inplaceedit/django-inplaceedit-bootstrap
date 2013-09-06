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

from django.contrib import admin

from testing.app.models import Chunk, Alert, Panel, ListGroup


class ChunkAdmin(admin.ModelAdmin):
    pass


class AlertAdmin(admin.ModelAdmin):
    pass


class PanelAdmin(admin.ModelAdmin):
    pass


class ListGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(Chunk, ChunkAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Panel, PanelAdmin)
admin.site.register(ListGroup, ListGroupAdmin)
