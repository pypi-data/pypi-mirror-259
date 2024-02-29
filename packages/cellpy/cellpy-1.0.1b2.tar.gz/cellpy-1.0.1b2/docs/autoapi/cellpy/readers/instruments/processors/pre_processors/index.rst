:py:mod:`cellpy.readers.instruments.processors.pre_processors`
==============================================================

.. py:module:: cellpy.readers.instruments.processors.pre_processors

.. autoapi-nested-parse::

   Pre-processing methods for instrument loaders.

   All methods must implement the following parameters/arguments::

       - filename: Union[str, pathlib.Path]
       - *args and **kwargs: Any additional parameters/arguments should be supported.

   All methods should return None (i.e. nothing).



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.processors.pre_processors.remove_empty_lines



.. py:function:: remove_empty_lines(filename: Union[str, pathlib.Path], *args, **kwargs) -> pathlib.Path

   Remove all the empty lines in the file.

   The method saves to the same name as the original file, so it is recommended to work on a temporary
   copy of the file instead of the original file.

   :param filename: path to the file.
   :param \*args: None supported.
   :param \*\*kwargs: None supported.

   :returns: pathlib.Path of modified file


