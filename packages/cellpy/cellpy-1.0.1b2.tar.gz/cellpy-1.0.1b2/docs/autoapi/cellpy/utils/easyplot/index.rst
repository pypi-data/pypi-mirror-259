:py:mod:`cellpy.utils.easyplot`
===============================

.. py:module:: cellpy.utils.easyplot

.. autoapi-nested-parse::

   easyplot module for cellpy. It provides easy plotting of any cellpy-readable data using matplotlib.
   Author: Amund M. Raniseth
   Date: 01.07.2021



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.utils.easyplot.EasyPlot



Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.easyplot.get_effective_C_rates
   cellpy.utils.easyplot.get_effective_C_rates_and_caps
   cellpy.utils.easyplot.help
   cellpy.utils.easyplot.main



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.easyplot.USER_PARAMS
   cellpy.utils.easyplot.hdr_journal


.. py:class:: EasyPlot(files=None, nicknames=None, journal=None, **kwargs)


   Main easyplot class.
   Takes all the inputs from the user in its kwargs upon object initialization.
   Gathers data, handles and plots it when object.plot() is called.

   Help: type easyplot.help()

   Initialization function of the EasyPlot class.
   Input parameters:
   filenames (list of strings).
   nicknames (list of strings), must match length of filenames.
   journal (str or pathlib.Path object): journal file name (should not be used if files is given).
   any kwargs: use easyplot.help() to print all kwargs to terminal.

   Returns:
   easyplot object

   Most basic usage:
   ezpltobj = easyplot.EasyPlot(["name1", "name2"], None)

   .. py:method:: fill_input()

      Fill in the rest of the variables from self.user_params if the user didn't specify


   .. py:method:: fix_cap_from_rc(fig, ax, handles)

      Makes the finishing touches to the capacity vs inverse C-rate plot


   .. py:method:: fix_cyclelife(fig, ax)

      Makes the finishing touches to the cyclelife plot


   .. py:method:: fix_dqdv(fig, ax)

      Makes the finishing touches to the dQdV plot


   .. py:method:: fix_gc(fig, ax)

      Makes the finishing touches to the voltage-curves plot


   .. py:method:: fix_gc_and_dqdv(fig, axs)

      Makes the finishing touches to the dQdV / Voltage curves plot


   .. py:method:: give_color()

      Picks the first color from the color list and gives it away


   .. py:method:: give_fig()

      Gives figure to whoever asks and appends it to figure list


   .. py:method:: handle_outpath()

      Makes sure that self.outpath exists, or creates it.


   .. py:method:: plot()

      This is the method the user calls on his/hers easyplot object in order to gather the data and plot it.
      Usage: object.plot()


   .. py:method:: plot_cap_from_rc()

      Takes all the parameters inserted in the object creation and plots capacity VS inverse c-rate


   .. py:method:: plot_cyclelife()

      Takes all the parameters inserted in the object creation and plots cyclelife


   .. py:method:: plot_dQdV()

      Takes all the parameters inserted in the object creation and plots dQdV


   .. py:method:: plot_gc()

      Takes all the parameters inserted in the object creation and plots Voltage-Capacity curves


   .. py:method:: plot_gc_and_dQdV()

      Takes all the parameters inserted in the object creation and plots Voltage-Curves and dQdV data together


   .. py:method:: save_fig(fig, savepath)

      The point of this is to have savefig parameters the same across
      all plots (for now just fig dpi and bbox inches)


   .. py:method:: set_arbin_sql_credentials(server='localhost', uid='sa', pwd='Changeme123', driver='ODBC Driver 17 for SQL Server')

      Sets cellpy.prms.Instruments.Arbin details to fit what is inserted.
      Parameters: Server = 'IP of server', uid = 'username', pwd = 'password', driver = 'ODBC Driver 17 for SQL Server'


   .. py:method:: verify_input()

      Verifies that the users' input to the object is correct.



.. py:function:: get_effective_C_rates(steptable)


.. py:function:: get_effective_C_rates_and_caps(steptable)


.. py:function:: help()

   Method of the EasyPlot class which prints some helptext in addition to all supported params.


.. py:function:: main()


.. py:data:: USER_PARAMS

   

.. py:data:: hdr_journal

   

