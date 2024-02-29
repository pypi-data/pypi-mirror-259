:py:mod:`cellpy.readers.instruments.neware_txt`
===============================================

.. py:module:: cellpy.readers.instruments.neware_txt

.. autoapi-nested-parse::

   Neware txt data - with explanations how it was implemented.

   1. Update SUPPORTED_MODELS, raw_ext and default_model
   2. Add instrument to prms.py
       a. create the boxed item:

           Neware = {"default_model": "UIO"}
           Neware = box.Box(Neware)

           ...
       b. add it to Instruments:
           Instruments = InstrumentsClass(
           ...
           Neware=Neware
           )

       c. Update the dataclass in prms.py:

           @dataclass
           class InstrumentsClass(CellPyConfig):
               tester: str
               custom_instrument_definitions_file: Union[str, None]
               Arbin: box.Box
               Maccor: box.Box
               Neware: box.Box

   3. (optionally) add Neware defaults to .cellpy_prms_default.conf

   4. Create instrument configuration file in readers/instruments/configurations

       formatters
       states
       normal_headers_renaming_dict
       file_info
       raw_units
       post_processors

   5. Put a file in test_data and create at least one test.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.neware_txt.DataLoader




Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.neware_txt.MUST_HAVE_RAW_COLUMNS
   cellpy.readers.instruments.neware_txt.SUPPORTED_MODELS


.. py:class:: DataLoader(*args, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.TxtLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.neware_txt.DataLoader
      :parts: 1

   Class for loading data from Neware txt files.

   .. py:attribute:: default_model

      

   .. py:attribute:: instrument_name
      :value: 'neware_txt'

      

   .. py:attribute:: raw_ext
      :value: 'csv'

      

   .. py:attribute:: supported_models

      

   .. py:method:: get_headers_aux(raw)
      :staticmethod:

      Defines the so-called auxiliary table column headings


   .. py:method:: validate(data)

      A simple check that all the needed columns has been successfully
      loaded and that they get the correct type



.. py:data:: MUST_HAVE_RAW_COLUMNS

   

.. py:data:: SUPPORTED_MODELS

   

