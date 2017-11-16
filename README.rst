NYC Mass Transit Countdown Clock
================================

|Build Status|

Copyright Shawn Tolidano, All Rights Reserved.

| Say something

What is this?
-------------

-  Say something

Say something

Quickstart
----------

Using NYC Mass Transit Countdown Clock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you just want to jump in and use it, follow this simple set of steps:


1. MTA API Key

In code, if you've followed the above, you would do the following:

::

    from __future__ import print_function
    _CONFIG_FILE=/path/to/config_file

Setup for Development
~~~~~~~~~~~~~~~~~~~~~

If you are interested in doing development on NYCMTCC, you need the
following packages:
- python (sudo yum install python27, sudo apt-get install python)
- python development (sudo yum install python27-devel, sudo apt-get install python-devel)
- pip (sudo yum install python27-pip, sudo apt-get install python-pip)
- virtualenv (sudo pip install virtualenv) 
- make (sudo yum install make, sudo apt-get install make)

You run: 
- make venv (create a virtualenv) 
- ``make active`` (activate the virtualenv note the backticks matter) 
- make dev (setuptools for development)

Now you’re ready to develop.

Be sure to: #. Keep code coverage over 90% #. Write relevant unit tests
#. Write Python doc strings #. Regenerate coverage and docs (make
covhtml and make docs)

How This Works
--------------

Say something

Caching values
--------------

If you want to cache values, consider also adding:
`pylru <https://pypi.python.org/pypi/pylru/>`__ Then you can write a
function in your codebase like:

.. code:: python

    import pylru
    TODO: WRITE CODE
    @lrudecorator(100)
    def get_countdown(line, station):
        return countdown.get(section, secret)

Building documentation
----------------------

To build the documentation from the python docstrings, run:

::

    make docs

And you can browse those here: <NYC\_TRANSIT\_COUNTDOWN>/docs/html/index.html

Running tests
-------------

All tests are in the nyc\_transit\_countdown/test/ directory. To run them do the
following:

::

    make test

You can also generate a coverage report:

::

    make cov

You can generate the HTML version:

::

    make covhtml

You can browse this locally from:
<NYC\_TRANSIT\_COUNTDOWN>/docs/cov/index.html

.. |Build Status| image:: https://circleci.com/gh/tolidano/nyc-transit-countdown/tree/master.svg?style=svg&circle-token=CIRCLE_TOKEN
:target: https://circleci.com/gh/tolidano/nyc-transit-countdown/tree/master
