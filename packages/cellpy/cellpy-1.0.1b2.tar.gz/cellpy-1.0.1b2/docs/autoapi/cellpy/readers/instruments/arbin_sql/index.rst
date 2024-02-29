:py:mod:`cellpy.readers.instruments.arbin_sql`
==============================================

.. py:module:: cellpy.readers.instruments.arbin_sql

.. autoapi-nested-parse::

   arbin MS SQL Server data



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.arbin_sql.DataLoader



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.arbin_sql.from_arbin_to_datetime



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.arbin_sql.ALLOW_MULTI_TEST_FILE
   cellpy.readers.instruments.arbin_sql.DATE_TIME_FORMAT
   cellpy.readers.instruments.arbin_sql.DEBUG_MODE
   cellpy.readers.instruments.arbin_sql.ODBC
   cellpy.readers.instruments.arbin_sql.SEARCH_FOR_ODBC_DRIVERS
   cellpy.readers.instruments.arbin_sql.SQL_DRIVER
   cellpy.readers.instruments.arbin_sql.SQL_PWD
   cellpy.readers.instruments.arbin_sql.SQL_SERVER
   cellpy.readers.instruments.arbin_sql.SQL_UID
   cellpy.readers.instruments.arbin_sql.TABLE_NAMES
   cellpy.readers.instruments.arbin_sql.normal_headers_renaming_dict
   cellpy.readers.instruments.arbin_sql.summary_headers_renaming_dict


.. py:class:: DataLoader(*args, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.BaseLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.arbin_sql.DataLoader
      :parts: 1

   Class for loading arbin-data from MS SQL server.

   initiates the ArbinSQLLoader class

   .. py:attribute:: instrument_name
      :value: 'arbin_sql'

      

   .. py:method:: get_headers_aux()
      :staticmethod:

      Defines the so-called auxiliary table column headings for Arbin SQL Server


   .. py:method:: get_headers_aux_global()
      :staticmethod:

      Defines the so-called auxiliary global column headings for Arbin SQL Server


   .. py:method:: get_headers_global()
      :staticmethod:

      Defines the so-called global column headings for Arbin SQL Server


   .. py:method:: get_headers_normal()
      :staticmethod:

      Defines the so-called normal column headings for Arbin SQL Server


   .. py:method:: get_raw_limits()
      :staticmethod:

      returns a dictionary with resolution limits


   .. py:method:: get_raw_units()
      :staticmethod:

      Units used by the instrument.

      The internal cellpy units are given in the ``cellpy_units`` attribute.

      :returns: dictionary of units (str)

      .. rubric:: Example

      A minimum viable implementation could look like this::

          @staticmethod
          def get_raw_units():
              raw_units = dict()
              raw_units["current"] = "A"
              raw_units["charge"] = "Ah"
              raw_units["mass"] = "g"
              raw_units["voltage"] = "V"
              return raw_units


   .. py:method:: loader(name, **kwargs)

      returns a Data object with loaded data.

      Loads data from arbin SQL server db.

      :param name: name of the test
      :type name: str

      :returns: new_tests (list of data objects)



.. py:function:: from_arbin_to_datetime(n)


.. py:data:: ALLOW_MULTI_TEST_FILE

   

.. py:data:: DATE_TIME_FORMAT

   

.. py:data:: DEBUG_MODE

   

.. py:data:: ODBC

   

.. py:data:: SEARCH_FOR_ODBC_DRIVERS

   

.. py:data:: SQL_DRIVER

   

.. py:data:: SQL_PWD

   

.. py:data:: SQL_SERVER

   

.. py:data:: SQL_UID

   

.. py:data:: TABLE_NAMES

   

.. py:data:: normal_headers_renaming_dict

   

.. py:data:: summary_headers_renaming_dict

   

