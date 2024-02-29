:py:mod:`cellpy.utils.batch_tools.sqlite_from_excel_db`
=======================================================

.. py:module:: cellpy.utils.batch_tools.sqlite_from_excel_db


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.sqlite_from_excel_db.DbColsRenamer



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.sqlite_from_excel_db.clean_up
   cellpy.utils.batch_tools.sqlite_from_excel_db.create_column_names_from_prms
   cellpy.utils.batch_tools.sqlite_from_excel_db.load_xlsx
   cellpy.utils.batch_tools.sqlite_from_excel_db.main
   cellpy.utils.batch_tools.sqlite_from_excel_db.run
   cellpy.utils.batch_tools.sqlite_from_excel_db.save_sqlite



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.sqlite_from_excel_db.DB_FILE_EXCEL
   cellpy.utils.batch_tools.sqlite_from_excel_db.DB_FILE_SQLITE
   cellpy.utils.batch_tools.sqlite_from_excel_db.HEADER_ROW
   cellpy.utils.batch_tools.sqlite_from_excel_db.TABLE_NAME_EXCEL
   cellpy.utils.batch_tools.sqlite_from_excel_db.UNIT_ROW


.. py:class:: DbColsRenamer


   .. py:attribute:: cellpy_col
      :type: str
      :value: ''

      

   .. py:attribute:: db_col
      :type: str
      :value: ''

      

   .. py:attribute:: dtype
      :type: str
      :value: ''

      

   .. py:attribute:: excel_col
      :type: str
      :value: ''

      


.. py:function:: clean_up(df, columns)

   Clean up the dataframe and return using 'proper cellpy headers'.


.. py:function:: create_column_names_from_prms()

   Create a list of DbColsRenamer objects from the cellpy.prms.DbCols object.


.. py:function:: load_xlsx(db_file=DB_FILE_EXCEL, table_name=TABLE_NAME_EXCEL, header_row=HEADER_ROW, unit_row=UNIT_ROW)

   Load the Excel file and return a pandas dataframe.


.. py:function:: main()


.. py:function:: run()


.. py:function:: save_sqlite(sheet, out_file=DB_FILE_SQLITE, table_name=TABLE_NAME_SQLITE, set_index=False)

   Save the pandas dataframe to a sqlite database.


.. py:data:: DB_FILE_EXCEL

   

.. py:data:: DB_FILE_SQLITE

   

.. py:data:: HEADER_ROW

   

.. py:data:: TABLE_NAME_EXCEL

   

.. py:data:: UNIT_ROW

   

