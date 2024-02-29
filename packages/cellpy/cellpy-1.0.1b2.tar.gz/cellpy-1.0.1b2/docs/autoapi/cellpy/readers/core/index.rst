:py:mod:`cellpy.readers.core`
=============================

.. py:module:: cellpy.readers.core

.. autoapi-nested-parse::

   This module contains several of the most important classes used in cellpy.

   It also contains functions that are used by readers and utils.
   And it has the file version definitions.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.core.BaseDbReader
   cellpy.readers.core.Data
   cellpy.readers.core.FileID
   cellpy.readers.core.InstrumentFactory
   cellpy.readers.core.PickleProtocol



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.core.check64bit
   cellpy.readers.core.collect_capacity_curves
   cellpy.readers.core.convert_from_simple_unit_label_to_string_unit_label
   cellpy.readers.core.find_all_instruments
   cellpy.readers.core.generate_default_factory
   cellpy.readers.core.group_by_interpolate
   cellpy.readers.core.humanize_bytes
   cellpy.readers.core.identify_last_data_point
   cellpy.readers.core.interpolate_y_on_x
   cellpy.readers.core.pickle_protocol
   cellpy.readers.core.xldate_as_datetime



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.core.HEADERS_NORMAL
   cellpy.readers.core.HEADERS_STEP_TABLE
   cellpy.readers.core.HEADERS_SUMMARY
   cellpy.readers.core.Q
   cellpy.readers.core.ureg


.. py:class:: BaseDbReader


   Base class for database readers.

   .. py:method:: from_batch(batch_name: str, include_key: bool = False, include_individual_arguments: bool = False) -> dict
      :abstractmethod:


   .. py:method:: get_area(pk: int) -> float
      :abstractmethod:


   .. py:method:: get_args(pk: int) -> dict
      :abstractmethod:


   .. py:method:: get_by_column_label(pk: int, name: str) -> Any
      :abstractmethod:


   .. py:method:: get_cell_name(pk: int) -> str
      :abstractmethod:


   .. py:method:: get_cell_type(pk: int) -> str
      :abstractmethod:


   .. py:method:: get_comment(pk: int) -> str
      :abstractmethod:


   .. py:method:: get_experiment_type(pk: int) -> str
      :abstractmethod:


   .. py:method:: get_group(pk: int) -> str
      :abstractmethod:


   .. py:method:: get_instrument(pk: int) -> str
      :abstractmethod:


   .. py:method:: get_label(pk: int) -> str
      :abstractmethod:


   .. py:method:: get_loading(pk: int) -> float
      :abstractmethod:


   .. py:method:: get_mass(pk: int) -> float
      :abstractmethod:


   .. py:method:: get_nom_cap(pk: int) -> float
      :abstractmethod:


   .. py:method:: get_total_mass(pk: int) -> float
      :abstractmethod:


   .. py:method:: inspect_hd5f_fixed(pk: int) -> int
      :abstractmethod:


   .. py:method:: select_batch(batch: str) -> List[int]
      :abstractmethod:



.. py:class:: Data(**kwargs)


   Object to store data for a cell-test.

   This class is used for storing all the relevant data for a cell-test, i.e. all
   the data collected by the tester as stored in the raw-files, and user-provided
   metadata about the cell-test.

   .. attribute:: raw_data_files

      list of FileID objects.

      :type: list

   .. attribute:: raw

      raw data.

      :type: pandas.DataFrame

   .. attribute:: summary

      summary data.

      :type: pandas.DataFrame

   .. attribute:: steps

      step data.

      :type: pandas.DataFrame

   .. attribute:: meta_common

      common meta-data.

      :type: CellpyMetaCommon

   .. attribute:: meta_test_dependent

      test-dependent meta-data.

      :type: CellpyMetaIndividualTest

   .. attribute:: custom_info

      custom meta-data.

      :type: Any

   .. attribute:: raw_units

      dictionary with units for the raw data.

      :type: dict

   .. attribute:: raw_limits

      dictionary with limits for the raw data.

      :type: dict

   .. attribute:: loaded_from

      name of the file where the data was loaded from.

      :type: str

   .. py:property:: active_electrode_area


   .. py:property:: cell_name


   .. py:property:: empty

      Check if the data object is empty.

   .. py:property:: has_data


   .. py:property:: has_steps

      check if the step table exists

   .. py:property:: has_summary

      check if the summary table exists

   .. py:property:: mass


   .. py:property:: material


   .. py:property:: nom_cap


   .. py:property:: raw_id


   .. py:property:: start_datetime


   .. py:property:: tot_mass


   .. py:method:: populate_defaults()

      Populate the data object with default values.



.. py:class:: FileID(filename: Union[str, cellpy.internals.core.OtherPath] = None, is_db: bool = False)


   class for storing information about the raw-data files.

   This class is used for storing and handling raw-data file information.
   It is important to keep track of when the data was extracted from the
   raw-data files so that it is easy to know if the hdf5-files used for
   @storing "treated" data is up-to-date.

   .. attribute:: name

      Filename of the raw-data file.

      :type: str

   .. attribute:: full_name

      Filename including path of the raw-data file.

      :type: str

   .. attribute:: size

      Size of the raw-data file.

      :type: float

   .. attribute:: last_modified

      Last time of modification of the raw-data
      file.

      :type: datetime

   .. attribute:: last_accessed

      last time of access of the raw-data file.

      :type: datetime

   .. attribute:: last_info_changed

      st_ctime of the raw-data file.

      :type: datetime

   .. attribute:: location

      Location of the raw-data file.

      :type: str

   Initialize the FileID class.

   .. py:property:: last_data_point

      Get the last data point.

   .. py:method:: get_last()

      Get last modification time of the file.


   .. py:method:: get_name()

      Get the filename.


   .. py:method:: get_raw()

      Get a list with information about the file.

      The returned list contains name, size, last_modified and location.


   .. py:method:: get_size()

      Get the size of the file.


   .. py:method:: populate(filename: Union[str, cellpy.internals.core.OtherPath])

      Finds the file-stats and populates the class with stat values.

      :param filename: name of the file.
      :type filename: str, OtherPath



.. py:class:: InstrumentFactory


   Factory for instrument loaders.

   .. py:method:: create(key: Union[str, None], **kwargs)

      Create the instrument loader module and initialize the loader class.

      :param key: instrument id
      :param \*\*kwargs: sent to the initializer of the loader class.

      :returns: instance of loader class.


   .. py:method:: query(key: str, variable: str) -> Any

      performs a get_params lookup for the instrument loader.

      :param key: instrument id.
      :param variable: the variable you want to lookup.

      :returns: The value of the variable if the loaders get_params method supports it.


   .. py:method:: register_builder(key: str, builder: Tuple[str, Any], **kwargs) -> None

      register an instrument loader module.

      :param key: instrument id
      :param builder: (module_name, module_path)
      :param \*\*kwargs: stored in the factory (will be used in the future for allowing to set
                         defaults to the builders to allow for using .query).



.. py:class:: PickleProtocol(level)


   Context for using a specific pickle protocol.


.. py:function:: check64bit(current_system='python')

   checks if you are on a 64-bit platform


.. py:function:: collect_capacity_curves(cell, direction='charge', trim_taper_steps=None, steps_to_skip=None, steptable=None, max_cycle_number=None, **kwargs)

   Create a list of pandas.DataFrames, one for each charge step.

   The DataFrames are named by its cycle number.

   :param cell: object
   :type cell: ``CellpyCell``
   :param direction:
   :type direction: str
   :param trim_taper_steps: number of taper steps to skip (counted
                            from the end, i.e. 1 means skip last step in each cycle).
   :type trim_taper_steps: integer
   :param steps_to_skip: step numbers that should not be included.
   :type steps_to_skip: list
   :param steptable: optional steptable.
   :type steptable: ``pandas.DataFrame``
   :param max_cycle_number: only select cycles up to this value.
   :type max_cycle_number: int

   :returns: list of pandas.DataFrames,
             list of cycle numbers,
             minimum voltage value,
             maximum voltage value


.. py:function:: convert_from_simple_unit_label_to_string_unit_label(k, v)

   Convert from simple unit label to string unit label.


.. py:function:: find_all_instruments() -> Dict[str, Tuple[str, pathlib.Path]]

   finds all the supported instruments


.. py:function:: generate_default_factory()

   This function searches for all available instrument readers
   and registers them in an InstrumentFactory instance.

   :returns: InstrumentFactory


.. py:function:: group_by_interpolate(df, x=None, y=None, group_by=None, number_of_points=100, tidy=False, individual_x_cols=False, header_name='Unit', dx=10.0, generate_new_x=True)

   Do a pandas.DataFrame.group_by and perform interpolation for all groups.

   This function is a wrapper around an internal interpolation function in
   cellpy (that uses scipy.interpolate.interp1d) that combines doing a group-by
   operation and interpolation.

   :param df: the dataframe to morph.
   :type df: pandas.DataFrame
   :param x: the header for the x-value
             (defaults to normal header step_time_txt) (remark that the default
             group_by column is the cycle column, and each cycle normally
             consist of several steps (so you risk interpolating / merging
             several curves on top of each other (not good)).
   :type x: str
   :param y: the header for the y-value
             (defaults to normal header voltage_txt).
   :type y: str
   :param group_by: the header to group by
                    (defaults to normal header cycle_index_txt)
   :type group_by: str
   :param number_of_points: if generating new x-column, how many values it
                            should contain.
   :type number_of_points: int
   :param tidy: return the result in tidy (i.e. long) format.
   :type tidy: bool
   :param individual_x_cols: return as xy xy xy ... data.
   :type individual_x_cols: bool
   :param header_name: name for the second level of the columns (only
                       applies for xy xy xy ... data) (defaults to "Unit").
   :type header_name: str
   :param dx: if generating new x-column and number_of_points is None or
              zero, distance between the generated values.
   :type dx: float
   :param generate_new_x: create a new x-column by
                          using the x-min and x-max values from the original dataframe where
                          the method is set by the number_of_points key-word:

                          1)  if number_of_points is not None (default is 100):

                              ```
                              new_x = np.linspace(x_max, x_min, number_of_points)
                              ```
                          2)  else:
                              ```
                              new_x = np.arange(x_max, x_min, dx)
                              ```
   :type generate_new_x: bool

   Returns: pandas.DataFrame with interpolated x- and y-values. The returned
       dataframe is in tidy (long) format for tidy=True.



.. py:function:: humanize_bytes(b, precision=1)

   Return a humanized string representation of a number of b.


.. py:function:: identify_last_data_point(data)

   Find the last data point and store it in the fid instance


.. py:function:: interpolate_y_on_x(df, x=None, y=None, new_x=None, dx=10.0, number_of_points=None, direction=1, **kwargs)

   Interpolate a column based on another column.

   :param df: DataFrame with the (cycle) data.
   :param x: Column name for the x-value (defaults to the step-time column).
   :param y: Column name for the y-value (defaults to the voltage column).
   :param new_x: Interpolate using these new x-values
                 instead of generating x-values based on dx or number_of_points.
   :type new_x: numpy array or None
   :param dx: step-value (defaults to 10.0)
   :param number_of_points: number of points for interpolated values (use
                            instead of dx and overrides dx if given).
   :param direction: if direction is negative, then invert the
                     x-values before interpolating.
   :type direction: -1,1
   :param \*\*kwargs: arguments passed to ``scipy.interpolate.interp1d``

   Returns: DataFrame with interpolated y-values based on given or
       generated x-values.



.. py:function:: pickle_protocol(level)


.. py:function:: xldate_as_datetime(xldate, datemode=0, option='to_datetime')

   Converts a xls date stamp to a more sensible format.

   :param xldate: date stamp in Excel format.
   :type xldate: str, int
   :param datemode: 0 for 1900-based, 1 for 1904-based.
   :type datemode: int
   :param option: option in ("to_datetime", "to_float", "to_string"),
                  return value
   :type option: str

   :returns: datetime (datetime object, float, or string).


.. py:data:: HEADERS_NORMAL

   

.. py:data:: HEADERS_STEP_TABLE

   

.. py:data:: HEADERS_SUMMARY

   

.. py:data:: Q

   

.. py:data:: ureg

   

