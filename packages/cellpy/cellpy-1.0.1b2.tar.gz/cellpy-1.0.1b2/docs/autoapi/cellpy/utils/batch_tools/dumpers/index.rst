:py:mod:`cellpy.utils.batch_tools.dumpers`
==========================================

.. py:module:: cellpy.utils.batch_tools.dumpers

.. autoapi-nested-parse::

   Dumpers are functions that are used by the Do-ers.
   Keyword Args: experiments, farms, barn, engine
   Returns nothing.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.dumpers.csv_dumper
   cellpy.utils.batch_tools.dumpers.excel_dumper
   cellpy.utils.batch_tools.dumpers.origin_dumper
   cellpy.utils.batch_tools.dumpers.ram_dumper
   cellpy.utils.batch_tools.dumpers.screen_dumper



.. py:function:: csv_dumper(**kwargs)

   dump data to csv


.. py:function:: excel_dumper(**kwargs)

   Dump data to excel xlxs-format.


.. py:function:: origin_dumper(**kwargs)

   Dump data to a format suitable for use in OriginLab.


.. py:function:: ram_dumper(**kwargs)

   Dump data to 'memory' for later usage.


.. py:function:: screen_dumper(**kwargs)

   Dump data to screen.


