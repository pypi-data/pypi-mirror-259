:py:mod:`cellpy.readers.dbreader`
=================================

.. py:module:: cellpy.readers.dbreader


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.dbreader.DbSheetCols
   cellpy.readers.dbreader.Reader




.. py:class:: DbSheetCols



.. py:class:: Reader(db_file=None, db_datadir=None, db_datadir_processed=None, db_frame=None, batch=None, batch_col_name=None)


   Bases: :py:obj:`cellpy.readers.core.BaseDbReader`

   .. autoapi-inheritance-diagram:: cellpy.readers.dbreader.Reader
      :parts: 1

   Base class for database readers.

   Simple excel reader.

   :param db_file: xlsx-file to read.
   :type db_file: str, pathlib.Path
   :param db_datadir: path where raw date is located.
   :type db_datadir: str, pathlib.Path
   :param db_datadir_processed: path where cellpy files are located.
   :type db_datadir_processed: str, pathlib.Path
   :param db_frame: use this instead of reading from xlsx-file.
   :type db_frame: pandas.DataFrame
   :param batch: batch name to use.
   :type batch: str
   :param batch_col_name: name of the column in the db-file that contains the batch name.
   :type batch_col_name: str

   .. py:method:: extract_date_from_cell_name(force=False)


   .. py:method:: filter_by_col(column_names)

      filters sheet/table by columns (input is column header)

      The routine returns the serial numbers with values>1 in the selected
      columns.

      :param column_names: the column headers.
      :type column_names: list

      :returns: pandas.DataFrame


   .. py:method:: filter_by_col_value(column_name, min_val=None, max_val=None)

      filters sheet/table by column.

      The routine returns the serial-numbers with min_val <= values >= max_val
      in the selected column.

      :param column_name: column name.
      :type column_name: str
      :param min_val: minimum value of serial number.
      :type min_val: int
      :param max_val: maximum value of serial number.
      :type max_val: int

      :returns: pandas.DataFrame


   .. py:method:: filter_by_slurry(slurry, appender='_')

      Filters sheet/table by slurry name.

      Input is slurry name or list of slurry names, for example 'es030' or
      ["es012","es033","es031"].

      :param slurry: slurry names.
      :type slurry: str or list of strings
      :param appender: char that surrounds slurry names.
      :type appender: chr

      :returns: List of serial_number (ints).


   .. py:method:: filter_selected(serial_numbers)


   .. py:method:: from_batch(batch_name: str, include_key: bool = False, include_individual_arguments: bool = False) -> dict
      :abstractmethod:


   .. py:method:: get_all()


   .. py:method:: get_area(serial_number)


   .. py:method:: get_areal_loading(serial_number)
      :abstractmethod:


   .. py:method:: get_args(serial_number: int) -> dict


   .. py:method:: get_by_column_label(column_name, serial_number)


   .. py:method:: get_cell_name(serial_number)


   .. py:method:: get_cell_type(serial_number)


   .. py:method:: get_comment(serial_number)


   .. py:method:: get_experiment_type(serial_number)


   .. py:method:: get_fileid(serial_number, full_path=True)


   .. py:method:: get_group(serial_number)


   .. py:method:: get_instrument(serial_number)


   .. py:method:: get_label(serial_number)


   .. py:method:: get_loading(serial_number)


   .. py:method:: get_mass(serial_number)


   .. py:method:: get_nom_cap(serial_number)


   .. py:method:: get_total_mass(serial_number)


   .. py:method:: inspect_exists(serial_number)


   .. py:method:: inspect_hd5f_fixed(serial_number)


   .. py:method:: intersect(lists)
      :staticmethod:


   .. py:method:: pick_table()

      Pick the table and return a pandas.DataFrame.


   .. py:method:: print_serial_number_info(serial_number, print_to_screen=True)

      Print information about the run.

      :param serial_number: serial number.
      :param print_to_screen: runs the print statement if True,
                              returns txt if not.

      :returns: txt if print_to_screen is False, else None.


   .. py:method:: select_all(serial_numbers)

      Select rows for identification for a list of serial_number.

      :param serial_numbers: list (or ndarray) of serial numbers

      :returns: pandas.DataFrame


   .. py:method:: select_batch(batch, batch_col_name=None, case_sensitive=True, drop=True) -> List[int]

      Selects the rows in column batch_col_number.

      :param batch: batch to select
      :param batch_col_name: column name to use for batch selection (default: DbSheetCols.batch).
      :param case_sensitive: if True, the batch name must match exactly (default: True).
      :param drop: if True, all un-selected rows are dropped from the table (default: True).

      :returns: List of row indices


   .. py:method:: select_serial_number_row(serial_number)

      Select row for identification number serial_number

      :param serial_number: serial number

      :returns: pandas.DataFrame


   .. py:method:: subtract(list1, list2)
      :staticmethod:


   .. py:method:: subtract_many(list1, lists)
      :staticmethod:


   .. py:method:: union(lists)
      :staticmethod:



