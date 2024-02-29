:py:mod:`cellpy.parameters.prms`
================================

.. py:module:: cellpy.parameters.prms

.. autoapi-nested-parse::

   cellpy parameters



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.parameters.prms.BatchClass
   cellpy.parameters.prms.CellInfoClass
   cellpy.parameters.prms.CellPyConfig
   cellpy.parameters.prms.CellPyDataConfig
   cellpy.parameters.prms.DbClass
   cellpy.parameters.prms.DbColsClass
   cellpy.parameters.prms.DbColsUnitClass
   cellpy.parameters.prms.FileNamesClass
   cellpy.parameters.prms.InstrumentsClass
   cellpy.parameters.prms.MaterialsClass
   cellpy.parameters.prms.PathsClass
   cellpy.parameters.prms.ReaderClass




Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.parameters.prms.Arbin
   cellpy.parameters.prms.Batch
   cellpy.parameters.prms.CellInfo
   cellpy.parameters.prms.Db
   cellpy.parameters.prms.DbCols
   cellpy.parameters.prms.FileNames
   cellpy.parameters.prms.Instruments
   cellpy.parameters.prms.Maccor
   cellpy.parameters.prms.Materials
   cellpy.parameters.prms.Neware
   cellpy.parameters.prms.Paths
   cellpy.parameters.prms.Reader
   cellpy.parameters.prms.cur_dir
   cellpy.parameters.prms.op_wdir
   cellpy.parameters.prms.script_dir
   cellpy.parameters.prms.user_dir
   cellpy.parameters.prms.wdir


.. py:class:: BatchClass


   Bases: :py:obj:`CellPyConfig`

   .. autoapi-inheritance-diagram:: cellpy.parameters.prms.BatchClass
      :parts: 1

   Settings for batch processing.

   .. py:attribute:: auto_use_file_list
      :type: bool
      :value: False

      

   .. py:attribute:: backend
      :type: str
      :value: 'plotly'

      

   .. py:attribute:: color_style_label
      :type: str
      :value: 'seaborn-deep'

      

   .. py:attribute:: dpi
      :type: int
      :value: 300

      

   .. py:attribute:: fig_extension
      :type: str
      :value: 'png'

      

   .. py:attribute:: figure_type
      :type: str
      :value: 'unlimited'

      

   .. py:attribute:: markersize
      :type: int
      :value: 4

      

   .. py:attribute:: notebook
      :type: bool
      :value: True

      

   .. py:attribute:: summary_plot_height
      :type: int
      :value: 800

      

   .. py:attribute:: summary_plot_height_fractions
      :type: List[float]

      

   .. py:attribute:: summary_plot_width
      :type: int
      :value: 900

      

   .. py:attribute:: symbol_label
      :type: str
      :value: 'simple'

      

   .. py:attribute:: template
      :type: str
      :value: 'standard'

      


.. py:class:: CellInfoClass


   Bases: :py:obj:`CellPyDataConfig`

   .. autoapi-inheritance-diagram:: cellpy.parameters.prms.CellInfoClass
      :parts: 1

   Values used for setting the parameters related to the cell and the cycling

   .. py:attribute:: active_electrode_area
      :type: float
      :value: 1.0

      

   .. py:attribute:: active_electrode_current_collector
      :type: str
      :value: 'standard'

      

   .. py:attribute:: active_electrode_thickness
      :type: float
      :value: 1.0

      

   .. py:attribute:: active_electrode_type
      :type: str
      :value: 'standard'

      

   .. py:attribute:: cell_type
      :type: str
      :value: 'standard'

      

   .. py:attribute:: comment
      :type: str
      :value: ''

      

   .. py:attribute:: counter_electrode_type
      :type: str
      :value: 'standard'

      

   .. py:attribute:: electrolyte_type
      :type: str
      :value: 'standard'

      

   .. py:attribute:: electrolyte_volume
      :type: float
      :value: 1.0

      

   .. py:attribute:: experiment_type
      :type: str
      :value: 'cycling'

      

   .. py:attribute:: reference_electrode_current_collector
      :type: str
      :value: 'standard'

      

   .. py:attribute:: reference_electrode_type
      :type: str
      :value: 'standard'

      

   .. py:attribute:: separator_type
      :type: str
      :value: 'standard'

      

   .. py:attribute:: voltage_lim_high
      :type: float
      :value: 1.0

      

   .. py:attribute:: voltage_lim_low
      :type: float
      :value: 0.0

      


.. py:class:: CellPyConfig


   Session settings (global).

   .. py:method:: keys()



.. py:class:: CellPyDataConfig


   Settings that can be unique for each CellpyCell instance.


.. py:class:: DbClass


   Bases: :py:obj:`CellPyConfig`

   .. autoapi-inheritance-diagram:: cellpy.parameters.prms.DbClass
      :parts: 1

   Settings for the handling the simple database.

   .. py:attribute:: db_connection
      :type: Optional[str]

      

   .. py:attribute:: db_data_start_row
      :type: int
      :value: 2

      

   .. py:attribute:: db_file_sqlite
      :type: str
      :value: 'excel.db'

      

   .. py:attribute:: db_header_row
      :type: int
      :value: 0

      

   .. py:attribute:: db_search_end_row
      :type: int

      

   .. py:attribute:: db_search_start_row
      :type: int
      :value: 2

      

   .. py:attribute:: db_table_name
      :type: str
      :value: 'db_table'

      

   .. py:attribute:: db_type
      :type: str
      :value: 'simple_excel_reader'

      

   .. py:attribute:: db_unit_row
      :type: int
      :value: 1

      


.. py:class:: DbColsClass


   Bases: :py:obj:`CellPyConfig`

   .. autoapi-inheritance-diagram:: cellpy.parameters.prms.DbColsClass
      :parts: 1

   Names of the columns in the simple database.

   .. py:attribute:: area
      :type: str
      :value: 'area'

      

   .. py:attribute:: argument
      :type: str
      :value: 'argument'

      

   .. py:attribute:: batch
      :type: str
      :value: 'batch'

      

   .. py:attribute:: cell_name
      :type: str
      :value: 'cell'

      

   .. py:attribute:: cell_type
      :type: str
      :value: 'cell_type'

      

   .. py:attribute:: cellpy_file_name
      :type: str
      :value: 'cellpy_file_name'

      

   .. py:attribute:: comment_cell
      :type: str
      :value: 'comment_cell'

      

   .. py:attribute:: comment_general
      :type: str
      :value: 'comment_general'

      

   .. py:attribute:: comment_slurry
      :type: str
      :value: 'comment_slurry'

      

   .. py:attribute:: exists
      :type: str
      :value: 'exists'

      

   .. py:attribute:: experiment_type
      :type: str
      :value: 'experiment_type'

      

   .. py:attribute:: file_name_indicator
      :type: str
      :value: 'file_name_indicator'

      

   .. py:attribute:: freeze
      :type: str
      :value: 'freeze'

      

   .. py:attribute:: group
      :type: str
      :value: 'group'

      

   .. py:attribute:: id
      :type: str
      :value: 'id'

      

   .. py:attribute:: instrument
      :type: str
      :value: 'instrument'

      

   .. py:attribute:: label
      :type: str
      :value: 'label'

      

   .. py:attribute:: loading
      :type: str
      :value: 'loading_active_material'

      

   .. py:attribute:: mass_active
      :type: str
      :value: 'mass_active_material'

      

   .. py:attribute:: mass_total
      :type: str
      :value: 'mass_total'

      

   .. py:attribute:: nom_cap
      :type: str
      :value: 'nominal_capacity'

      

   .. py:attribute:: project
      :type: str
      :value: 'project'

      

   .. py:attribute:: raw_file_names
      :type: str
      :value: 'raw_file_names'

      

   .. py:attribute:: selected
      :type: str
      :value: 'selected'

      

   .. py:attribute:: sub_batch_01
      :type: str
      :value: 'b01'

      

   .. py:attribute:: sub_batch_02
      :type: str
      :value: 'b02'

      

   .. py:attribute:: sub_batch_03
      :type: str
      :value: 'b03'

      

   .. py:attribute:: sub_batch_04
      :type: str
      :value: 'b04'

      

   .. py:attribute:: sub_batch_05
      :type: str
      :value: 'b05'

      

   .. py:attribute:: sub_batch_06
      :type: str
      :value: 'b06'

      

   .. py:attribute:: sub_batch_07
      :type: str
      :value: 'b07'

      


.. py:class:: DbColsUnitClass


   Bases: :py:obj:`CellPyConfig`

   .. autoapi-inheritance-diagram:: cellpy.parameters.prms.DbColsUnitClass
      :parts: 1

   Unit of the columns in the simple database.

   .. py:attribute:: area
      :type: str
      :value: 'float'

      

   .. py:attribute:: argument
      :type: str
      :value: 'str'

      

   .. py:attribute:: batch
      :type: str
      :value: 'str'

      

   .. py:attribute:: cell_name
      :type: str
      :value: 'str'

      

   .. py:attribute:: cell_type
      :type: str
      :value: 'str'

      

   .. py:attribute:: cellpy_file_name
      :type: str
      :value: 'str'

      

   .. py:attribute:: comment_cell
      :type: str
      :value: 'str'

      

   .. py:attribute:: comment_general
      :type: str
      :value: 'str'

      

   .. py:attribute:: comment_slurry
      :type: str
      :value: 'str'

      

   .. py:attribute:: exists
      :type: str
      :value: 'int'

      

   .. py:attribute:: experiment_type
      :type: str
      :value: 'str'

      

   .. py:attribute:: file_name_indicator
      :type: str
      :value: 'str'

      

   .. py:attribute:: freeze
      :type: str
      :value: 'int'

      

   .. py:attribute:: group
      :type: str
      :value: 'str'

      

   .. py:attribute:: id
      :type: str
      :value: 'str'

      

   .. py:attribute:: instrument
      :type: str
      :value: 'str'

      

   .. py:attribute:: label
      :type: str
      :value: 'str'

      

   .. py:attribute:: loading
      :type: str
      :value: 'float'

      

   .. py:attribute:: mass_active
      :type: str
      :value: 'float'

      

   .. py:attribute:: mass_total
      :type: str
      :value: 'float'

      

   .. py:attribute:: nom_cap
      :type: str
      :value: 'float'

      

   .. py:attribute:: project
      :type: str
      :value: 'str'

      

   .. py:attribute:: raw_file_names
      :type: str
      :value: 'str'

      

   .. py:attribute:: selected
      :type: str
      :value: 'int'

      

   .. py:attribute:: sub_batch_01
      :type: str
      :value: 'str'

      

   .. py:attribute:: sub_batch_02
      :type: str
      :value: 'str'

      

   .. py:attribute:: sub_batch_03
      :type: str
      :value: 'str'

      

   .. py:attribute:: sub_batch_04
      :type: str
      :value: 'str'

      

   .. py:attribute:: sub_batch_05
      :type: str
      :value: 'str'

      

   .. py:attribute:: sub_batch_06
      :type: str
      :value: 'str'

      

   .. py:attribute:: sub_batch_07
      :type: str
      :value: 'str'

      


.. py:class:: FileNamesClass


   Bases: :py:obj:`CellPyConfig`

   .. autoapi-inheritance-diagram:: cellpy.parameters.prms.FileNamesClass
      :parts: 1

   Settings for file names and file handling.

   .. py:attribute:: cellpy_file_extension
      :type: str
      :value: 'h5'

      

   .. py:attribute:: file_list_location
      :type: str

      

   .. py:attribute:: file_list_name
      :type: str

      

   .. py:attribute:: file_list_type
      :type: str

      

   .. py:attribute:: file_name_format
      :type: str
      :value: 'YYYYMMDD_[NAME]EEE_CC_TT_RR'

      

   .. py:attribute:: raw_extension
      :type: str
      :value: 'res'

      

   .. py:attribute:: reg_exp
      :type: str

      

   .. py:attribute:: sub_folders
      :type: bool
      :value: True

      


.. py:class:: InstrumentsClass


   Bases: :py:obj:`CellPyConfig`

   .. autoapi-inheritance-diagram:: cellpy.parameters.prms.InstrumentsClass
      :parts: 1

   Settings for the instruments.

   .. py:attribute:: Arbin
      :type: box.Box

      

   .. py:attribute:: Maccor
      :type: box.Box

      

   .. py:attribute:: Neware
      :type: box.Box

      

   .. py:attribute:: custom_instrument_definitions_file
      :type: Union[str, None]

      

   .. py:attribute:: tester
      :type: Union[str, None]

      


.. py:class:: MaterialsClass


   Bases: :py:obj:`CellPyDataConfig`

   .. autoapi-inheritance-diagram:: cellpy.parameters.prms.MaterialsClass
      :parts: 1

   Default material-specific values used in processing the data.

   .. py:attribute:: cell_class
      :type: str
      :value: 'Li-Ion'

      

   .. py:attribute:: default_mass
      :type: float
      :value: 1.0

      

   .. py:attribute:: default_material
      :type: str
      :value: 'silicon'

      

   .. py:attribute:: default_nom_cap
      :type: float
      :value: 1.0

      

   .. py:attribute:: default_nom_cap_specifics
      :type: str
      :value: 'gravimetric'

      


.. py:class:: PathsClass


   Bases: :py:obj:`CellPyConfig`

   .. autoapi-inheritance-diagram:: cellpy.parameters.prms.PathsClass
      :parts: 1

   Paths used in cellpy.

   .. py:property:: cellpydatadir
      :type: cellpy.internals.core.OtherPath


   .. py:property:: rawdatadir
      :type: cellpy.internals.core.OtherPath


   .. py:attribute:: batchfiledir
      :type: Union[pathlib.Path, str]

      

   .. py:attribute:: db_filename
      :type: str
      :value: 'cellpy_db.xlsx'

      

   .. py:attribute:: db_path
      :type: Union[pathlib.Path, str]

      

   .. py:attribute:: env_file
      :type: Union[pathlib.Path, str]

      

   .. py:attribute:: examplesdir
      :type: Union[pathlib.Path, str]

      

   .. py:attribute:: filelogdir
      :type: Union[pathlib.Path, str]

      

   .. py:attribute:: instrumentdir
      :type: Union[pathlib.Path, str]

      

   .. py:attribute:: notebookdir
      :type: Union[pathlib.Path, str]

      

   .. py:attribute:: outdatadir
      :type: Union[pathlib.Path, str]

      

   .. py:attribute:: templatedir
      :type: Union[pathlib.Path, str]

      


.. py:class:: ReaderClass


   Bases: :py:obj:`CellPyConfig`

   .. autoapi-inheritance-diagram:: cellpy.parameters.prms.ReaderClass
      :parts: 1

   Settings for reading data.

   .. py:attribute:: auto_dirs
      :type: bool
      :value: True

      

   .. py:attribute:: capacity_interpolation_step
      :type: float
      :value: 2.0

      

   .. py:attribute:: cycle_mode
      :type: str
      :value: 'anode'

      

   .. py:attribute:: diagnostics
      :type: bool
      :value: False

      

   .. py:attribute:: ensure_step_table
      :type: bool
      :value: False

      

   .. py:attribute:: ensure_summary_table
      :type: bool
      :value: False

      

   .. py:attribute:: filestatuschecker
      :type: str
      :value: 'size'

      

   .. py:attribute:: force_all
      :type: bool
      :value: False

      

   .. py:attribute:: force_step_table_creation
      :type: bool
      :value: True

      

   .. py:attribute:: jupyter_executable
      :type: str
      :value: 'jupyter'

      

   .. py:attribute:: limit_loaded_cycles
      :type: Optional[int]

      

   .. py:attribute:: select_minimal
      :type: bool
      :value: False

      

   .. py:attribute:: sep
      :type: str
      :value: ';'

      

   .. py:attribute:: sorted_data
      :type: bool
      :value: True

      

   .. py:attribute:: time_interpolation_step
      :type: float
      :value: 10.0

      

   .. py:attribute:: use_cellpy_stat_file
      :type: bool
      :value: False

      

   .. py:attribute:: voltage_interpolation_step
      :type: float
      :value: 0.01

      


.. py:data:: Arbin

   

.. py:data:: Batch

   

.. py:data:: CellInfo

   

.. py:data:: Db

   

.. py:data:: DbCols

   

.. py:data:: FileNames

   

.. py:data:: Instruments

   

.. py:data:: Maccor

   

.. py:data:: Materials

   

.. py:data:: Neware

   

.. py:data:: Paths

   

.. py:data:: Reader

   

.. py:data:: cur_dir

   

.. py:data:: op_wdir

   

.. py:data:: script_dir

   

.. py:data:: user_dir

   

.. py:data:: wdir

   

