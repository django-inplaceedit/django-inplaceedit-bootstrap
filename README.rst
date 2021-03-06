.. contents::

============================
django-inplaceedit-bootstrap
============================

Information
===========

.. image:: https://badge.fury.io/py/django-inplaceedit-bootstrap.png
    :target: https://badge.fury.io/py/django-inplaceedit-bootstrap


Integration of `django-inplaceedit <http://pypi.python.org/pypi/django-inplaceedit/>`_ with `bootstrap 3 <http://getbootstrap.com/>`_

It is distributed under the terms of the `GNU Lesser General Public
License <http://www.gnu.org/licenses/lgpl.html>`_.

This egg would not have been possible without the help of `Tyrdall <https://github.com/django-inplaceedit/django-inplaceedit/pull/33>`_

Requirements
============

 * `django-inplaceedit <http://pypi.python.org/pypi/django-inplaceedit/>`_ (== 1.4.1)
 * `Bootstrap <https://github.com/twbs/bootstrap/archive/v3.3.5.zip>`_  (== 3.3.5)
 * `django-inplace-edit-extra-fields <http://pypi.python.org/pypi/django-inplaceedit-extra-fields/>`_ (== 0.6.1, optional but recommended)
 * `django-bootstrap3-datetimepicker <http://pypi.python.org/pypi/django-bootstrap3-datetimepicker/>`_ (== 2.2.3, optional but recommended)

Demo (this video use a very old version of django-inplaceedit and django-inplaceedit-extra-fields)
==================================================================================================

Video Demo, of `django-inplaceedit <http://pypi.python.org/pypi/django-inplaceedit/>`_, `django-inplaceedit-extra-fields <http://pypi.python.org/pypi/django-inplaceedit-extra-fields>`_ and `django-inlinetrans <http://pypi.python.org/pypi/django-inlinetrans>`_ (Set full screen mode to view it correctly)


.. image:: https://github.com/django-inplaceedit/django-inplaceedit/raw/master/video-frame.png
   :target: http://www.youtube.com/watch?v=_EjisXtMy_Y?t=34s

**Attention**: This demo is not a demo of this package, in this video there are not any inegration with bootstrap. Please to see a demo use the `testing django project <https://github.com/django-inplaceedit/django-inplaceedit-bootstrap/tree/master/testing/>`_.

Installation
============

After installing `django-inplaceedit egg`_ (1.4.1)


.. _`django-inplaceedit egg`: https://django-inplaceedit.readthedocs.org/en/latest/install.html


After installing `django-inplaceedit-extra-fields egg`_ (0.6.1, this is optional but recommended)


.. _`django-inplaceedit-extra-fields egg`: https://pypi.python.org/pypi/django-inplaceedit-extra-fields#installation

And after installing `django-bootstrap3-datetimepicker egg`_ (2.2.3, this is optional but recommended)


.. _`django-bootstrap3-datetimepicker egg`: https://pypi.python.org/pypi/django-bootstrap3-datetimepicker


In your settings.py
-------------------

::

    INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        'django.contrib.admin',
        #.....................#
        'inplaceeditform_bootstrap',  # it is very important that this app is before that inplaceeditform and inplaceeditform_extra_fields
        'inplaceeditform',
        'inplaceeditform_extra_fields',  # this is optional but recommended
        'bootstrap3_datetime', # this is optional but recommended
    )

    ...
    # Optional, but recommended

    ADAPTOR_INPLACEEDIT = {}
    if 'inplaceeditform_extra_fields' in INSTALLED_APPS:
        ADAPTOR_INPLACEEDIT['tiny'] = 'inplaceeditform_extra_fields.fields.AdaptorTinyMCEField'
        # You can add the other adaptors of inplaceeditform_extra_fields
        # https://pypi.python.org/pypi/django-inplaceedit-extra-fields#installation
    if 'bootstrap3_datetime' in INSTALLED_APPS:
        ADAPTOR_INPLACEEDIT['date'] = 'inplaceeditform_bootstrap.fields.AdaptorDateBootStrapField'
        ADAPTOR_INPLACEEDIT['datetime'] = 'inplaceeditform_bootstrap.fields.AdaptorDateTimeBootStrapField'

    INPLACEEDIT_EDIT_TOOLTIP_TEXT = 'Please doubleclick to edit'

If you want, you can register these fields in your settings with different keys:

::

    ...

    if 'bootstrap3_datetime' in INSTALLED_APPS:
        ADAPTOR_INPLACEEDIT['date_bootstrap'] = 'inplaceeditform_bootstrap.fields.AdaptorDateBootStrapField'
        ADAPTOR_INPLACEEDIT['datetime_bootstrap'] = 'inplaceeditform_bootstrap.fields.AdaptorDateTimeBootStrapField'

And after that, to want use a specific adaptor you can pass it to the templatetag, e.g.:

::

   {% inplace_edit "content.field_name" adaptor="date_bootstrap" %}
   {% inplace_edit "content.field_name" adaptor="datetime_bootstrap" %}



Why this code is not in django-inplaceedit?
===========================================

 * This code depends on the bootstrap
 * This is a specific solution


Testing
=======

Exists a `testing django project <https://github.com/django-inplaceedit/django-inplaceedit-bootstrap/tree/master/testing/>`_. This project can use as demo project.

This project overwrites the default options of `django-inplaceedit <http://pypi.python.org/pypi/django-inplaceedit/>`_ and a default option of django-inplaceedit-bootstrap

::

    INPLACEEDIT_AUTO_SAVE = True
    INPLACEEDIT_EVENT = 'click'
    INPLACEEDIT_EDIT_TOOLTIP_TEXT = 'Click to edit'  # This option is of django-inplaceedit-bootstrap


Development
===========

You can get the bleeding edge version of django-inplaceedit-bootstrap by doing a clone
of its git repository::

    git clone git@github.com:django-inplaceedit/django-inplaceedit-bootstrap.git
