:py:mod:`cellpy.readers.cellreader`
===================================

.. py:module:: cellpy.readers.cellreader

.. autoapi-nested-parse::

   Datareader for cell testers and potentiostats.

   This module is used for loading data and databases created by different cell
   testers and exporing them in a common hdf5-format.

   .. rubric:: Example

   >>> c = cellpy.get(["super_battery_run_01.res", "super_battery_run_02.res"]) # loads and merges the runs
   >>> voltage_curves = c.get_cap()
   >>> c.save("super_battery_run.hdf")



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.cellreader.CellpyCell



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.cellreader.get



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.cellreader.DIGITS_C_RATE
   cellpy.readers.cellreader.HEADERS_NORMAL
   cellpy.readers.cellreader.HEADERS_STEP_TABLE
   cellpy.readers.cellreader.HEADERS_SUMMARY


.. py:class:: CellpyCell(filenames=None, selected_scans=None, profile=False, filestatuschecker=None, tester=None, initialize=False, cellpy_units=None, output_units=None, debug=False)


   Main class for working and storing data.

   This class is the main work-horse for cellpy where methods for
   reading, selecting, and tweaking your data is located. It also contains the
   header definitions, both for the cellpy hdf5 format, and for the various
   cell-tester file-formats that can be read.

   .. attribute:: data

      cellpy.Data object

   .. attribute:: cellpy_units

      cellpy.units object

   .. attribute:: cellpy_datadir

      path to cellpy data directory

   .. attribute:: raw_datadir

      path to raw data directory

   .. attribute:: filestatuschecker

      filestatuschecker object

   .. attribute:: force_step_table_creation

      force step table creation

   .. attribute:: ensure_step_table

      ensure step table

   .. attribute:: limit_loaded_cycles

      limit loaded cycles

   .. attribute:: profile

      profile

   .. attribute:: select_minimal

      select minimal

   .. attribute:: empty

      empty

   .. attribute:: forced_errors

      forced errors

   .. attribute:: capacity_modifiers

      capacity modifiers

   .. attribute:: sep

      separator

   .. attribute:: cycle_mode

      cycle mode

   .. attribute:: tester

      tester

   .. attribute:: cell_name

      cell name

   :param filenames: list of files to load.
   :param selected_scans:
   :param profile: experimental feature.
   :param filestatuschecker: property to compare cellpy and raw-files;
                             default read from prms-file.
   :param tester: instrument used (e.g. "arbin_res") (checks prms-file as
                  default).
   :param initialize: create a dummy (empty) dataset; defaults to False.
   :param cellpy_units: sent to cellpy.parameters.internal_settings.get_cellpy_units
   :type cellpy_units: dict
   :param output_units: sent to cellpy.parameters.internal_settings.get_default_output_units
   :type output_units: dict
   :param debug: set to True if you want to see debug messages.
   :type debug: bool

   .. py:property:: active_electrode_area

      Returns the area

   .. py:property:: active_mass

      Returns the active mass (same as mass)

   .. py:property:: cell_name

      Returns the session name

   .. py:property:: cycle_mode


   .. py:property:: data

      Returns the DataSet instance

   .. py:property:: empty

      Gives True if the CellpyCell object is empty (or non-functional)

   .. py:property:: mass

      Returns the mass

   .. py:property:: nom_cap

      Returns the nominal capacity

   .. py:property:: nom_cap_specifics

      Returns the nominal capacity specific

   .. py:property:: nominal_capacity

      Returns the nominal capacity

   .. py:property:: raw_units

      Returns the raw_units dictionary

   .. py:property:: tot_mass

      Returns the total mass

   .. py:method:: check_file_ids(rawfiles, cellpyfile, detailed=False)

      Check the stats for the files (raw-data and cellpy hdf5).

      This method checks if the hdf5 file and the res-files have the same
      timestamps etc. to find out if we need to bother to load .res -files.

      if detailed is set to True, the method returns dict
      containing True or False for each individual raw-file. If not, it returns
      False if the raw files are newer than the cellpy hdf5-file (i.e. update is needed), else True.

      :param cellpyfile: filename of the cellpy hdf5-file.
      :type cellpyfile: str
      :param rawfiles: name(s) of raw-data file(s).
      :type rawfiles: list of str
      :param detailed: return a dict containing True or False for each individual raw-file.
      :type detailed: bool

      :returns: Bool or dict


   .. py:method:: drop_edges(start, end)

      Select middle part of experiment (CellpyCell object) from cycle
      number 'start' to 'end'


   .. py:method:: drop_from(cycle=None)

      Select first part of experiment (CellpyCell object) up to cycle number
      'cycle'


   .. py:method:: drop_to(cycle=None)

      Select last part of experiment (CellpyCell object) from cycle number
      'cycle'


   .. py:method:: from_raw(file_names=None, pre_processor_hook=None, post_processor_hook=None, is_a_file=True, refuse_copying=False, **kwargs)

      Load a raw data-file.

      :param file_names: uses CellpyCell.file_names if
                         None. If the list contains more than one file name, then the
                         runs will be merged together. Remark! the order of the files in
                         the list is important.
      :type file_names: list of raw-file names
      :param pre_processor_hook: function that will be applied to the data within the loader.
      :type pre_processor_hook: callable
      :param post_processor_hook: function that will be applied to the
                                  cellpy.Dataset object after initial loading.
      :type post_processor_hook: callable
      :param is_a_file: set this to False if it is a not a file-like object.
      :type is_a_file: bool
      :param refuse_copying: if set to True, the raw-file will not be copied before loading.
      :type refuse_copying: bool

      :Transferred Parameters: * **recalc** (*bool*) -- used by merging. Set to false if you don't want cellpy to automatically shift cycle number
                                 and time (e.g. add last cycle number from previous file to the cycle numbers
                                 in the next file).
                               * **bad_steps** (*list of tuples*) -- used by ``ArbinLoader``. (c, s) tuples of steps s (in cycle c)
                                 to skip loading.
                               * **data_points** (*tuple of ints*) -- used by ``ArbinLoader``. Load only data from data_point[0] to
                                 data_point[1] (use None for infinite). NOT IMPLEMENTED YET.


   .. py:method:: get_cap(cycle=None, cycles=None, method='back-and-forth', insert_nan=None, shift=0.0, categorical_column=False, label_cycle_number=False, split=False, interpolated=False, dx=0.1, number_of_points=None, ignore_errors=True, dynamic=False, inter_cycle_shift=True, interpolate_along_cap=False, capacity_then_voltage=False, mode='gravimetric', mass=None, area=None, volume=None, cycle_mode=None, **kwargs)

      Gets the capacity for the run.

      :param cycle: cycle number (s).
      :type cycle: int, list
      :param cycles: list of cycle numbers.
      :type cycles: list
      :param method: how the curves are given
                     "back-and-forth" - standard back and forth; discharge
                     (or charge) reversed from where charge (or discharge) ends.
                     "forth" - discharge (or charge) continues along x-axis.
                     "forth-and-forth" - discharge (or charge) also starts at 0
                     (or shift if not shift=0.0)
      :type method: string
      :param insert_nan: insert a np.nan between the charge and discharge curves.
                         Defaults to True for "forth-and-forth", else False
      :type insert_nan: bool
      :param shift: start-value for charge (or discharge) (typically used when
                    plotting shifted-capacity).
      :param categorical_column: add a categorical column showing if it is
                                 charge or discharge.
      :param label_cycle_number: add column for cycle number
                                 (tidy format).
      :type label_cycle_number: bool
      :param split: return a list of c and v instead of the default
                    that is to return them combined in a DataFrame. This is only
                    possible for some specific combinations of options (neither
                    categorical_column=True or label_cycle_number=True are
                    allowed).
      :type split: bool
      :param interpolated: set to True if you would like to get
                           interpolated data (typically if you want to save disk space
                           or memory). Defaults to False.
      :type interpolated: bool
      :param dx: the step used when interpolating.
      :type dx: float
      :param number_of_points: number of points to use (over-rides dx)
                               for interpolation (i.e. the length of the interpolated data).
      :type number_of_points: int
      :param ignore_errors: don't break out of loop if an error occurs.
      :type ignore_errors: bool
      :param dynamic: for dynamic retrieving data from cellpy-file.
                      [NOT IMPLEMENTED YET]
      :param inter_cycle_shift: cumulative shifts between consecutive
                                cycles. Defaults to True.
      :type inter_cycle_shift: bool
      :param interpolate_along_cap: interpolate along capacity axis instead
                                    of along the voltage axis. Defaults to False.
      :type interpolate_along_cap: bool
      :param capacity_then_voltage: return capacity and voltage instead of
                                    voltage and capacity. Defaults to False.
      :type capacity_then_voltage: bool
      :param mode: 'gravimetric', 'areal', 'volumetric' or 'absolute'. Defaults
                   to 'gravimetric'.
      :type mode: string
      :param mass: mass of active material (in set cellpy unit, typically mg).
      :type mass: float
      :param area: area of electrode (in set cellpy units, typically cm2).
      :type area: float
      :param volume: volume of electrode (in set cellpy units, typically cm3).
      :type volume: float
      :param cycle_mode: if 'anode' the first step is assumed to be the discharge,
                         else charge (defaults to ``CellpyCell.cycle_mode``).
      :type cycle_mode: string
      :param \*\*kwargs: sent to ``get_ccap`` and ``get_dcap``.

      :returns: ``pandas.DataFrame`` ((cycle) voltage, capacity, (direction (-1, 1)))
                unless split is explicitly set to True. Then it returns a tuple
                with capacity and voltage.


   .. py:method:: get_ccap(cycle=None, converter=None, mode='gravimetric', as_frame=True, **kwargs)

      Returns charge capacity and voltage for the selected cycle.

      :param cycle: cycle number.
      :type cycle: int
      :param converter: a multiplication factor that converts the values to
                        specific values (i.e. from Ah to mAh/g). If not provided (or None),
                        the factor is obtained from the self.get_converter_to_specific() method.
      :type converter: float
      :param mode: 'gravimetric', 'areal' or 'absolute'. Defaults to 'gravimetric'. Used
                   if converter is not provided (or None).
      :type mode: string
      :param as_frame: if True: returns pd.DataFrame instead of capacity, voltage series.
      :type as_frame: bool
      :param \*\*kwargs: additional keyword arguments sent to the internal _get_cap method.
      :type \*\*kwargs: dict

      :returns: ``pandas.DataFrame`` or list of ``pandas.Series`` if cycle=None and as_frame=False.


   .. py:method:: get_converter_to_specific(dataset: cellpy.readers.core.Data = None, value: float = None, from_units: cellpy.parameters.internal_settings.CellpyUnits = None, to_units: cellpy.parameters.internal_settings.CellpyUnits = None, mode: str = 'gravimetric') -> float

      Convert from absolute units to specific (areal or gravimetric).

      The method provides a conversion factor that you can multiply your
      values with to get them into specific values.

      :param dataset: data instance
      :param value: value used to scale on.
      :param from_units: defaults to data.raw_units.
      :param to_units: defaults to cellpy_units.
      :param mode: gravimetric, areal or absolute
      :type mode: str

      :returns: conversion factor (float)


   .. py:method:: get_current(cycle=None, with_index=True, with_time=False, as_frame=True)

      Returns current (in raw units).

      :param cycle: cycle number (all cycles if None).
      :param with_index: if True, includes the cycle index as a column in the returned pandas.DataFrame.
      :param with_time: if True, includes the time as a column in the returned pandas.DataFrame.
      :param as_frame: if not True, returns a list of current values as numpy arrays (one for each cycle).
                       Remark that with_time and with_index will be False if as_frame is set to False.

      :returns: ``pandas.DataFrame`` (or list of ``pandas.Series`` if cycle=None and as_frame=False)


   .. py:method:: get_cycle_numbers(steptable=None, rate=None, rate_on=None, rate_std=None, rate_agg='first', inverse=False)

      Get a array containing the cycle numbers in the test.

      :param steptable: the step-table to use (if None, the step-table
                        from the cellpydata object will be used).
      :type steptable: pandas.DataFrame
      :param rate: the rate to filter on. Remark that it should be given
                   as a float, i.e. you will have to convert from C-rate to
                   the actual numeric value. For example, use rate=0.05 if you want
                   to filter on cycles that has a C/20 rate.
      :type rate: float
      :param rate_on: only select cycles if based on the rate of this step-type (e.g. on="discharge").
      :type rate_on: str
      :param rate_std: allow for this inaccuracy in C-rate when selecting cycles
      :type rate_std: float
      :param rate_agg: perform an aggregation on rate if more than one step of charge or discharge is found
                       (e.g. "mean", "first", "max"). For example, if agg='mean', the average rate for each cycle
                       will be returned. Set to None if you want to keep all the rates.
      :type rate_agg: str
      :param inverse: select steps that does not have the given C-rate.
      :type inverse: bool

      :returns: numpy.ndarray of cycle numbers.


   .. py:method:: get_datetime(cycle=None, with_index=True, with_time=False, as_frame=True)

      Returns datetime (in raw units).

      :param cycle: cycle number (all cycles if None).
      :param with_index: if True, includes the cycle index as a column in the returned pandas.DataFrame.
      :param with_time: if True, includes the time as a column in the returned pandas.DataFrame.
      :param as_frame: if not True, returns a list of current values as numpy arrays (one for each cycle).
                       Remark that with_time and with_index will be False if as_frame is set to False.

      :returns: ``pandas.DataFrame`` (or list of ``pandas.Series`` if cycle=None and as_frame=False)


   .. py:method:: get_dcap(cycle=None, converter=None, mode='gravimetric', as_frame=True, **kwargs)

      Returns discharge-capacity and voltage for the selected cycle.

      :param cycle: cycle number.
                    converter (float): a multiplication factor that converts the values to
                        specific values (i.e. from Ah to mAh/g). If not provided (or None),
                        the factor is obtained from the self.get_converter_to_specific() method.
                    mode (string): 'gravimetric', 'areal' or 'absolute'. Defaults to 'gravimetric'. Used
                        if converter is not provided (or None).
                    as_frame (bool): if True: returns pd.DataFrame instead of capacity, voltage series.
                    **kwargs (dict): additional keyword arguments sent to the internal _get_cap method.
      :type cycle: int

      :returns: ``pandas.DataFrame`` or list of ``pandas.Series`` if cycle=None and as_frame=False.


   .. py:method:: get_ir()

      Get the IR data (Deprecated).


   .. py:method:: get_mass()

      Returns the mass of the active material (in mg).

      This method will be deprecated in the future.


   .. py:method:: get_number_of_cycles(steptable=None)

      Get the number of cycles in the test.


   .. py:method:: get_ocv(cycles=None, direction='up', remove_first=False, interpolated=False, dx=None, number_of_points=None) -> pandas.DataFrame

      Get the open circuit voltage relaxation curves.

      :param cycles: the cycles to extract from
                     (selects all if not given).
      :type cycles: list of ints or None
      :param direction: extract only relaxations that
                        is performed during discharge for "up" (because then the
                        voltage relaxes upwards) etc.
      :type direction: "up", "down", or "both"
      :param remove_first: remove the first relaxation curve (typically,
                           the first curve is from the initial rest period between
                           assembling the data to the actual testing/cycling starts)
      :param interpolated: set to True if you want the data to be
                           interpolated (e.g. for creating smaller files)
      :type interpolated: bool
      :param dx: the step used when interpolating.
      :type dx: float
      :param number_of_points: number of points to use (over-rides dx)
                               for interpolation (i.e. the length of the interpolated data).
      :type number_of_points: int

      :returns: ``pandas.DataFrame`` with cycle-number, step-number, step-time, and voltage columns.


   .. py:method:: get_rates(steptable=None, agg='first', direction=None)

      Get the rates in the test (only valid for constant current).

      :param steptable: provide custom steptable (if None, the steptable from the cellpydata object will be used).
      :param agg: perform an aggregation if more than one step of charge or
                  discharge is found (e.g. "mean", "first", "max"). For example, if agg='mean', the average rate
                  for each cycle will be returned. Set to None if you want to keep all the rates.
      :type agg: str
      :param direction: only select rates for this direction (e.g. "charge" or "discharge").
      :type direction: str or list of str

      :returns: ``pandas.DataFrame`` with cycle, type, and rate_avr (i.e. C-rate) columns.


   .. py:method:: get_raw(header, cycle: Optional[Union[Iterable, int]] = None, with_index: bool = True, with_step: bool = False, with_time: bool = False, additional_headers: Optional[list] = None, as_frame: bool = True, scaler: Optional[float] = None) -> Union[pandas.DataFrame, List[numpy.array]]

      Returns the values for column with given header (in raw units).

      :param header: header name.
      :param cycle: cycle number (all cycles if None).
      :param with_index: if True, includes the cycle index as a column in the returned pandas.DataFrame.
      :param with_step: if True, includes the step index as a column in the returned pandas.DataFrame.
      :param with_time: if True, includes the time as a column in the returned pandas.DataFrame.
      :param additional_headers: additional headers to include in the returned pandas.DataFrame.
      :type additional_headers: list
      :param as_frame: if not True, returns a list of current values as numpy arrays (one for each cycle).
                       Remark that with_time and with_index will be False if as_frame is set to False.
      :param scaler: if not None, the returned values are scaled by this value.

      :returns: pandas.DataFrame (or list of numpy arrays if as_frame=False)


   .. py:method:: get_step_numbers(steptype='charge', allctypes=True, pdtype=False, cycle_number=None, trim_taper_steps=None, steps_to_skip=None, steptable=None)

      Get the step numbers of selected type.

      Returns the selected step_numbers for the selected type of step(s).
      Either in a dictionary containing a list of step numbers corresponding
      to the selected steptype for the cycle(s), or a ``pandas.DataFrame`` instead of
      a dict of lists if pdtype is set to True. The frame is a sub-set of the
      step-table frame (i.e. all the same columns, only filtered by rows).

      :param steptype: string identifying type of step.
      :type steptype: string
      :param allctypes: get all types of charge (or discharge).
      :type allctypes: bool
      :param pdtype: return results as pandas.DataFrame
      :type pdtype: bool
      :param cycle_number: selected cycle, selects all if not set.
      :type cycle_number: int
      :param trim_taper_steps: number of taper steps to skip (counted
                               from the end, i.e. 1 means skip last step in each cycle).
      :type trim_taper_steps: integer
      :param steps_to_skip: step numbers that should not be included.
      :type steps_to_skip: list
      :param steptable: optional steptable
      :type steptable: pandas.DataFrame

      :returns: dict or ``pandas.DataFrame``

      .. rubric:: Example

      >>> my_charge_steps = CellpyCell.get_step_numbers(
      >>>    "charge",
      >>>    cycle_number = 3
      >>> )
      >>> print my_charge_steps
      {3: [5,8]}


   .. py:method:: get_summary(use_summary_made=False)

      Retrieve summary returned as a pandas DataFrame.

      .. warning:: This function is deprecated. Use the CellpyCell.data.summary property instead.


   .. py:method:: get_timestamp(cycle=None, with_index=True, as_frame=True, in_minutes=False, units='raw')

      Returns timestamp.

      :param cycle: cycle number (all cycles if None).
      :param with_index: if True, includes the cycle index as a column in the returned pandas.DataFrame.
      :param as_frame: if not True, returns a list of current values as numpy arrays (one for each cycle).
                       Remark that with_time and with_index will be False if as_frame is set to False.
      :param in_minutes: (deprecated, use units="minutes" instead) return values in minutes
                         instead of seconds if True.
      :param units: return values in given time unit ("raw", "seconds", "minutes", "hours").

      :returns: ``pandas.DataFrame`` (or list of ``pandas.Series`` if cycle=None and as_frame=False)


   .. py:method:: get_voltage(cycle=None, with_index=True, with_time=False, as_frame=True)

      Returns voltage (in raw units).

      :param cycle: cycle number (all cycles if None).
      :param with_index: if True, includes the cycle index as a column in the returned pandas.DataFrame.
      :param with_time: if True, includes the time as a column in the returned pandas.DataFrame.
      :param as_frame: if not True, returns a list of current values as numpy arrays (one for each cycle).
                       Remark that with_time and with_index will be False if as_frame is set to False.

      :returns: pandas.DataFrame (or list of pandas.Series if cycle=None and as_frame=False)


   .. py:method:: has_data_point_as_column()

      Check if the raw data has data_point as column.


   .. py:method:: has_data_point_as_index()

      Check if the raw data has data_point as index.


   .. py:method:: has_no_full_duplicates()

      Check if the raw data has no full duplicates.


   .. py:method:: has_no_partial_duplicates(subset='data_point')

      Check if the raw data has no partial duplicates.


   .. py:method:: initialize()

      Initialize the CellpyCell object with empty Data instance.


   .. py:method:: inspect_nominal_capacity(cycles=None)

      Method for estimating the nominal capacity

      :param cycles: the cycles where it is assumed that the data reaches nominal capacity.
      :type cycles: list of ints

      :returns: Nominal capacity (float).


   .. py:method:: load(cellpy_file, parent_level=None, return_cls=True, accept_old=True, selector=None, **kwargs)

      Loads a cellpy file.

      :param cellpy_file: Full path to the cellpy file.
      :type cellpy_file: OtherPath, str
      :param parent_level: Parent level. Warning! Deprecating this soon!
      :type parent_level: str, optional
      :param return_cls: Return the class.
      :type return_cls: bool
      :param accept_old: Accept loading old cellpy-file versions.
                         Instead of raising WrongFileVersion it only issues a warning.
      :type accept_old: bool
      :param selector (): under development

      :returns: cellpy.CellPyCellpy class if return_cls is True


   .. py:method:: load_step_specifications(file_name, short=False)

      Load a table that contains step-type definitions.

      This method loads a file containing a specification for each step or
      for each (cycle_number, step_number) combinations if `short==False`, and
      runs the `make_step_table` method. The step_cycle specifications that
      are allowed are stored in the variable `cellreader.list_of_step_types`.

      :param file_name: name of the file to load
      :type file_name: str
      :param short: if True, the file only contains step numbers and
                    step types. If False, the file contains cycle numbers as well.
      :type short: bool

      :returns: None


   .. py:method:: loadcell(raw_files, cellpy_file=None, mass=None, summary_on_raw=True, summary_on_cellpy_file=True, find_ir=True, find_end_voltage=True, force_raw=False, use_cellpy_stat_file=None, cell_type=None, loading=None, area=None, estimate_area=True, selector=None, **kwargs)

      Loads data for given cells (soon to be deprecated).

      :param raw_files: name of res-files
      :type raw_files: list
      :param cellpy_file: name of cellpy-file
      :type cellpy_file: path
      :param mass: mass of electrode or active material
      :type mass: float
      :param summary_on_raw: calculate summary if loading from raw
      :type summary_on_raw: bool
      :param summary_on_cellpy_file: calculate summary if loading from cellpy-file.
      :type summary_on_cellpy_file: bool
      :param find_ir: summarize ir
      :type find_ir: bool
      :param find_end_voltage: summarize end voltage
      :type find_end_voltage: bool
      :param force_raw: only use raw-files
      :type force_raw: bool
      :param use_cellpy_stat_file: use stat file if creating summary
                                   from raw
      :type use_cellpy_stat_file: bool
      :param cell_type: set the data type (e.g. "anode"). If not, the default from
                        the config file is used.
      :type cell_type: str
      :param loading: loading in units [mass] / [area], used to calculate area if area not given
      :type loading: float
      :param area: area of active electrode
      :type area: float
      :param estimate_area: calculate area from loading if given (defaults to True).
      :type estimate_area: bool
      :param selector: passed to load.
      :type selector: dict
      :param \*\*kwargs: passed to from_raw

      .. rubric:: Example

      >>> srnos = my_dbreader.select_batch("testing_new_solvent")
      >>> cell_datas = []
      >>> for srno in srnos:
      >>> ... my_run_name = my_dbreader.get_cell_name(srno)
      >>> ... mass = my_dbreader.get_mass(srno)
      >>> ... rawfiles, cellpyfiles =             >>> ...     filefinder.search_for_files(my_run_name)
      >>> ... cell_data = cellreader.CellpyCell()
      >>> ... cell_data.loadcell(raw_files=rawfiles,
      >>> ...                    cellpy_file=cellpyfiles)
      >>> ... cell_data.set_mass(mass)
      >>> ... cell_data.make_summary() # etc. etc.
      >>> ... cell_datas.append(cell_data)
      >>>

      .. warning:: This method will soon be deprecated. Use ``cellpy.get`` instead.


   .. py:method:: make_step_table(step_specifications=None, short=False, override_step_types=None, override_raw_limits=None, profiling=False, all_steps=False, add_c_rate=True, skip_steps=None, sort_rows=True, from_data_point=None, nom_cap_specifics=None)

      Create a table (v.4) that contains summary information for each step.

      This function creates a table containing information about the
      different steps for each cycle and, based on that, decides what type of
      step it is (e.g. charge) for each cycle.

      The format of the steps is:

      - index: cycleno - stepno - sub-step-no - ustep
      - Time info: average, stdev, max, min, start, end, delta
      - Logging info: average, stdev, max, min, start, end, delta
      - Current info: average, stdev, max, min, start, end, delta
      - Voltage info: average,  stdev, max, min, start, end, delta
      - Type: (from pre-defined list) - SubType
      - Info: not used.

      :param step_specifications: step specifications
      :type step_specifications: pandas.DataFrame
      :param short: step specifications in short format
      :type short: bool
      :param override_step_types: override the provided step types, for example set all
                                  steps with step number 5 to "charge" by providing {5: "charge"}.
      :type override_step_types: dict
      :param override_raw_limits: override the instrument limits (resolution), for example set
                                  'current_hard' to 0.1 by providing {'current_hard': 0.1}.
      :type override_raw_limits: dict
      :param profiling: turn on profiling
      :type profiling: bool
      :param all_steps: investigate all steps including same steps within
                        one cycle (this is useful for e.g. GITT).
      :type all_steps: bool
      :param add_c_rate: include a C-rate estimate in the steps
      :type add_c_rate: bool
      :param skip_steps: list of step numbers that should not
                         be processed (future feature - not used yet).
      :type skip_steps: list of integers
      :param sort_rows: sort the rows after processing.
      :type sort_rows: bool
      :param from_data_point: first data point to use.
      :type from_data_point: int
      :param nom_cap_specifics: "gravimetric", "areal", or "absolute".
      :type nom_cap_specifics: str

      :returns: None


   .. py:method:: make_summary(find_ir=False, find_end_voltage=True, use_cellpy_stat_file=None, ensure_step_table=True, remove_duplicates=True, normalization_cycles=None, nom_cap=None, nom_cap_specifics=None, old=False, create_copy=False, exclude_types=None, exclude_steps=None, selector_type=None, selector=None, **kwargs)

      Convenience function that makes a summary of the cycling data.

      :param find_ir: if True, the internal resistance will be calculated.
      :type find_ir: bool
      :param find_end_voltage: if True, the end voltage will be calculated.
      :type find_end_voltage: bool
      :param use_cellpy_stat_file: if True, the summary will be made from
                                   the cellpy_stat file (soon to be deprecated).
      :type use_cellpy_stat_file: bool
      :param ensure_step_table: if True, the step-table will be made if it does not exist.
      :type ensure_step_table: bool
      :param remove_duplicates: if True, duplicates will be removed from the summary.
      :type remove_duplicates: bool
      :param normalization_cycles: cycles to use for normalization.
      :type normalization_cycles: int or list of int
      :param nom_cap: nominal capacity (if None, the nominal capacity from the data will be used).
      :type nom_cap: float or str
      :param nom_cap_specifics: gravimetric, areal, or volumetric.
      :type nom_cap_specifics: str
      :param old: if True, the old summary method will be used.
      :type old: bool
      :param create_copy: if True, a copy of the cellpy object will be returned.
      :type create_copy: bool
      :param exclude_types: exclude these types from the summary.
      :type exclude_types: list of str
      :param exclude_steps: exclude these steps from the summary.
      :type exclude_steps: list of int
      :param selector_type: select based on type (e.g. "non-cv", "non-rest", "non-ocv", "only-cv").
      :type selector_type: str
      :param selector: custom selector function.
      :type selector: callable
      :param \*\*kwargs: additional keyword arguments sent to internal method (check source for info).

      :returns: cellpy object with the summary added to it.
      :rtype: cellpy.CellpyData


   .. py:method:: merge(datasets: list, **kwargs)

      This function merges datasets into one set.


   .. py:method:: mod_raw_split_cycle(data_points: List) -> None

      Split cycle(s) into several cycles.

      :param data_points: list of the first data point(s) for additional cycle(s).


   .. py:method:: nominal_capacity_as_absolute(value=None, specific=None, nom_cap_specifics=None, convert_charge_units=False)

      Get the nominal capacity as absolute value.


   .. py:method:: populate_step_dict(step)

      Returns a dict with cycle numbers as keys
      and corresponding steps (list) as values.


   .. py:method:: print_steps()

      Print the step table.


   .. py:method:: register_instrument_readers()

      Register instrument readers.


   .. py:method:: save(filename, force=False, overwrite=None, extension='h5', ensure_step_table=None, ensure_summary_table=None)

      Save the data structure to cellpy-format.

      :param filename: (str or pathlib.Path) the name you want to give the file
      :param force: (bool) save a file even if the summary is not made yet
                    (not recommended)
      :param overwrite: (bool) save the new version of the file even if old one
                        exists.
      :param extension: (str) filename extension.
      :param ensure_step_table: (bool) make step-table if missing.
      :param ensure_summary_table: (bool) make summary-table if missing.

      :returns: None


   .. py:method:: select_steps(step_dict, append_df=False)

      Select steps (not documented yet).


   .. py:method:: set_cellpy_datadir(directory=None)

      Set the directory containing .hdf5-files.

      Used for setting directory for looking for hdf5-files.
      A valid directory name is required.

      :param directory: path to hdf5-directory
      :type directory: str

      .. rubric:: Example

      >>> d = CellpyCell()
      >>> directory = "MyData/HDF5"
      >>> d.set_raw_datadir(directory)


   .. py:method:: set_col_first(df, col_names)
      :staticmethod:

      Set selected columns first in a pandas.DataFrame.

      This function sets cols with names given in  col_names (a list) first in
      the DataFrame. The last col in col_name will come first (processed last)



   .. py:method:: set_instrument(instrument=None, model=None, instrument_file=None, **kwargs)

      Set the instrument (i.e. tell cellpy the file-type you use).

      Three different modes of setting instruments are currently supported. You can
      provide the already supported instrument names (see the documentation, e.g. "arbin_res").
      You can use the "custom" loader by providing the path to a yaml-file
      describing the file format. This can be done either by setting instrument to
      "instrument_name::instrument_definition_file_name", or by setting instrument to "custom" and
      provide the definition file name through the instrument_file keyword argument. A last option
      exists where you provide the yaml-file name directly to the instrument parameter. Cellpy
      will then look into your local instrument folder and search for the yaml-file. Some
      instrument types also supports a model key-word.

      :param instrument: (str) in ["arbin_res", "maccor_txt",...]. If
                         instrument ends with ".yml" a local instrument file will be used. For example,
                         if instrument is "my_instrument.yml", cellpy will look into the local
                         instruments folders for a file called "my_instrument.yml" and then
                         use LocalTxtLoader to load after registering the instrument. If the instrument
                         name contains a '::' separator, the part after the separator will be interpreted
                         as 'instrument_file'.
      :param model: (str) optionally specify if the instrument loader supports handling several models
                    (some instruments allow for exporting data in slightly different formats depending on
                    the choices made during the export or the model of the instrument, e.g. different number of
                    header lines, different encoding).
      :param instrument_file: (path) instrument definition file,
      :param kwargs: key-word arguments sent to the initializer of the
                     loader class
      :type kwargs: dict

      .. rubric:: Notes

      If you are using a local instrument loader, you will have to register it first to the loader factory.

      >>> c = CellpyCell()  # this will automatically register the already implemented loaders
      >>> c.instrument_factory.register_builder(instrument_id, (module_name, path_to_instrument_loader_file))

      It is highly recommended using the module_name as the instrument_id.


   .. py:method:: set_mass(mass, validated=None)

      .. warning:: This function is deprecated. Use the setter instead (mass = value).


   .. py:method:: set_nom_cap(nom_cap, validated=None)

      .. warning:: This function is deprecated. Use the setter instead (nom_cap = value).


   .. py:method:: set_raw_datadir(directory=None)

      Set the directory containing .res-files.

      Used for setting directory for looking for res-files.@
      A valid directory name is required.

      :param directory: path to res-directory
      :type directory: str

      .. rubric:: Example

      >>> d = CellpyCell()
      >>> directory = "MyData/cycler-data"
      >>> d.set_raw_datadir(directory)


   .. py:method:: set_tot_mass(mass, validated=None)

      .. warning:: This function is deprecated. Use the setter instead (tot_mass = value).


   .. py:method:: sget_current(cycle, step)

      Returns current for cycle, step.

      Convenience function; same as issuing::

          raw[(raw[cycle_index_header] == cycle) & (raw[step_index_header] == step)][current_header]

      :param cycle: cycle number
      :param step: step number

      :returns: pandas.Series or None if empty


   .. py:method:: sget_step_numbers(cycle, step)

      Returns step number for cycle, step.

      Convenience function; same as issuing::

          raw[(raw[cycle_index_header] == cycle) &
               (raw[step_index_header] == step)][step_index_header]

      :param cycle: cycle number
      :param step: step number (can be a list of several step numbers)

      :returns: ``pandas.Series``


   .. py:method:: sget_steptime(cycle, step)

      Returns step time for cycle, step.

      Convenience function; Convenience function; same as issuing::

          raw[(raw[cycle_index_header] == cycle) & (raw[step_index_header] == step)][step_time_header]

      :param cycle: cycle number
      :param step: step number

      :returns: ``pandas.Series`` or None if empty


   .. py:method:: sget_timestamp(cycle, step)

      Returns timestamp for cycle, step.

      Convenience function; same as issuing::

          raw[(raw[cycle_index_header] == cycle) &
               (raw[step_index_header] == step)][timestamp_header]

      :param cycle: cycle number
      :param step: step number (can be a list of several step numbers)

      :returns: ``pandas.Series``


   .. py:method:: sget_voltage(cycle, step)

      Returns voltage for cycle, step.

      Convenience function; same as issuing::

          raw[(raw[cycle_index_header] == cycle) &
               (raw[step_index_header] == step)][voltage_header]

      :param cycle: cycle number
      :param step: step number

      :returns: pandas.Series or None if empty


   .. py:method:: split(cycle=None)

      Split experiment (CellpyCell object) into two sub-experiments. if cycle
      is not give, it will split on the median cycle number


   .. py:method:: split_many(base_cycles=None)

      Split experiment (CellpyCell object) into several sub-experiments.

      :param base_cycles: cycle(s) to do the split on.
      :type base_cycles: int or list of ints

      :returns: List of CellpyCell objects


   .. py:method:: to_cellpy_unit(value, physical_property)

      Convert value to cellpy units.

      :param value: what you want to convert from
      :type value: numeric, pint.Quantity or str
      :param physical_property: What this value is a measure of
                                (must correspond to one of the keys in the CellpyUnits class).
      :type physical_property: str

      Returns (numeric):
          the value in cellpy units


   .. py:method:: to_csv(datadir=None, sep=None, cycles=False, raw=True, summary=True, shifted=False, method=None, shift=0.0, last_cycle=None)

      Saves the data as .csv file(s).

      :param datadir: folder where to save the data (uses current folder if not
                      given).
      :param sep: the separator to use in the csv file
                  (defaults to CellpyCell.sep).
      :param cycles: (bool) export voltage-capacity curves if True.
      :param raw: (bool) export raw-data if True.
      :param summary: (bool) export summary if True.
      :param shifted: export with cumulated shift.
      :type shifted: bool
      :param method:
                     how the curves are given::
                         
                         "back-and-forth" - standard back and forth; discharge (or charge)
                             reversed from where charge (or discharge) ends.
                         
                         "forth" - discharge (or charge) continues along x-axis.
                         
                         "forth-and-forth" - discharge (or charge) also starts at 0
                             (or shift if not shift=0.0)
      :type method: string
      :param shift: start-value for charge (or discharge)
      :param last_cycle: process only up to this cycle (if not None).

      :returns: Nothing


   .. py:method:: to_excel(filename=None, cycles=None, raw=False, steps=True, nice=True, get_cap_kwargs=None, to_excel_kwargs=None)

      Saves the data as .xlsx file(s).

      :param filename: name of the Excel file.
      :param cycles: (None, bool, or list of ints) export voltage-capacity curves if given.
      :param raw: (bool) export raw-data if True.
      :param steps: (bool) export steps if True.
      :param nice: (bool) use nice formatting if True.
      :param get_cap_kwargs: (dict) kwargs for CellpyCell.get_cap method.
      :param to_excel_kwargs: (dict) kwargs for pandas.DataFrame.to_excel method.


   .. py:method:: total_time_at_voltage_level(cycles=None, voltage_limit=0.5, sampling_unit='S', at='low')

      Experimental method for getting the total time spent at low / high voltage.

      :param cycles: cycle number (all cycles if None).
      :param voltage_limit: voltage limit (default 0.5 V). Can be a tuple (low, high) if at="between".
      :param sampling_unit: sampling unit (default "S")
                            H: hourly frequency
                            T, min: minutely frequency
                            S: secondly frequency
                            L, ms:  milliseconds
                            U, us: microseconds
                            N: nanoseconds
      :param at: "low", "high", or "between" (default "low")
      :type at: str


   .. py:method:: unit_scaler_from_raw(unit, physical_property)

      Get the conversion factor going from raw to given unit.

      :param unit: what you want to convert to
      :type unit: str
      :param physical_property: what this value is a measure of
                                (must correspond to one of the keys in the CellpyUnits class).
      :type physical_property: str

      Returns (numeric):
          conversion factor (scaler)


   .. py:method:: vacant(cell=None)
      :classmethod:

      Create a CellpyCell instance.

      :param cell: the attributes from the data will be
                   copied to the new Cellpydata instance.
      :type cell: CellpyCell instance

       Returns:
          CellpyCell instance.



   .. py:method:: with_cellpy_unit(parameter, as_str=False)

      Return quantity as `pint.Quantity` object.



.. py:function:: get(filename=None, instrument=None, instrument_file=None, cellpy_file=None, cycle_mode=None, mass: Union[str, numbers.Number] = None, nominal_capacity: Union[str, numbers.Number] = None, nom_cap_specifics=None, loading=None, area: Union[str, numbers.Number] = None, estimate_area=True, logging_mode=None, auto_pick_cellpy_format=True, auto_summary=True, units=None, step_kwargs=None, summary_kwargs=None, selector=None, testing=False, refuse_copying=False, initialize=False, debug=False, **kwargs)

   Create a CellpyCell object

   :param filename: path to file(s) to load
   :type filename: str, os.PathLike, OtherPath, or list of raw-file names
   :param instrument: instrument to use (defaults to the one in your cellpy config file)
   :type instrument: str
   :param instrument_file: yaml file for custom file type
   :type instrument_file: str or path
   :param cellpy_file: if both filename (a raw-file) and cellpy_file (a cellpy file)
                       is provided, cellpy will try to check if the raw-file is has been updated since the
                       creation of the cellpy-file and select this instead of the raw file if cellpy thinks
                       they are similar (use with care!).
   :type cellpy_file: str, os.PathLike, or OtherPath
   :param logging_mode: "INFO" or "DEBUG"
   :type logging_mode: str
   :param cycle_mode: the cycle mode (e.g. "anode" or "full_cell")
   :type cycle_mode: str
   :param mass: mass of active material (mg) (defaults to mass given in cellpy-file or 1.0)
   :type mass: float
   :param nominal_capacity: nominal capacity for the cell (e.g. used for finding C-rates)
   :type nominal_capacity: float
   :param nom_cap_specifics: either "gravimetric" (pr mass), or "areal" (per area).
                             ("volumetric" is not fully implemented yet - let us know if you need it).
   :type nom_cap_specifics: str
   :param loading: loading in units [mass] / [area]
   :type loading: float
   :param area: active electrode area (e.g. used for finding the areal capacity)
   :type area: float
   :param estimate_area: calculate area from loading if given (defaults to True)
   :type estimate_area: bool
   :param auto_pick_cellpy_format: decide if it is a cellpy-file based on suffix.
   :type auto_pick_cellpy_format: bool
   :param auto_summary: (re-) create summary.
   :type auto_summary: bool
   :param units: update cellpy units (used after the file is loaded, e.g. when creating summary).
   :type units: dict
   :param step_kwargs: sent to make_steps
   :type step_kwargs: dict
   :param summary_kwargs: sent to make_summary
   :type summary_kwargs: dict
   :param selector: passed to load (when loading cellpy-files).
   :type selector: dict
   :param testing: set to True if testing (will for example prevent making .log files)
   :type testing: bool
   :param refuse_copying: set to True if you do not want to copy the raw-file before loading.
   :type refuse_copying: bool
   :param initialize: set to True if you want to initialize the CellpyCell object (probably only
                      useful if you want to return a cellpy-file with no data in it)
   :type initialize: bool
   :param debug: set to True if you want to debug the loader.
   :type debug: bool
   :param \*\*kwargs: sent to the loader

   Keyword args ("arbin_res"):
       bad_steps (list of tuples): (c, s) tuples of steps s (in cycle c) to skip loading [arbin_res].
       dataset_number (int): the data set number ('Test-ID') to select if you are dealing
           with arbin files with more than one data-set. Defaults to selecting all data-sets and merging them.
       data_points (tuple of ints): load only data from data_point[0] to
               data_point[1] (use None for infinite).
       increment_cycle_index (bool): increment the cycle index if merging several datasets (default True).

   Keyword args ("maccor_txt", "neware_txt", "local_instrument", "custom"):
       sep (str): separator used in the file.
       skip_rows (int): number of rows to skip in the beginning of the file.
       header (int): row number of the header.
       encoding (str): encoding of the file.
       decimal (str): decimal separator.
       thousand (str): thousand separator.
       pre_processor_hook (callable): pre-processors to use.

   Keyword args ("pec_csv"):
       bad_steps (list): separator used in the file (not implemented yet).

   :returns: CellpyCell object (if successful, None if not)

   .. rubric:: Examples

   >>> # read an arbin .res file and create a cellpy object with
   >>> # populated summary and step-table:
   >>> c = cellpy.get("my_data.res", instrument="arbin_res", mass=1.14, area=2.12, loading=1.2, nom_cap=155.2)
   >>>
   >>> # load a cellpy-file:
   >>> c = cellpy.get("my_cellpy_file.clp")
   >>>
   >>> # load a txt-file exported from Maccor:
   >>> c = cellpy.get("my_data.txt", instrument="maccor_txt", model="one")
   >>>
   >>> # load a raw-file if it is newer than the corresponding cellpy-file,
   >>> # if not, load the cellpy-file:
   >>> c = cellpy.get("my_data.res", cellpy_file="my_data.clp")
   >>>
   >>> # load a file with a custom file-description:
   >>> c = cellpy.get("my_file.csv", instrument_file="my_instrument.yaml")
   >>>
   >>> # load three subsequent raw-files (of one cell) and merge them:
   >>> c = cellpy.get(["my_data_01.res", "my_data_02.res", "my_data_03.res"])
   >>>
   >>> # load a data set and get the summary charge and discharge capacities
   >>> # in Ah/g:
   >>> c = cellpy.get("my_data.res", units=dict(capacity="Ah"))
   >>>
   >>> # get an empty CellpyCell instance:
   >>> c = cellpy.get()  # or c = cellpy.get(initialize=True) if you want to initialize it.


.. py:data:: DIGITS_C_RATE
   :value: 5

   

.. py:data:: HEADERS_NORMAL

   

.. py:data:: HEADERS_STEP_TABLE

   

.. py:data:: HEADERS_SUMMARY

   

