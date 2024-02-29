:py:mod:`cellpy.utils.batch_tools.engines`
==========================================

.. py:module:: cellpy.utils.batch_tools.engines

.. autoapi-nested-parse::

   Engines are functions that are used by the Do-ers.

   Keyword Args: experiments, farms, barn, optionals
   Returns: farms, barn



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.engines.cycles_engine
   cellpy.utils.batch_tools.engines.dq_dv_engine
   cellpy.utils.batch_tools.engines.raw_data_engine
   cellpy.utils.batch_tools.engines.simple_db_engine
   cellpy.utils.batch_tools.engines.sql_db_engine
   cellpy.utils.batch_tools.engines.summary_engine



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.engines.SELECTED_SUMMARIES
   cellpy.utils.batch_tools.engines.hdr_journal
   cellpy.utils.batch_tools.engines.hdr_summary


.. py:function:: cycles_engine(**kwargs)

   engine to extract cycles


.. py:function:: dq_dv_engine(**kwargs)

   engine that performs incremental analysis of the cycle-data


.. py:function:: raw_data_engine(**kwargs)

   engine to extract raw data


.. py:function:: simple_db_engine(reader=None, cell_ids=None, file_list=None, pre_path=None, include_key=False, include_individual_arguments=True, additional_column_names=None, batch_name=None, **kwargs)

   Engine that gets values from the db for given set of cell IDs.

   The simple_db_engine looks up values for mass, names, etc. from
   the db using the reader object. In addition, it searches for the
   corresponding raw files / data.

   :param reader: a reader object (defaults to dbreader.Reader)
   :param cell_ids: keys (cell IDs) (assumes that the db has already been filtered, if not, use batch_name).
   :param file_list: file list to send to filefinder (instead of searching in folders for files).
   :param pre_path: prepended path to send to filefinder.
   :param include_key: include the key col in the pages (the cell IDs).
   :param include_individual_arguments: include the argument column in the pages.
   :param additional_column_names: list of additional column names to include in the pages.
   :param batch_name: name of the batch (used if cell_ids are not given)
   :param \*\*kwargs: sent to filefinder

   :returns: pages (pandas.DataFrame)


.. py:function:: sql_db_engine(*args, **kwargs) -> pandas.DataFrame


.. py:function:: summary_engine(**kwargs)

   engine to extract summary data


.. py:data:: SELECTED_SUMMARIES

   

.. py:data:: hdr_journal

   

.. py:data:: hdr_summary

   

