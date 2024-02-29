:py:mod:`cellpy.utils.batch_tools.batch_reporters`
==================================================

.. py:module:: cellpy.utils.batch_tools.batch_reporters


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_reporters.HTMLReporter
   cellpy.utils.batch_tools.batch_reporters.PPTReporter




.. py:class:: HTMLReporter


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseReporter`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_reporters.HTMLReporter
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


.. py:class:: PPTReporter


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BaseReporter`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_reporters.PPTReporter
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


