:py:mod:`cellpy.utils.collectors`
=================================

.. py:module:: cellpy.utils.collectors

.. autoapi-nested-parse::

   Collectors are used for simplifying plotting and exporting batch objects.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.collectors.BatchCollector
   cellpy.utils.collectors.BatchCyclesCollector
   cellpy.utils.collectors.BatchICACollector
   cellpy.utils.collectors.BatchSummaryCollector



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.collectors.cycles_collector
   cellpy.utils.collectors.cycles_plotter
   cellpy.utils.collectors.histogram_equalization
   cellpy.utils.collectors.ica_collector
   cellpy.utils.collectors.ica_plotter
   cellpy.utils.collectors.legend_replacer
   cellpy.utils.collectors.load_data
   cellpy.utils.collectors.load_figure
   cellpy.utils.collectors.load_plotly_figure
   cellpy.utils.collectors.pick_named_cell
   cellpy.utils.collectors.remove_markers
   cellpy.utils.collectors.sequence_plotter
   cellpy.utils.collectors.spread_plot
   cellpy.utils.collectors.summary_collector
   cellpy.utils.collectors.summary_plotter
   cellpy.utils.collectors.y_axis_replacer



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.collectors.CELLPY_MINIMUM_VERSION
   cellpy.utils.collectors.DEFAULT_CYCLES
   cellpy.utils.collectors.HDF_KEY
   cellpy.utils.collectors.IMAGE_TO_FILE_TIMEOUT
   cellpy.utils.collectors.PLOTLY_BASE_TEMPLATE
   cellpy.utils.collectors.fig_pr_cell_template
   cellpy.utils.collectors.fig_pr_cycle_template
   cellpy.utils.collectors.film_template
   cellpy.utils.collectors.px_template_all_axis_shown
   cellpy.utils.collectors.summary_template
   cellpy.utils.collectors.supported_backends


.. py:class:: BatchCollector(b, data_collector, plotter, collector_name=None, name=None, nick=None, autorun=True, backend='plotly', elevated_data_collector_arguments=None, elevated_plotter_arguments=None, data_collector_arguments: dict = None, plotter_arguments: dict = None, experimental: bool = False, **kwargs)


   
   Update both the collected data and the plot(s).
   :param b: the batch object.
   :type b: cellpy.utils.Batch
   :param data_collector: method that collects the data.
   :type data_collector: callable
   :param plotter: method that crates the plots.
   :type plotter: callable
   :param collector_name: name of collector.
   :type collector_name: str
   :param name: name used for auto-generating filenames etc.
   :type name: str or bool
   :param autorun: run collector and plotter immediately if True.
   :type autorun: bool
   :param use_templates: also apply template(s) in autorun mode if True.
   :type use_templates: bool
   :param backend: name of plotting backend to use ("plotly" or "matplotlib").
   :type backend: str
   :param elevated_data_collector_arguments: arguments picked up by the child class' initializer.
   :type elevated_data_collector_arguments: dict
   :param elevated_plotter_arguments: arguments picked up by the child class' initializer.
   :type elevated_plotter_arguments: dict
   :param data_collector_arguments: keyword arguments sent to the data collector.
   :type data_collector_arguments: dict
   :param plotter_arguments: keyword arguments sent to the plotter.
   :type plotter_arguments: dict
   :param update_name: update the name (using automatic name generation) based on new settings.
   :type update_name: bool
   :param \*\*kwargs: set Collector attributes.

   .. py:property:: data_collector_arguments


   .. py:property:: plotter_arguments


   .. py:attribute:: autorun
      :type: bool
      :value: True

      

   .. py:attribute:: collector_name
      :type: str

      

   .. py:attribute:: data
      :type: pandas.DataFrame

      

   .. py:attribute:: data_directory
      :type: pathlib.Path

      

   .. py:attribute:: elevated_data_collector_arguments
      :type: dict

      

   .. py:attribute:: elevated_plotter_arguments
      :type: dict

      

   .. py:attribute:: figure
      :type: Any

      

   .. py:attribute:: figure_directory
      :type: pathlib.Path

      

   .. py:attribute:: name
      :type: str

      

   .. py:attribute:: nick
      :type: str

      

   .. py:attribute:: renderer
      :type: Any

      

   .. py:attribute:: units
      :type: dict

      

   .. py:method:: generate_name()


   .. py:method:: parse_units(**kwargs)

      Look through your cellpy objects and search for units.


   .. py:method:: preprocess_data_for_csv()


   .. py:method:: render()


   .. py:method:: reset_arguments(data_collector_arguments: dict = None, plotter_arguments: dict = None)

      Reset the arguments to the defaults.
      :param data_collector_arguments: optional additional keyword arguments for the data collector.
      :type data_collector_arguments: dict
      :param plotter_arguments: optional additional keyword arguments for the plotter.
      :type plotter_arguments: dict


   .. py:method:: save(serial_number=None)


   .. py:method:: show(**kwargs)

      Show the figure.

      Note that show returns the `figure` object and  if the `backend` used
      does not provide automatic rendering in the editor / running environment you
      are using, you might have to issue the rendering yourself. For example, if you
      are using `plotly` and running it as a script in a typical command shell,
      you will have to issue `.show()` on the returned `figure` object.

      :param \*\*kwargs: sent to the plotter.

      :returns: Figure object


   .. py:method:: to_csv(serial_number=None)


   .. py:method:: to_hdf5(serial_number=None)


   .. py:method:: to_image_files(serial_number=None)


   .. py:method:: update(data_collector_arguments: dict = None, plotter_arguments: dict = None, reset: bool = False, update_data: bool = False, update_name: bool = False, update_plot: bool = True)

      Update both the collected data and the plot(s).
      :param data_collector_arguments: keyword arguments sent to the data collector.
      :type data_collector_arguments: dict
      :param plotter_arguments: keyword arguments sent to the plotter.
      :type plotter_arguments: dict
      :param reset: reset the arguments first.
      :type reset: bool
      :param update_data: update the data before updating the plot even if data has been collected before.
      :type update_data: bool
      :param update_name: update the name (using automatic name generation) based on new settings.
      :type update_name: bool
      :param update_plot: update the plot.
      :type update_plot: bool



.. py:class:: BatchCyclesCollector(b, plot_type='fig_pr_cell', collector_type='back-and-forth', cycles=None, max_cycle=None, rate=None, rate_on=None, rate_std=None, rate_agg=None, inverse=False, label_mapper=None, backend='plotly', cycles_to_plot=None, width=None, palette=None, show_legend=None, legend_position=None, fig_title=None, cols=None, group_legend_muting=True, *args, **kwargs)


   Bases: :py:obj:`BatchCollector`

   .. autoapi-inheritance-diagram:: cellpy.utils.collectors.BatchCyclesCollector
      :parts: 1

   
   Create a collection of capacity plots.

   :param b:
   :param plot_type: either 'fig_pr_cell' or 'fig_pr_cycle'
   :type plot_type: str
   :param backend: what plotting backend to use (currently only 'plotly' is supported)
   :type backend: str
   :param collector_type: how the curves are given
                          "back-and-forth" - standard back and forth; discharge
                              (or charge) reversed from where charge (or discharge) ends.
                          "forth" - discharge (or charge) continues along x-axis.
                          "forth-and-forth" - discharge (or charge) also starts at 0
   :type collector_type: str
   :param data_collector_arguments:
   :type data_collector_arguments: dict
   :param plotter_arguments:
   :type plotter_arguments: dict

   Elevated data collector args:
       cycles (list): select these cycles.
       max_cycle (int): drop all cycles above this value.
       rate (float): filter on rate (C-rate)
       rate_on (str or list of str): only select cycles if based on the rate of this step-type (e.g. on="charge").
       rate_std (float): allow for this inaccuracy when selecting cycles based on rate
       rate_agg (str): how to aggregate the rate (e.g. "mean", "max", "min", "first", "last")
       inverse (bool): select steps that do not have the given C-rate.
       label_mapper (callable or dict): function (or dict) that changes the cell names.
           The dictionary must have the cell labels as given in the `journal.pages` index and new label as values.
           Similarly, if it is a function it takes the cell label as input and returns the new label.
           Remark! No check are performed to ensure that the new cell labels are unique.

   Elevated plotter args:
       cycles_to_plot (int): plot points if True
       width (float): width of plot
       legend_position (str): position of the legend
       show_legend (bool): set to False if you don't want to show legend
       fig_title (str): title (will be put above the figure)
       palette (str): color-map to use
       cols (int): number of columns

   .. py:method:: generate_name()



.. py:class:: BatchICACollector(b, plot_type='fig_pr_cell', cycles=None, max_cycle=None, rate=None, rate_on=None, rate_std=None, rate_agg=None, inverse=False, label_mapper=None, backend='plotly', cycles_to_plot=None, width=None, palette=None, show_legend=None, legend_position=None, fig_title=None, cols=None, group_legend_muting=True, *args, **kwargs)


   Bases: :py:obj:`BatchCollector`

   .. autoapi-inheritance-diagram:: cellpy.utils.collectors.BatchICACollector
      :parts: 1

   
   Create a collection of ica (dQ/dV) plots.

   .. py:method:: generate_name()



.. py:class:: BatchSummaryCollector(b, max_cycle: int = None, rate=None, on=None, columns=None, column_names=None, normalize_capacity_on=None, scale_by=None, nom_cap=None, normalize_cycles=None, group_it=None, rate_std=None, rate_column=None, inverse=None, inverted: bool = None, key_index_bounds=None, backend: str = 'plotly', title: str = None, points: bool = None, line: bool = None, width: int = None, height: int = None, legend_title: str = None, marker_size: int = None, cmap=None, spread: bool = None, fig_title: str = None, *args, **kwargs)


   Bases: :py:obj:`BatchCollector`

   .. autoapi-inheritance-diagram:: cellpy.utils.collectors.BatchSummaryCollector
      :parts: 1

   
   Collects and shows summaries.

   :param backend: what plotting backend to use (currently only 'plotly' is supported)
   :type backend: str

   Elevated data collector args:
       max_cycle (int): drop all cycles above this value.
       rate (float): filter on rate (C-rate)
       on (str or list of str): only select cycles if based on the rate of this step-type (e.g. on="charge").
       columns (list): selected column(s) (using cellpy attribute name)
           [defaults to "charge_capacity_gravimetric"]
       column_names (list): selected column(s) (using exact column name)
       normalize_capacity_on (list): list of cycle numbers that will be used for setting the basis of the
           normalization (typically the first few cycles after formation)
       scale_by (float or str): scale the normalized data with nominal capacity if "nom_cap",
           or given value (defaults to one).
       nom_cap (float): nominal capacity of the cell
       normalize_cycles (bool): perform a normalization of the cycle numbers (also called equivalent cycle index)
       group_it (bool): if True, average pr group.
       rate_std (float): allow for this inaccuracy when selecting cycles based on rate
       rate_column (str): name of the column containing the C-rates.
       inverse (bool): select steps that do not have the given C-rate.
       inverted (bool): select cycles that do not have the steps filtered by given C-rate.
       key_index_bounds (list): used when creating a common label for the cells in a group
           (when group_it is set to True) by splitting and combining from key_index_bound[0] to key_index_bound[1].
           For example, if your cells are called "cell_01_01" and "cell_01_02" and you set
           key_index_bounds=[0, 2], the common label will be "cell_01". Or if they are called
           "20230101_cell_01_01_01" and "20230101_cell_01_01_02" and you set key_index_bounds=[1, 3],
           the common label will be "cell_01_01".

   Elevated plotter args:
       points (bool): plot points if True
       line (bool): plot line if True
       width: width of plot
       height: height of plot
       legend_title: title to put over the legend
       marker_size: size of the markers used
       cmap: color-map to use
       spread (bool): plot error-bands instead of error-bars if True
       fig_title (str): title of the figure

   .. py:method:: generate_name()


   .. py:method:: preprocess_data_for_csv()



.. py:function:: cycles_collector(b, cycles=None, rate=None, rate_on=None, rate_std=None, rate_agg='first', inverse=False, interpolated=True, number_of_points=100, max_cycle=50, abort_on_missing=False, method='back-and-forth', label_mapper=None)


.. py:function:: cycles_plotter(collected_curves, cycles_to_plot=None, backend='plotly', method='fig_pr_cell', **kwargs)

   Plot charge-discharge curves.

   :param collected_curves: collected data in long format.
   :type collected_curves: pd.DataFrame
   :param cycles_to_plot: cycles to plot
   :type cycles_to_plot: list
   :param backend: what backend to use.
   :type backend: str
   :param method: 'fig_pr_cell' or 'fig_pr_cycle'.
   :type method: str
   :param \*\*kwargs: consumed first in current function, rest sent to backend in sequence_plotter.

   :returns: styled figure object


.. py:function:: histogram_equalization(image: numpy.array) -> numpy.array

   Perform histogram equalization on a numpy array.

   # from http://www.janeriksolem.net/histogram-equalization-with-python-and.html


.. py:function:: ica_collector(b, cycles=None, rate=None, rate_on=None, rate_std=None, rate_agg='first', inverse=False, voltage_resolution=0.005, max_cycle=50, abort_on_missing=False, label_direction=True, number_of_points=None, label_mapper=None, **kwargs)


.. py:function:: ica_plotter(collected_curves, cycles_to_plot=None, backend='plotly', method='fig_pr_cell', direction='charge', **kwargs)

   Plot charge-discharge curves.

   :param collected_curves: collected data in long format.
   :type collected_curves: pd.DataFrame
   :param cycles_to_plot: cycles to plot
   :type cycles_to_plot: list
   :param backend: what backend to use.
   :type backend: str
   :param method: 'fig_pr_cell' or 'fig_pr_cycle' or 'film'.
   :type method: str
   :param direction: 'charge' or 'discharge'.
   :type direction: str
   :param \*\*kwargs: consumed first in current function, rest sent to backend in sequence_plotter.

   :returns: styled figure object


.. py:function:: legend_replacer(trace, df, group_legends=True)


.. py:function:: load_data(filename)

   Load data from hdf5 file.


.. py:function:: load_figure(filename, backend='plotly')

   Load figure from file.


.. py:function:: load_plotly_figure(filename)

   Load plotly figure from file.


.. py:function:: pick_named_cell(b, label_mapper=None)

   generator that picks a cell from the batch object, yields its label and the cell itself.

   :param b: your batch object
   :type b: cellpy.batch object
   :param label_mapper: function (or dict) that changes the cell names.
                        The dictionary must have the cell labels as given in the `journal.pages` index and new label as values.
                        Similarly, if it is a function it takes the cell label as input and returns the new label.
                        Remark! No check are performed to ensure that the new cell labels are unique.
   :type label_mapper: callable or dict

   :Yields: label, group, subgroup, cell

   .. rubric:: Example

   def my_mapper(n):
       return "_".join(n.split("_")[1:-1])

   # outputs "nnn_x" etc., if cell-names are of the form "date_nnn_x_y":
   for label, group, subgroup, cell in pick_named_cell(b, label_mapper=my_mapper):
       print(label)


.. py:function:: remove_markers(trace)


.. py:function:: sequence_plotter(collected_curves: pandas.DataFrame, x: str = 'capacity', y: str = 'voltage', z: str = 'cycle', g: str = 'cell', standard_deviation: str = None, group: str = 'group', subgroup: str = 'sub_group', x_label: str = 'Capacity', x_unit: str = 'mAh/g', y_label: str = 'Voltage', y_unit: str = 'V', z_label: str = 'Cycle', z_unit: str = 'n.', y_label_mapper: dict = None, nbinsx: int = 100, histfunc: str = 'avg', histscale: str = 'abs-log', direction: str = 'charge', direction_col: str = 'direction', method: str = 'fig_pr_cell', markers: bool = False, group_cells: bool = True, group_legend_muting: bool = True, backend: str = 'plotly', cycles: list = None, facetplot: bool = False, cols: int = 3, palette_discrete: str = None, palette_continuous: str = 'Viridis', palette_range: tuple = None, height: float = None, width: float = None, spread: bool = False, **kwargs) -> Any

   create a plot made up of sequences of data (voltage curves, dQ/dV, etc).

   This method contains the "common" operations done for all the sequence plots,
   currently supporting filtering out the specific cycles, selecting either
   dividing into subplots by cell or by cycle, and creating the (most basic) figure object.

   :param collected_curves: collected data in long format.
   :type collected_curves: pd.DataFrame
   :param x: column name for x-values.
   :type x: str
   :param y: column name for y-values.
   :type y: str
   :param z: if method is 'fig_pr_cell', column name for color (legend), else for subplot.
   :type z: str
   :param g: if method is 'fig_pr_cell', column name for subplot, else for color.
   :type g: str
   :param standard_deviation: str = standard deviation column (skipped if None).
   :param group: column name for group.
   :type group: str
   :param subgroup: column name for subgroup.
   :type subgroup: str
   :param x_label: x-label.
   :type x_label: str
   :param x_unit: x-unit (will be put in parentheses after the label).
   :type x_unit: str
   :param y_label: y-label.
   :type y_label: str
   :param y_unit: y-unit (will be put in parentheses after the label).
   :type y_unit: str
   :param z_label: z-label.
   :type z_label: str
   :param z_unit: z-unit (will be put in parentheses after the label).
   :type z_unit: str
   :param y_label_mapper: map the y-labels to something else.
   :type y_label_mapper: dict
   :param nbinsx: number of bins to use in interpolations.
   :type nbinsx: int
   :param histfunc: aggregation method.
   :type histfunc: str
   :param histscale: used for scaling the z-values for 2D array plots (heatmaps and similar).
   :type histscale: str
   :param direction: "charge", "discharge", or "both".
   :type direction: str
   :param direction_col: name of columns containing information about direction ("charge" or "discharge").
   :type direction_col: str
   :param method: 'fig_pr_cell' or 'fig_pr_cycle'.
   :param markers: set to True if you want markers.
   :param group_cells: give each cell within a group same color.
   :type group_cells: bool
   :param group_legend_muting: if True, you can click on the legend to mute the whole group.
   :type group_legend_muting: bool
   :param backend: what backend to use.
   :type backend: str
   :param cycles: what cycles to include in the plot.
   :param palette_discrete: palette to use for discrete color mapping.
   :param palette_continuous: palette to use for continuous color mapping.
   :param palette_range: range of palette to use for continuous color mapping (from 0 to 1).
   :type palette_range: tuple
   :param facetplot: square layout with group horizontally and subgroup vertically.
   :type facetplot: bool
   :param cols: number of columns for layout.
   :type cols: int
   :param height: plot height.
   :type height: int
   :param width: plot width.
   :type width: int
   :param spread: plot error-bands instead of error-bars if True.
   :type spread: bool
   :param \*\*kwargs: sent to backend (if `backend == "plotly"`, it will be
                      sent to `plotly.express` etc.)

   :returns: figure object


.. py:function:: spread_plot(curves, plotly_arguments, **kwargs)

   Create a spread plot (error-bands instead of error-bars).


.. py:function:: summary_collector(*args, **kwargs)

   Collects summaries using cellpy.utils.helpers.concat_summaries.


.. py:function:: summary_plotter(collected_curves, cycles_to_plot=None, backend='plotly', **kwargs)

   Plot summaries (value vs cycle number).

   Assuming data as pandas.DataFrame with either
   1) long format (where variables, for example charge capacity, are in the column "variable") or
   2) mixed long and wide format where the variables are own columns.


.. py:function:: y_axis_replacer(ax, label)


.. py:data:: CELLPY_MINIMUM_VERSION
   :value: '1.0.0'

   

.. py:data:: DEFAULT_CYCLES
   :value: [1, 10, 20]

   

.. py:data:: HDF_KEY
   :value: 'collected_data'

   

.. py:data:: IMAGE_TO_FILE_TIMEOUT
   :value: 30

   

.. py:data:: PLOTLY_BASE_TEMPLATE
   :value: 'seaborn'

   

.. py:data:: fig_pr_cell_template

   

.. py:data:: fig_pr_cycle_template

   

.. py:data:: film_template

   

.. py:data:: px_template_all_axis_shown

   

.. py:data:: summary_template

   

.. py:data:: supported_backends
   :value: []

   

