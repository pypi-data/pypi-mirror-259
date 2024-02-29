:py:mod:`cellpy.readers.instruments.neware_xlsx`
================================================

.. py:module:: cellpy.readers.instruments.neware_xlsx

.. autoapi-nested-parse::

   neware xlsx exported data



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.neware_xlsx.DataLoader
   cellpy.readers.instruments.neware_xlsx.ModelParameters



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.neware_xlsx.to_datetime



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.neware_xlsx.ALLOW_MULTI_TEST_FILE
   cellpy.readers.instruments.neware_xlsx.DATE_TIME_FORMAT
   cellpy.readers.instruments.neware_xlsx.DEBUG_MODE


.. py:class:: DataLoader(*args, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.BaseLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.neware_xlsx.DataLoader
      :parts: 1

   Class for loading arbin-data from MS SQL server.

   initiates the neware xlsx reader class

   .. py:attribute:: instrument_name
      :value: 'neware_xlsx'

      

   .. py:attribute:: raw_ext
      :value: 'xlsx'

      

   .. py:method:: get_headers_aux(df)
      :staticmethod:

      Defines the so-called auxiliary table column headings for Neware xlsx export

      Warning: not properly implemented yet



   .. py:method:: get_headers_normal()
      :staticmethod:

      Defines the so-called normal column headings for export


   .. py:method:: get_normal_headers_renaming_dict()


   .. py:method:: get_raw_limits()
      :staticmethod:

      returns a dictionary with resolution limits


   .. py:method:: get_raw_units()

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



.. py:class:: ModelParameters


   .. py:attribute:: states
      :type: dict

      


.. py:function:: to_datetime(n)


.. py:data:: ALLOW_MULTI_TEST_FILE

   

.. py:data:: DATE_TIME_FORMAT

   

.. py:data:: DEBUG_MODE

   

