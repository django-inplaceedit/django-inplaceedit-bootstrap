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


from django.db import models
from django.utils.translation import ugettext_lazy as _


class Chunk(models.Model):

    key = models.CharField(verbose_name=_(u'key'),
                           max_length=100)
    text = models.TextField(verbose_name=_(u'Text'))

    class Meta:
        verbose_name = _('Chunk')
        verbose_name_plural = _('Chunks')

    def __unicode__(self):
        return self.text


class Alert(models.Model):

    msg = models.TextField(verbose_name=_(u'Msg'))

    class Meta:
        verbose_name = _('Alert')
        verbose_name_plural = _('Alerts')

    def __unicode__(self):
        return self.msg


class Panel(models.Model):

    title = models.CharField(verbose_name=_(u'Title'),
                             max_length=100)
    content = models.TextField(verbose_name=_(u'Content'))

    class Meta:
        verbose_name = _('Panel')
        verbose_name_plural = _('Panels')

    def __unicode__(self):
        return self.title


class ListGroup(models.Model):

    title = models.CharField(verbose_name=_(u'Title'),
                             max_length=100)
    subtitle = models.CharField(verbose_name=_(u'Subtitle'),
                                max_length=100)
    content = models.TextField(verbose_name=_(u'Content'))

    class Meta:
        verbose_name = _('ListGroup')
        verbose_name_plural = _('ListGroups')

    def __unicode__(self):
        return self.title
