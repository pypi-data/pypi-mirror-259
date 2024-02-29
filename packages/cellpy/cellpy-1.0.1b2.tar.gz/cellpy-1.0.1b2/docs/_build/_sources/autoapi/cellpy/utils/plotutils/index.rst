:py:mod:`cellpy.utils.plotutils`
================================

.. py:module:: cellpy.utils.plotutils

.. autoapi-nested-parse::

   Utilities for helping to plot cellpy-data.



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.plotutils.create_col_info
   cellpy.utils.plotutils.create_colormarkerlist
   cellpy.utils.plotutils.create_colormarkerlist_for_journal
   cellpy.utils.plotutils.create_label_dict
   cellpy.utils.plotutils.cycle_info_plot
   cellpy.utils.plotutils.partition_summary_cv_steps
   cellpy.utils.plotutils.raw_plot
   cellpy.utils.plotutils.summary_plot



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.plotutils.COLOR_DICT
   cellpy.utils.plotutils.SYMBOL_DICT
   cellpy.utils.plotutils.plotly_available
   cellpy.utils.plotutils.seaborn_available


.. py:function:: create_col_info(c)

   Create column information for summary plots.

   :param c: cellpy object

   :returns: x_columns (tuple), y_cols (dict)


.. py:function:: create_colormarkerlist(groups, sub_groups, symbol_label='all', color_style_label='seaborn-colorblind')

   Fetch lists with color names and marker types of correct length.

   :param groups: list of group numbers (used to generate the list of colors)
   :param sub_groups: list of sub-group numbers (used to generate the list of markers).
   :param symbol_label: sub-set of markers to use
   :param color_style_label: cmap to use for colors

   :returns: colors (list), markers (list)


.. py:function:: create_colormarkerlist_for_journal(journal, symbol_label='all', color_style_label='seaborn-colorblind')

   Fetch lists with color names and marker types of correct length for a journal.

   :param journal: cellpy journal
   :param symbol_label: sub-set of markers to use
   :param color_style_label: cmap to use for colors

   :returns: colors (list), markers (list)


.. py:function:: create_label_dict(c)

   Create label dictionary for summary plots.

   :param c: cellpy object

   :returns: x_axis_labels (dict), y_axis_label (dict)


.. py:function:: cycle_info_plot(cell, cycle=None, get_axes=False, interactive=True, t_unit='hours', v_unit='V', i_unit='mA', **kwargs)

   Show raw data together with step and cycle information.

   :param cell: cellpy object
   :param cycle: cycle(s) to select (must be int for matplotlib)
   :type cycle: int or list or tuple
   :param get_axes: return axes (for matplotlib) or figure (for plotly)
   :type get_axes: bool
   :param interactive: use interactive plotting (if available)
   :type interactive: bool
   :param t_unit: unit for x-axis (default: "hours")
   :type t_unit: str
   :param v_unit: unit for y-axis (default: "V")
   :type v_unit: str
   :param i_unit: unit for current (default: "mA")
   :type i_unit: str
   :param \*\*kwargs: parameters specific to plotting backend.

   :returns: ``matplotlib.axes`` or None


.. py:function:: partition_summary_cv_steps(c, x: str, column_set: list, split: bool = False, var_name: str = 'variable', value_name: str = 'value')

   Partition the summary data into CV and non-CV steps.

   :param c: cellpy object
   :param x: x-axis column name
   :param column_set: names of columns to include
   :param split: add additional column that can be used to split the data when plotting.
   :param var_name: name of the variable column after melting
   :param value_name: name of the value column after melting

   :returns: ``pandas.DataFrame`` (melted with columns x, var_name, value_name, and optionally "row" if split is True)


.. py:function:: raw_plot(cell, y=None, y_label=None, x=None, x_label=None, title=None, interactive=True, **kwargs)

   Plot raw data.

   :param cell: cellpy object
   :param y: y-axis column
   :param y_label: label for y-axis
   :param x: x-axis column
   :param x_label: label for x-axis
   :param title: title of the plot
   :param interactive: use interactive plotting
   :param \*\*kwargs: additional parameters for the plotting backend

   :returns: ``matplotlib`` figure or ``plotly`` figure


.. py:function:: summary_plot(c, x: str = None, y: str = 'capacities_gravimetric', height: int = 600, markers: bool = True, title=None, x_range: list = None, y_range: list = None, split: bool = False, interactive: bool = True, share_y: bool = False, rangeslider: bool = False, **kwargs)

   Create a summary plot. Currently only supports plotly.


   :param c: cellpy object
   :param x: x-axis column (default: 'cycle_index')
   :param y: y-axis column or column set. Currently, the following predefined sets exists:

             - "voltages", "capacities_gravimetric", "capacities_areal", "capacities_gravimetric_split_constant_voltage",
               "capacities_areal_split_constant_voltage"
   :param height: height of the plot
   :param markers: use markers
   :param title: title of the plot
   :param x_range: limits for x-axis
   :param y_range: limits for y-axis
   :param split: split the plot
   :param interactive: use interactive plotting
   :param rangeslider: add a range slider to the x-axis (only for plotly)
   :param share_y: share y-axis
   :type share_y: bool
   :param \*\*kwargs: additional parameters for the plotting backend

   :returns: ``plotly`` figure or None


.. py:data:: COLOR_DICT

   

.. py:data:: SYMBOL_DICT

   

.. py:data:: plotly_available

   

.. py:data:: seaborn_available

   

