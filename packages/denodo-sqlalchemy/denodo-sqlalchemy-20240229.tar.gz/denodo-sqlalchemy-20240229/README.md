`Denodo Dialect for SQLAlchemy`
********************************************************************************

This package includes the Denodo Dialect for SQLAlchemy, which offers an easy way to connect to Denodo databases from SQLAlchemy https://www.sqlalchemy.org/

Denodo documentation and software resources are available at https://community.denodo.com

This dialect supports SQLAlchemy v1.4 and higher and Denodo 7.0 and higher.

Pre-requisites
================================================================================

This dialect requires the following Python modules:
   * SQLAlchemy version 1.4 or higher
   * psycopg2 version 2.7 or higher.
   
However, these dependencies do not need to be installed because when you install Denodo Dialect for SQLAlchemy both should be installed automatically.

Alternatively, these packages can be manually installed by means of:

    .. code-block::

        pip install sqlalchemy
        pip install psycopg2

Important: note also that psycopg2 has its own requirements for installation which need to be satisfied: https://www.psycopg.org/docs/install.html#prerequisites

Installation
================================================================================

The Denodo SQLAlchemy package can be installed from the public PyPI repository using :code:`pip`:

    .. code-block::

        pip install --upgrade denodo-sqlalchemy

:code:`pip` automatically installs all required modules.

Usage
================================================================================

To connect to Denodo VDP Server with SQLAlchemy, the following URL pattern can be used:

    .. code-block::

        denodo://<username>:<password>@<host>:<odbcport>/<database>