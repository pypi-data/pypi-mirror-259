:py:mod:`cellpy.readers.instruments.arbin_sql_h5`
=================================================

.. py:module:: cellpy.readers.instruments.arbin_sql_h5

.. autoapi-nested-parse::

   arbin MS SQL Server exported h5 data



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.arbin_sql_h5.DataLoader



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.arbin_sql_h5.from_arbin_to_datetime



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.arbin_sql_h5.ALLOW_MULTI_TEST_FILE
   cellpy.readers.instruments.arbin_sql_h5.DATE_TIME_FORMAT
   cellpy.readers.instruments.arbin_sql_h5.DEBUG_MODE
   cellpy.readers.instruments.arbin_sql_h5.normal_headers_renaming_dict


.. py:class:: DataLoader(*args, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.BaseLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.arbin_sql_h5.DataLoader
      :parts: 1

   Class for loading arbin-data from MS SQL server.

   initiates the ArbinSQLLoader class

   .. py:attribute:: instrument_name
      :value: 'arbin_sql_h5'

      

   .. py:attribute:: raw_ext
      :value: 'h5'

      

   .. py:method:: get_headers_aux(df)
      :staticmethod:

      Defines the so-called auxiliary table column headings for Arbin SQL Server h5 export


   .. py:method:: get_headers_normal()
      :staticmethod:

      Defines the so-called normal column headings for Arbin SQL Server h5 export


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

      Loads data from arbin SQL server h5 export.

      :param name: name of the file
      :type name: str

      :returns: data object



.. py:function:: from_arbin_to_datetime(n)


.. py:data:: ALLOW_MULTI_TEST_FILE

   

.. py:data:: DATE_TIME_FORMAT

   

.. py:data:: DEBUG_MODE

   

.. py:data:: normal_headers_renaming_dict

   

