:py:mod:`cellpy.utils.batch_tools.batch_journals`
=================================================

.. py:module:: cellpy.utils.batch_tools.batch_journals


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_journals.LabJournal




Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_journals.hdr_journal
   cellpy.utils.batch_tools.batch_journals.missing_keys
   cellpy.utils.batch_tools.batch_journals.trans_dict


.. py:class:: LabJournal(db_reader='default', engine=None, batch_col=None, **kwargs)


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseJournal`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_journals.LabJournal
      :parts: 1

   A journal keeps track of the details of the experiment.

   The journal should at a mimnimum contain information about the name and
   project the experiment has.

   .. attribute:: pages

      table with information about each cell/file.

      :type: pandas.DataFrame

   .. attribute:: name

      the name of the experiment (used in db-lookup).

      :type: str

   .. attribute:: project

      the name of the project the experiment belongs to (used
      for making folder names).

      :type: str

   .. attribute:: file_name

      the file name used in the to_file method.

      :type: str or path

   .. attribute:: project_dir

      folder where to put the batch (or experiment) files and
      information.

   .. attribute:: batch_dir

      folder in project_dir where summary-files and information
      and results related to the current experiment are stored.

   .. attribute:: raw_dir

      folder in batch_dir where cell-specific information and results
      are stored (e.g. raw-data, dq/dv data, voltage-capacity cycles).

   Journal for selected batch.

   The journal contains pages (pandas.DataFrame) with prms for
   each cell (one cell pr row).

   :param db_reader: either default (a simple excel reader already
                     implemented in cellpy) or other db readers that implement
                     the needed API.
   :param engine: defaults to simple_db_engine for parsing db using the
                  db_reader
                      self.pages = simple_db_engine(
                          self.db_reader, id_keys, **kwargs
                      )
   :param batch_col: the column name for the batch column in the db (used by simple_db_engine).
   :param \*\*kwargs: passed to the db_reader

   .. py:method:: add_cell(cell_id, **kwargs)

      Add a cell to the pages


   .. py:method:: add_comment(comment)

      add a comment (will be saved in the journal file)


   .. py:method:: create_empty_pages(description=None)


   .. py:method:: duplicate_journal(folder=None) -> None

      Copy the journal to folder.

      :param folder: folder to copy to (defaults to the
      :type folder: str or pathlib.Path
      :param current folder).:


   .. py:method:: from_db(project=None, name=None, batch_col=None, **kwargs)

      populate journal from db.

      :param project: project name.
      :type project: str
      :param name: experiment name.
      :type name: str
      :param batch_col: batch column.
      :type batch_col: int

      **kwargs: sent to engine.

      simple_db-engine -> filefinder.search_for_files:
          run_name(str): run-file identification.
          raw_extension(str): optional, extension of run-files (without the '.').
          cellpy_file_extension(str): optional, extension for cellpy files
              (without the '.').
          raw_file_dir(path): optional, directory where to look for run-files
              (default: read prm-file)
          cellpy_file_dir(path): optional, directory where to look for
              cellpy-files (default: read prm-file)
          prm_filename(path): optional parameter file can be given.
          file_name_format(str): format of raw-file names or a glob pattern
              (default: YYYYMMDD_[name]EEE_CC_TT_RR) [not finished yet].
          reg_exp(str): use regular expression instead (defaults to None) [not finished yet].
          sub_folders (bool): perform search also in sub-folders.
          file_list (list of str): perform the search within a given list
              of filenames instead of searching the folder(s). The list should
              not contain the full filepath (only the actual file names). If
              you want to provide the full path, you will have to modify the
              file_name_format or reg_exp accordingly.
          pre_path (path or str): path to prepend the list of files selected
               from the file_list.

      :returns: None


   .. py:method:: from_file(file_name=None, paginate=True, **kwargs)

      Loads a DataFrame with all the needed info about the experiment


   .. py:method:: from_file_old(file_name=None)

      Loads a DataFrame with all the needed info about the experiment


   .. py:method:: from_frame(frame, name=None, project=None, paginate=None, **kwargs)


   .. py:method:: generate_empty_session()


   .. py:method:: generate_file_name()

      generate a suitable file name for the experiment


   .. py:method:: generate_folder_names()

      Set appropriate folder names.


   .. py:method:: get_cell(id_key)

      get additional cell info from db


   .. py:method:: get_column(header)

      populate new column from db


   .. py:method:: look_for_file()


   .. py:method:: paginate()

      Make folders where we would like to put results etc.


   .. py:method:: read_journal_excel_file(file_name, **kwargs)
      :classmethod:


   .. py:method:: read_journal_jason_file(file_name, **kwargs)
      :classmethod:


   .. py:method:: remove_cell(cell_id)


   .. py:method:: remove_comment(comment_id)


   .. py:method:: to_file(file_name=None, paginate=True, to_project_folder=True, duplicate_to_local_folder=True)

      Saves a DataFrame with all the needed info about the experiment.

      :param file_name: journal file name (.json or .xlsx)
      :type file_name: str or pathlib.Path
      :param paginate: make project folders
      :type paginate: bool
      :param to_project_folder: save journal file to the folder containing your cellpy projects
      :type to_project_folder: bool
      :param duplicate_to_local_folder: save journal file to the folder you are in now also
      :type duplicate_to_local_folder: bool

      :returns: None


   .. py:method:: view_comments()



.. py:data:: hdr_journal

   

.. py:data:: missing_keys
   :value: []

   

.. py:data:: trans_dict

   

