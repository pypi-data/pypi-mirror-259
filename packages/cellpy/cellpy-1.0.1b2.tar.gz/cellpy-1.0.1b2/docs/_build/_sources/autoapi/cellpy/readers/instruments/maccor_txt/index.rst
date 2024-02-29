:py:mod:`cellpy.readers.instruments.maccor_txt`
===============================================

.. py:module:: cellpy.readers.instruments.maccor_txt

.. autoapi-nested-parse::

   Maccor txt data



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.maccor_txt.DataLoader



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.maccor_txt.c_heck_loader



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.maccor_txt.MUST_HAVE_RAW_COLUMNS
   cellpy.readers.instruments.maccor_txt.SUPPORTED_MODELS


.. py:class:: DataLoader(*args, **kwargs)


   Bases: :py:obj:`cellpy.readers.instruments.base.TxtLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.maccor_txt.DataLoader
      :parts: 1

   Class for loading data from Maccor txt files.

   .. py:attribute:: default_model

      

   .. py:attribute:: instrument_name
      :value: 'maccor_txt'

      

   .. py:attribute:: raw_ext
      :value: 'txt'

      

   .. py:attribute:: supported_models

      

   .. py:method:: get_headers_aux(raw)
      :staticmethod:

      Defines the so-called auxiliary table column headings


   .. py:method:: validate(data)

      A simple check that all the needed columns has been successfully
      loaded and that they get the correct type



.. py:function:: c_heck_loader(name=None, number=1, model='one')


.. py:data:: MUST_HAVE_RAW_COLUMNS

   

.. py:data:: SUPPORTED_MODELS

   

