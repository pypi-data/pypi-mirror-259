:py:mod:`cellpy.utils.batch_tools.batch_helpers`
================================================

.. py:module:: cellpy.utils.batch_tools.batch_helpers


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_helpers.create_factory
   cellpy.utils.batch_tools.batch_helpers.create_folder_structure
   cellpy.utils.batch_tools.batch_helpers.create_labels
   cellpy.utils.batch_tools.batch_helpers.create_selected_summaries_dict
   cellpy.utils.batch_tools.batch_helpers.export_dqdv
   cellpy.utils.batch_tools.batch_helpers.find_files
   cellpy.utils.batch_tools.batch_helpers.fix_groups
   cellpy.utils.batch_tools.batch_helpers.generate_folder_names
   cellpy.utils.batch_tools.batch_helpers.join_summaries
   cellpy.utils.batch_tools.batch_helpers.look_up_and_get
   cellpy.utils.batch_tools.batch_helpers.make_unique_groups
   cellpy.utils.batch_tools.batch_helpers.pick_summary_data
   cellpy.utils.batch_tools.batch_helpers.save_multi



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.utils.batch_tools.batch_helpers.CELL_TYPE_IDS
   cellpy.utils.batch_tools.batch_helpers.hdr_journal
   cellpy.utils.batch_tools.batch_helpers.hdr_summary


.. py:function:: create_factory()


.. py:function:: create_folder_structure(project_name, batch_name)

   This function creates a folder structure for the batch project.

   The folder structure consists of main working folder ``project_name`
   located in the ``outdatadir`` (as defined in the cellpy configuration file)
   with a sub-folder named ``batch_name``. It also creates a folder
   inside the ``batch_name`` folder for storing the raw data.
   If the folders does not exist, they will be made. The function also returns
   the name of the info-df.

   :param project_name: name of the project
   :param batch_name: name of the batch

   Returns: (info_file, (project_dir, batch_dir, raw_dir))



.. py:function:: create_labels(label, *args)

   Returns a re-formatted label (currently it only removes the dates
   from the run-name)


.. py:function:: create_selected_summaries_dict(summaries_list)

   Creates a dictionary with summary column headers.

   .. rubric:: Examples

   >>> summaries_to_output = ["discharge_capacity_gravimetric", "charge_capacity_gravimetric"]
   >>> summaries_to_output_dict = create_selected_summaries_dict(
   >>>    summaries_to_output
   >>> )
   >>> print(summaries_to_output_dict)
   {'discharge_capacity_gravimetric': "discharge_capacity_gravimetric",
          'charge_capacity_gravimetric': "discharge_capacity_gravimetric"}

   :param summaries_list: list containing cellpy summary column id names

   Returns: dictionary of the form {cellpy id name: cellpy summary
       header name,}



.. py:function:: export_dqdv(cell_data, savedir, sep, last_cycle=None)

   Exports dQ/dV data from a CellpyCell instance.

   :param cell_data: CellpyCell instance
   :param savedir: path to the folder where the files should be saved
   :param sep: separator for the .csv-files.
   :param last_cycle: only export up to this cycle (if not None)


.. py:function:: find_files(info_dict, file_list=None, pre_path=None, sub_folders=None, **kwargs)

   Find files using cellpy.filefinder.

   :param info_dict: journal pages.
   :param file_list: list of files names to search through.
   :param pre_path: path to prepend found files from file_list (if file_list is given).
   :param sub_folders: perform search also in sub-folders.
   :type sub_folders: bool

   **kwargs (filefinder.search_for_files):
       run_name(str): run-file identification.
       raw_extension(str): optional, extension of run-files (without the '.').
       cellpy_file_extension(str): optional, extension for cellpy files
           (without the '.').
       raw_file_dir(path): optional, directory where to look for run-files
           (default: read prm-file)
       cellpy_file_dir(path): optional, directory where to look for
           cellpy-files (default: read prm-file)
       prm_filename(path): optional parameter file can be given.
       file_name_format(str): format of raw-file names or a glob pattern
           (default: YYYYMMDD_[name]EEE_CC_TT_RR).
       reg_exp(str): use regular expression instead (defaults to None).
       file_list (list of str): perform the search within a given list
           of filenames instead of searching the folder(s). The list should
           not contain the full filepath (only the actual file names). If
           you want to provide the full path, you will have to modify the
           file_name_format or reg_exp accordingly.
       pre_path (path or str): path to prepend the list of files selected
            from the file_list.

   :returns: info_dict


.. py:function:: fix_groups(groups)

   Takes care of strange group numbers.


.. py:function:: generate_folder_names(name, project)

   Creates sensible folder names.


.. py:function:: join_summaries(summary_frames, selected_summaries, keep_old_header=False)

   parse the summaries and combine based on column (selected_summaries)


.. py:function:: look_up_and_get(cellpy_file_name, table_name, root=None, max_cycle=None)

   Extracts table from cellpy hdf5-file.


.. py:function:: make_unique_groups(info_df)

   This function cleans up the group numbers a bit.


.. py:function:: pick_summary_data(key, summary_df, selected_summaries)

   picks the selected pandas.DataFrame


.. py:function:: save_multi(data, file_name, sep=';')

   Convenience function for storing data column-wise in a csv-file.


.. py:data:: CELL_TYPE_IDS
   :value: ['cc', 'ec', 'eth']

   

.. py:data:: hdr_journal

   

.. py:data:: hdr_summary

   

