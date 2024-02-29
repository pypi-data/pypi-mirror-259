:py:mod:`cellpy.utils.batch_tools.batch_analyzers`
==================================================

.. py:module:: cellpy.utils.batch_tools.batch_analyzers


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_analyzers.BaseSummaryAnalyzer
   cellpy.utils.batch_tools.batch_analyzers.EISAnalyzer
   cellpy.utils.batch_tools.batch_analyzers.ICAAnalyzer
   cellpy.utils.batch_tools.batch_analyzers.OCVRelaxationAnalyzer




.. py:class:: BaseSummaryAnalyzer


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseAnalyzer`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_analyzers.BaseSummaryAnalyzer
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


.. py:class:: EISAnalyzer


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseAnalyzer`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_analyzers.EISAnalyzer
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


.. py:class:: ICAAnalyzer


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseAnalyzer`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_analyzers.ICAAnalyzer
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


.. py:class:: OCVRelaxationAnalyzer


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseAnalyzer`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_analyzers.OCVRelaxationAnalyzer
      :parts: 1

   Analyze open curcuit relaxation curves.

   This analyzer is still under development.
   (Partly) implented so far: select_ocv_points -> farms.
   To get the DataFrames from the farms, you can use
   >>> ocv_point_frames = OCVRelaxationAnalyzer.last

   .. attribute:: selection_method

      criteria for selecting points
      (martin: select first and last, and then last/2, last/2/2 etc. until you have reached the wanted number of points; fixed_time: select first, and same interval; defaults to "martin")

   .. attribute:: number_of_points

      number of points you want.
      defaults to 5

   .. attribute:: interval

      interval between each point (in use only for methods
      where interval makes sense). If it is a list, then
      number_of_points will be calculated as len(interval) + 1 (and
      override the set number_of_points).
      defaults to 10

   .. attribute:: relative_voltage

      set to True if you would like the voltage to be
      relative to the voltage before starting the ocv rlx step.
      Defaults to False. Remark that for the initial rxl step (when
      you just have put your cell on the tester) does not have any
      prior voltage. The relative voltage will then be versus the
      first measurement point.
      defaults to False

   .. attribute:: report_times

      also report the ocv rlx total time if True (defaults
      to False)

   .. attribute:: direction

      select "up" if you would like
      to process only the ocv rlx steps where the voltage is relaxing
      upwards and vize versa. Defaults to "both

      :type: "up", "down" or "both"

   .. rubric:: Notes

   This analyzer is not working as intended yet. Todos:

   - include better engine-dumper methodology and dump
     stuff to both memory and file(s)
     (should add this to BaseAnalyser)
   - recieve settings and parameters
   - option (dumper) for plotting?
   - automatic fitting of OCV rlx data?

   Setting up the Do-er.

   :param \*args: list of experiments

   .. py:property:: dframe
      :type: pandas.DataFrame


   .. py:property:: last
      :type: list


   .. py:method:: do()

      Do what is needed and dump it for each engine.


   .. py:method:: do2()


   .. py:method:: ocv_points_engine(**kwargs)


   .. py:method:: run_dumper(dumper)

      Place the animals in the barn


   .. py:method:: run_engine(engine)

      Run the engine, build the barn and put the animals on the farm


   .. py:method:: screen_dumper(**kwargs)



