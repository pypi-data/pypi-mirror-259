:py:mod:`cellpy.readers.instruments.configurations`
===================================================

.. py:module:: cellpy.readers.instruments.configurations

.. autoapi-nested-parse::

   Very simple implementation of a plugin-like infrastructure



Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   maccor_txt_four/index.rst
   maccor_txt_one/index.rst
   maccor_txt_three/index.rst
   maccor_txt_two/index.rst
   maccor_txt_zero/index.rst
   neware_txt_zero/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.configurations.ModelParameters



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.configurations.register_configuration_from_module
   cellpy.readers.instruments.configurations.register_local_configuration_from_yaml_file



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.configurations.HARD_CODED_MODULE_PATH
   cellpy.readers.instruments.configurations.OPTIONAL_DICTIONARY_ATTRIBUTE_NAMES
   cellpy.readers.instruments.configurations.OPTIONAL_LIST_ATTRIBUTE_NAMES
   cellpy.readers.instruments.configurations.RAW_LIMITS


.. py:class:: ModelParameters


   Dataclass to store sub-model specific parameters.

   .. py:attribute:: columns_to_keep
      :type: list

      

   .. py:attribute:: file_info
      :type: dict

      

   .. py:attribute:: formatters
      :type: dict

      

   .. py:attribute:: incremental_unit_labels
      :type: dict

      

   .. py:attribute:: meta_keys
      :type: dict

      

   .. py:attribute:: name
      :type: str

      

   .. py:attribute:: normal_headers_renaming_dict
      :type: dict

      

   .. py:attribute:: not_implemented_in_cellpy_yet_renaming_dict
      :type: dict

      

   .. py:attribute:: post_processors
      :type: dict

      

   .. py:attribute:: pre_processors
      :type: dict

      

   .. py:attribute:: prefixes
      :type: dict

      

   .. py:attribute:: raw_limits
      :type: dict

      

   .. py:attribute:: raw_units
      :type: dict

      

   .. py:attribute:: states
      :type: dict

      

   .. py:attribute:: unit_labels
      :type: dict

      


.. py:function:: register_configuration_from_module(name: str = 'one', module: str = 'maccor_txt_one', _module_path=None, _m=None) -> ModelParameters

   Register a python module (.py file) and return it.

   This function will dynamically import the given module from the
   `cellpy.readers.instruments.configurations` module and return it.

   :returns: ModelParameters


.. py:function:: register_local_configuration_from_yaml_file(instrument) -> ModelParameters

   Register a module (.yml file) and return it.

   This function will dynamically import the given module from the
   `cellpy.readers.instruments.configurations` module and return it.

   :returns: ModelParameters


.. py:data:: HARD_CODED_MODULE_PATH
   :value: 'cellpy.readers.instruments.configurations'

   

.. py:data:: OPTIONAL_DICTIONARY_ATTRIBUTE_NAMES
   :value: ['file_info', 'formatters', 'prefixes', 'pre_processors', 'post_processors', 'meta_keys',...

   

.. py:data:: OPTIONAL_LIST_ATTRIBUTE_NAMES
   :value: ['columns_to_keep']

   

.. py:data:: RAW_LIMITS

   

