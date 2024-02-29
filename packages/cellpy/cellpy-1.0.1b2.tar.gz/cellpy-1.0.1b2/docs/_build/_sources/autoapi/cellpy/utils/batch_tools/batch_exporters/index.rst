:py:mod:`cellpy.utils.batch_tools.batch_exporters`
==================================================

.. py:module:: cellpy.utils.batch_tools.batch_exporters


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_exporters.CSVExporter
   cellpy.utils.batch_tools.batch_exporters.ExcelExporter
   cellpy.utils.batch_tools.batch_exporters.OriginLabExporter




.. py:class:: CSVExporter(use_screen_dumper=False)


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseExporter`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_exporters.CSVExporter
      :parts: 1

   Export experiment(s) to csv-files.

   CSV Exporter looks at your experiments and exports data to csv
   format. It contains two engines: summary_engine and cycles_engine,
   and two dumpers: csv_dumper and screen_dumper.

   You assign experiments to CSVExporter either as input during
   instantiation or by issuing the assign(experiment) method.

   To perform the exporting, issue CSVExporter.do()

   .. rubric:: Example

   >>> exporter = CSVExporter(my_experiment)
   >>> exporter.do()

   :param use_screen_dumper: dump info to screen (default False).
   :type use_screen_dumper: bool

   Setting up the Do-er.

   :param \*args: list of experiments

   .. py:method:: run_dumper(dumper)

      run dumber (once pr. engine)

      :param dumper: dumper to run (function or method).

      The dumper takes the attributes experiments, farms, and barn as input.


   .. py:method:: run_engine(engine, **kwargs)

      run engine (once pr. experiment).

      :param engine: engine to run (function or method).

      The method issues the engine command (with experiments and farms
      as input) that returns an updated farms as well as the barn and
      assigns them both to self.

      The farms attribute is a list of farms, i.e. [farm1, farm2, ...], where
      each farm contains pandas DataFrames.

      The barns attribute is a pre-defined string used for picking what
      folder(s) the file(s) should be exported to.
      For example, if barn equals "batch_dir", the file(s) will be saved
      to the experiments batch directory.



.. py:class:: ExcelExporter


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseExporter`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_exporters.ExcelExporter
      :parts: 1

   Exporter that saves the file in a format that Excel likes.

   Setting up the Do-er.

   :param \*args: list of experiments


.. py:class:: OriginLabExporter


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseExporter`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_exporters.OriginLabExporter
      :parts: 1

   Exporter that saves the files in a format convenient for OriginLab.

   Setting up the Do-er.

   :param \*args: list of experiments


