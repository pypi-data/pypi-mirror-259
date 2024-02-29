:py:mod:`cellpy.readers.instruments.processors.post_processors`
===============================================================

.. py:module:: cellpy.readers.instruments.processors.post_processors

.. autoapi-nested-parse::

   Post-processing methods for instrument loaders.

   All methods must implement the following parameters/arguments::

       - data: Data
       - config_params: ModelParameters

   All methods should return the modified Data object.

   You can access the individual parameters for the post processor from
   the ``config_params.post_processor[<name of post processor>]``.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.processors.post_processors.convert_date_time_to_datetime
   cellpy.readers.instruments.processors.post_processors.convert_step_time_to_timedelta
   cellpy.readers.instruments.processors.post_processors.convert_test_time_to_timedelta
   cellpy.readers.instruments.processors.post_processors.cumulate_capacity_within_cycle
   cellpy.readers.instruments.processors.post_processors.date_time_from_test_time
   cellpy.readers.instruments.processors.post_processors.remove_last_if_bad
   cellpy.readers.instruments.processors.post_processors.rename_headers
   cellpy.readers.instruments.processors.post_processors.select_columns_to_keep
   cellpy.readers.instruments.processors.post_processors.set_cycle_number_not_zero
   cellpy.readers.instruments.processors.post_processors.set_index
   cellpy.readers.instruments.processors.post_processors.split_capacity
   cellpy.readers.instruments.processors.post_processors.split_current



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.processors.post_processors.ORDERED_POST_PROCESSING_STEPS


.. py:function:: convert_date_time_to_datetime(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Convert date_time column to datetime.


.. py:function:: convert_step_time_to_timedelta(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Convert step_time to timedelta.


.. py:function:: convert_test_time_to_timedelta(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Convert test_time to timedelta.


.. py:function:: cumulate_capacity_within_cycle(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Cumulates the capacity within each cycle


.. py:function:: date_time_from_test_time(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Add a date_time column (based on the test_time column).


.. py:function:: remove_last_if_bad(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Drop the last row if it contains more NaNs than second to last.


.. py:function:: rename_headers(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Rename headers to the correct Cellpy headers.


.. py:function:: select_columns_to_keep(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Select columns to keep in the raw data.


.. py:function:: set_cycle_number_not_zero(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Set cycle number to start from 1 instead of 0.


.. py:function:: set_index(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Set index to data_point.


.. py:function:: split_capacity(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Split capacity into charge and discharge


.. py:function:: split_current(data: cellpy.readers.core.Data, config_params: cellpy.readers.instruments.configurations.ModelParameters) -> cellpy.readers.core.Data

   Split current into positive and negative


.. py:data:: ORDERED_POST_PROCESSING_STEPS
   :value: ['get_column_names', 'rename_headers', 'select_columns_to_keep', 'remove_last_if_bad']

   

