:py:mod:`cellpy.readers.instruments.ext_nda_reader`
===================================================

.. py:module:: cellpy.readers.instruments.ext_nda_reader


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.ext_nda_reader.DataLoader



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.ext_nda_reader.load_nda



.. py:class:: DataLoader(*args, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.BaseLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.ext_nda_reader.DataLoader
      :parts: 1

   Class for using the NDA loader by Frederik Huld (Beyonder).

   initiates the NdaLoader class

   .. py:attribute:: instrument_name
      :value: 'neware_nda'

      

   .. py:method:: get_params(parameter=None)
      :staticmethod:

      Retrieves parameters needed for facilitating working with the
      instrument without registering it.

      Typically, it should include the name and raw_ext.

      Return: parameters or a selected parameter


   .. py:method:: get_raw_limits()
      :abstractmethod:

      Include the settings for how to decide what kind of step you are examining here.

      The raw limits are 'epsilons' used to check if the current and/or voltage is stable (for example
      for galvanostatic steps, one would expect that the current is stable (constant) and non-zero).
      It is expected that different instruments (with different resolution etc.) have different
      'epsilons'.

      Returns: the raw limits (dict)



   .. py:method:: get_raw_units()
      :abstractmethod:

      Include the settings for the units used by the instrument.

      The units are defined w.r.t. the SI units ('unit-fractions'; currently only units that are multiples of
      Si units can be used). For example, for current defined in mA, the value for the
      current unit-fraction will be 0.001.

      Returns: dictionary containing the unit-fractions for current, charge, and mass



   .. py:method:: loader(file_name, *args, **kwargs)

      Loads data into a DataSet object and returns it



.. py:function:: load_nda(*args, **kwargs)


