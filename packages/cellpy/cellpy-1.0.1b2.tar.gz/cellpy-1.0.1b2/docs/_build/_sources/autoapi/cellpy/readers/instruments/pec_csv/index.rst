:py:mod:`cellpy.readers.instruments.pec_csv`
============================================

.. py:module:: cellpy.readers.instruments.pec_csv

.. autoapi-nested-parse::

   pec csv-type data files



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.pec_csv.DataLoader




Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.pec_csv.pec_headers_normal


.. py:class:: DataLoader(*args, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.BaseLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.pec_csv.DataLoader
      :parts: 1

   Class for loading exported data from PEC

   .. py:attribute:: instrument_name
      :value: 'pec_csv'

      

   .. py:attribute:: raw_ext
      :value: 'csv'

      

   .. py:method:: get_raw_limits()

      Limits used to identify type of step.

      The raw limits are 'epsilons' used to check if the current and/or voltage is stable (for example
      for galvanostatic steps, one would expect that the current is stable (constant) and non-zero).
      If the (accumulated) change is less than 'epsilon', then cellpy interpret it to be stable.
      It is expected that different instruments (with different resolution etc.) have different
      resolutions and noice levels, thus different 'epsilons'.

      :returns: the raw limits (dict)


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


   .. py:method:: loader(file_name, bad_steps=None, **kwargs)

      Loads data into a Data object and returns it


   .. py:method:: timestamp_to_seconds(timestamp)
      :staticmethod:

      Changes hh:mm:s.xxx time format to seconds



.. py:data:: pec_headers_normal

   

