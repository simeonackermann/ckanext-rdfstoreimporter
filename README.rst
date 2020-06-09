=============
ckanext-rdfstoreimporter
=============

Sync CKAN datasets with external RDF store (eg Virtuoso).

------------
Installation
------------

.. Add any additional install steps to the list below.
   For example installing any non-Python dependencies or adding any required
   config settings.

To install ckanext-rdfstoreimporter:

1. Activate your CKAN virtual environment, for example::

     . /usr/lib/ckan/default/bin/activate

2. Install the ckanext-rdfstoreimporter Python package into your virtual environment::

     pip install ckanext-rdfstoreimporter

3. Add ``rdfstoreimporter`` to the ``ckan.plugins`` setting in your CKAN
   config file (by default the config file is located at
   ``/etc/ckan/default/production.ini``).

4. Restart CKAN. For example if you've deployed CKAN with Apache on Ubuntu::

     sudo service apache2 reload


------------------------
Development Installation
------------------------

To install ckanext-rdfstoreimporter for development, activate your CKAN virtualenv and
do::

    git clone https://github.com//ckanext-rdfstoreimporter.git
    cd ckanext-rdfstoreimporter
    python setup.py develop
    pip install -r dev-requirements.txt


------------------------
Run RDF sync
------------------------

Run the following command to run the rdf store sync extension (ensuring the pyenv is activated):

     (pyenv) $ paster --plugin=ckanext-rdfstoreimporter rdfstoresync run --config=/etc/ckan/default/production.ini
