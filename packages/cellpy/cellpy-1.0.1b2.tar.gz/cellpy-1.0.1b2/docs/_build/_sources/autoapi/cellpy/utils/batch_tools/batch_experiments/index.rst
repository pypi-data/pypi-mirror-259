:py:mod:`cellpy.utils.batch_tools.batch_experiments`
====================================================

.. py:module:: cellpy.utils.batch_tools.batch_experiments


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_experiments.CyclingExperiment
   cellpy.utils.batch_tools.batch_experiments.ImpedanceExperiment
   cellpy.utils.batch_tools.batch_experiments.LifeTimeExperiment




Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_experiments.hdr_journal
   cellpy.utils.batch_tools.batch_experiments.hdr_summary
   cellpy.utils.batch_tools.batch_experiments.project_dir


.. py:class:: CyclingExperiment(*args, **kwargs)


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseExperiment`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_experiments.CyclingExperiment
      :parts: 1

   Load experimental data into memory.

   This is a re-implementation of the old batch behaviour where
   all the data-files are processed sequentially (and optionally exported)
   while the summary tables are kept and processed. This implementation
   also saves the step tables (for later use when using look-up
   functionality).


   .. attribute:: journal (

      obj: LabJournal): information about the experiment.

   .. attribute:: force_cellpy

      tries only to load the cellpy-file if True.

      :type: bool

   .. attribute:: force_raw

      loads raw-file(s) even though appropriate cellpy-file
      exists if True.

      :type: bool

   .. attribute:: save_cellpy

      saves a cellpy-file for each cell if True.

      :type: bool

   .. attribute:: accept_errors

      in case of error, dont raise an exception, but
      continue to the next file if True.

      :type: bool

   .. attribute:: all_in_memory

      store the cellpydata-objects in memory if True.

      :type: bool

   .. attribute:: export_cycles

      export voltage-capacity curves if True.

      :type: bool

   .. attribute:: shifted_cycles

      set this to True if you want to export the
      voltage-capacity curves using the shifted-cycles option (only valid
      if you set export_cycles to True).

      :type: bool

   .. attribute:: export_raw

      export the raw-data if True.

      :type: bool

   .. attribute:: export_ica

      export dq-dv curves if True.

      :type: bool

   .. attribute:: last_cycle

      sets the last cycle (i.e. the highest cycle number)
      that you would like to process dq-dv on). Use all if None (the
      default value).

      :type: int

   .. attribute:: selected_summaries

      a list of summary labels defining what
      summary columns to make joint summaries from (optional).

      :type: list

   .. attribute:: errors

      contains a dictionary listing all the errors encountered.

      :type: dict

   :param db_reader: custom db_reader (see doc on db_reader).
   :type db_reader: str or object

   Example:



   .. py:property:: cell_names

      Returns a list of cell-names (strings)

   .. py:method:: export_cellpy_files(path=None, **kwargs)

      Export all cellpy-files to a given path.

      Remarks:
          This method can only export to local folders
          (OtherPath objects are not formally supported, but
          might still work if the path is local).

      :param path: path to export to (default: current working directory)
      :type path: str, pathlib.Path


   .. py:method:: link(**kwargs)

      Ensure that an appropriate link to the cellpy-files exists for
      each cell.

      The experiment will then contain a CellpyCell object for each cell
      (in the cell_data_frames attribute) with only the step-table stored.

      Remark that running update persists the summary frames instead (or
      everything in case you specify all_in_memory=True).
      This might be considered "a strange and unexpected behaviour". Sorry
      for that (but the authors of this package is also a bit strange...).

      (OK, I will change it. Soon.)

      **kwargs: passed to _link_cellpy_file
          max_cycle (int): maximum cycle number to link/load (remark that the
              cellpy objects will get the property overwrite_able set to False
              if you give a max_cycle to prevent accidentally saving a "truncated"
              file (use c.save(filename, overwrite=True) to force overwrite))




   .. py:method:: parallel_update(all_in_memory=None, cell_specs=None, logging_mode=None, **kwargs)

      Updates the selected datasets in parallel.

      :param all_in_memory: store the `cellpydata` in memory (default
                            False)
      :type all_in_memory: bool
      :param cell_specs: individual arguments pr. cell. The `cellspecs` key-word argument
                         dictionary will override the **kwargs and the parameters from the journal pages
                         for the indicated cell.
      :type cell_specs: dict of dicts
      :param logging_mode: sets the logging mode for the loader(s).
      :type logging_mode: str
      :param kwargs: transferred all the way to the instrument loader, if not
                     picked up earlier. Remark that you can obtain the same pr. cell by
                     providing a `cellspecs` dictionary. The kwargs have precedence over the
                     parameters given in the journal pages, but will be overridden by parameters
                     given by `cellspecs`.

                     Merging:
                         recalc (Bool): set to False if you don't want automatic "recalc" of
                             cycle numbers etc. when merging several data-sets.
                     Loading:
                         selector (dict): selector-based parameters sent to the cellpy-file loader (hdf5) if
                         loading from raw is not necessary (or turned off).

                     Debugging:
                         debug (Bool): set to True if you want to run in debug mode (should never be used by non-developers).

      Debug-mode:
               - runs only for the first item in your journal

      .. rubric:: Examples

      >>> # Don't perform recalculation of cycle numbers etc. when merging
      >>> # All cells:
      >>> b.update(recalc=False)
      >>> # For specific cell(s):
      >>> cell_specs_cell_01 = {"name_of_cell_01": {"recalc": False}}
      >>> b.update(cell_specs=cell_specs_cell_01)


   .. py:method:: recalc(save=True, step_opts=None, summary_opts=None, indexes=None, calc_steps=True, testing=False)

      Run make_step_table and make_summary on all cells.

      :param save: Save updated cellpy-files if True.
      :type save: bool
      :param step_opts: parameters to inject to make_steps.
      :type step_opts: dict
      :param summary_opts: parameters to inject to make_summary.
      :type summary_opts: dict
      :param indexes: Only recalculate for given indexes (i.e. list of cell-names).
      :type indexes: list
      :param calc_steps: Run make_steps before making the summary.
      :type calc_steps: bool
      :param testing: Only for testing purposes.
      :type testing: bool

      :returns: None


   .. py:method:: status()

      Describe the status and health of your experiment.


   .. py:method:: update(all_in_memory=None, cell_specs=None, logging_mode=None, accept_errors=None, **kwargs)

      Updates the selected datasets.

      :param all_in_memory: store the `cellpydata` in memory (default
                            False)
      :type all_in_memory: bool
      :param cell_specs: individual arguments pr. cell. The `cellspecs` key-word argument
                         dictionary will override the **kwargs and the parameters from the journal pages
                         for the indicated cell.
      :type cell_specs: dict of dicts
      :param logging_mode: sets the logging mode for the loader(s).
      :type logging_mode: str
      :param accept_errors: if True, the loader will continue even if it encounters errors.
      :type accept_errors: bool
      :param kwargs: transferred all the way to the instrument loader, if not
                     picked up earlier. Remark that you can obtain the same pr. cell by
                     providing a `cellspecs` dictionary. The kwargs have precedence over the
                     parameters given in the journal pages, but will be overridden by parameters
                     given by `cellspecs`.

                     Merging:
                         recalc (Bool): set to False if you don't want automatic "recalc" of
                             cycle numbers etc. when merging several data-sets.
                     Loading:
                         selector (dict): selector-based parameters sent to the cellpy-file loader (hdf5) if
                         loading from raw is not necessary (or turned off).

                     Debugging:
                         debug (Bool): set to True if you want to run in debug mode (should never be used by non-developers).

      Debug-mode:
               - runs only for the first item in your journal

      .. rubric:: Examples

      >>> # Don't perform recalculation of cycle numbers etc. when merging
      >>> # All cells:
      >>> b.update(recalc=False)
      >>> # For specific cell(s):
      >>> cell_specs_cell_01 = {"name_of_cell_01": {"recalc": False}}
      >>> b.update(cell_specs=cell_specs_cell_01)



.. py:class:: ImpedanceExperiment


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseExperiment`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_experiments.ImpedanceExperiment
      :parts: 1

   An experiment contains experimental data and meta-data.


.. py:class:: LifeTimeExperiment


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseExperiment`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_experiments.LifeTimeExperiment
      :parts: 1

   An experiment contains experimental data and meta-data.


.. py:data:: hdr_journal

   

.. py:data:: hdr_summary

   

.. py:data:: project_dir

   

