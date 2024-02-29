:py:mod:`cellpy.utils.batch`
============================

.. py:module:: cellpy.utils.batch

.. autoapi-nested-parse::

   Routines for batch processing of cells (v2).



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.batch.Batch



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch.from_journal
   cellpy.utils.batch.init
   cellpy.utils.batch.iterate_batches
   cellpy.utils.batch.load
   cellpy.utils.batch.load_journal
   cellpy.utils.batch.load_pages
   cellpy.utils.batch.naked
   cellpy.utils.batch.process_batch



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch.COLUMNS_SELECTED_FOR_VIEW


.. py:class:: Batch(*args, **kwargs)


   A convenience class for running batch procedures.

   The Batch class contains (among other things):

   - iterator protocol
   - a journal with info about the different cells where the
     main information is accessible as a pandas.DataFrame through the ``.pages`` attribute
   - a data lookup accessor ``.data`` that behaves similarly as a dict.


   The initialization accepts arbitrary arguments and keyword arguments.
   It first looks for the ``file_name`` and ``db_reader`` keyword arguments.

   **Usage**::

       b = Batch((name, (project)), **kwargs)

   .. rubric:: Examples

   >>> b = Batch("experiment001", "main_project")
   >>> b = Batch("experiment001", "main_project", batch_col="b02")
   >>> b = Batch(name="experiment001", project="main_project", batch_col="b02")
   >>> b = Batch(file_name="cellpydata/batchfiles/cellpy_batch_experiment001.json")

   :param name: (project (str))
   :type name: str

   :keyword file_name: journal file name to load.
   :kwtype file_name: str or pathlib.Path
   :keyword db_reader: data-base reader to use (defaults to "default" as given
                       in the config-file or prm-class).
   :kwtype db_reader: str
   :keyword frame: load from given dataframe.
   :kwtype frame: pandas.DataFrame
   :keyword default_log_level: custom log-level (defaults to None (i.e. default log-level in cellpy)).
   :kwtype default_log_level: str
   :keyword custom_log_dir: custom folder for putting the log-files.
   :kwtype custom_log_dir: str or pathlib.Path
   :keyword force_raw_file: load from raw regardless (defaults to False).
   :kwtype force_raw_file: bool
   :keyword force_cellpy: load cellpy-files regardless (defaults to False).
   :kwtype force_cellpy: bool
   :keyword force_recalc: Always recalculate (defaults to False).
   :kwtype force_recalc: bool
   :keyword export_cycles: Extract and export individual cycles to csv (defaults to True).
   :kwtype export_cycles: bool
   :keyword export_raw: Extract and export raw-data to csv (defaults to True).
   :kwtype export_raw: bool
   :keyword export_ica: Extract and export individual dQ/dV data to csv (defaults to True).
   :kwtype export_ica: bool
   :keyword accept_errors: Continue automatically to next file if error is raised (defaults to False).
   :kwtype accept_errors: bool
   :keyword nom_cap: give a nominal capacity if you want to use another value than
                     the one given in the config-file or prm-class.
   :kwtype nom_cap: float

   .. py:property:: cell_names
      :type: list


   .. py:property:: cell_raw_headers
      :type: pandas.Index


   .. py:property:: cell_step_headers
      :type: pandas.Index


   .. py:property:: cell_summary_headers
      :type: pandas.Index


   .. py:property:: cells
      :type: cellpy.utils.batch_tools.batch_core.Data

      Access cells as a Data object (attribute lookup and automatic loading).

      .. note::

         Write ``b.cells.x`` and press <TAB>. Then a pop-up might appear, and you can choose the
         cell you would like to retrieve.

      .. warning::

         It seems that it is not always working as intended,
         at least not in my jupyter lab anymore. Instead, you can use ``b.experiment.data`` or
         write ``cells = b.cells`` and then use ``cells.x`` and press <TAB> to get the pop-up.

   .. py:property:: info_file

      The name of the info file.

      .. warning:: Will be deprecated soon - use ``journal_name`` instead.

   .. py:property:: journal
      :type: cellpy.utils.batch_tools.batch_journals.LabJournal


   .. py:property:: journal_name


   .. py:property:: labels


   .. py:property:: name


   .. py:property:: pages
      :type: pandas.DataFrame


   .. py:property:: summaries

      Concatenated summaries from all cells (multiindex dataframe).

   .. py:property:: summary_headers

      The column names of the concatenated summaries

   .. py:property:: view

      Show the selected info about each cell.

      .. warning:: Will be deprecated soon - use report() instead.

   .. py:method:: combine_summaries(export_to_csv=True, **kwargs) -> None

      Combine selected columns from each of the cells into single frames.

      :keyword export_to_csv: export the combined summaries to csv (defaults to True).
      :kwtype export_to_csv: bool
      :keyword \*\*kwargs: sent to the summary_collector.

      :returns: None


   .. py:method:: create_journal(description=None, from_db=True, auto_use_file_list=None, file_list_kwargs=None, **kwargs)

      Create journal pages.

      This method is a wrapper for the different Journal methods for making
      journal pages (``Batch.experiment.journal.xxx``). It is under development. If you
      want to use 'advanced' options (i.e. not loading from a db), please consider
      using the methods available in Journal for now.

      :param description: the information and meta-data needed to generate the journal pages:

                          - empty: create an empty journal
                          - ``dict``: create journal pages from a dictionary
                          - ``pd.DataFrame``: create journal pages from a ``pandas.DataFrame``
                          - 'filename.json': load cellpy batch file
                          - 'filename.xlsx': create journal pages from an Excel file.
      :param from_db: Deprecation Warning: this parameter will be removed as it is
                      the default anyway. Generate the pages from a db (the default option).
                      This will be over-ridden if description is given.
      :type from_db: bool
      :param auto_use_file_list: Experimental feature. If True, a file list will be generated and used
                                 instead of searching for files in the folders.
      :type auto_use_file_list: bool
      :param file_list_kwargs: Experimental feature. Keyword arguments to be sent to the file list generator.
      :type file_list_kwargs: dict
      :param \*\*kwargs: sent to sub-function(s) (*e.g.* ``from_db`` -> ``simple_db_reader`` -> ``find_files`` ->
                         ``filefinder.search_for_files``).

      The following keyword arguments are picked up by ``from_db``:

      :Transferred Parameters: * **project** -- None
                               * **name** -- None
                               * **batch_col** -- None

      The following keyword arguments are picked up by ``simple_db_reader``:

      :Transferred Parameters: * **reader** -- a reader object (defaults to dbreader.Reader)
                               * **cell_ids** -- keys (cell IDs)
                               * **file_list** -- file list to send to filefinder (instead of searching in folders for files).
                               * **pre_path** -- prepended path to send to filefinder.
                               * **include_key** -- include the key col in the pages (the cell IDs).
                               * **include_individual_arguments** -- include the argument column in the pages.
                               * **additional_column_names** -- list of additional column names to include in the pages.

      The following keyword arguments are picked up by ``filefinder.search_for_files``:

      :Transferred Parameters: * **run_name** (*str*) -- run-file identification.
                               * **raw_extension** (*str*) -- optional, extension of run-files (without the '.').
                               * **cellpy_file_extension** (*str*) -- optional, extension for cellpy files
                                 (without the '.').
                               * **raw_file_dir** (*path*) -- optional, directory where to look for run-files
                                 (default: read prm-file)
                               * **project_dir** (*path*) -- subdirectory in raw_file_dir to look for run-files
                               * **cellpy_file_dir** (*path*) -- optional, directory where to look for
                                 cellpy-files (default: read prm-file)
                               * **prm_filename** (*path*) -- optional parameter file can be given.
                               * **file_name_format** (*str*) -- format of raw-file names or a glob pattern
                                 (default: YYYYMMDD_[name]EEE_CC_TT_RR).
                               * **reg_exp** (*str*) -- use regular expression instead (defaults to None).
                               * **sub_folders** (*bool*) -- perform search also in sub-folders.
                               * **file_list** (*list of str*) -- perform the search within a given list
                                 of filenames instead of searching the folder(s). The list should
                                 not contain the full filepath (only the actual file names). If
                                 you want to provide the full path, you will have to modify the
                                 file_name_format or reg_exp accordingly.
                               * **pre_path** (*path or str*) -- path to prepend the list of files selected
                                 from the file_list.

      The following keyword arguments are picked up by ``journal.to_file``:

      :Transferred Parameters: **duplicate_to_local_folder** (*bool*) -- default True.

      :returns: None


   .. py:method:: drop(cell_label=None)

      Drop cells from the journal.

      If ``cell_label`` is not given, ``cellpy`` will look into the journal for session
      info about bad cells, and if it finds it, it will remove those from the
      journal.

      .. note:: Remember to save your journal again after modifying it.

      .. warning:: This method has not been properly tested yet.

      :param cell_label: the cell label of the cell you would like to remove.
      :type cell_label: str

      :returns: ``cellpy.utils.batch`` object (returns a copy if `keep_old` is ``True``).


   .. py:method:: drop_cell(cell_label)

      Drop a cell from the journal.

      :param cell_label: the cell label of the cell you would like to remove.


   .. py:method:: drop_cells(cell_labels)

      Drop cells from the journal.

      :param cell_labels: the cell labels of the cells you would like to remove.


   .. py:method:: drop_cells_marked_bad()

      Drop cells that has been marked as bad from the journal (experimental feature).


   .. py:method:: duplicate_cellpy_files(location: str = 'standard', selector: dict = None, **kwargs) -> None

      Copy the cellpy files and make a journal with the new names available in
      the current folder.

      :param location: where to copy the files. Either choose among the following options:

                       - 'standard': data/interim folder
                       - 'here': current directory
                       - 'cellpydatadir': the stated cellpy data dir in your settings (prms)

                       or if the location is not one of the above, use the actual value of the location argument.
      :param selector: if given, the cellpy files are reloaded after duplicating and
                       modified based on the given selector(s).
      :type selector: dict
      :param \*\*kwargs: sent to ``Batch.experiment.update`` if selector is provided

      :returns: The updated journal pages.


   .. py:method:: duplicate_journal(folder=None) -> None

      Copy the journal to folder.

      :param folder: folder to copy to (defaults to the
      :type folder: str or pathlib.Path
      :param current folder).:


   .. py:method:: export_cellpy_files(path=None, **kwargs) -> None


   .. py:method:: export_journal(filename=None) -> None

      Export the journal to xlsx.

      :param filename: the name of the file to save the journal to.
                       If not given, the journal will be saved to the default name.
      :type filename: str or pathlib.Path


   .. py:method:: link(max_cycle=None, force_combine_summaries=False) -> None

      Link journal content to the cellpy-files and load the step information.

      :param max_cycle: set maximum cycle number to link to.
      :type max_cycle: int
      :param force_combine_summaries: automatically run combine_summaries (set this to True
                                      if you are re-linking without max_cycle for a batch that previously were linked
                                      with max_cycle)
      :type force_combine_summaries: bool


   .. py:method:: load() -> None

      Load the selected datasets.

      .. warning:: Will be deprecated soon - use ``update`` instead.


   .. py:method:: make_summaries() -> None

      Combine selected columns from each of the cells into single frames and export.

      .. warning:: This method will be deprecated in the future. Use ``combine_summaries`` instead.


   .. py:method:: mark_as_bad(cell_label)

      Mark a cell as bad (experimental feature).

      :param cell_label: the cell label of the cell you would like to mark as bad.


   .. py:method:: paginate() -> None

      Create the folders where cellpy will put its output.


   .. py:method:: plot(backend=None, reload_data=False, **kwargs)

      Plot the summaries (e.g. capacity vs. cycle number).

      :param backend: plotting backend (plotly, bokeh, matplotlib, seaborn)
      :type backend: str
      :param reload_data: reload the data before plotting
      :type reload_data: bool
      :param \*\*kwargs: sent to the plotter

      :keyword color_map: color map to use (defaults to ``px.colors.qualitative.Set1``
                          for ``plotly`` and "Set1" for ``seaborn``)
      :kwtype color_map: str, any
      :keyword ce_range: optional range for the coulombic efficiency plot
      :kwtype ce_range: list
      :keyword min_cycle: minimum cycle number to plot
      :kwtype min_cycle: int
      :keyword max_cycle: maximum cycle number to plot
      :kwtype max_cycle: int
      :keyword title: title of the figure (defaults to "Cycle Summary")
      :kwtype title: str
      :keyword x_label: title of the x-label (defaults to "Cycle Number")
      :kwtype x_label: str
      :keyword direction: plot charge or discharge (defaults to "charge")
      :kwtype direction: str
      :keyword rate: (defaults to False)
      :kwtype rate: bool
      :keyword ir: (defaults to True)
      :kwtype ir: bool
      :keyword group_legends: group the legends so that they can be turned visible/invisible
                              as a group (defaults to True) (only for plotly)
      :kwtype group_legends: bool
      :keyword base_template: template to use for the plot (only for plotly)
      :kwtype base_template: str


   .. py:method:: plot_summaries(output_filename=None, backend=None, reload_data=False, **kwargs) -> None

      Plot the summaries.

      .. warning:: This method will be deprecated in the future. Use ``plot`` instead.


   .. py:method:: recalc(**kwargs) -> None

      Run ``make_step_table`` and ``make_summary`` on all cells.

      :keyword save: Save updated cellpy-files if True (defaults to True).
      :kwtype save: bool
      :keyword step_opts: parameters to inject to make_steps (defaults to None).
      :kwtype step_opts: dict
      :keyword summary_opts: parameters to inject to make_summary (defaults to None).
      :kwtype summary_opts: dict
      :keyword indexes: Only recalculate for given indexes (i.e. list of cell-names) (defaults to None).
      :kwtype indexes: list
      :keyword calc_steps: Run make_steps before making the summary (defaults to True).
      :kwtype calc_steps: bool
      :keyword testing: Only for testing purposes (defaults to False).
      :kwtype testing: bool

      :returns: None


   .. py:method:: remove_mark_as_bad(cell_label)

      Remove the bad cell mark from a cell (experimental feature).

      :param cell_label: the cell label of the cell you would like to remove the bad mark from.


   .. py:method:: report(stylize=True, grouped=False, check=False)

      Create a report on all the cells in the batch object.

      .. important:: To perform a reporting, cellpy needs to access all the data (and it might take some time).

      :param stylize: apply some styling to the report (default True).
      :type stylize: bool
      :param grouped: add information based on the group cell belongs to (default False).
      :type grouped: bool
      :param check: check if the data seems to be without errors (0 = no errors, 1 = partial duplicates)
                    (default False).
      :type check: bool

      :returns: ``pandas.DataFrame``


   .. py:method:: save_journal() -> None

      Save the journal (json-format).

      The journal file will be saved in the project directory and in the
      batch-file-directory (``prms.Paths.batchfiledir``). The latter is useful
      for processing several batches using the ``iterate_batches`` functionality.



   .. py:method:: show_pages(number_of_rows=5)

      Show the journal pages.

      .. warning:: Will be deprecated soon - use pages.head() instead.


   .. py:method:: update(pool=False, **kwargs) -> None

      Updates the selected datasets.

      :keyword all_in_memory: store the `cellpydata` in memory (default
                              False)
      :kwtype all_in_memory: bool
      :keyword cell_specs: individual arguments pr. cell. The ``cellspecs`` key-word argument
                           dictionary will override the **kwargs and the parameters from the journal pages
                           for the indicated cell.
      :kwtype cell_specs: dict of dicts
      :keyword logging_mode: sets the logging mode for the loader(s).
      :kwtype logging_mode: str
      :keyword accept_errors: if True, the loader will continue even if it encounters errors.
      :kwtype accept_errors: bool

      Additional keyword arguments are sent to the loader(s)  if not
      picked up earlier. Remark that you can obtain the same pr. cell by
      providing a ``cellspecs`` dictionary. The kwargs have precedence over the
      parameters given in the journal pages, but will be overridden by parameters
      given by ``cellspecs``.

      Merging picks up the following keyword arguments:

      :Transferred Parameters: **recalc** (*Bool*) -- set to False if you don't want automatic recalculation of
                               cycle numbers etc. when merging several data-sets.

      Loading picks up the following keyword arguments:

      :Transferred Parameters: **selector** (*dict*) -- selector-based parameters sent to the cellpy-file loader (hdf5) if
                               loading from raw is not necessary (or turned off).



.. py:function:: from_journal(journal_file, autolink=True, testing=False) -> Batch

   Create a Batch from a journal file


.. py:function:: init(*args, empty=False, **kwargs) -> Batch

   Returns an initialized instance of the Batch class.

   :param empty: if True, the batch will not be linked to any database and
                 an empty batch is returned
   :type empty: bool
   :param \*args: passed directly to Batch()

                  - **name**: name of batch.
                  - **project**: name of project.
                  - **batch_col**: batch column identifier.

   :keyword file_name: json file if loading from pages (journal).
   :keyword default_log_level: "INFO" or "DEBUG". Defaults to "CRITICAL".

   Other keyword arguments are sent to the Batch object.

   .. rubric:: Examples

   >>> empty_batch = Batch.init(db_reader=None)
   >>> batch_from_file = Batch.init(file_name="cellpy_batch_my_experiment.json")
   >>> normal_init_of_batch = Batch.init()


.. py:function:: iterate_batches(folder, extension='.json', glob_pattern=None, **kwargs)

   Iterate through all journals in given folder.

   .. warning::

      This function is from ancient times and needs to be updated. It might have grown old and grumpy.
      Expect it to change in the near future.

   :param folder: folder containing the journal files.
   :type folder: str or pathlib.Path
   :param extension: extension for the journal files (used when creating a default glob-pattern).
   :type extension: str
   :param glob_pattern: optional glob pattern.
   :type glob_pattern: str
   :param \*\*kwargs: keyword arguments passed to ``batch.process_batch``.


.. py:function:: load(name, project, batch_col=None, allow_from_journal=True, drop_bad_cells=True, force_reload=False, **kwargs)

   Load a batch from a journal file or create a new batch and load it if the journal file does not exist.

   :param name: name of batch
   :type name: str
   :param project: name of project
   :type project: str
   :param batch_col: batch column identifier (only used for loading from db with simple_db_reader)
   :type batch_col: str
   :param allow_from_journal: if True, the journal file will be loaded if it exists
   :type allow_from_journal: bool
   :param force_reload: if True, the batch will be reloaded even if the journal file exists
   :type force_reload: bool
   :param drop_bad_cells: if True, bad cells will be dropped (only apply if journal file is loaded)
   :type drop_bad_cells: bool
   :param \*\*kwargs: sent to Batch during initialization

   :returns: populated Batch object (``cellpy.utils.batch.Batch``)


.. py:function:: load_journal(journal_file, **kwargs)

   Load a journal file.

   :param journal_file: path to journal file.
   :type journal_file: str
   :param \*\*kwargs: sent to ``Journal.from_file``

   :returns: journal


.. py:function:: load_pages(file_name) -> pandas.DataFrame

   Retrieve pages from a Journal file.

   This function is here to let you easily inspect a Journal file without
   starting up the full batch-functionality.

   .. rubric:: Examples

   >>> from cellpy.utils import batch
   >>> journal_file_name = 'cellpy_journal_one.json'
   >>> pages = batch.load_pages(journal_file_name)

   :returns: pandas.DataFrame


.. py:function:: naked(name=None, project=None) -> Batch

   Returns an empty instance of the Batch class.

   .. rubric:: Examples

   >>> empty_batch = naked()


.. py:function:: process_batch(*args, **kwargs) -> Batch

   Execute a batch run, either from a given file_name or by giving the name and project as input.

   .. warning::

      This function is from ancient times and needs to be updated. It might have grown old and grumpy.
      Expect it to change in the near future.

   .. rubric:: Examples

   >>> process_batch(file_name | (name, project), **kwargs)

   :param \*args: file_name or name and project (both string)

   :keyword backend: what backend to use when plotting ('bokeh' or 'matplotlib').
                     Defaults to 'matplotlib'.
   :kwtype backend: str
   :keyword dpi: resolution used when saving matplotlib plot(s). Defaults to 300 dpi.
   :kwtype dpi: int
   :keyword default_log_level: What log-level to use for console output. Chose between
                               'CRITICAL', 'DEBUG', or 'INFO'. The default is 'CRITICAL' (i.e. usually no log output to console).
   :kwtype default_log_level: str

   :returns: ``cellpy.batch.Batch`` object


.. py:data:: COLUMNS_SELECTED_FOR_VIEW

   

