:py:mod:`cellpy.readers.instruments.arbin_res`
==============================================

.. py:module:: cellpy.readers.instruments.arbin_res

.. autoapi-nested-parse::

   arbin res-type data files



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.arbin_res.DataLoader




Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.arbin_res.ALLOW_MULTI_TEST_FILE
   cellpy.readers.instruments.arbin_res.DEBUG_MODE
   cellpy.readers.instruments.arbin_res.NORMAL_HEADERS_RENAMING_DICT
   cellpy.readers.instruments.arbin_res.ODBC
   cellpy.readers.instruments.arbin_res.SEARCH_FOR_ODBC_DRIVERS
   cellpy.readers.instruments.arbin_res.SUMMARY_HEADERS_RENAMING_DICT
   cellpy.readers.instruments.arbin_res.TABLE_NAMES
   cellpy.readers.instruments.arbin_res.USE_SQLALCHEMY_ACCESS_ENGINE
   cellpy.readers.instruments.arbin_res.current_platform
   cellpy.readers.instruments.arbin_res.dbloader
   cellpy.readers.instruments.arbin_res.driver_dll


.. py:class:: DataLoader(*args, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.BaseLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.arbin_res.DataLoader
      :parts: 1

   Class for loading arbin-data from res-files.

   Parameters from configuration (`prms.Instruments.Arbin`)::

       - max_res_filesize: break if file size exceeds this limit.
       - chunk_size: size of chunks to load.
       - max_chunks: max number of chunks to load.
       - use_subprocess: use mdbtools or not.
       - detect_subprocess_need: detect if mdbtools is needed.
       - sub_process_path: path to mdbtools (or similar).
       - office_version: version of office (32 or 64 bit).


   .. py:attribute:: instrument_name
      :value: 'arbin_res'

      

   .. py:attribute:: raw_ext
      :value: 'res'

      

   .. py:method:: get_headers_aux()
      :staticmethod:

      Defines the so-called auxiliary table column headings for Arbin .res-files


   .. py:method:: get_headers_aux_global()
      :staticmethod:

      Defines the so-called auxiliary global column headings for Arbin .res-files


   .. py:method:: get_headers_global()
      :staticmethod:

      Defines the so-called global column headings for Arbin .res-files


   .. py:method:: get_headers_normal()
      :staticmethod:

      Defines the so-called normal column headings for Arbin .res-files


   .. py:method:: get_raw_limits()
      :staticmethod:

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


   .. py:method:: loader(name, *args, bad_steps=None, dataset_number=None, data_points=None, increment_cycle_index=True, **kwargs)

      Loads data from arbin .res files.

      :param name: path to .res file.
      :type name: str
      :param bad_steps: (c, s) tuples of steps s (in cycle c)
                        to skip loading.
      :type bad_steps: list of tuples
      :param dataset_number: the data set number ('Test-ID') to select if you are dealing
                             with arbin files with more than one data-set.
                             Defaults to selecting all data-sets and merging them.
      :type dataset_number: int
      :param data_points: load only data from data_point[0] to
                          data_point[1] (use None for infinite).
      :type data_points: tuple of ints
      :param increment_cycle_index: increment the cycle index if merging several datasets (default True).
      :type increment_cycle_index: bool

      :returns: new data (Data)


   .. py:method:: repair(file_name)

      try to repair a broken/corrupted file



.. py:data:: ALLOW_MULTI_TEST_FILE
   :value: False

   

.. py:data:: DEBUG_MODE

   

.. py:data:: NORMAL_HEADERS_RENAMING_DICT

   

.. py:data:: ODBC

   

.. py:data:: SEARCH_FOR_ODBC_DRIVERS

   

.. py:data:: SUMMARY_HEADERS_RENAMING_DICT

   

.. py:data:: TABLE_NAMES

   

.. py:data:: USE_SQLALCHEMY_ACCESS_ENGINE
   :value: True

   

.. py:data:: current_platform

   

.. py:data:: dbloader

   

.. py:data:: driver_dll

   

