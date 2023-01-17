Installation
============

User Installation
-----------------

As a user, install from pypi:

.. code-block:: shell

    $ pip install project-template-python-pure

Or ``conda-forge``:

.. code-block:: shell

    $ mamba install -c conda-forge project-template-python-pure



Developer Setup
---------------

As a developer, clone the repository, create a virtual environment
and then install the package in development mode:

.. code-block:: shell

   $ git clone git@gitlab.cta-observatory.org:cta-computing/documentation/python-project-template
   $ cd python-project-template
   $ python -m venv venv
   $ source venv/bin/activate
   $ pip install -e .[test,doc,dev]

The same also works with conda, create a conda env instead of a venv above.
