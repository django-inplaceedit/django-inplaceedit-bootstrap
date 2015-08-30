django-inplaceedit-bootstrap test project
=========================================
Project to reproduce errors for others to debug it.

default login : test
default password : testtest

Howto
======

Create a virtual env

::

    $ virtualenv virt-inplaceedit

Get in and activate the env

::

    $ source virt-inplaceedit/bin/activate

Install the required packages

::

    $ pip install Django
    $ pip install Pillow (the version depends on your Python version)
    $ pip install django-inplaceedit==1.4.1
    $ pip install django-inplaceedit-extra-fields==0.6.1
    $ pip install sorl-thumbnail==12.3
    $ pip install django-bootstrap3-datetimepicker==2.2.3
    $ python setup.py develop
    $ cd testing

Install django-transmeta, if you want test this integration

::

    $ pip install django-transmeta==0.7.3

Create db and load fixtures

::

    python manage.py migrate (syncdb if you are useing a old Django version)

Start the debug server

::

    $ python manage.py runserver

Do your stuffs
