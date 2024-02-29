:py:mod:`cellpy.parameters.internal_settings`
=============================================

.. py:module:: cellpy.parameters.internal_settings

.. autoapi-nested-parse::

   Internal settings and definitions and functions for getting them.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.parameters.internal_settings.BaseHeaders
   cellpy.parameters.internal_settings.BaseSettings
   cellpy.parameters.internal_settings.CellpyLimits
   cellpy.parameters.internal_settings.CellpyMeta
   cellpy.parameters.internal_settings.CellpyMetaCommon
   cellpy.parameters.internal_settings.CellpyMetaIndividualTest
   cellpy.parameters.internal_settings.CellpyUnits
   cellpy.parameters.internal_settings.DictLikeClass
   cellpy.parameters.internal_settings.HeaderDict
   cellpy.parameters.internal_settings.HeadersJournal
   cellpy.parameters.internal_settings.HeadersNormal
   cellpy.parameters.internal_settings.HeadersStepTable
   cellpy.parameters.internal_settings.HeadersSummary
   cellpy.parameters.internal_settings.InstrumentSettings



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.parameters.internal_settings.get_cellpy_units
   cellpy.parameters.internal_settings.get_default_cellpy_file_raw_units
   cellpy.parameters.internal_settings.get_default_custom_headers_summary
   cellpy.parameters.internal_settings.get_default_output_units
   cellpy.parameters.internal_settings.get_default_raw_limits
   cellpy.parameters.internal_settings.get_default_raw_units
   cellpy.parameters.internal_settings.get_headers_journal
   cellpy.parameters.internal_settings.get_headers_normal
   cellpy.parameters.internal_settings.get_headers_step_table
   cellpy.parameters.internal_settings.get_headers_summary



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.parameters.internal_settings.ATTRS_TO_IMPORT_FROM_EXCEL_SQLITE
   cellpy.parameters.internal_settings.BATCH_ATTRS_TO_IMPORT_FROM_EXCEL_SQLITE
   cellpy.parameters.internal_settings.CELLPY_FILE_VERSION
   cellpy.parameters.internal_settings.COLUMNS_EXCEL_PK
   cellpy.parameters.internal_settings.COLUMNS_RENAMER
   cellpy.parameters.internal_settings.MINIMUM_CELLPY_FILE_VERSION
   cellpy.parameters.internal_settings.OTHERPATHS
   cellpy.parameters.internal_settings.PICKLE_PROTOCOL
   cellpy.parameters.internal_settings.RAW_TABLE_VERSION
   cellpy.parameters.internal_settings.STEP_TABLE_VERSION
   cellpy.parameters.internal_settings.SUMMARY_TABLE_VERSION
   cellpy.parameters.internal_settings.TABLE_NAME_SQLITE
   cellpy.parameters.internal_settings.base_columns_float
   cellpy.parameters.internal_settings.base_columns_int
   cellpy.parameters.internal_settings.cellpy_units
   cellpy.parameters.internal_settings.headers_journal
   cellpy.parameters.internal_settings.headers_normal
   cellpy.parameters.internal_settings.headers_step_table
   cellpy.parameters.internal_settings.headers_summary
   cellpy.parameters.internal_settings.keys_journal_session


.. py:class:: BaseHeaders


   Bases: :py:obj:`BaseSettings`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.BaseHeaders
      :parts: 1

   Subclass of BaseSetting including option to add postfixes.

   .. rubric:: Example

   >>> header["key_postfix"]  # returns "value_postfix"

   .. py:attribute:: postfixes
      :value: []

      


.. py:class:: BaseSettings


   Bases: :py:obj:`DictLikeClass`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.BaseSettings
      :parts: 1

   Base class for internal cellpy settings.

   Usage::

        @dataclass
        class MyCoolCellpySetting(BaseSetting):
            var1: str = "first var"
            var2: int = 12


   .. py:method:: get(key)

      Get the value (postfixes not supported).


   .. py:method:: to_frame()

      Converts to pandas dataframe



.. py:class:: CellpyLimits


   Bases: :py:obj:`BaseSettings`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.CellpyLimits
      :parts: 1

   These are the limits used inside ``cellpy`` for finding step types.

   Since all instruments have an inherent inaccuracy, it is naive to assume that
   for example the voltage within a constant voltage step does not change at all.
   Therefore, we need to define some limits for what we consider to be a constant and
   what we assume to be zero.


   .. py:attribute:: current_hard
      :type: float
      :value: 1e-13

      

   .. py:attribute:: current_soft
      :type: float
      :value: 1e-05

      

   .. py:attribute:: ir_change
      :type: float
      :value: 1e-05

      

   .. py:attribute:: stable_charge_hard
      :type: float
      :value: 0.9

      

   .. py:attribute:: stable_charge_soft
      :type: float
      :value: 5.0

      

   .. py:attribute:: stable_current_hard
      :type: float
      :value: 2.0

      

   .. py:attribute:: stable_current_soft
      :type: float
      :value: 4.0

      

   .. py:attribute:: stable_voltage_hard
      :type: float
      :value: 2.0

      

   .. py:attribute:: stable_voltage_soft
      :type: float
      :value: 4.0

      


.. py:class:: CellpyMeta


   Base class for meta-data in cellpy.

   .. py:method:: digest(as_list: bool = False, **kwargs)

      Pops from dictionary of form {key: [values]}

      :param as_list: pick only first scalar if True.
      :type as_list: bool
      :param \*\*kwargs: key word attributes to pick.
      :type \*\*kwargs: dict

      :returns: Dictionary containing the non-digested part.


   .. py:method:: to_frame()

      Converts to pandas dataframe


   .. py:method:: update(as_list: bool = False, **kwargs)

      Updates from dictionary of form {key: [values]}

      :param as_list: pick only first scalar if True.
      :type as_list: bool
      :param \*\*kwargs: key word attributes to update.
      :type \*\*kwargs: dict

      :returns: None



.. py:class:: CellpyMetaCommon


   Bases: :py:obj:`CellpyMeta`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.CellpyMetaCommon
      :parts: 1

   Common (not test-dependent) meta-data for cellpy.

   .. py:attribute:: active_electrode_area
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: active_electrode_current_collector
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: active_electrode_thickness
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: active_electrode_type
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: cell_name
      :type: Optional[str]

      

   .. py:attribute:: cell_type
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: cellpy_file_version
      :type: int

      

   .. py:attribute:: comment
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: counter_electrode_type
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: electrolyte_type
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: electrolyte_volume
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: experiment_type
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: file_errors
      :type: Optional[str]

      

   .. py:attribute:: mass
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: material
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: nom_cap
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: nom_cap_specifics
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: raw_id
      :type: Optional[str]

      

   .. py:attribute:: reference_electrode_current_collector
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: reference_electrode_type
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: separator_type
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: start_datetime
      :type: Optional[str]

      

   .. py:attribute:: tester_ID
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: tester_calibration_date
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: tester_client_software_version
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: tester_server_software_version
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: time_zone
      :type: Optional[str]

      

   .. py:attribute:: tot_mass
      :type: Optional[cellpy.prms.CellPyDataConfig]

      


.. py:class:: CellpyMetaIndividualTest


   Bases: :py:obj:`CellpyMeta`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.CellpyMetaIndividualTest
      :parts: 1

   Test-dependent meta-data for cellpy.

   .. py:attribute:: channel_index
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: creator
      :type: Optional[str]

      

   .. py:attribute:: cycle_mode
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: schedule_file_name

      

   .. py:attribute:: test_ID
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: test_type
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: voltage_lim_high
      :type: Optional[cellpy.prms.CellPyDataConfig]

      

   .. py:attribute:: voltage_lim_low
      :type: Optional[cellpy.prms.CellPyDataConfig]

      


.. py:class:: CellpyUnits


   Bases: :py:obj:`BaseSettings`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.CellpyUnits
      :parts: 1

   These are the units used inside Cellpy.

   At least two sets of units needs to be defined; `cellpy_units` and `raw_units`.
   The `data.raw` dataframe is given in `raw_units` where the units are defined
   inside the instrument loader used. Since the `data.steps` dataframe is a summary of
   the step statistics from the `data.raw` dataframe, this also uses the `raw_units`.
   The `data.summary` dataframe contains columns with values directly from the `data.raw` dataframe
   given in `raw_units` as well as calculated columns given in `cellpy_units`.

   Remark that all input to cellpy through user interaction (or utils) should be in `cellpy_units`.
   This is also true for meta-data collected from the raw files. The instrument loader needs to
   take care of the translation from its raw units to `cellpy_units` during loading the raw data
   file for the meta-data (remark that this is not necessary and not recommended for the actual
   "raw" data that is going to be stored in the `data.raw` dataframe).

   As of 2022.09.29, cellpy does not automatically ensure unit conversion for input of meta-data,
   but has an internal method (`CellPyData.to_cellpy_units`) that can be used.

   These are the different attributes currently supported for data in the dataframes::

       current: str = "A"
       charge: str = "mAh"
       voltage: str = "V"
       time: str = "sec"
       resistance: str = "Ohms"
       power: str = "W"
       energy: str = "Wh"
       frequency: str = "hz"

   And here are the different attributes currently supported for meta-data::

       # output-units for specific capacity etc.
       specific_gravimetric: str = "g"
       specific_areal: str = "cm**2"  # used for calculating specific capacity etc.
       specific_volumetric: str = "cm**3"  # used for calculating specific capacity etc.

       # other meta-data
       nominal_capacity: str = "mAh/g"  # used for calculating rates etc.
       mass: str = "mg"
       length: str = "cm"
       area: str = "cm**2"
       volume: str = "cm**3"
       temperature: str = "C"


   .. py:attribute:: area
      :type: str
      :value: 'cm**2'

      

   .. py:attribute:: charge
      :type: str
      :value: 'mAh'

      

   .. py:attribute:: current
      :type: str
      :value: 'A'

      

   .. py:attribute:: energy
      :type: str
      :value: 'Wh'

      

   .. py:attribute:: frequency
      :type: str
      :value: 'hz'

      

   .. py:attribute:: length
      :type: str
      :value: 'cm'

      

   .. py:attribute:: mass
      :type: str
      :value: 'mg'

      

   .. py:attribute:: nominal_capacity
      :type: str
      :value: 'mAh/g'

      

   .. py:attribute:: power
      :type: str
      :value: 'W'

      

   .. py:attribute:: pressure
      :type: str
      :value: 'bar'

      

   .. py:attribute:: resistance
      :type: str
      :value: 'ohm'

      

   .. py:attribute:: specific_areal
      :type: str
      :value: 'cm**2'

      

   .. py:attribute:: specific_gravimetric
      :type: str
      :value: 'g'

      

   .. py:attribute:: specific_volumetric
      :type: str
      :value: 'cm**3'

      

   .. py:attribute:: temperature
      :type: str
      :value: 'C'

      

   .. py:attribute:: time
      :type: str
      :value: 'sec'

      

   .. py:attribute:: voltage
      :type: str
      :value: 'V'

      

   .. py:attribute:: volume
      :type: str
      :value: 'cm**3'

      

   .. py:method:: update(new_units: dict)

      Update the units.



.. py:class:: DictLikeClass


   Add some dunder-methods so that it does not break old code that used
   dictionaries for storing settings

   Remarks: it is not a complete dictionary experience - for example,
   setting new attributes (new keys) is not supported (raises ``KeyError``
   if using the typical dict setting method) since it uses the
   ``dataclasses.fields`` method to find its members.


   .. py:method:: items()


   .. py:method:: keys()


   .. py:method:: values()



.. py:class:: HeaderDict(dict=None, /, **kwargs)


   Bases: :py:obj:`collections.UserDict`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.HeaderDict
      :parts: 1

   A Sub-class of dict to allow for tab-completion.


.. py:class:: HeadersJournal


   Bases: :py:obj:`BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.HeadersJournal
      :parts: 1

   Headers used for the journal (batch) (used as column headers for the journal pandas DataFrames)

   .. py:attribute:: area
      :type: str
      :value: 'area'

      

   .. py:attribute:: argument
      :type: str
      :value: 'argument'

      

   .. py:attribute:: cell_type
      :type: str
      :value: 'cell_type'

      

   .. py:attribute:: cellpy_file_name
      :type: str
      :value: 'cellpy_file_name'

      

   .. py:attribute:: comment
      :type: str
      :value: 'comment'

      

   .. py:attribute:: experiment
      :type: str
      :value: 'experiment'

      

   .. py:attribute:: filename
      :type: str
      :value: 'filename'

      

   .. py:attribute:: fixed
      :type: str
      :value: 'fixed'

      

   .. py:attribute:: group
      :type: str
      :value: 'group'

      

   .. py:attribute:: instrument
      :type: str
      :value: 'instrument'

      

   .. py:attribute:: label
      :type: str
      :value: 'label'

      

   .. py:attribute:: loading
      :type: str
      :value: 'loading'

      

   .. py:attribute:: mass
      :type: str
      :value: 'mass'

      

   .. py:attribute:: nom_cap
      :type: str
      :value: 'nom_cap'

      

   .. py:attribute:: raw_file_names
      :type: str
      :value: 'raw_file_names'

      

   .. py:attribute:: sub_group
      :type: str
      :value: 'sub_group'

      

   .. py:attribute:: total_mass
      :type: str
      :value: 'total_mass'

      


.. py:class:: HeadersNormal


   Bases: :py:obj:`BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.HeadersNormal
      :parts: 1

   Headers used for the normal (raw) data (used as column headers for the main data pandas DataFrames)

   .. py:attribute:: ac_impedance_txt
      :type: str
      :value: 'ac_impedance'

      

   .. py:attribute:: aci_phase_angle_txt
      :type: str
      :value: 'aci_phase_angle'

      

   .. py:attribute:: amplitude_txt
      :type: str
      :value: 'amplitude'

      

   .. py:attribute:: channel_id_txt
      :type: str
      :value: 'channel_id'

      

   .. py:attribute:: charge_capacity_txt
      :type: str
      :value: 'charge_capacity'

      

   .. py:attribute:: charge_energy_txt
      :type: str
      :value: 'charge_energy'

      

   .. py:attribute:: current_txt
      :type: str
      :value: 'current'

      

   .. py:attribute:: cycle_index_txt
      :type: str
      :value: 'cycle_index'

      

   .. py:attribute:: data_flag_txt
      :type: str
      :value: 'data_flag'

      

   .. py:attribute:: data_point_txt
      :type: str
      :value: 'data_point'

      

   .. py:attribute:: datetime_txt
      :type: str
      :value: 'date_time'

      

   .. py:attribute:: discharge_capacity_txt
      :type: str
      :value: 'discharge_capacity'

      

   .. py:attribute:: discharge_energy_txt
      :type: str
      :value: 'discharge_energy'

      

   .. py:attribute:: dv_dt_txt
      :type: str
      :value: 'dv_dt'

      

   .. py:attribute:: frequency_txt
      :type: str
      :value: 'frequency'

      

   .. py:attribute:: internal_resistance_txt
      :type: str
      :value: 'internal_resistance'

      

   .. py:attribute:: is_fc_data_txt
      :type: str
      :value: 'is_fc_data'

      

   .. py:attribute:: power_txt
      :type: str
      :value: 'power'

      

   .. py:attribute:: ref_ac_impedance_txt
      :type: str
      :value: 'ref_ac_impedance'

      

   .. py:attribute:: ref_aci_phase_angle_txt
      :type: str
      :value: 'ref_aci_phase_angle'

      

   .. py:attribute:: ref_voltage_txt
      :type: str
      :value: 'reference_voltage'

      

   .. py:attribute:: step_index_txt
      :type: str
      :value: 'step_index'

      

   .. py:attribute:: step_time_txt
      :type: str
      :value: 'step_time'

      

   .. py:attribute:: sub_step_index_txt
      :type: str
      :value: 'sub_step_index'

      

   .. py:attribute:: sub_step_time_txt
      :type: str
      :value: 'sub_step_time'

      

   .. py:attribute:: test_id_txt
      :type: str
      :value: 'test_id'

      

   .. py:attribute:: test_name_txt
      :type: str
      :value: 'test_name'

      

   .. py:attribute:: test_time_txt
      :type: str
      :value: 'test_time'

      

   .. py:attribute:: voltage_txt
      :type: str
      :value: 'voltage'

      


.. py:class:: HeadersStepTable


   Bases: :py:obj:`BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.HeadersStepTable
      :parts: 1

   Headers used for the steps table (used as column headers for the steps pandas DataFrames)

   .. py:attribute:: charge
      :type: str
      :value: 'charge'

      

   .. py:attribute:: current
      :type: str
      :value: 'current'

      

   .. py:attribute:: cycle
      :type: str
      :value: 'cycle'

      

   .. py:attribute:: discharge
      :type: str
      :value: 'discharge'

      

   .. py:attribute:: info
      :type: str
      :value: 'info'

      

   .. py:attribute:: internal_resistance
      :type: str
      :value: 'ir'

      

   .. py:attribute:: internal_resistance_change
      :type: str
      :value: 'ir_pct_change'

      

   .. py:attribute:: point
      :type: str
      :value: 'point'

      

   .. py:attribute:: rate_avr
      :type: str
      :value: 'rate_avr'

      

   .. py:attribute:: step
      :type: str
      :value: 'step'

      

   .. py:attribute:: step_time
      :type: str
      :value: 'step_time'

      

   .. py:attribute:: sub_step
      :type: str
      :value: 'sub_step'

      

   .. py:attribute:: sub_type
      :type: str
      :value: 'sub_type'

      

   .. py:attribute:: test
      :type: str
      :value: 'test'

      

   .. py:attribute:: test_time
      :type: str
      :value: 'test_time'

      

   .. py:attribute:: type
      :type: str
      :value: 'type'

      

   .. py:attribute:: ustep
      :type: str
      :value: 'ustep'

      

   .. py:attribute:: voltage
      :type: str
      :value: 'voltage'

      


.. py:class:: HeadersSummary


   Bases: :py:obj:`BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.HeadersSummary
      :parts: 1

   Headers used for the summary data (used as column headers for the main data pandas DataFrames)

   In addition to the headers defined here, the summary might also contain
   specific headers (ending in _gravimetric or _areal).

   .. py:property:: areal_charge_capacity
      :type: str


   .. py:property:: areal_discharge_capacity
      :type: str


   .. py:property:: specific_columns
      :type: List[str]

      Returns a list of the columns that can be "specific" (e.g. pr. mass or pr. area) for the summary table.

   .. py:attribute:: channel_id
      :type: str
      :value: 'channel_id'

      

   .. py:attribute:: charge_c_rate
      :type: str
      :value: 'charge_c_rate'

      

   .. py:attribute:: charge_capacity
      :type: str
      :value: 'charge_capacity'

      

   .. py:attribute:: charge_capacity_loss
      :type: str
      :value: 'charge_capacity_loss'

      

   .. py:attribute:: charge_capacity_raw
      :type: str
      :value: 'charge_capacity'

      

   .. py:attribute:: coulombic_difference
      :type: str
      :value: 'coulombic_difference'

      

   .. py:attribute:: coulombic_efficiency
      :type: str
      :value: 'coulombic_efficiency'

      

   .. py:attribute:: cumulated_charge_capacity
      :type: str
      :value: 'cumulated_charge_capacity'

      

   .. py:attribute:: cumulated_charge_capacity_loss
      :type: str
      :value: 'cumulated_charge_capacity_loss'

      

   .. py:attribute:: cumulated_coulombic_difference
      :type: str
      :value: 'cumulated_coulombic_difference'

      

   .. py:attribute:: cumulated_coulombic_efficiency
      :type: str
      :value: 'cumulated_coulombic_efficiency'

      

   .. py:attribute:: cumulated_discharge_capacity
      :type: str
      :value: 'cumulated_discharge_capacity'

      

   .. py:attribute:: cumulated_discharge_capacity_loss
      :type: str
      :value: 'cumulated_discharge_capacity_loss'

      

   .. py:attribute:: cumulated_ric
      :type: str
      :value: 'cumulated_ric'

      

   .. py:attribute:: cumulated_ric_disconnect
      :type: str
      :value: 'cumulated_ric_disconnect'

      

   .. py:attribute:: cumulated_ric_sei
      :type: str
      :value: 'cumulated_ric_sei'

      

   .. py:attribute:: cycle_index
      :type: str
      :value: 'cycle_index'

      

   .. py:attribute:: data_flag
      :type: str
      :value: 'data_flag'

      

   .. py:attribute:: data_point
      :type: str
      :value: 'data_point'

      

   .. py:attribute:: datetime
      :type: str
      :value: 'date_time'

      

   .. py:attribute:: discharge_c_rate
      :type: str
      :value: 'discharge_c_rate'

      

   .. py:attribute:: discharge_capacity
      :type: str
      :value: 'discharge_capacity'

      

   .. py:attribute:: discharge_capacity_loss
      :type: str
      :value: 'discharge_capacity_loss'

      

   .. py:attribute:: discharge_capacity_raw
      :type: str
      :value: 'discharge_capacity'

      

   .. py:attribute:: end_voltage_charge
      :type: str
      :value: 'end_voltage_charge'

      

   .. py:attribute:: end_voltage_discharge
      :type: str
      :value: 'end_voltage_discharge'

      

   .. py:attribute:: high_level
      :type: str
      :value: 'high_level'

      

   .. py:attribute:: ir_charge
      :type: str
      :value: 'ir_charge'

      

   .. py:attribute:: ir_discharge
      :type: str
      :value: 'ir_discharge'

      

   .. py:attribute:: low_level
      :type: str
      :value: 'low_level'

      

   .. py:attribute:: normalized_charge_capacity
      :type: str
      :value: 'normalized_charge_capacity'

      

   .. py:attribute:: normalized_cycle_index
      :type: str
      :value: 'normalized_cycle_index'

      

   .. py:attribute:: normalized_discharge_capacity
      :type: str
      :value: 'normalized_discharge_capacity'

      

   .. py:attribute:: ocv_first_max
      :type: str
      :value: 'ocv_first_max'

      

   .. py:attribute:: ocv_first_min
      :type: str
      :value: 'ocv_first_min'

      

   .. py:attribute:: ocv_second_max
      :type: str
      :value: 'ocv_second_max'

      

   .. py:attribute:: ocv_second_min
      :type: str
      :value: 'ocv_second_min'

      

   .. py:attribute:: postfixes
      :value: ['gravimetric', 'areal']

      

   .. py:attribute:: pre_aux
      :type: str
      :value: 'aux_'

      

   .. py:attribute:: shifted_charge_capacity
      :type: str
      :value: 'shifted_charge_capacity'

      

   .. py:attribute:: shifted_discharge_capacity
      :type: str
      :value: 'shifted_discharge_capacity'

      

   .. py:attribute:: temperature_last
      :type: str
      :value: 'temperature_last'

      

   .. py:attribute:: temperature_mean
      :type: str
      :value: 'temperature_mean'

      

   .. py:attribute:: test_name
      :type: str
      :value: 'test_name'

      

   .. py:attribute:: test_time
      :type: str
      :value: 'test_time'

      


.. py:class:: InstrumentSettings


   Bases: :py:obj:`DictLikeClass`

   .. autoapi-inheritance-diagram:: cellpy.parameters.internal_settings.InstrumentSettings
      :parts: 1

   Base class for instrument settings.

   Usage::

       @dataclass
       class MyCoolInstrumentSetting(InstrumentSettings):
           var1: str = "first var"
           var2: int = 12

   Remark! Try to use it as you would use a normal dataclass.



.. py:function:: get_cellpy_units(*args, **kwargs) -> CellpyUnits

   Returns an augmented global dictionary with units


.. py:function:: get_default_cellpy_file_raw_units(*args, **kwargs) -> CellpyUnits

   Returns a dictionary with units to use as default for old versions of cellpy files


.. py:function:: get_default_custom_headers_summary() -> HeadersSummary

   Returns an augmented dictionary that can be used to create custom header-strings for the summary
   (used as column headers for the summary pandas DataFrames)

   This function is mainly implemented to provide an example.



.. py:function:: get_default_output_units(*args, **kwargs) -> CellpyUnits

   Returns an augmented dictionary with units to use as default.


.. py:function:: get_default_raw_limits() -> CellpyLimits

   Returns an augmented dictionary with units as default for raw data


.. py:function:: get_default_raw_units(*args, **kwargs) -> CellpyUnits

   Returns a dictionary with units as default for raw data


.. py:function:: get_headers_journal() -> HeadersJournal

   Returns an augmented global dictionary containing the header-strings for the journal (batch)
   (used as column headers for the journal pandas DataFrames)


.. py:function:: get_headers_normal() -> HeadersNormal

   Returns an augmented global dictionary containing the header-strings for the normal data
   (used as column headers for the main data pandas DataFrames)


.. py:function:: get_headers_step_table() -> HeadersStepTable

   Returns an augmented global dictionary containing the header-strings for the steps table
   (used as column headers for the steps pandas DataFrames)


.. py:function:: get_headers_summary() -> HeadersSummary

   Returns an augmented global dictionary containing the header-strings for the summary
   (used as column headers for the summary pandas DataFrames)


.. py:data:: ATTRS_TO_IMPORT_FROM_EXCEL_SQLITE
   :value: ['name', 'label', 'project', 'cell_group', 'cellpy_file_name', 'instrument', 'cell_type',...

   

.. py:data:: BATCH_ATTRS_TO_IMPORT_FROM_EXCEL_SQLITE
   :value: ['comment_history', 'sub_batch_01', 'sub_batch_02', 'sub_batch_03', 'sub_batch_04',...

   

.. py:data:: CELLPY_FILE_VERSION
   :value: 8

   

.. py:data:: COLUMNS_EXCEL_PK
   :value: 'id'

   

.. py:data:: COLUMNS_RENAMER

   

.. py:data:: MINIMUM_CELLPY_FILE_VERSION
   :value: 4

   

.. py:data:: OTHERPATHS
   :value: ['rawdatadir', 'cellpydatadir']

   

.. py:data:: PICKLE_PROTOCOL
   :value: 4

   

.. py:data:: RAW_TABLE_VERSION
   :value: 5

   

.. py:data:: STEP_TABLE_VERSION
   :value: 5

   

.. py:data:: SUMMARY_TABLE_VERSION
   :value: 7

   

.. py:data:: TABLE_NAME_SQLITE
   :value: 'cells'

   

.. py:data:: base_columns_float

   

.. py:data:: base_columns_int

   

.. py:data:: cellpy_units

   

.. py:data:: headers_journal

   

.. py:data:: headers_normal

   

.. py:data:: headers_step_table

   

.. py:data:: headers_summary

   

.. py:data:: keys_journal_session
   :value: ['starred', 'bad_cells', 'bad_cycles', 'notes']

   

