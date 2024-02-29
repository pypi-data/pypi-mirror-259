:py:mod:`cellpy.utils.example_data`
===================================

.. py:module:: cellpy.utils.example_data

.. autoapi-nested-parse::

   Tools for getting some data to play with



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.example_data.arbin_file_path
   cellpy.utils.example_data.arbin_multi_file_path
   cellpy.utils.example_data.biologics_file_path
   cellpy.utils.example_data.cellpy_file
   cellpy.utils.example_data.cellpy_file_path
   cellpy.utils.example_data.maccor_file_path
   cellpy.utils.example_data.neware_file_path
   cellpy.utils.example_data.pec_file_path
   cellpy.utils.example_data.rate_file
   cellpy.utils.example_data.raw_file



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.example_data.CURRENT_PATH
   cellpy.utils.example_data.H5_PATH
   cellpy.utils.example_data.RAW_PATH


.. py:function:: arbin_file_path() -> pathlib.Path

   Get the path to an example arbin res file


.. py:function:: arbin_multi_file_path() -> pathlib.Path

   Get the path to an example arbin res file


.. py:function:: biologics_file_path() -> pathlib.Path

   Get the path to an example biologics mpr file


.. py:function:: cellpy_file(testing: bool = False) -> cellpy.cellreader.CellpyData

   load an example cellpy file.

   :param testing: run in test mode
   :type testing: bool

   :returns: cellpy.CellpyCell object with the data loaded


.. py:function:: cellpy_file_path() -> pathlib.Path

   Get the path to an example cellpy file


.. py:function:: maccor_file_path() -> pathlib.Path

   Get the path to an example maccor txt file


.. py:function:: neware_file_path() -> pathlib.Path

   Get the path to an example neware csv file


.. py:function:: pec_file_path() -> pathlib.Path

   Get the path to an example pec csv file


.. py:function:: rate_file(testing: bool = False) -> cellpy.cellreader.CellpyData

   load an example cellpy file.

   :param testing: run in test mode
   :type testing: bool

   :returns: cellpy.CellpyCell object with the rate data loaded


.. py:function:: raw_file(auto_summary: bool = True, testing: bool = False) -> cellpy.cellreader.CellpyData

   load an example data file (arbin).

   :param auto_summary: run make_summary automatically (defaults to True)
   :type auto_summary: bool
   :param testing: run in test mode
   :type testing: bool

   :returns: cellpy.CellpyCell object with the data loaded


.. py:data:: CURRENT_PATH

   

.. py:data:: H5_PATH

   

.. py:data:: RAW_PATH

   

