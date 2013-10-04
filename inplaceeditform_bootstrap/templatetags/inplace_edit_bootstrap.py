# -*- coding: utf-8 -*-
# Copyright (c) 2013 by Pablo Martín <goinnn@gmail.com>
#
# This software is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.
from django.template import Library

from inplaceeditform_bootstrap import settings as inplaceeditform_bootstrap_settings

register = Library()


def inplace_bootstrap_extra_options(context):
    return {
        'tooltip_text': inplaceeditform_bootstrap_settings.INPLACEEDIT_EDIT_TOOLTIP_TEXT,
    }
register.inclusion_tag("inplaceeditform_bootstrap/extra_options.html", takes_context=True)(inplace_bootstrap_extra_options)
