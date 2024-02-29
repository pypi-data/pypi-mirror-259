:py:mod:`cellpy.readers.instruments.base`
=========================================

.. py:module:: cellpy.readers.instruments.base

.. autoapi-nested-parse::

   When you make a new loader you have to subclass the Loader class.
   Remember also to register it in cellpy.cellreader.

   (for future development, not used very efficiently yet).



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.base.AtomicLoad
   cellpy.readers.instruments.base.AutoLoader
   cellpy.readers.instruments.base.BaseLoader
   cellpy.readers.instruments.base.TxtLoader



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.base.find_delimiter_and_start
   cellpy.readers.instruments.base.query_csv



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.instruments.base.MINIMUM_SELECTION


.. py:class:: AtomicLoad


   Atomic loading class

   .. py:property:: fid

      The unique file id

   .. py:property:: is_db

      Is the file stored in the database

   .. py:property:: name

      The name of the file to be loaded

   .. py:property:: refuse_copying

      Should the file be copied to a temporary file

   .. py:property:: temp_file_path

      The name of the file to be loaded if copied to a temporary file

   .. py:attribute:: instrument_name
      :value: 'atomic_loader'

      

   .. py:method:: copy_to_temporary()

      Copy file to a temporary file


   .. py:method:: generate_fid(value=None)

      Generate a unique file id


   .. py:method:: loader(*args, **kwargs)

      The method that does the actual loading.

      This method should be overwritten by the specific loader class.


   .. py:method:: loader_executor(*args, **kwargs)

      Load the file



.. py:class:: AutoLoader(*args, **kwargs)


   Bases: :py:obj:`BaseLoader`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.base.AutoLoader
      :parts: 1

   Main autoload class.

   This class can be sub-classed if you want to make a data-reader for different type of "easily parsed" files
   (for example csv-files). The subclass needs to have at least one
   associated CONFIGURATION_MODULE defined and must have the following attributes as minimum::

       default_model: str = NICK_NAME_OF_DEFAULT_CONFIGURATION_MODULE
       supported_models: dict = SUPPORTED_MODELS

   where SUPPORTED_MODELS is a dictionary with ``{"NICK_NAME" : "CONFIGURATION_MODULE_NAME"}``  key-value pairs.
   Remark! the NICK_NAME must be in upper-case!

   It is also possible to set these in a custom pre_init method::

       @classmethod
       def pre_init(cls):
           cls.default_model: str = NICK_NAME_OF_DEFAULT_CONFIGURATION_MODULE
           cls.supported_models: dict = SUPPORTED_MODELS

   or turn off automatic registering of configuration::

       @classmethod
       def pre_init(cls):
           cls.auto_register_config = False  # defaults to True

   During initialisation of the class, if ``auto_register_config == True``,  it will dynamically load the definitions
   provided in the CONFIGURATION_MODULE.py located in the ``cellpy.readers.instruments.configurations``
   folder/package.

   Attributes can be set during initialisation of the class as **kwargs that are then handled by the
   ``parse_formatter_parameters`` method.

   Remark that some also can be provided as arguments to the ``loader`` method and will then automatically
   be "transparent" to the ``cellpy.get`` function. So if you would like to give the user access to modify
   these arguments, you should implement them in the ``parse_loader_parameters`` method.


   .. py:attribute:: instrument_name
      :value: 'auto_loader'

      

   .. py:method:: get_headers_aux(raw: pandas.DataFrame) -> dict
      :staticmethod:
      :abstractmethod:


   .. py:method:: get_raw_limits()

      Limits used to identify type of step.

      The raw limits are 'epsilons' used to check if the current and/or voltage is stable (for example
      for galvanostatic steps, one would expect that the current is stable (constant) and non-zero).
      If the (accumulated) change is less than 'epsilon', then cellpy interpret it to be stable.
      It is expected that different instruments (with different resolution etc.) have different
      resolutions and noice levels, thus different 'epsilons'.

      :returns: the raw limits (dict)


   .. py:method:: get_raw_units()

      Units used by the instrument.

      The internal cellpy units are given in the ``cellpy_units`` attribute.

      :returns: dictionary of units (str)

      .. rubric:: Example

      A minimum viable implementation could look like this::

          @staticmethod
          def get_raw_units():
              raw_units = dict()
              raw_units["current"] = "A"
              raw_units["charge"] = "Ah"
              raw_units["mass"] = "g"
              raw_units["voltage"] = "V"
              return raw_units


   .. py:method:: loader(name: Union[str, pathlib.Path], **kwargs: str) -> cellpy.readers.core.Data

      returns a Data object with loaded data.

      Loads data from a txt file (csv-ish).

      :param name: name of the file.
      :type name: str, pathlib.Path
      :param kwargs: key-word arguments from raw_loader.
      :type kwargs: dict

      :returns: new_tests (list of data objects)


   .. py:method:: parse_formatter_parameters(**kwargs) -> None
      :abstractmethod:


   .. py:method:: parse_loader_parameters(**kwargs)
      :abstractmethod:


   .. py:method:: parse_meta() -> dict

      Method that parses the data for meta-data (e.g. start-time, channel number, ...)


   .. py:method:: pre_init() -> None


   .. py:method:: query_file(file_path: Union[str, pathlib.Path]) -> pandas.DataFrame
      :abstractmethod:


   .. py:method:: register_configuration() -> cellpy.readers.instruments.configurations.ModelParameters

      Register and load model configuration


   .. py:method:: validate(data: cellpy.readers.core.Data) -> cellpy.readers.core.Data

      Validation of the loaded data, should raise an appropriate exception if it fails.



.. py:class:: BaseLoader


   Bases: :py:obj:`AtomicLoad`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.base.BaseLoader
      :parts: 1

   Main loading class

   .. py:attribute:: instrument_name
      :value: 'base_loader'

      

   .. py:method:: get_params(parameter: Union[str, None]) -> dict
      :classmethod:

      Retrieves parameters needed for facilitating working with the
      instrument without registering it.

      Typically, it should include the name and raw_ext.

      Return: parameters or a selected parameter


   .. py:method:: get_raw_limits() -> dict
      :abstractmethod:

      Limits used to identify type of step.

      The raw limits are 'epsilons' used to check if the current and/or voltage is stable (for example
      for galvanostatic steps, one would expect that the current is stable (constant) and non-zero).
      If the (accumulated) change is less than 'epsilon', then cellpy interpret it to be stable.
      It is expected that different instruments (with different resolution etc.) have different
      resolutions and noice levels, thus different 'epsilons'.

      :returns: the raw limits (dict)


   .. py:method:: get_raw_units() -> dict
      :staticmethod:
      :abstractmethod:

      Units used by the instrument.

      The internal cellpy units are given in the ``cellpy_units`` attribute.

      :returns: dictionary of units (str)

      .. rubric:: Example

      A minimum viable implementation could look like this::

          @staticmethod
          def get_raw_units():
              raw_units = dict()
              raw_units["current"] = "A"
              raw_units["charge"] = "Ah"
              raw_units["mass"] = "g"
              raw_units["voltage"] = "V"
              return raw_units


   .. py:method:: identify_last_data_point(data: cellpy.readers.core.Data) -> cellpy.readers.core.Data
      :staticmethod:

      This method is used to find the last record in the data.


   .. py:method:: loader(*args, **kwargs) -> list
      :abstractmethod:

      Loads data into a Data object and returns it



.. py:class:: TxtLoader(*args, **kwargs)


   Bases: :py:obj:`AutoLoader`, :py:obj:`abc.ABC`

   .. autoapi-inheritance-diagram:: cellpy.readers.instruments.base.TxtLoader
      :parts: 1

   Main txt loading class (for sub-classing).

   The subclass of a ``TxtLoader`` gets its information by loading model specifications from its respective module
   (``cellpy.readers.instruments.configurations.<module>``) or configuration file (yaml).

   Remark that if you implement automatic loading of the formatter, the module / yaml-file must include all
   the required formatter parameters (sep, skiprows, header, encoding, decimal, thousands).

   If you need more flexibility, try using the ``CustomTxtLoader`` or subclass directly
   from ``AutoLoader`` or ``Loader``.

   .. attribute:: model

      short name of the (already implemented) sub-model.

      :type: str

   .. attribute:: sep

      delimiter.

      :type: str

   .. attribute:: skiprows

      number of lines to skip.

      :type: int

   .. attribute:: header

      number of the header lines.

      :type: int

   .. attribute:: encoding

      encoding.

      :type: str

   .. attribute:: decimal

      character used for decimal in the raw data, defaults to '.'.

      :type: str

   .. attribute:: processors

      pre-processing steps to take (before loading with pandas).

      :type: dict

   .. attribute:: post_processors

      post-processing steps to make after loading the data, but before

      :type: dict

   .. attribute:: returning them to the caller.

      

   .. attribute:: include_aux

      also parse so-called auxiliary columns / data. Defaults to False.

      :type: bool

   .. attribute:: keep_all_columns

      load all columns, also columns that are not 100% necessary for ``cellpy`` to work.

      :type: bool

   Remark that the configuration settings for the sub-model must include a list of column header names
   that should be kept if keep_all_columns is False (default).

   :param sep: the delimiter (also works as a switch to turn on/off automatic detection of delimiter and
               start of data (skiprows)).
   :type sep: str

   .. py:attribute:: instrument_name
      :value: 'txt_loader'

      

   .. py:attribute:: raw_ext
      :value: '*'

      

   .. py:method:: parse_formatter_parameters(**kwargs)


   .. py:method:: parse_loader_parameters(**kwargs)


   .. py:method:: query_file(name)



.. py:function:: find_delimiter_and_start(file_name, separators=None, checking_length_header=30, checking_length_whole=200)

   Function to automatically detect the delimiter and what line the first data appears on.

   This function is fairly stupid. It splits the data into two parts, the (possible) header part
   (using the number of lines defined in ``checking_length_header``) and the rest of the data.
   Then it counts the appearances of the different possible delimiters in the rest of
   the data part, and then selects a delimiter if it has unique counts for all the lines.

   The first line is defined as where the delimiter is used same number of times (probably a header line).

   :param file_name: path to the file.
   :param separators: list of possible delimiters.
   :param checking_length_header: number of lines to check for header.
   :param checking_length_whole: number of lines to check for delimiter.

   :returns: the delimiter.
             first_index: the index of the first line with data.
   :rtype: separator


.. py:function:: query_csv(self, name, sep=None, skiprows=None, header=None, encoding=None, decimal=None, thousands=None)

   function to query a csv file using pandas.read_csv.


   :param name: path to the file.
   :param sep: delimiter.
   :param skiprows: number of lines to skip.
   :param header: number of the header lines.
   :param encoding: encoding.
   :param decimal: character used for decimal in the raw data, defaults to '.'.
   :param thousands: character used for thousands in the raw data, defaults to ','.

   :returns: pandas.DataFrame


.. py:data:: MINIMUM_SELECTION
   :value: ['Data_Point', 'Test_Time', 'Step_Time', 'DateTime', 'Step_Index', 'Cycle_Index', 'Current',...

   

