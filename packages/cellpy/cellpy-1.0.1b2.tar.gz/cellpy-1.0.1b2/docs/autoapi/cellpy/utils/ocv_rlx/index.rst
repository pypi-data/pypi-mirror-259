:py:mod:`cellpy.utils.ocv_rlx`
==============================

.. py:module:: cellpy.utils.ocv_rlx


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.ocv_rlx.MultiCycleOcvFit
   cellpy.utils.ocv_rlx.OcvFit



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.ocv_rlx.fit
   cellpy.utils.ocv_rlx.select_ocv_points



.. py:class:: MultiCycleOcvFit(cellpydata, cycles, circuits=3)


   Object for performing fitting of multiple cycles.

   Remarks:
       This is only tested for OCV relaxation data for half-cells in anode mode
       where the OCV relaxation is performed according to the standard protocol
       implemented at IFE in the battery development group.

       If you want to use this for other data or protocols, please report an issue
       on the GitHub page.


   Object for performing fitting of multiple cycles.

   :param cellpydata: ``CellpyCell-object``
   :param cycles: cycles to fit.
   :type cycles: list
   :param circuits: number of circuits to use in fitting.
   :type circuits: int

   .. py:property:: cycles


   .. py:method:: create_colormap(name='plasma', cycles=None)
      :staticmethod:


   .. py:method:: find_zero(cycle, direction)


   .. py:method:: get_best_fit_data()

      Returns the best fit data.


   .. py:method:: get_best_fit_parameters() -> list

      Returns parameters for the best fit.


   .. py:method:: get_best_fit_parameters_grouped() -> dict

      Returns a dictionary of the best fit.


   .. py:method:: get_best_fit_parameters_translated() -> list

      Returns the parameters in 'real units' for the best fit.


   .. py:method:: get_best_fit_parameters_translated_grouped() -> dict

      Returns the parameters as a dictionary of the 'real units'
      for the best fit.


   .. py:method:: get_fit_cycles()

      Returns a list of the fit cycles


   .. py:method:: plot_summary(cycles=None)

      Convenience function for plotting the summary of the fit


   .. py:method:: plot_summary_translated()

      Convenience function for plotting the summary of the
      fit (translated)


   .. py:method:: run_fitting(direction='up', weighted=True)

      :param direction: what type of ocv relaxation to fit
      :type direction: 'up' | 'down'
      :param weighted: use weighted fitting.
      :type weighted: bool

      :returns: None


   .. py:method:: set_cycles(cycles)

      Sets the cycles.


   .. py:method:: set_data(cellpydata)

      Sets the CellpyCell.


   .. py:method:: summary_translated() -> pandas.DataFrame

      Convenience function for creating a dataframe of the summary of the
      fit (translated)



.. py:class:: OcvFit(circuits=None, direction=None, zero_current=0.1, zero_voltage=0.05)


   Bases: :py:obj:`object`

   Class for fitting open circuit relaxation data.

   The model is a sum of exponentials and a constant offset (Ohmic resistance).
   The number of exponentials is set by the number of circuits.
   The model is:
       v(t) = v0 + R0 + sum(wi * exp(-t/tau_i))
       where v0 is the OCV, wi is the weight of the exponential tau_i is the
       time constant of the exponential and R0 is the Ohmic resistance.

       r is found by calculating v0 / i_start --> err(r)= err(v0) + err(i_start).
       c is found from using tau / r --> err(c) = err(r) + err(tau).

   The fit is performed by using lmfit.

   .. attribute:: data

      The data to be fitted.

      :type: cellpydata-object

   .. attribute:: time

      Time measured during relaxation (extracted from data if provided).

      :type: list

   .. attribute:: voltage

      Time measured during relaxation (extracted from data if provided).

      :type: list

   .. attribute:: steps

      Step information (if data is provided).

      :type: str

   .. attribute:: circuits

      The number of circuits to be fitted.

      :type: int

   .. attribute:: weights

      The weights of the different circuits.

      :type: list

   .. attribute:: zero_current

      Last current observed before turning the current off.

      :type: float

   .. attribute:: zero_voltage

      Last voltage observed before turning the current off.

      :type: float

   .. attribute:: model

      The model used for fitting.

      :type: lmfit-object

   .. attribute:: params

      The parameters used for fitting.

      :type: lmfit-object

   .. attribute:: result

      The result of the fitting.

      :type: lmfit-object

   .. attribute:: best_fit_data

      The best fit data [x, y_measured, y_fitted].

      :type: list

   .. attribute:: best_fit_parameters

      The best fit parameters.

      :type: dict

   Remarks:
       This class does not take advantage of the cellpydata-object. It is
       primarily used for fitting data that does not originate from cellpy,
       but it can also be used for fitting cellpy-data.

       If you have cellpy-data, you should use the MultiCycleOcvFit class instead.


   Initializes the class.

   :param circuits: The number of circuits to be fitted (including R0).
   :type circuits: int
   :param direction: The direction of the relaxation (up or down).
   :type direction: str
   :param zero_current: Last current observed before turning the current off.
   :type zero_current: float
   :param zero_voltage: Last voltage observed before turning the current off.
   :type zero_voltage: float

   .. py:method:: create_model()

      Create the model to be used in the fit.


   .. py:method:: fit_model()


   .. py:method:: get_best_fit_data()


   .. py:method:: get_best_fit_parameters()


   .. py:method:: get_best_fit_parameters_translated()


   .. py:method:: get_result()


   .. py:method:: reset_weights()


   .. py:method:: run_fit()

      Performing fit of the OCV steps in the cycles set by set_cycles()
      from the data set by set_data()

      r is found by calculating v0 / i_start --> err(r)= err(v0) + err(i_start).

      c is found from using tau / r --> err(c) = err(r) + err(tau).

      The resulting best fit parameters are stored in self.result for the given cycles.

      :returns: None


   .. py:method:: set_cellpydata(cellpydata, cycle)

      Convenience method for setting the data from a cellpydata-object.
      :param cellpydata: data object from cellreader
      :type cellpydata: CellpyCell
      :param cycle: cycle number to get from CellpyCell object
      :type cycle: int

      Remarks:
          You need to set the direction before calling this method if you
          don't want to use the default direction (up).

      :returns: None


   .. py:method:: set_circuits(circuits)

      Set the number of circuits to be used in the fit.

      :param circuits: number of circuits to be used in the fit. Can be 1 to 4.
      :type circuits: int


   .. py:method:: set_data(t, v)

      Set the data to be fitted.


   .. py:method:: set_weights(weights)


   .. py:method:: set_weights_power_law(prefactor=1, power=-2, zero_level=1)


   .. py:method:: set_zero_current(zero_current)


   .. py:method:: set_zero_voltage(zero_voltage)



.. py:function:: fit(c, direction='up', circuits=3, cycles=None, return_fit_object=False)

   Fits the OCV steps in CellpyCell object c.

   :param c: CellpyCell object
   :param direction: direction of the OCV steps ('up' or 'down')
   :param circuits: number of circuits to use (first is IR, rest is RC) in the fitting (min=1, max=4)
   :param cycles: list of cycles to fit (if None, all cycles will be used)
   :param return_fit_object: if True, returns the MultiCycleOcvFit instance.

   :returns: pd.DataFrame with the fitted parameters for each cycle if return_fit_object=False,
             else MultiCycleOcvFit instance


.. py:function:: select_ocv_points(cellpydata, cycles=None, cell_label=None, include_times=True, selection_method='martin', number_of_points=5, interval=10, relative_voltage=False, report_times=False, direction='both')

   Select points from the ocvrlx steps.

   :param cellpydata: ``CellpyData-object``
   :param cycles: list of cycle numbers to process (optional)
   :param cell_label: optional, will be added to the frame if given
   :type cell_label: str
   :param include_times: include additional information including times.
   :type include_times: bool
   :param selection_method: criteria for selecting points ('martin': select first and last, and
                            then last/2, last/2/2 etc. until you have reached the wanted number of points; 'fixed_times': select first,
                            and then same interval between each subsequent point).
   :type selection_method: 'martin' | 'fixed_times'
   :param number_of_points: number of points you want.
   :param interval: interval between each point (in use only for methods
                    where interval makes sense). If it is a list, then
                    number_of_points will be calculated as len(interval) + 1 (and
                    override the set number_of_points).
   :param relative_voltage: set to True if you would like the voltage to be
                            relative to the voltage before starting the ocv rlx step.
                            Defaults to False. Remark that for the initial rxl step (when
                            you just have put your cell on the tester) does not have any
                            prior voltage. The relative voltage will then be versus the
                            first measurement point.
   :param report_times: also report the ocv rlx total time if True (defaults
                        to False)
   :param direction: select "up" if you would like
                     to process only the ocv rlx steps where the voltage is relaxing
                     upwards and vice versa. Defaults to "both".
   :type direction: "up", "down" or "both"

   :returns: ``pandas.DataFrame`` (and another ``pandas.DataFrame`` if return_times is True)


