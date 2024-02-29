:py:mod:`cellpy.parameters.legacy.update_headers`
=================================================

.. py:module:: cellpy.parameters.legacy.update_headers


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.parameters.legacy.update_headers.HeadersJournalV5
   cellpy.parameters.legacy.update_headers.HeadersJournalV7
   cellpy.parameters.legacy.update_headers.HeadersRawV4
   cellpy.parameters.legacy.update_headers.HeadersRawV5
   cellpy.parameters.legacy.update_headers.HeadersRawV6
   cellpy.parameters.legacy.update_headers.HeadersRawV7
   cellpy.parameters.legacy.update_headers.HeadersStepTableV7
   cellpy.parameters.legacy.update_headers.HeadersSummaryV5
   cellpy.parameters.legacy.update_headers.HeadersSummaryV6
   cellpy.parameters.legacy.update_headers.HeadersSummaryV7



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.parameters.legacy.update_headers.get_column_name_mapper
   cellpy.parameters.legacy.update_headers.rename_columns
   cellpy.parameters.legacy.update_headers.rename_fid_columns
   cellpy.parameters.legacy.update_headers.rename_raw_columns
   cellpy.parameters.legacy.update_headers.rename_step_columns
   cellpy.parameters.legacy.update_headers.rename_summary_columns



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.parameters.legacy.update_headers.HEADERS_KEYS_STEP_TABLE_EXTENDED
   cellpy.parameters.legacy.update_headers.HEADERS_STEP_TABLE_EXTENSIONS
   cellpy.parameters.legacy.update_headers.headers_journal_v0
   cellpy.parameters.legacy.update_headers.journal_header_versions
   cellpy.parameters.legacy.update_headers.raw_header_versions
   cellpy.parameters.legacy.update_headers.steps_header_versions
   cellpy.parameters.legacy.update_headers.summary_header_versions


.. py:class:: HeadersJournalV5


   Bases: :py:obj:`cellpy.parameters.internal_settings.BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.legacy.update_headers.HeadersJournalV5
      :parts: 1

   Subclass of BaseSetting including option to add postfixes.

   .. rubric:: Example

   >>> header["key_postfix"]  # returns "value_postfix"

   .. py:attribute:: cell_type
      :type: str
      :value: 'cell_types'

      

   .. py:attribute:: cellpy_file_name
      :type: str
      :value: 'cellpy_file_names'

      

   .. py:attribute:: filename
      :type: str
      :value: 'filenames'

      

   .. py:attribute:: fixed
      :type: str
      :value: 'fixed'

      

   .. py:attribute:: group
      :type: str
      :value: 'groups'

      

   .. py:attribute:: label
      :type: str
      :value: 'labels'

      

   .. py:attribute:: loading
      :type: str
      :value: 'loadings'

      

   .. py:attribute:: mass
      :type: str
      :value: 'masses'

      

   .. py:attribute:: raw_file_names
      :type: str
      :value: 'raw_file_names'

      

   .. py:attribute:: sub_group
      :type: str
      :value: 'sub_groups'

      

   .. py:attribute:: total_mass
      :type: str
      :value: 'total_masses'

      


.. py:class:: HeadersJournalV7


   Bases: :py:obj:`cellpy.parameters.internal_settings.BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.legacy.update_headers.HeadersJournalV7
      :parts: 1

   Subclass of BaseSetting including option to add postfixes.

   .. rubric:: Example

   >>> header["key_postfix"]  # returns "value_postfix"

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

      


.. py:class:: HeadersRawV4


   Bases: :py:obj:`cellpy.parameters.internal_settings.BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.legacy.update_headers.HeadersRawV4
      :parts: 1

   Subclass of BaseSetting including option to add postfixes.

   .. rubric:: Example

   >>> header["key_postfix"]  # returns "value_postfix"

   .. py:attribute:: ac_impedance_txt
      :type: str
      :value: 'AC_Impedance'

      

   .. py:attribute:: aci_phase_angle_txt
      :type: str
      :value: 'ACI_Phase_Angle'

      

   .. py:attribute:: amplitude_txt
      :type: str
      :value: 'Amplitude'

      

   .. py:attribute:: charge_capacity_txt
      :type: str
      :value: 'Charge_Capacity'

      

   .. py:attribute:: charge_energy_txt
      :type: str
      :value: 'Charge_Energy'

      

   .. py:attribute:: current_txt
      :type: str
      :value: 'Current'

      

   .. py:attribute:: cycle_index_txt
      :type: str
      :value: 'Cycle_Index'

      

   .. py:attribute:: data_point_txt
      :type: str
      :value: 'Data_Point'

      

   .. py:attribute:: datetime_txt
      :type: str
      :value: 'DateTime'

      

   .. py:attribute:: discharge_capacity_txt
      :type: str
      :value: 'Discharge_Capacity'

      

   .. py:attribute:: discharge_energy_txt
      :type: str
      :value: 'Discharge_Energy'

      

   .. py:attribute:: dv_dt_txt
      :type: str
      :value: 'dV/dt'

      

   .. py:attribute:: frequency_txt
      :type: str
      :value: 'Frequency'

      

   .. py:attribute:: internal_resistance_txt
      :type: str
      :value: 'Internal_Resistance'

      

   .. py:attribute:: is_fc_data_txt
      :type: str
      :value: 'Is_FC_Data'

      

   .. py:attribute:: ref_ac_impedance_txt
      :type: str
      :value: 'Reference_AC_Impedance'

      

   .. py:attribute:: ref_aci_phase_angle_txt
      :type: str
      :value: 'Reference_ACI_Phase_Angle'

      

   .. py:attribute:: ref_voltage_txt
      :type: str
      :value: 'Reference_Voltage'

      

   .. py:attribute:: step_index_txt
      :type: str
      :value: 'Step_Index'

      

   .. py:attribute:: step_time_txt
      :type: str
      :value: 'Step_Time'

      

   .. py:attribute:: sub_step_index_txt
      :type: str
      :value: 'Sub_Step_Index'

      

   .. py:attribute:: sub_step_time_txt
      :type: str
      :value: 'Sub_Step_Time'

      

   .. py:attribute:: test_id_txt
      :type: str
      :value: 'Test_ID'

      

   .. py:attribute:: test_time_txt
      :type: str
      :value: 'Test_Time'

      

   .. py:attribute:: voltage_txt
      :type: str
      :value: 'Voltage'

      


.. py:class:: HeadersRawV5


   Bases: :py:obj:`cellpy.parameters.internal_settings.BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.legacy.update_headers.HeadersRawV5
      :parts: 1

   Subclass of BaseSetting including option to add postfixes.

   .. rubric:: Example

   >>> header["key_postfix"]  # returns "value_postfix"

   .. py:attribute:: ac_impedance_txt
      :type: str
      :value: 'AC_Impedance'

      

   .. py:attribute:: aci_phase_angle_txt
      :type: str
      :value: 'ACI_Phase_Angle'

      

   .. py:attribute:: amplitude_txt
      :type: str
      :value: 'Amplitude'

      

   .. py:attribute:: charge_capacity_txt
      :type: str
      :value: 'Charge_Capacity'

      

   .. py:attribute:: charge_energy_txt
      :type: str
      :value: 'Charge_Energy'

      

   .. py:attribute:: current_txt
      :type: str
      :value: 'Current'

      

   .. py:attribute:: cycle_index_txt
      :type: str
      :value: 'Cycle_Index'

      

   .. py:attribute:: data_point_txt
      :type: str
      :value: 'Data_Point'

      

   .. py:attribute:: datetime_txt
      :type: str
      :value: 'DateTime'

      

   .. py:attribute:: discharge_capacity_txt
      :type: str
      :value: 'Discharge_Capacity'

      

   .. py:attribute:: discharge_energy_txt
      :type: str
      :value: 'Discharge_Energy'

      

   .. py:attribute:: dv_dt_txt
      :type: str
      :value: 'dV/dt'

      

   .. py:attribute:: frequency_txt
      :type: str
      :value: 'Frequency'

      

   .. py:attribute:: internal_resistance_txt
      :type: str
      :value: 'Internal_Resistance'

      

   .. py:attribute:: is_fc_data_txt
      :type: str
      :value: 'Is_FC_Data'

      

   .. py:attribute:: ref_ac_impedance_txt
      :type: str
      :value: 'Reference_AC_Impedance'

      

   .. py:attribute:: ref_aci_phase_angle_txt
      :type: str
      :value: 'Reference_ACI_Phase_Angle'

      

   .. py:attribute:: ref_voltage_txt
      :type: str
      :value: 'Reference_Voltage'

      

   .. py:attribute:: step_index_txt
      :type: str
      :value: 'Step_Index'

      

   .. py:attribute:: step_time_txt
      :type: str
      :value: 'Step_Time'

      

   .. py:attribute:: sub_step_index_txt
      :type: str
      :value: 'Sub_Step_Index'

      

   .. py:attribute:: sub_step_time_txt
      :type: str
      :value: 'Sub_Step_Time'

      

   .. py:attribute:: test_id_txt
      :type: str
      :value: 'Test_ID'

      

   .. py:attribute:: test_time_txt
      :type: str
      :value: 'Test_Time'

      

   .. py:attribute:: voltage_txt
      :type: str
      :value: 'Voltage'

      


.. py:class:: HeadersRawV6


   Bases: :py:obj:`cellpy.parameters.internal_settings.BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.legacy.update_headers.HeadersRawV6
      :parts: 1

   Subclass of BaseSetting including option to add postfixes.

   .. rubric:: Example

   >>> header["key_postfix"]  # returns "value_postfix"

   .. py:attribute:: ac_impedance_txt
      :type: str
      :value: 'AC_Impedance'

      

   .. py:attribute:: aci_phase_angle_txt
      :type: str
      :value: 'ACI_Phase_Angle'

      

   .. py:attribute:: amplitude_txt
      :type: str
      :value: 'Amplitude'

      

   .. py:attribute:: charge_capacity_txt
      :type: str
      :value: 'Charge_Capacity'

      

   .. py:attribute:: charge_energy_txt
      :type: str
      :value: 'Charge_Energy'

      

   .. py:attribute:: current_txt
      :type: str
      :value: 'Current'

      

   .. py:attribute:: cycle_index_txt
      :type: str
      :value: 'Cycle_Index'

      

   .. py:attribute:: data_point_txt
      :type: str
      :value: 'Data_Point'

      

   .. py:attribute:: datetime_txt
      :type: str
      :value: 'DateTime'

      

   .. py:attribute:: discharge_capacity_txt
      :type: str
      :value: 'Discharge_Capacity'

      

   .. py:attribute:: discharge_energy_txt
      :type: str
      :value: 'Discharge_Energy'

      

   .. py:attribute:: dv_dt_txt
      :type: str
      :value: 'dV/dt'

      

   .. py:attribute:: frequency_txt
      :type: str
      :value: 'Frequency'

      

   .. py:attribute:: internal_resistance_txt
      :type: str
      :value: 'Internal_Resistance'

      

   .. py:attribute:: is_fc_data_txt
      :type: str
      :value: 'Is_FC_Data'

      

   .. py:attribute:: ref_ac_impedance_txt
      :type: str
      :value: 'Reference_AC_Impedance'

      

   .. py:attribute:: ref_aci_phase_angle_txt
      :type: str
      :value: 'Reference_ACI_Phase_Angle'

      

   .. py:attribute:: ref_voltage_txt
      :type: str
      :value: 'Reference_Voltage'

      

   .. py:attribute:: step_index_txt
      :type: str
      :value: 'Step_Index'

      

   .. py:attribute:: step_time_txt
      :type: str
      :value: 'Step_Time'

      

   .. py:attribute:: sub_step_index_txt
      :type: str
      :value: 'Sub_Step_Index'

      

   .. py:attribute:: sub_step_time_txt
      :type: str
      :value: 'Sub_Step_Time'

      

   .. py:attribute:: test_id_txt
      :type: str
      :value: 'Test_ID'

      

   .. py:attribute:: test_time_txt
      :type: str
      :value: 'Test_Time'

      

   .. py:attribute:: voltage_txt
      :type: str
      :value: 'Voltage'

      


.. py:class:: HeadersRawV7


   Bases: :py:obj:`cellpy.parameters.internal_settings.BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.legacy.update_headers.HeadersRawV7
      :parts: 1

   Subclass of BaseSetting including option to add postfixes.

   .. rubric:: Example

   >>> header["key_postfix"]  # returns "value_postfix"

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

      


.. py:class:: HeadersStepTableV7


   Bases: :py:obj:`cellpy.parameters.internal_settings.BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.legacy.update_headers.HeadersStepTableV7
      :parts: 1

   Subclass of BaseSetting including option to add postfixes.

   .. rubric:: Example

   >>> header["key_postfix"]  # returns "value_postfix"

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

      


.. py:class:: HeadersSummaryV5


   Bases: :py:obj:`cellpy.parameters.internal_settings.BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.legacy.update_headers.HeadersSummaryV5
      :parts: 1

   Subclass of BaseSetting including option to add postfixes.

   .. rubric:: Example

   >>> header["key_postfix"]  # returns "value_postfix"

   .. py:attribute:: areal_charge_capacity
      :type: str
      :value: 'areal_charge_capacity_u_mAh_cm2'

      

   .. py:attribute:: areal_discharge_capacity
      :type: str
      :value: 'areal_discharge_capacity_u_mAh_cm2'

      

   .. py:attribute:: charge_c_rate
      :type: str
      :value: 'Charge_C_rate'

      

   .. py:attribute:: charge_capacity
      :type: str
      :value: 'charge_capacity_u_mAh_g'

      

   .. py:attribute:: charge_capacity_loss
      :type: str
      :value: 'charge_capacity_loss_u_mAh_g'

      

   .. py:attribute:: charge_capacity_raw
      :type: str
      :value: 'Charge_Capacity'

      

   .. py:attribute:: coulombic_difference
      :type: str
      :value: 'coulombic_difference_u_mAh_g'

      

   .. py:attribute:: coulombic_efficiency
      :type: str
      :value: 'Coulombic_Efficiency(percentage)'

      

   .. py:attribute:: cumulated_charge_capacity
      :type: str
      :value: 'cumulated_charge_capacity_u_mAh_g'

      

   .. py:attribute:: cumulated_charge_capacity_loss
      :type: str
      :value: 'cumulated_charge_capacity_loss_u_mAh_g'

      

   .. py:attribute:: cumulated_coulombic_difference
      :type: str
      :value: 'cumulated_coulombic_difference_u_mAh_g'

      

   .. py:attribute:: cumulated_coulombic_efficiency
      :type: str
      :value: 'cumulated_coulombic_efficiency_u_percentage'

      

   .. py:attribute:: cumulated_discharge_capacity
      :type: str
      :value: 'cumulated_discharge_capacity_u_mAh_g'

      

   .. py:attribute:: cumulated_discharge_capacity_loss
      :type: str
      :value: 'cumulated_discharge_capacity_loss_u_mAh_g'

      

   .. py:attribute:: cumulated_ric
      :type: str
      :value: 'RIC(none)'

      

   .. py:attribute:: cumulated_ric_disconnect
      :type: str
      :value: 'RIC_Disconnect(none)'

      

   .. py:attribute:: cumulated_ric_sei
      :type: str
      :value: 'RIC_SEI(none)'

      

   .. py:attribute:: cycle_index
      :type: str
      :value: 'Cycle_Index'

      

   .. py:attribute:: data_point
      :type: str
      :value: 'Data_Point'

      

   .. py:attribute:: datetime
      :type: str
      :value: 'DateTime'

      

   .. py:attribute:: discharge_c_rate
      :type: str
      :value: 'Discharge_C_rate'

      

   .. py:attribute:: discharge_capacity
      :type: str
      :value: 'discharge_capacity_u_mAh_g'

      

   .. py:attribute:: discharge_capacity_loss
      :type: str
      :value: 'discharge_capacity_loss_u_mAh_g'

      

   .. py:attribute:: discharge_capacity_raw
      :type: str
      :value: 'Discharge_Capacity'

      

   .. py:attribute:: end_voltage_charge
      :type: str
      :value: 'End_Voltage_Charge(V)'

      

   .. py:attribute:: end_voltage_discharge
      :type: str
      :value: 'End_Voltage_Discharge(V)'

      

   .. py:attribute:: high_level
      :type: str
      :value: 'High_Level(percentage)'

      

   .. py:attribute:: ir_charge
      :type: str
      :value: 'IR_Charge(Ohms)'

      

   .. py:attribute:: ir_discharge
      :type: str
      :value: 'IR_Discharge(Ohms)'

      

   .. py:attribute:: low_level
      :type: str
      :value: 'Low_Level(percentage)'

      

   .. py:attribute:: normalized_charge_capacity
      :type: str
      :value: 'normalized_charge_capacity'

      

   .. py:attribute:: normalized_cycle_index
      :type: str
      :value: 'Normalized_Cycle_Index'

      

   .. py:attribute:: normalized_discharge_capacity
      :type: str
      :value: 'normalized_discharge_capacity'

      

   .. py:attribute:: ocv_first_max
      :type: str
      :value: 'OCV_First_Max(V)'

      

   .. py:attribute:: ocv_first_min
      :type: str
      :value: 'OCV_First_Min(V)'

      

   .. py:attribute:: ocv_second_max
      :type: str
      :value: 'OCV_Second_Max(V)'

      

   .. py:attribute:: ocv_second_min
      :type: str
      :value: 'OCV_Second_Min(V)'

      

   .. py:attribute:: shifted_charge_capacity
      :type: str
      :value: 'Charge_Endpoint_Slippage(mAh/g)'

      

   .. py:attribute:: shifted_discharge_capacity
      :type: str
      :value: 'Discharge_Endpoint_Slippage(mAh/g)'

      

   .. py:attribute:: temperature_last
      :type: str
      :value: 'Last_Temperature(C)'

      

   .. py:attribute:: temperature_mean
      :type: str
      :value: 'Average_Temperature(C)'

      

   .. py:attribute:: test_time
      :type: str
      :value: 'Test_Time'

      


.. py:class:: HeadersSummaryV6


   Bases: :py:obj:`cellpy.parameters.internal_settings.BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.legacy.update_headers.HeadersSummaryV6
      :parts: 1

   Subclass of BaseSetting including option to add postfixes.

   .. rubric:: Example

   >>> header["key_postfix"]  # returns "value_postfix"

   .. py:attribute:: areal_charge_capacity
      :type: str
      :value: 'areal_charge_capacity_u_mAh_cm2'

      

   .. py:attribute:: areal_discharge_capacity
      :type: str
      :value: 'areal_discharge_capacity_u_mAh_cm2'

      

   .. py:attribute:: channel_id
      :type: str
      :value: 'channel_id'

      

   .. py:attribute:: charge_c_rate
      :type: str
      :value: 'charge_c_rate'

      

   .. py:attribute:: charge_capacity
      :type: str
      :value: 'charge_capacity_u_mAh_g'

      

   .. py:attribute:: charge_capacity_loss
      :type: str
      :value: 'charge_capacity_loss_u_mAh_g'

      

   .. py:attribute:: charge_capacity_raw
      :type: str
      :value: 'charge_capacity'

      

   .. py:attribute:: coulombic_difference
      :type: str
      :value: 'coulombic_difference_u_mAh_g'

      

   .. py:attribute:: coulombic_efficiency
      :type: str
      :value: 'coulombic_efficiency_u_percentage'

      

   .. py:attribute:: cumulated_charge_capacity
      :type: str
      :value: 'cumulated_charge_capacity_u_mAh_g'

      

   .. py:attribute:: cumulated_charge_capacity_loss
      :type: str
      :value: 'cumulated_charge_capacity_loss_u_mAh_g'

      

   .. py:attribute:: cumulated_coulombic_difference
      :type: str
      :value: 'cumulated_coulombic_difference_u_mAh_g'

      

   .. py:attribute:: cumulated_coulombic_efficiency
      :type: str
      :value: 'cumulated_coulombic_efficiency_u_percentage'

      

   .. py:attribute:: cumulated_discharge_capacity
      :type: str
      :value: 'cumulated_discharge_capacity_u_mAh_g'

      

   .. py:attribute:: cumulated_discharge_capacity_loss
      :type: str
      :value: 'cumulated_discharge_capacity_loss_u_mAh_g'

      

   .. py:attribute:: cumulated_ric
      :type: str
      :value: 'cumulated_ric_u_none'

      

   .. py:attribute:: cumulated_ric_disconnect
      :type: str
      :value: 'cumulated_ric_disconnect_u_none'

      

   .. py:attribute:: cumulated_ric_sei
      :type: str
      :value: 'cumulated_ric_sei_u_none'

      

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
      :value: 'discharge_capacity_u_mAh_g'

      

   .. py:attribute:: discharge_capacity_loss
      :type: str
      :value: 'discharge_capacity_loss_u_mAh_g'

      

   .. py:attribute:: discharge_capacity_raw
      :type: str
      :value: 'discharge_capacity'

      

   .. py:attribute:: end_voltage_charge
      :type: str
      :value: 'end_voltage_charge_u_V'

      

   .. py:attribute:: end_voltage_discharge
      :type: str
      :value: 'end_voltage_discharge_u_V'

      

   .. py:attribute:: high_level
      :type: str
      :value: 'high_level_u_percentage'

      

   .. py:attribute:: ir_charge
      :type: str
      :value: 'ir_charge_u_Ohms'

      

   .. py:attribute:: ir_discharge
      :type: str
      :value: 'ir_discharge_u_Ohms'

      

   .. py:attribute:: low_level
      :type: str
      :value: 'low_level_u_percentage'

      

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
      :value: 'ocv_first_max_u_V'

      

   .. py:attribute:: ocv_first_min
      :type: str
      :value: 'ocv_first_min_u_V'

      

   .. py:attribute:: ocv_second_max
      :type: str
      :value: 'ocv_second_max_u_V'

      

   .. py:attribute:: ocv_second_min
      :type: str
      :value: 'ocv_second_min_u_V'

      

   .. py:attribute:: shifted_charge_capacity
      :type: str
      :value: 'shifted_charge_capacity_u_mAh_g'

      

   .. py:attribute:: shifted_discharge_capacity
      :type: str
      :value: 'shifted_discharge_capacity_u_mAh_g'

      

   .. py:attribute:: temperature_last
      :type: str
      :value: 'temperature_last_u_C'

      

   .. py:attribute:: temperature_mean
      :type: str
      :value: 'temperature_mean_u_C'

      

   .. py:attribute:: test_name
      :type: str
      :value: 'test_name'

      

   .. py:attribute:: test_time
      :type: str
      :value: 'test_time'

      


.. py:class:: HeadersSummaryV7


   Bases: :py:obj:`cellpy.parameters.internal_settings.BaseHeaders`

   .. autoapi-inheritance-diagram:: cellpy.parameters.legacy.update_headers.HeadersSummaryV7
      :parts: 1

   Subclass of BaseSetting including option to add postfixes.

   .. rubric:: Example

   >>> header["key_postfix"]  # returns "value_postfix"

   .. py:attribute:: areal_charge_capacity
      :type: str
      :value: 'charge_capacity_areal'

      

   .. py:attribute:: areal_discharge_capacity
      :type: str
      :value: 'discharge_capacity_areal'

      

   .. py:attribute:: channel_id
      :type: str
      :value: 'channel_id'

      

   .. py:attribute:: charge_c_rate
      :type: str
      :value: 'charge_c_rate'

      

   .. py:attribute:: charge_capacity
      :type: str
      :value: 'charge_capacity_gravimetric'

      

   .. py:attribute:: charge_capacity_loss
      :type: str
      :value: 'charge_capacity_loss_gravimetric'

      

   .. py:attribute:: charge_capacity_raw
      :type: str
      :value: 'charge_capacity'

      

   .. py:attribute:: coulombic_difference
      :type: str
      :value: 'coulombic_difference_gravimetric'

      

   .. py:attribute:: coulombic_efficiency
      :type: str
      :value: 'coulombic_efficiency'

      

   .. py:attribute:: cumulated_charge_capacity
      :type: str
      :value: 'cumulated_charge_capacity_gravimetric'

      

   .. py:attribute:: cumulated_charge_capacity_loss
      :type: str
      :value: 'cumulated_charge_capacity_loss_gravimetric'

      

   .. py:attribute:: cumulated_coulombic_difference
      :type: str
      :value: 'cumulated_coulombic_difference_gravimetric'

      

   .. py:attribute:: cumulated_coulombic_efficiency
      :type: str
      :value: 'cumulated_coulombic_efficiency'

      

   .. py:attribute:: cumulated_discharge_capacity
      :type: str
      :value: 'cumulated_discharge_capacity_gravimetric'

      

   .. py:attribute:: cumulated_discharge_capacity_loss
      :type: str
      :value: 'cumulated_discharge_capacity_loss_gravimetric'

      

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
      :value: 'discharge_capacity_gravimetric'

      

   .. py:attribute:: discharge_capacity_loss
      :type: str
      :value: 'discharge_capacity_loss_gravimetric'

      

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

      

   .. py:attribute:: shifted_charge_capacity
      :type: str
      :value: 'shifted_charge_capacity_gravimetric'

      

   .. py:attribute:: shifted_discharge_capacity
      :type: str
      :value: 'shifted_discharge_capacity_gravimetric'

      

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

      


.. py:function:: get_column_name_mapper(old_columns: cellpy.parameters.internal_settings.BaseHeaders, new_columns: cellpy.parameters.internal_settings.BaseHeaders) -> Tuple[Dict[str, str], List[str], List[str]]

   Create a dictionary that maps old column names to new column names.

   :param old_columns: The BaseHeaders for the old format.
   :param new_columns: The BaseHeaders for the new format.

   :returns: Translation dictionary, list of missing keys in new format, list of missing keys in old format.


.. py:function:: rename_columns(df: pandas.DataFrame, old: cellpy.parameters.internal_settings.BaseHeaders, new: cellpy.parameters.internal_settings.BaseHeaders, remove_missing_in_new: bool = False, populate_missing_in_old: bool = True) -> pandas.DataFrame

   Rename the column headers of a cells dataframe.

   Usage:
       >>>  old_format_headers = HeadersSummaryV6()
       >>>  new_format_headers = HeadersSummaryV7()
       >>>  df_new_format = rename_columns(df_old_format, old_format_headers, new_format_headers)

   :param df: The dataframe.
   :param old: The BaseHeaders for the old format.
   :param new: The BaseHeaders for the new format.
   :param remove_missing_in_new: remove the columns that are not defined in the new format.
   :param populate_missing_in_old: add "new-format" missing columns (with np.NAN).

   :returns: Dataframe with updated columns


.. py:function:: rename_fid_columns(fid_table: pandas.DataFrame, old_version: int, new_version: int = CELLPY_FILE_VERSION, **kwargs) -> pandas.DataFrame


.. py:function:: rename_raw_columns(raw: pandas.DataFrame, old_version: int, new_version: int = CELLPY_FILE_VERSION, **kwargs) -> pandas.DataFrame


.. py:function:: rename_step_columns(steps: pandas.DataFrame, old_version: int, new_version: int = CELLPY_FILE_VERSION, **kwargs) -> pandas.DataFrame


.. py:function:: rename_summary_columns(summary: pandas.DataFrame, old_version: int, new_version: int = CELLPY_FILE_VERSION, **kwargs) -> pandas.DataFrame

   Rename the summary headers to new format.

   :param summary: summary dataframe in old format.
   :param old_version: old format (cellpy_file_format (might use summary format number instead soon)).
   :param new_version: new format (cellpy_file_format (might use summary format number instead soon)).
   :param \*\*kwargs: remove_missing_in_new (bool): remove the columns that are not defined in the new format.
                      populate_missing_in_old (bool): add "new-format" missing columns (with np.NAN).

   :returns: summary (pandas.DataFrame) with column headers in the new format.


.. py:data:: HEADERS_KEYS_STEP_TABLE_EXTENDED
   :value: ['point', 'test_time', 'step_time', 'current', 'voltage', 'charge', 'discharge', 'internal_resistance']

   

.. py:data:: HEADERS_STEP_TABLE_EXTENSIONS
   :value: ['min', 'max', 'avr', 'first', 'last', 'delta', 'std']

   

.. py:data:: headers_journal_v0

   

.. py:data:: journal_header_versions

   

.. py:data:: raw_header_versions

   

.. py:data:: steps_header_versions

   

.. py:data:: summary_header_versions

   

