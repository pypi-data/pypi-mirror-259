:py:mod:`cellpy.utils.batch_tools.batch_core`
=============================================

.. py:module:: cellpy.utils.batch_tools.batch_core


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_core.BaseAnalyzer
   cellpy.utils.batch_tools.batch_core.BaseExperiment
   cellpy.utils.batch_tools.batch_core.BaseExporter
   cellpy.utils.batch_tools.batch_core.BaseJournal
   cellpy.utils.batch_tools.batch_core.BasePlotter
   cellpy.utils.batch_tools.batch_core.BaseReporter
   cellpy.utils.batch_tools.batch_core.Data
   cellpy.utils.batch_tools.batch_core.Doer




Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_core.empty_farm
   cellpy.utils.batch_tools.batch_core.hdr_journal


.. py:class:: BaseAnalyzer(*args)


   Bases: :py:obj:`Doer`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_core.BaseAnalyzer
      :parts: 1

   Base class for all the classes that do something to the experiment(s).

   .. attribute:: experiments

      list of experiments.

   .. attribute:: farms

      list of farms (one pr experiment) (containing pandas DataFrames).

   .. attribute:: barn

      identifier for where to place the output-files (i.e. the animals)
      (typically a directory path).

      :type: str

   The do-er iterates through all the connected engines and dumpers (the dumpers are
   run for each engine).

   It is the responsibility of the engines and dumpers to iterate through the experiments.
   The most natural way is to work with just one experiment.

   Setting up the Do-er.

   :param \*args: list of experiments

   .. py:method:: run_dumper(dumper)

      Place the animals in the barn


   .. py:method:: run_engine(engine, **kwargs)

      Run the engine, build the barn and put the animals on the farm



.. py:class:: BaseExperiment(*args)


   An experiment contains experimental data and meta-data.

   .. py:property:: data
      :type: Data

      Property for accessing the underlying data in an experiment.

      .. rubric:: Example

      >>> cell_data_one = experiment.data["2018_cell_001"]
      >>> capacity, voltage = cell_data_one.get_cap(cycle=1)

   .. py:property:: max_cycle


   .. py:method:: info()

      Print information about the experiment.


   .. py:method:: status()
      :abstractmethod:

      Describe the status and health of your experiment.


   .. py:method:: update()
      :abstractmethod:

      Get or link data.



.. py:class:: BaseExporter(*args)


   Bases: :py:obj:`Doer`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_core.BaseExporter
      :parts: 1

   An exporter exports your data to a given format.

   Setting up the Do-er.

   :param \*args: list of experiments

   .. py:method:: run_dumper(dumper)


   .. py:method:: run_engine(engine, **kwargs)

      Set the current_engine and run it.

      The method sets and engages the engine (callable) and provide
      appropriate binding to at least the class attributes self.farms and
      self.barn.

      .. rubric:: Example

      self.current_engine = engine
      self.farms, self.barn = engine(experiments=self.experiments, farms=self.farms, **kwargs)

      :param engine: the function that should be called.
      :type engine: callable
      :param \*\*kwargs: additional keyword arguments sent to the callable.



.. py:class:: BaseJournal


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

   .. py:attribute:: packable
      :value: ['name', 'project', 'time_stamp', 'project_dir', 'batch_dir', 'raw_dir']

      

   .. py:method:: create()
      :abstractmethod:

      Create a journal manually


   .. py:method:: from_db()

      Make journal pages by looking up a database.

      Default to using the simple excel "database" provided by cellpy.

      If you don't have a database, or you don't know how to make and use one,
      look in the cellpy documentation for other solutions
      (e.g. manually create a file that can be loaded by the ``from_file``
      method).


   .. py:method:: from_file(file_name)
      :abstractmethod:


   .. py:method:: generate_file_name()

      Create a file name for saving the journal.


   .. py:method:: paginate()
      :abstractmethod:

      Create folders used for saving the different output files.


   .. py:method:: to_file(file_name=None)
      :abstractmethod:

      Save journal pages to a file.

      The file can then be used in later sessions using the
      `from_file` method.



.. py:class:: BasePlotter(*args)


   Bases: :py:obj:`Doer`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_core.BasePlotter
      :parts: 1

   Base class for all the classes that do something to the experiment(s).

   .. attribute:: experiments

      list of experiments.

   .. attribute:: farms

      list of farms (one pr experiment) (containing pandas DataFrames).

   .. attribute:: barn

      identifier for where to place the output-files (i.e. the animals)
      (typically a directory path).

      :type: str

   The do-er iterates through all the connected engines and dumpers (the dumpers are
   run for each engine).

   It is the responsibility of the engines and dumpers to iterate through the experiments.
   The most natural way is to work with just one experiment.

   Setting up the Do-er.

   :param \*args: list of experiments

   .. py:method:: run_dumper(dumper)
      :abstractmethod:


   .. py:method:: run_engine(engine, **kwargs)
      :abstractmethod:

      Set the current_engine and run it.

      The method sets and engages the engine (callable) and provide
      appropriate binding to at least the class attributes self.farms and
      self.barn.

      .. rubric:: Example

      self.current_engine = engine
      self.farms, self.barn = engine(experiments=self.experiments, farms=self.farms, **kwargs)

      :param engine: the function that should be called.
      :type engine: callable
      :param \*\*kwargs: additional keyword arguments sent to the callable.



.. py:class:: BaseReporter(*args)


   Bases: :py:obj:`Doer`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_core.BaseReporter
      :parts: 1

   Base class for all the classes that do something to the experiment(s).

   .. attribute:: experiments

      list of experiments.

   .. attribute:: farms

      list of farms (one pr experiment) (containing pandas DataFrames).

   .. attribute:: barn

      identifier for where to place the output-files (i.e. the animals)
      (typically a directory path).

      :type: str

   The do-er iterates through all the connected engines and dumpers (the dumpers are
   run for each engine).

   It is the responsibility of the engines and dumpers to iterate through the experiments.
   The most natural way is to work with just one experiment.

   Setting up the Do-er.

   :param \*args: list of experiments

   .. py:method:: run_dumper(dumper)
      :abstractmethod:


   .. py:method:: run_engine(engine)
      :abstractmethod:

      Set the current_engine and run it.

      The method sets and engages the engine (callable) and provide
      appropriate binding to at least the class attributes self.farms and
      self.barn.

      .. rubric:: Example

      self.current_engine = engine
      self.farms, self.barn = engine(experiments=self.experiments, farms=self.farms, **kwargs)

      :param engine: the function that should be called.
      :type engine: callable
      :param \*\*kwargs: additional keyword arguments sent to the callable.



.. py:class:: Data(experiment, *args)


   Bases: :py:obj:`collections.UserDict`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_core.Data
      :parts: 1

   Class that is used to access the experiment.journal.pages DataFrame.

   The Data class loads the complete cellpy-file if raw-data is not already
   loaded in memory. In future version, it could be that the Data object
   will return a link allowing querying instead to save memory usage...

   Remark that some cellpy (cellreader.CellpyCell) function might not work if
   you have the raw-data in memory, but not summary data (if the cellpy function
   requires summary data or other settings not set as default).

   .. py:method:: first()

      Pick out first cell from the batch


   .. py:method:: last()

      Pick out last cell from the batch


   .. py:method:: sample()

      Pick out one random cell from the batch



.. py:class:: Doer(*args)


   Base class for all the classes that do something to the experiment(s).

   .. attribute:: experiments

      list of experiments.

   .. attribute:: farms

      list of farms (one pr experiment) (containing pandas DataFrames).

   .. attribute:: barn

      identifier for where to place the output-files (i.e. the animals)
      (typically a directory path).

      :type: str

   The do-er iterates through all the connected engines and dumpers (the dumpers are
   run for each engine).

   It is the responsibility of the engines and dumpers to iterate through the experiments.
   The most natural way is to work with just one experiment.

   Setting up the Do-er.

   :param \*args: list of experiments

   .. py:method:: assign(experiment)

      Assign an experiment.


   .. py:method:: do(**kwargs)

      Do what is needed and dump it for each engine.


   .. py:method:: empty_the_farms()

      Free all the farms for content (empty all lists).


   .. py:method:: info()

      Delivers some info to you about the class.


   .. py:method:: run_dumper(dumper)
      :abstractmethod:


   .. py:method:: run_engine(engine, **kwargs)
      :abstractmethod:

      Set the current_engine and run it.

      The method sets and engages the engine (callable) and provide
      appropriate binding to at least the class attributes self.farms and
      self.barn.

      .. rubric:: Example

      self.current_engine = engine
      self.farms, self.barn = engine(experiments=self.experiments, farms=self.farms, **kwargs)

      :param engine: the function that should be called.
      :type engine: callable
      :param \*\*kwargs: additional keyword arguments sent to the callable.



.. py:data:: empty_farm
   :value: []

   

.. py:data:: hdr_journal

   

