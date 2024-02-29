:py:mod:`cellpy.readers.instruments.custom`
===========================================

.. py:module:: cellpy.readers.instruments.custom

.. autoapi-nested-parse::

   This module is used for loading data using the ``instrument="custom"`` method.
   If no ``instrument_file`` is given (either directly or through the use
   of the ``::`` separator), the default instrument file (yaml) will be used.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.custom.DataLoader




.. py:class:: DataLoader(instrument_file=None, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.AutoLoader`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.custom.DataLoader
      :parts: 1

   Class for loading data from txt files.

   .. py:attribute:: default_model

      

   .. py:attribute:: instrument_name
      :value: 'custom'

      

   .. py:attribute:: raw_ext
      :value: '*'

      

   .. py:attribute:: supported_models

      

   .. py:method:: parse_formatter_parameters(**kwargs)


   .. py:method:: parse_loader_parameters(**kwargs)


   .. py:method:: pre_init()


   .. py:method:: query_file(name)

      Query the file and return a pandas dataframe.



