.. contents::

============================
django-inplaceedit-bootstrap
============================

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

 * `django-inplace (>= 1.1.0) <http://pypi.python.org/pypi/django-inplaceedit/>`_
 * `Bootstrap (3.0.0) <https://github.com/twbs/bootstrap/archive/v3.0.0.zip>`_ 
 * `django-inplace-edit-extra-fields (>= 0.1.0) <http://pypi.python.org/pypi/django-inplaceedit-extra-fields/>`_ (optional but recommended)

Demo (this video use a very old version of django-inplaceedit and django-inplaceedit-extra-fields)
==================================================================================================

Video Demo, of django-inplaceedit, `django-inplaceedit-extra-fields <http://pypi.python.org/pypi/django-inplaceedit-extra-fields>`_ and `django-inlinetrans <http://pypi.python.org/pypi/django-inlinetrans>`_ (Set full screen mode to view it correctly)


.. image:: https://github.com/Yaco-Sistemas/django-inplaceedit/raw/master/video-frame.png
   :target: http://www.youtube.com/watch?v=_EjisXtMy_Y?t=34s

**Attention**: This demo is not a demo of this package, in this video there are not any inegration with bootstrap. Please to see a demo use the `testing django project <https://github.com/goinnn/django-inplaceedit-bootstrap/tree/master/testing/>`_.

Installation
============

After installing `django-inplaceedit egg`_


.. _`django-inplaceedit egg`: https://django-inplaceedit.readthedocs.org/en/latest/install.html


And after installing `django-inplaceedit-extra-fields egg`_ (this is optional but recommended)


.. _`django-inplaceedit-extra-fields egg`: https://pypi.python.org/pypi/django-inplaceedit-extra-fields#installation

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
 * This is a specific solution


Testing
=======

Exists a `testing django project <https://github.com/goinnn/django-inplaceedit-bootstrap/tree/master/testing/>`_. This project can use as demo project.

This project overwrites the default options of `django-inplace <http://pypi.python.org/pypi/django-inplaceedit/>`_

::

    INPLACEEDIT_AUTO_SAVE = True
    INPLACEEDIT_EVENT = "click"



Development
===========

You can get the bleeding edge version of django-inplaceedit-bootstrap by doing a clone
of its git repository:

  git clone git@github.com:goinnn/django-inplaceedit-bootstrap.git
