pandas-datareader, with Interactive Brokers Gateway
=================

I'm using this fork to add Interactive Brokers Gateway to Pandas Datareader.

This package relies on a IB Gateway being active at its default location: https://localhost:5000.  You can get the Gateway `here <https://www.interactivebrokers.com/en/index.php?f=16457>`_.  Getting started guide is `here <https://interactivebrokers.github.io/cpwebapi/>`_ for running the service.

Usage
-----

.. code-block:: python

   import requests
   import pandas_datareader as pdr

   session = requests.Session()
   session.verify = False #required due to self-signed SSL cert
   
   pdr.ib.time_series.IBTimeSeriesReader(symbols='396336017', period = '1w', bar = '1h', session = session).read()

Future Work
-----------

If anyone at Interactive Brokers is watching, please surface options data and an isTruncated flag!

Pandas Datareader readme continues below.

pandas-datareader
=================

Up to date remote data access for pandas, works for multiple versions of pandas.

.. image:: https://img.shields.io/pypi/v/pandas-datareader.svg
    :target: https://pypi.python.org/pypi/pandas-datareader/

.. image:: https://travis-ci.org/pydata/pandas-datareader.svg?branch=master
    :target: https://travis-ci.org/pydata/pandas-datareader

.. image:: https://coveralls.io/repos/pydata/pandas-datareader/badge.svg?branch=master
    :target: https://coveralls.io/r/pydata/pandas-datareader

.. image:: https://codecov.io/gh/pydata/pandas-datareader/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/pydata/pandas-datareader

.. image:: https://readthedocs.org/projects/pandas-datareader/badge/?version=latest
    :target: https://pandas-datareader.readthedocs.io/en/latest/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/psf/black

Installation
------------

Install using ``pip``

.. code-block:: shell

   pip install pandas-datareader

Usage
-----

.. code-block:: python

   import pandas_datareader as pdr
   pdr.get_data_fred('GS10')

Documentation
-------------

`Stable documentation <https://pydata.github.io/pandas-datareader/>`__
is available on
`github.io <https://pydata.github.io/pandas-datareader/>`__.
A second copy of the stable documentation is hosted on
`read the docs <https://pandas-datareader.readthedocs.io/>`_ for more details.

`Development documentation <https://pydata.github.io/pandas-datareader/devel/>`__
is available for the latest changes in master.

Requirements
~~~~~~~~~~~~

Using pandas datareader requires the following packages:

* pandas>=0.23
* lxml
* requests>=2.19.0

Building the documentation additionally requires:

* matplotlib
* ipython
* requests_cache
* sphinx
* pydata_sphinx_theme

Development and testing additionally requires:

* black
* coverage
* codecov
* coveralls
* flake8
* pytest
* pytest-cov
* wrapt

Install latest development version
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: shell

   pip install git+https://github.com/pydata/pandas-datareader.git

or

.. code-block:: shell

   git clone https://github.com/pydata/pandas-datareader.git
   cd pandas-datareader
   python setup.py install
