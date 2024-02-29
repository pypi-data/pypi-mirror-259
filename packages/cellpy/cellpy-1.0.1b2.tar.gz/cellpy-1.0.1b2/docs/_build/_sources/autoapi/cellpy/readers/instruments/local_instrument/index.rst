:py:mod:`cellpy.readers.instruments.local_instrument`
=====================================================

.. py:module:: cellpy.readers.instruments.local_instrument

.. autoapi-nested-parse::

   This module is used for loading data using the corresponding local
   yaml file with definitions on how the data should be loaded. This loader
   is based on the ``TxtLoader`` and can only be used to load csv-type files



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.local_instrument.DataLoader




.. py:class:: DataLoader(instrument_file=None, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.TxtLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.local_instrument.DataLoader
      :parts: 1

   Class for loading data from txt files.

   :param instrument_file: name of the local instrument file.
   :param \*\*kwargs: not used.

   .. py:attribute:: default_model

      

   .. py:attribute:: instrument_name
      :value: 'local_instrument'

      

   .. py:attribute:: raw_ext
      :value: '*'

      

   .. py:attribute:: supported_models

      

   .. py:method:: pre_init()



