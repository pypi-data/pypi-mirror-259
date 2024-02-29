:py:mod:`cellpy.utils.helpers`
==============================

.. py:module:: cellpy.utils.helpers


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.helpers.add_areal_capacity
   cellpy.utils.helpers.add_c_rate
   cellpy.utils.helpers.add_normalized_capacity
   cellpy.utils.helpers.add_normalized_cycle_index
   cellpy.utils.helpers.collect_frames
   cellpy.utils.helpers.concat_summaries
   cellpy.utils.helpers.concatenate_summaries
   cellpy.utils.helpers.create_group_names
   cellpy.utils.helpers.create_rate_column
   cellpy.utils.helpers.filter_cells
   cellpy.utils.helpers.fix_group_names
   cellpy.utils.helpers.load_and_save_resfile
   cellpy.utils.helpers.make_new_cell
   cellpy.utils.helpers.remove_first_cycles_from_summary
   cellpy.utils.helpers.remove_last_cycles_from_summary
   cellpy.utils.helpers.remove_outliers_from_summary_on_index
   cellpy.utils.helpers.remove_outliers_from_summary_on_nn_distance
   cellpy.utils.helpers.remove_outliers_from_summary_on_value
   cellpy.utils.helpers.remove_outliers_from_summary_on_window
   cellpy.utils.helpers.remove_outliers_from_summary_on_zscore
   cellpy.utils.helpers.select_summary_based_on_rate
   cellpy.utils.helpers.update_journal_cellpy_data_dir
   cellpy.utils.helpers.yank_after
   cellpy.utils.helpers.yank_before
   cellpy.utils.helpers.yank_outliers



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.helpers.hdr_journal
   cellpy.utils.helpers.hdr_normal
   cellpy.utils.helpers.hdr_steps
   cellpy.utils.helpers.hdr_summary


.. py:function:: add_areal_capacity(cell, cell_id, journal)

   Adds areal capacity to the summary.


.. py:function:: add_c_rate(cell, nom_cap=None, column_name=None)

   Adds C-rates to the step table data frame.

   This functionality is now also implemented as default when creating
   the step_table (make_step_table). However, it is kept here if you would
   like to recalculate the C-rates, for example if you want to use another
   nominal capacity or if you would like to have more than one column with
   C-rates.

   :param cell: cell object
   :type cell: CellpyCell
   :param nom_cap: nominal capacity to use for estimating C-rates.
                   Defaults to the nominal capacity defined in the cell object
                   (this is typically set during creation of the CellpyData object
                   based on the value given in the parameter file).
   :type nom_cap: float
   :param column_name: name of the new column. Uses the name defined in
                       cellpy.parameters.internal_settings as default.
   :type column_name: str

   :returns: data object.


.. py:function:: add_normalized_capacity(cell, norm_cycles=None, individual_normalization=False, scale=1.0)

   Add normalized capacity to the summary.

   :param cell: cell to add normalized capacity to.
   :type cell: CellpyCell
   :param norm_cycles: the cycles that will be used to find
                       the normalization factor from (averaging their capacity)
   :type norm_cycles: list of ints
   :param individual_normalization: find normalization factor for both
                                    the charge and the discharge if true, else use normalization factor
                                    from charge on both charge and discharge.
   :type individual_normalization: bool
   :param scale: scale of normalization (default is 1.0).
   :type scale: float

   :returns: cell (CellpyData) with added normalization capacity columns in
             the summary.


.. py:function:: add_normalized_cycle_index(summary, nom_cap, column_name=None)

   Adds normalized cycles to the summary data frame.

   This functionality is now also implemented as default when creating
   the summary (make_summary). However, it is kept here if you would like to
   redo the normalization, for example if you want to use another nominal
   capacity or if you would like to have more than one normalized cycle index.

   :param summary: data summary
   :type summary: pandas.DataFrame
   :param nom_cap: nominal capacity to use when normalizing.
   :type nom_cap: float
   :param column_name: name of the new column. Uses the name defined in
                       cellpy.parameters.internal_settings as default.
   :type column_name: str

   :returns: data object now with normalized cycle index in its summary.


.. py:function:: collect_frames(frames, group_it: bool, hdr_norm_cycle: str, keys: list, normalize_cycles: bool)

   Helper function for concat_summaries.


.. py:function:: concat_summaries(b: cellpy.utils.batch.Batch, max_cycle=None, rate=None, on='charge', columns=None, column_names=None, normalize_capacity_on=None, scale_by=None, nom_cap=None, normalize_cycles=False, group_it=False, custom_group_labels=None, rate_std=None, rate_column=None, inverse=False, inverted=False, key_index_bounds=None, pages=None, recalc_summary_kwargs=None, recalc_step_table_kwargs=None) -> pandas.DataFrame

   Merge all summaries in a batch into a gigantic summary data frame.

   :param b: the batch with the cells.
   :type b: cellpy.batch object
   :param max_cycle: drop all cycles above this value.
   :type max_cycle: int
   :param rate: filter on rate (C-rate)
   :type rate: float
   :param on: only select cycles if based on the rate of this step-type (e.g. on="charge").
   :type on: str or list of str
   :param columns: selected column(s) (using cellpy attribute name) [defaults to "charge_capacity_gravimetric"]
   :type columns: list
   :param column_names: selected column(s) (using exact column name)
   :type column_names: list
   :param normalize_capacity_on: list of cycle numbers that will be used for setting the basis of the
                                 normalization (typically the first few cycles after formation)
   :type normalize_capacity_on: list
   :param scale_by: scale the normalized data with nominal capacity if "nom_cap",
                    or given value (defaults to one).
   :type scale_by: float or str
   :param nom_cap: nominal capacity of the cell
   :type nom_cap: float
   :param normalize_cycles: perform a normalization of the cycle numbers (also called equivalent cycle index)
   :type normalize_cycles: bool
   :param group_it: if True, average pr group.
   :type group_it: bool
   :param custom_group_labels: dictionary of custom labels (key must be the group number/name).
   :type custom_group_labels: dict
   :param rate_std: allow for this inaccuracy when selecting cycles based on rate
   :type rate_std: float
   :param rate_column: name of the column containing the C-rates.
   :type rate_column: str
   :param inverse: select steps that do not have the given C-rate.
   :type inverse: bool
   :param inverted: select cycles that do not have the steps filtered by given C-rate.
   :type inverted: bool
   :param key_index_bounds: used when creating a common label for the cells by splitting the label on '_'
                            and combining again using the key_index_bounds as start and end index.
   :type key_index_bounds: list
   :param pages: alternative pages (journal) of the batch object (if not given, it will use the
                 pages from the batch object).
   :type pages: pandas.DataFrame
   :param recalc_summary_kwargs: keyword arguments to be used when recalculating the summary. If not given, it
                                 will not recalculate the summary.
   :type recalc_summary_kwargs: dict
   :param recalc_step_table_kwargs: keyword arguments to be used when recalculating the step table. If not given,
                                    it will not recalculate the step table.
   :type recalc_step_table_kwargs: dict

   :returns: ``pandas.DataFrame``


.. py:function:: concatenate_summaries(b: cellpy.utils.batch.Batch, max_cycle=None, rate=None, on='charge', columns=None, column_names=None, normalize_capacity_on=None, scale_by=None, nom_cap=None, normalize_cycles=False, group_it=False, custom_group_labels=None, rate_std=None, rate_column=None, inverse=False, inverted=False, key_index_bounds=None) -> pandas.DataFrame

   Merge all summaries in a batch into a gigantic summary data frame.

   :param b: the batch with the cells.
   :type b: cellpy.batch object
   :param max_cycle: drop all cycles above this value.
   :type max_cycle: int
   :param rate: filter on rate (C-rate)
   :type rate: float
   :param on: only select cycles if based on the rate of this step-type (e.g. on="charge").
   :type on: str or list of str
   :param columns: selected column(s) (using cellpy attribute name) [defaults to "charge_capacity_gravimetric"]
   :type columns: list
   :param column_names: selected column(s) (using exact column name)
   :type column_names: list
   :param normalize_capacity_on: list of cycle numbers that will be used for setting the basis of the
                                 normalization (typically the first few cycles after formation)
   :type normalize_capacity_on: list
   :param scale_by: scale the normalized data with nominal capacity if "nom_cap",
                    or given value (defaults to one).
   :type scale_by: float or str
   :param nom_cap: nominal capacity of the cell
   :type nom_cap: float
   :param normalize_cycles: perform a normalization of the cycle numbers (also called equivalent cycle index)
   :type normalize_cycles: bool
   :param group_it: if True, average pr group.
   :type group_it: bool
   :param custom_group_labels: dictionary of custom labels (key must be the group number/name).
   :type custom_group_labels: dict
   :param rate_std: allow for this inaccuracy when selecting cycles based on rate
   :type rate_std: float
   :param rate_column: name of the column containing the C-rates.
   :type rate_column: str
   :param inverse: select steps that do not have the given C-rate.
   :type inverse: bool
   :param inverted: select cycles that do not have the steps filtered by given C-rate.
   :type inverted: bool
   :param key_index_bounds: used when creating a common label for the cells by splitting and combining from
                            key_index_bound[0] to key_index_bound[1].
   :type key_index_bounds: list

   :returns: ``pandas.DataFrame``


.. py:function:: create_group_names(custom_group_labels, gno, key_index_bounds, keys_sub, pages)

   Helper function for concat_summaries.

   :param custom_group_labels: dictionary of custom labels (key must be the group number).
   :type custom_group_labels: dict
   :param gno: group number.
   :type gno: int
   :param key_index_bounds: used when creating a common label for the cells by splitting the label on '_'
                            and combining again using the key_index_bounds as start and end index.
   :type key_index_bounds: list
   :param keys_sub: list of keys.
   :type keys_sub: list
   :param pages: pages (journal) of the batch object. If the column "group_label" is present, it will
                 be used to create the group name.
   :type pages: pandas.DataFrame


.. py:function:: create_rate_column(df, nom_cap, spec_conv_factor, column='current_avr')

   Adds a rate column to the dataframe (steps).


.. py:function:: filter_cells()

   Filter cells based on some criteria.

   This is a helper function that can be used to filter cells based on
   some criteria. It is not very flexible, but it is easy to use.

   :returns: a list of cell names that passed the criteria.


.. py:function:: fix_group_names(keys)

   Helper function for concat_summaries.


.. py:function:: load_and_save_resfile(filename, outfile=None, outdir=None, mass=1.0)

   Load a raw data file and save it as cellpy-file.

   :param mass: active material mass [mg].
   :type mass: float
   :param outdir: optional, path to directory for saving the hdf5-file.
   :type outdir: path
   :param outfile: optional, name of hdf5-file.
   :type outfile: str
   :param filename: name of the resfile.
   :type filename: str

   :returns: name of saved file.
   :rtype: out_file_name (str)


.. py:function:: make_new_cell()

   create an empty CellpyCell object.


.. py:function:: remove_first_cycles_from_summary(s, first=None)

   Remove last rows after given cycle number


.. py:function:: remove_last_cycles_from_summary(s, last=None)

   Remove last rows after given cycle number


.. py:function:: remove_outliers_from_summary_on_index(s, indexes=None, remove_last=False)

   Remove rows with supplied indexes (where the indexes typically are cycle-indexes).

   :param s: cellpy summary to process
   :type s: pandas.DataFrame
   :param indexes: list of indexes
   :type indexes: list
   :param remove_last: remove the last point
   :type remove_last: bool

   :returns: pandas.DataFrame


.. py:function:: remove_outliers_from_summary_on_nn_distance(s, distance=0.7, filter_cols=None, freeze_indexes=None)

   Remove outliers with missing neighbours.

   :param s: summary frame
   :type s: pandas.DataFrame
   :param distance: cut-off (all cycles that have a closest neighbour further apart this number will be removed)
   :type distance: float
   :param filter_cols: list of column headers to perform the filtering on (defaults to charge and discharge capacity)
   :type filter_cols: list
   :param freeze_indexes: list of cycle indexes that should never be removed (defaults to cycle 1)
   :type freeze_indexes: list

   :returns: filtered summary (pandas.DataFrame)

   Returns:



.. py:function:: remove_outliers_from_summary_on_value(s, low=0.0, high=7000, filter_cols=None, freeze_indexes=None)

   Remove outliers based highest and lowest allowed value

   :param s: summary frame
   :type s: pandas.DataFrame
   :param low: low cut-off (all cycles with values below this number will be removed)
   :type low: float
   :param high: high cut-off (all cycles with values above this number will be removed)
   :type high: float
   :param filter_cols: list of column headers to perform the filtering on (defaults to charge and discharge capacity)
   :type filter_cols: list
   :param freeze_indexes: list of cycle indexes that should never be removed (defaults to cycle 1)
   :type freeze_indexes: list

   :returns: filtered summary (pandas.DataFrame)

   Returns:



.. py:function:: remove_outliers_from_summary_on_window(s, window_size=3, cut=0.1, iterations=1, col_name=None, freeze_indexes=None)

   Removes outliers based on neighbours


.. py:function:: remove_outliers_from_summary_on_zscore(s, zscore_limit=4, filter_cols=None, freeze_indexes=None)

   Remove outliers based on z-score.

   :param s: summary frame
   :type s: pandas.DataFrame
   :param zscore_limit: remove outliers outside this z-score limit
   :type zscore_limit: int
   :param filter_cols: list of column headers to perform the filtering on (defaults to charge and discharge capacity)
   :type filter_cols: list
   :param freeze_indexes: list of cycle indexes that should never be removed (defaults to cycle 1)
   :type freeze_indexes: list

   :returns: filtered summary (pandas.DataFrame)


.. py:function:: select_summary_based_on_rate(cell, rate=None, on=None, rate_std=None, rate_column=None, inverse=False, inverted=False, fix_index=True)

   Select only cycles charged or discharged with a given rate.

   :param cell:
   :type cell: cellpy.CellpyCell
   :param rate: the rate to filter on. Remark that it should be given
                as a float, i.e. you will have to convert from C-rate to
                the actual numeric value. For example, use rate=0.05 if you want
                to filter on cycles that has a C/20 rate.
   :type rate: float
   :param on: only select cycles if based on the rate of this step-type (e.g. on="charge").
   :type on: str
   :param rate_std: allow for this inaccuracy in C-rate when selecting cycles
   :type rate_std: float
   :param rate_column: column header name of the rate column,
   :type rate_column: str
   :param inverse: select steps that do not have the given C-rate.
   :type inverse: bool
   :param inverted: select cycles that do not have the steps filtered by given C-rate.
   :type inverted: bool
   :param fix_index: automatically set cycle indexes as the index for the summary dataframe if not already set.
   :type fix_index: bool

   :returns: filtered summary (Pandas.DataFrame).


.. py:function:: update_journal_cellpy_data_dir(pages, new_path=None, from_path='PureWindowsPath', to_path='Path')

   Update the path in the pages (batch) from one type of OS to another.

   I use this function when I switch from my work PC (windows) to my home
   computer (mac).

   :param pages: the (batch.experiment.)journal.pages object (pandas.DataFrame)
   :param new_path: the base path (uses prms.Paths.cellpydatadir if not given)
   :param from_path: type of path to convert from.
   :param to_path: type of path to convert to.

   :returns: journal.pages (pandas.DataFrame)


.. py:function:: yank_after(b, last=None, keep_old=False)

   Cut all cycles after a given cycle index number.

   :param b: the batch object to perform the cut on.
   :type b: batch object
   :param last (int or dict {cell_name: last index}): the last cycle index to keep
                                        (if dict: use individual last indexes for each cell).
   :param keep_old: keep the original batch object and return a copy instead.
   :type keep_old: bool

   :returns: batch object if keep_old is True, else None


.. py:function:: yank_before(b, first=None, keep_old=False)

   Cut all cycles before a given cycle index number.

   :param b: the batch object to perform the cut on.
   :type b: batch object
   :param first (int or dict {cell_name: first index}): the first cycle index to keep
                                         (if dict: use individual first indexes for each cell).
   :param keep_old: keep the original batch object and return a copy instead.
   :type keep_old: bool

   :returns: batch object if keep_old is True, else None


.. py:function:: yank_outliers(b: cellpy.utils.batch.Batch, zscore_limit=None, low=0.0, high=7000.0, filter_cols=None, freeze_indexes=None, remove_indexes=None, remove_last=False, iterations=1, zscore_multiplyer=1.3, distance=None, window_size=None, window_cut=0.1, keep_old=False)

   Remove outliers from a batch object.

   :param b: the batch object to perform filtering one (required).
   :type b: cellpy.utils.batch object
   :param zscore_limit: will filter based on z-score if given.
   :type zscore_limit: int
   :param low: low cut-off (all cycles with values below this number will be removed)
   :type low: float
   :param high: high cut-off (all cycles with values above this number will be removed)
   :type high: float
   :param filter_cols: what columns to filter on.
   :type filter_cols: str
   :param freeze_indexes: indexes (cycles) that should never be removed.
   :type freeze_indexes: list
   :param remove_indexes: if dict, look-up on cell label, else a list that will be the same for all
   :type remove_indexes: dict or list
   :param remove_last: if dict, look-up on cell label.
   :type remove_last: dict or bool
   :param iterations: repeat z-score filtering if `zscore_limit` is given.
   :type iterations: int
   :param zscore_multiplyer: multiply `zscore_limit` with this number between each z-score filtering
                             (should usually be less than 1).
   :type zscore_multiplyer: int
   :param distance: nearest neighbour normalised distance required (typically 0.5).
   :type distance: float
   :param window_size: number of cycles to include in the window.
   :type window_size: int
   :param window_cut: cut-off.
   :type window_cut: float
   :param keep_old: perform filtering of a copy of the batch object
                    (not recommended at the moment since it then loads the full cellpyfile).
   :type keep_old: bool

   :returns: new cellpy.utils.batch object.
             else: dictionary of removed cycles
   :rtype: if keep_old


.. py:data:: hdr_journal

   

.. py:data:: hdr_normal

   

.. py:data:: hdr_steps

   

.. py:data:: hdr_summary

   

