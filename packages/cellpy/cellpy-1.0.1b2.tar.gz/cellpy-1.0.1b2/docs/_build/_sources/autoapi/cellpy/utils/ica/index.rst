:py:mod:`cellpy.utils.ica`
==========================

.. py:module:: cellpy.utils.ica

.. autoapi-nested-parse::

   ica contains routines for creating and working with
   incremental capacity analysis data



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.ica.Converter



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.ica.dqdv
   cellpy.utils.ica.dqdv_cycle
   cellpy.utils.ica.dqdv_cycles
   cellpy.utils.ica.dqdv_frames
   cellpy.utils.ica.index_bounds
   cellpy.utils.ica.value_bounds



.. py:class:: Converter(capacity=None, voltage=None, points_pr_split=10, max_points=None, voltage_resolution=None, capacity_resolution=None, minimum_splits=3, interpolation_method='linear', increment_method='diff', pre_smoothing=False, smoothing=False, post_smoothing=True, normalize=True, normalizing_factor=None, normalizing_roof=None, savgol_filter_window_divisor_default=50, savgol_filter_window_order=3, voltage_fwhm=0.01, gaussian_order=0, gaussian_mode='reflect', gaussian_cval=0.0, gaussian_truncate=4.0)


   Class for dq-dv handling.

   Typical usage is to (1) set the data, (2) inspect the data,
   (3) pre-process the data,
   (4) perform the dq-dv transform, and finally (5) post-process the data.

   A short note about normalization:

       - If ``normalization`` is set to ``False``, then no normalization will be done.
       - If ``normalization`` is ``True``, and ``normalization_factor`` is ``None``, the total capacity of
         the half cycle will be used for normalization, else the ``normalization_factor`` will be used.
       - If ``normalization`` is ``True``, and ``normalization_roof`` is not ``None``,
         the capacity divided by ``normalization_roof`` will be used for normalization.


   .. py:method:: increment_data()

      Perform the dq-dv transform.


   .. py:method:: inspect_data(capacity=None, voltage=None, err_est=False, diff_est=False)

      Check and inspect the data.


   .. py:method:: post_process_data(voltage=None, incremental_capacity=None, voltage_step=None)

      Perform post-processing (smoothing, normalisation, interpolation) of the data.


   .. py:method:: pre_process_data()

      Perform some pre-processing of the data (i.e. interpolation).


   .. py:method:: set_data(capacity, voltage=None, capacity_label='q', voltage_label='v')

      Set the data.



.. py:function:: dqdv(voltage, capacity, voltage_resolution=None, capacity_resolution=None, voltage_fwhm=0.01, pre_smoothing=True, diff_smoothing=False, post_smoothing=True, post_normalization=True, interpolation_method=None, gaussian_order=None, gaussian_mode=None, gaussian_cval=None, gaussian_truncate=None, points_pr_split=None, savgol_filter_window_divisor_default=None, savgol_filter_window_order=None, max_points=None, **kwargs)

   Convenience functions for creating dq-dv data from given capacity
   and voltage data.

   :param voltage: nd.array or pd.Series
   :param capacity: nd.array or pd.Series
   :param voltage_resolution: used for interpolating voltage data (e.g. 0.005)
   :param capacity_resolution: used for interpolating capacity data
   :param voltage_fwhm: used for setting the post-processing gaussian sigma
   :param pre_smoothing: set to True for pre-smoothing (window)
   :param diff_smoothing: set to True for smoothing during differentiation
                          (window)
   :param post_smoothing: set to True for post-smoothing (gaussian)
   :param post_normalization: set to True for normalizing to capacity
   :param interpolation_method: scipy interpolation method
   :param gaussian_order: int
   :param gaussian_mode: mode
   :param gaussian_cval:
   :param gaussian_truncate:
   :param points_pr_split: only used when investigating data using splits
   :param savgol_filter_window_divisor_default: used for window smoothing
   :param savgol_filter_window_order: used for window smoothing
   :param max_points: restricting to max points in vector (capacity-selected)

   :returns: (voltage, dqdv)


.. py:function:: dqdv_cycle(cycle, splitter=True, label_direction=False, **kwargs)

   Convenience functions for creating dq-dv data from given capacity and
   voltage cycle.

   Returns the DataFrame with a 'voltage' and a 'incremental_capacity'
   column.

   :param cycle: the cycle data ('voltage', 'capacity', 'direction' (1 or -1)).
   :type cycle: pandas.DataFrame
   :param splitter: insert a np.NaN row between charge and discharge.
   :type splitter: bool
   :param label_direction:
   :type label_direction: bool

   :returns: List of step numbers corresponding to the selected steptype.
             Returns a ``pandas.DataFrame`` instead of a list if ``pdtype`` is set to ``True``.

   Additional key-word arguments are sent to Converter:

   :keyword points_pr_split: only used when investigating data using splits, defaults to 10.
   :kwtype points_pr_split: int
   :keyword max_points: None
   :keyword voltage_resolution: used for interpolating voltage data (e.g. 0.005)
   :kwtype voltage_resolution: float
   :keyword capacity_resolution: used for interpolating capacity data
   :keyword minimum_splits: defaults to 3.
   :kwtype minimum_splits: int
   :keyword interpolation_method: scipy interpolation method
   :keyword increment_method: defaults to "diff"
   :kwtype increment_method: str
   :keyword pre_smoothing: set to True for pre-smoothing (window)
   :kwtype pre_smoothing: bool
   :keyword smoothing: set to True for smoothing during differentiation (window)
   :kwtype smoothing: bool
   :keyword post_smoothing: set to True for post-smoothing (gaussian)
   :kwtype post_smoothing: bool
   :keyword normalize: set to True for normalizing to capacity
   :kwtype normalize: bool
   :keyword normalizing_factor:
   :kwtype normalizing_factor: float
   :keyword normalizing_roof:
   :kwtype normalizing_roof: float
   :keyword savgol_filter_window_divisor_default: used for window smoothing, defaults to 50
   :kwtype savgol_filter_window_divisor_default: int
   :keyword savgol_filter_window_order: used for window smoothing
   :keyword voltage_fwhm: used for setting the post-processing gaussian sigma, defaults to 0.01
   :kwtype voltage_fwhm: float
   :keyword gaussian_order: defaults to 0
   :kwtype gaussian_order: int
   :keyword gaussian_mode: defaults to "reflect"
   :kwtype gaussian_mode: str
   :keyword gaussian_cval: defaults to 0.0
   :kwtype gaussian_cval: float
   :keyword gaussian_truncate: defaults to 4.0
   :kwtype gaussian_truncate: float

   .. rubric:: Example

   >>> cycle_df = my_data.get_cap(
   >>> ...   1,
   >>> ...   categorical_column=True,
   >>> ...   method = "forth-and-forth"
   >>> ...   insert_nan=False,
   >>> ... )
   >>> voltage, incremental = ica.dqdv_cycle(cycle_df)


.. py:function:: dqdv_cycles(cycles, not_merged=False, label_direction=False, **kwargs)

   Convenience functions for creating dq-dv data from given capacity and
   voltage cycles.

   Returns a DataFrame with a 'voltage' and a 'incremental_capacity'
   column.

   :param cycles: the cycle data ('cycle', 'voltage',
                  'capacity', 'direction' (1 or -1)).
   :type cycles: pandas.DataFrame
   :param not_merged: return list of frames instead of concatenating (
                      defaults to False).
   :type not_merged: bool
   :param label_direction: include 'direction' (1 or -1).
   :type label_direction: bool

   :returns: ``pandas.DataFrame`` with columns 'cycle', 'voltage', 'dq' (and 'direction' if label_direction is True).

   Additional key-word arguments are sent to Converter:

   :keyword points_pr_split: only used when investigating data using
                             splits, defaults to 10.
   :kwtype points_pr_split: int
   :keyword max_points: None
   :keyword voltage_resolution: used for interpolating voltage data
                                (e.g. 0.005)
   :kwtype voltage_resolution: float
   :keyword capacity_resolution: used for interpolating capacity data
   :keyword minimum_splits: defaults to 3.
   :kwtype minimum_splits: int
   :keyword interpolation_method: scipy interpolation method
   :keyword increment_method: defaults to "diff"
   :kwtype increment_method: str
   :keyword pre_smoothing: set to True for pre-smoothing (window)
   :kwtype pre_smoothing: bool
   :keyword smoothing: set to True for smoothing during
                       differentiation (window)
   :kwtype smoothing: bool
   :keyword post_smoothing: set to True for post-smoothing (gaussian)
   :kwtype post_smoothing: bool
   :keyword normalize: set to True for normalizing to capacity
   :kwtype normalize: bool
   :keyword normalizing_factor:
   :kwtype normalizing_factor: float
   :keyword normalizing_roof:
   :kwtype normalizing_roof: float
   :keyword savgol_filter_window_divisor_default: used for window
                                                  smoothing, defaults to 50
   :kwtype savgol_filter_window_divisor_default: int
   :keyword savgol_filter_window_order: used for window smoothing
   :keyword voltage_fwhm: used for setting the post-processing
                          gaussian sigma, defaults to 0.01
   :kwtype voltage_fwhm: float
   :keyword gaussian_order: defaults to 0
   :kwtype gaussian_order: int
   :keyword gaussian_mode: defaults to "reflect"
   :kwtype gaussian_mode: str
   :keyword gaussian_cval: defaults to 0.0
   :kwtype gaussian_cval: float
   :keyword gaussian_truncate: defaults to 4.0
   :kwtype gaussian_truncate: float

   .. rubric:: Example

   >>> cycles_df = my_data.get_cap(
   >>> ...   categorical_column=True,
   >>> ...   method = "forth-and-forth",
   >>> ...   label_cycle_number=True,
   >>> ...   insert_nan=False,
   >>> ... )
   >>> ica_df = ica.dqdv_cycles(cycles_df)


.. py:function:: dqdv_frames(cell, split=False, tidy=True, label_direction=False, **kwargs)

   Returns dqdv data as pandas.DataFrame(s) for all cycles.

   :param cell:
   :type cell: CellpyCell-object
   :param split: return one frame for charge and one for
                 discharge if True (defaults to False).
   :type split: bool
   :param tidy: returns the split frames in wide format (defaults
                to True. Remark that this option is currently not available
                for non-split frames).
   :type tidy: bool

   :returns: cycle: cycle number (if split is set to True).
             voltage: voltage
             dq: the incremental capacity
   :rtype: one or two ``pandas.DataFrame`` with the following columns

   Additional key-word arguments are sent to Converter:

   :keyword cycle: will process all (or up to max_cycle_number)
                   if not given or equal to None.
   :kwtype cycle: int or list of ints (cycle numbers)
   :keyword points_pr_split: only used when investigating data
                             using splits, defaults to 10.
   :kwtype points_pr_split: int
   :keyword max_points: None
   :keyword voltage_resolution: used for interpolating voltage
                                data (e.g. 0.005)
   :kwtype voltage_resolution: float
   :keyword capacity_resolution: used for interpolating capacity data
   :keyword minimum_splits: defaults to 3.
   :kwtype minimum_splits: int
   :keyword interpolation_method: scipy interpolation method
   :keyword increment_method: defaults to "diff"
   :kwtype increment_method: str
   :keyword pre_smoothing: set to True for pre-smoothing (window)
   :kwtype pre_smoothing: bool
   :keyword smoothing: set to True for smoothing during
                       differentiation (window)
   :kwtype smoothing: bool
   :keyword post_smoothing: set to True for post-smoothing
                            (gaussian)
   :kwtype post_smoothing: bool
   :keyword normalize: set to True for normalizing to capacity
   :kwtype normalize: bool
   :keyword normalizing_factor:
   :kwtype normalizing_factor: float
   :keyword normalizing_roof:
   :kwtype normalizing_roof: float
   :keyword savgol_filter_window_divisor_default: used for window
                                                  smoothing, defaults to 50
   :kwtype savgol_filter_window_divisor_default: int
   :keyword savgol_filter_window_order: used for window smoothing
   :keyword voltage_fwhm: used for setting the post-processing
                          gaussian sigma, defaults to 0.01
   :kwtype voltage_fwhm: float
   :keyword gaussian_order: defaults to 0
   :kwtype gaussian_order: int
   :keyword gaussian_mode: defaults to "reflect"
   :kwtype gaussian_mode: str
   :keyword gaussian_cval: defaults to 0.0
   :kwtype gaussian_cval: float
   :keyword gaussian_truncate: defaults to 4.0
   :kwtype gaussian_truncate: float

   .. rubric:: Example

   >>> from cellpy.utils import ica
   >>> charge_df, dcharge_df = ica.ica_frames(my_cell, split=True)
   >>> charge_df.plot(x=("voltage", "v"))


.. py:function:: index_bounds(x)

   Returns tuple with first and last item.


.. py:function:: value_bounds(x)

   Returns tuple with min and max in x.


