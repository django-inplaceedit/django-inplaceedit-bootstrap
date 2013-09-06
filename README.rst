.. contents::

===========================
Inplace Edit Form Bootstrap
===========================

Information
===========

.. image:: https://badge.fury.io/py/django-inplaceedit-bootstrap.png
    :target: https://badge.fury.io/py/django-inplaceedit-bootstrap

.. image:: https://pypip.in/d/django-inplaceedit-bootstrap/badge.png
    :target: https://pypi.python.org/pypi/django-inplaceedit-bootstrap

Integration of `django-inplaceedit <http://pypi.python.org/pypi/django-inplaceedit/>`_ with `bootstrap 3 <http://getbootstrap.com/>`_

It is distributed under the terms of the `GNU Lesser General Public
License <http://www.gnu.org/licenses/lgpl.html>`_.

This egg would not have been possible without the help of `Tyrdall <https://github.com/Yaco-Sistemas/django-inplaceedit/pull/33>`_

Requirements
============

 * `Django Inplace Edit (>= 1.1.0) <http://pypi.python.org/pypi/django-inplaceedit/>`_
 * `Bootstrap (3.0.0) <https://github.com/twbs/bootstrap/archive/v3.0.0.zip>`_ 
 * `Django Inplace Edit Extra fields (>= 0.1.0) <http://pypi.python.org/pypi/django-inplaceedit-extra-fields/>`_ (optional but recommended)

Demo (this video use a very old version of django-inplaceedit and django-inplaceedit-extra-fields)
==================================================================================================

Video Demo, of django-inplaceedit, `django-inplaceedit-extra-fields <http://pypi.python.org/pypi/django-inplaceedit-extra-fields>`_ and `django-inlinetrans <http://pypi.python.org/pypi/django-inlinetrans>`_ (Set full screen mode to view it correctly)


.. image:: https://github.com/Yaco-Sistemas/django-inplaceedit/raw/master/video-frame.png
   :target: http://www.youtube.com/watch?v=_EjisXtMy_Y

**Attention**: This demo is not a demo of this package, please use the testing project

Installation
============

After installing `django inplace edit egg`_


.. _`django inplace edit egg`: https://django-inplaceedit.readthedocs.org/en/latest/install.html


And after installing `django inplace edit extra fields egg`_ (this is optional but recommended)


.. _`django inplace edit extra fields egg`: https://pypi.python.org/pypi/django-inplaceedit-extra-fields#installation

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
    )


Why this code is not in django-inplaceedit?
===========================================

 * This code depends on the bootstrap
 * They are a specific solution


Testing
=======

Exists a `testing django project <https://github.com/goinnn/django-inplaceedit-bootstrap/tree/master/testing/>`_. This project can use as demo project.


Development
===========

You can get the leading edge version of inplaceedit-bootstrap by doing a checkout
of its repository:

  https://github.com/goinnn/django-inplaceedit-bootstrap
