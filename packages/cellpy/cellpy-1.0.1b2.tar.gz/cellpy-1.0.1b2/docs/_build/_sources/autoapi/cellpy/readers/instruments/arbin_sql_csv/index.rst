:py:mod:`cellpy.readers.instruments.arbin_sql_csv`
==================================================

.. py:module:: cellpy.readers.instruments.arbin_sql_csv

.. autoapi-nested-parse::

   arbin MS SQL Server csv data



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.arbin_sql_csv.DataLoader




Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.arbin_sql_csv.ALLOW_MULTI_TEST_FILE
   cellpy.readers.instruments.arbin_sql_csv.DEBUG_MODE
   cellpy.readers.instruments.arbin_sql_csv.FILE_NAME_POST_LABEL
   cellpy.readers.instruments.arbin_sql_csv.incremental_unit_labels
   cellpy.readers.instruments.arbin_sql_csv.normal_headers_renaming_dict
   cellpy.readers.instruments.arbin_sql_csv.not_implemented_in_cellpy_yet_renaming_dict
   cellpy.readers.instruments.arbin_sql_csv.unit_labels


.. py:class:: DataLoader(*args, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.BaseLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.arbin_sql_csv.DataLoader
      :parts: 1

   Class for loading csv-exported arbin-data from MS SQL server.

   .. py:attribute:: instrument_name
      :value: 'arbin_sql_csv'

      

   .. py:attribute:: raw_ext
      :value: 'csv'

      

   .. py:method:: get_headers_aux(df)
      :staticmethod:

      Defines the so-called auxiliary table column headings
      for Arbin SQL Server csv


   .. py:method:: get_headers_normal()
      :staticmethod:

      Defines the so-called normal column headings
      for Arbin SQL Server csv


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

      :param name: name of the file
      :type name: str

      :returns: a Data object
      :rtype: Data



.. py:data:: ALLOW_MULTI_TEST_FILE

   

.. py:data:: DEBUG_MODE

   

.. py:data:: FILE_NAME_POST_LABEL

   

.. py:data:: incremental_unit_labels

   

.. py:data:: normal_headers_renaming_dict

   

.. py:data:: not_implemented_in_cellpy_yet_renaming_dict

   

.. py:data:: unit_labels

   

