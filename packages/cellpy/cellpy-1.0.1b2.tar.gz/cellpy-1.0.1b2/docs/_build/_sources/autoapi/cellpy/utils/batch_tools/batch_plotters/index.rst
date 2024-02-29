:py:mod:`cellpy.utils.batch_tools.batch_plotters`
=================================================

.. py:module:: cellpy.utils.batch_tools.batch_plotters


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_plotters.CyclingSummaryPlotter
   cellpy.utils.batch_tools.batch_plotters.EISPlotter



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_plotters.create_legend
   cellpy.utils.batch_tools.batch_plotters.create_plot_option_dicts
   cellpy.utils.batch_tools.batch_plotters.create_summary_plot_bokeh
   cellpy.utils.batch_tools.batch_plotters.exporting_plots
   cellpy.utils.batch_tools.batch_plotters.generate_summary_frame_for_plotting
   cellpy.utils.batch_tools.batch_plotters.generate_summary_plots
   cellpy.utils.batch_tools.batch_plotters.look_up_group
   cellpy.utils.batch_tools.batch_plotters.plot_cycle_life_summary_bokeh
   cellpy.utils.batch_tools.batch_plotters.plot_cycle_life_summary_matplotlib
   cellpy.utils.batch_tools.batch_plotters.plot_cycle_life_summary_plotly
   cellpy.utils.batch_tools.batch_plotters.plot_cycle_life_summary_seaborn
   cellpy.utils.batch_tools.batch_plotters.summary_plotting_engine



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_plotters.available_plotting_backends
   cellpy.utils.batch_tools.batch_plotters.bokeh_available
   cellpy.utils.batch_tools.batch_plotters.csp
   cellpy.utils.batch_tools.batch_plotters.hdr_journal
   cellpy.utils.batch_tools.batch_plotters.hdr_summary
   cellpy.utils.batch_tools.batch_plotters.plotly_available
   cellpy.utils.batch_tools.batch_plotters.seaborn_available


.. py:class:: CyclingSummaryPlotter(*args, reset_farms=True)


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BasePlotter`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_plotters.CyclingSummaryPlotter
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

   Attributes (inherited):
       experiments: list of experiments.
       farms: list of farms (containing pandas DataFrames or figs).
       barn (str): identifier for where to place the output-files.
       reset_farms (bool): empty the farms before running the engine.

   .. py:property:: columns


   .. py:method:: run_dumper(dumper)

      run dumber (once pr. engine)

      :param dumper: dumper to run (function or method).

      The dumper takes the attributes experiments, farms, and barn as input.
      It does not return anything. But can, if the dumper designer feels in
      a bad and nasty mood, modify the input objects
      (for example experiments).


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

      The engine(s) is given `self.experiments` and `self.farms` as input and
      returns farms to `self.farms` and barn to `self.barn`. Thus, one could
      in principle modify `self.experiments` within the engine without
      explicitly 'notifying' the poor soul who is writing a batch routine
      using that engine. However, it is strongly advised not to do such
      things. And if you, as engine designer, really need to, then at least
      notify it through a debug (logger) statement.



.. py:class:: EISPlotter


   Bases: :py:obj:`cellpy.utils.batch_tools.batch_core.BasePlotter`

   .. autoapi-inheritance-diagram:: cellpy.utils.batch_tools.batch_plotters.EISPlotter
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

   .. py:method:: do()

      Do what is needed and dump it for each engine.



.. py:function:: create_legend(info, c, option='clean', use_index=False)

   creating more informative legends


.. py:function:: create_plot_option_dicts(info, marker_types=None, colors=None, line_dash=None, size=None, palette=None)

   Create two dictionaries with plot-options.

   The first iterates colors (based on group-number), the second iterates
   through marker types.

   Returns: group_styles (dict), sub_group_styles (dict)


.. py:function:: create_summary_plot_bokeh(data, info, group_styles, sub_group_styles, label=None, title='Capacity', x_axis_label='Cycle number', y_axis_label='Capacity (mAh/g)', width=900, height=400, legend_option='clean', legend_location='bottom_right', x_range=None, y_range=None, tools=None)


.. py:function:: exporting_plots(**kwargs)


.. py:function:: generate_summary_frame_for_plotting(pages, experiment, **kwargs)


.. py:function:: generate_summary_plots(experiment, **kwargs)


.. py:function:: look_up_group(info, c)


.. py:function:: plot_cycle_life_summary_bokeh(info, summaries, width=900, height=800, height_fractions=None, legend_option='all', add_rate=True, **kwargs)


.. py:function:: plot_cycle_life_summary_matplotlib(info, summaries, width=900, height=800, height_fractions=None, legend_option='all', **kwargs)


.. py:function:: plot_cycle_life_summary_plotly(summaries: pandas.DataFrame, **kwargs)


.. py:function:: plot_cycle_life_summary_seaborn(summaries: pandas.DataFrame, **kwargs)


.. py:function:: summary_plotting_engine(**kwargs)

   creates plots of summary data.


.. py:data:: available_plotting_backends
   :value: ['matplotlib']

   

.. py:data:: bokeh_available

   

.. py:data:: csp

   

.. py:data:: hdr_journal

   

.. py:data:: hdr_summary

   

.. py:data:: plotly_available

   

.. py:data:: seaborn_available

   

