:py:mod:`cellpy.readers.instruments.biologics_mpr`
==================================================

.. py:module:: cellpy.readers.instruments.biologics_mpr

.. autoapi-nested-parse::

   This file contains methods for importing Bio-Logic mpr-type files



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.biologics_mpr.DataLoader



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.biologics_mpr.datetime2ole
   cellpy.readers.instruments.biologics_mpr.ole2datetime



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.biologics_mpr.MINIMUM_SELECTION
   cellpy.readers.instruments.biologics_mpr.OLE_TIME_ZERO
   cellpy.readers.instruments.biologics_mpr.SEEK_CUR
   cellpy.readers.instruments.biologics_mpr.SEEK_END
   cellpy.readers.instruments.biologics_mpr.SEEK_SET


.. py:class:: DataLoader(*args, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.BaseLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.biologics_mpr.DataLoader
      :parts: 1

   Class for loading biologics-data from mpr-files.

   .. py:attribute:: instrument_name
      :value: 'biologics_mpr'

      

   .. py:attribute:: raw_ext
      :value: 'mpr'

      

   .. py:method:: dump(file_name, path)
      :abstractmethod:

      Dumps the raw file to an intermediate hdf5 file.

      This method can be used if the raw file is too difficult to load and it
      is likely that it is more efficient to convert it to an hdf5 format
      and then load it using the `from_intermediate_file` function.

      :param file_name: name of the raw file
      :param path: path to where to store the intermediate hdf5 file (optional)

      :returns: full path to stored intermediate hdf5 file
                information about the raw file (needed by the
                `from_intermediate_file` function)


   .. py:method:: get_raw_limits()
      :staticmethod:

      Include the settings for how to decide what kind of
      step you are examining here.

      The raw limits are 'epsilons' used to check if the current
      and/or voltage is stable (for example
      for galvanostatic steps, one would expect that the current
      is stable (constant) and non-zero).
      It is expected that different instruments (with different
      resolution etc.) have different
      'epsilons'.

      Returns: the raw limits (dict)



   .. py:method:: get_raw_units()
      :staticmethod:

      Include the settings for the units used by the instrument.

      The units are defined w.r.t. the SI units ('unit-fractions';
      currently only units that are multiples of
      Si units can be used). For example, for current defined in mA,
      the value for the
      current unit-fraction will be 0.001.

      Returns: dictionary containing the unit-fractions for current, charge,
      and mass



   .. py:method:: inspect(run_data)

      inspect the file.


   .. py:method:: loader(file_name, bad_steps=None, **kwargs)

      Loads data from BioLogics mpr files.

      :param file_name: path to .res file.
      :type file_name: str
      :param bad_steps: (c, s) tuples of steps s
                        (in cycle c) to skip loading.
      :type bad_steps: list of tuples

      :returns: new test


   .. py:method:: repair(file_name)
      :abstractmethod:

      try to repair a broken/corrupted file



.. py:function:: datetime2ole(dt)

   converts from datetime object to ole datetime float


.. py:function:: ole2datetime(oledt)

   converts from ole datetime float to datetime


.. py:data:: MINIMUM_SELECTION
   :value: ['Data_Point', 'Test_Time', 'Step_Time', 'DateTime', 'Step_Index', 'Cycle_Index', 'Current',...

   

.. py:data:: OLE_TIME_ZERO

   

.. py:data:: SEEK_CUR
   :value: 1

   

.. py:data:: SEEK_END
   :value: 2

   

.. py:data:: SEEK_SET
   :value: 0

   

