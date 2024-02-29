:py:mod:`cellpy.readers.filefinder`
===================================

.. py:module:: cellpy.readers.filefinder


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.readers.filefinder.find_in_raw_file_directory
   cellpy.readers.filefinder.list_raw_file_directory
   cellpy.readers.filefinder.search_for_files



.. py:function:: find_in_raw_file_directory(raw_file_dir: Union[cellpy.internals.core.OtherPath, pathlib.Path, str, None] = None, project_dir: Union[cellpy.internals.core.OtherPath, pathlib.Path, str, None] = None, extension: Optional[str] = None, glob_txt: Optional[str] = None)

   Dumps the raw-file directory to a list.

   :param raw_file_dir: optional, directory where to look for run-files
                        (default: read prm-file)
   :type raw_file_dir: path
   :param project_dir: optional, subdirectory in raw_file_dir to look for run-files
   :type project_dir: path
   :param extension: optional, extension of run-files (without the '.'). If
                     not given, all files will be listed.
   :type extension: str
   :param glob_txt: optional, glob pattern to use when searching for files.
   :type glob_txt: str, optional

   :returns: list of file paths.
   :rtype: list of str

   .. rubric:: Examples

   # find all files in your raw-file directory:
   >>> filelist_1 = filefinder.find_in_raw_file_directory()

   # find all files in your raw-file directory in the subdirectory 'MY-PROJECT':
   >>> filelist_2 = filefinder.find_in_raw_file_directory(raw_file_dir=rawdatadir/"MY-PROJECT")

   # find all files in your raw-file directory with the extension '.raw' in the subdirectory 'MY-PROJECT':
   >>> filelist_3 = filefinder.find_in_raw_file_directory(raw_file_dir=rawdatadir/"MY-PROJECT", extension="raw")

   # find all files in your raw-file directory with the extension '.raw' in the subdirectory 'MY-PROJECT'
   # that contains the string 'good' in the file name:
   >>> filelist_4 = filefinder.find_in_raw_file_directory(
   >>>     raw_file_dir=rawdatadir/"MY-PROJECT",
   >>>     glob_txt="*good*",
   >>>     extension="raw"
   >>>)

   .. rubric:: Notes

   Uses 'find' and 'ssh' to search for files.


.. py:function:: list_raw_file_directory(raw_file_dir: Union[cellpy.internals.core.OtherPath, pathlib.Path, str, None] = None, project_dir: Union[cellpy.internals.core.OtherPath, pathlib.Path, str, None] = None, extension: Optional[str] = None, levels: Optional[int] = 1, only_filename: Optional[bool] = False, with_prefix: Optional[bool] = True)

   Dumps the raw-file directory to a list.

   :param raw_file_dir: optional, directory where to look for run-files
                        (default: read prm-file)
   :type raw_file_dir: path
   :param project_dir: optional, subdirectory in raw_file_dir to look for run-files
   :type project_dir: path
   :param extension: optional, extension of run-files (without the '.'). If
                     not given, all files will be listed.
   :type extension: str
   :param levels: How many sublevels to list. Defaults to 1.
                  If you want to list all sublevels, use `listdir(levels=-1)`.
                  If you want to list only the current level (no subdirectories),
                  use `listdir(levels=0)`.
   :type levels: int, optional
   :param only_filename: If True, only the file names will be
                         returned. Defaults to False.
   :type only_filename: bool, optional
   :param with_prefix: If True, the full path to the files including
                       the prefix and the location (e.g. 'scp://user@server.com/...')
                       will be returned. Defaults to True.
   :type with_prefix: bool, optional

   :returns: list of file paths (only the actual file names).
   :rtype: list of str

   .. rubric:: Notes

   This function might be rather slow and memory consuming if you have
   a lot of files in your raw-file directory. If you have a lot of files,
   you might want to consider running this function in a separate process
   (e.g. in a separate python script or using multiprocessing).

   The function currently returns the full path to the files from the
   root directory. It does not include the prefix (e.g. ssh://).
   Future versions might change this to either include the prefix or
   return the files relative to the ``raw_file_dir`` directory.


.. py:function:: search_for_files(run_name: str, raw_extension: Optional[str] = None, cellpy_file_extension: Optional[str] = None, raw_file_dir: Union[cellpy.internals.core.OtherPath, pathlib.Path, str, None] = None, project_dir: Union[cellpy.internals.core.OtherPath, pathlib.Path, str, None] = None, cellpy_file_dir: Union[cellpy.internals.core.OtherPath, pathlib.Path, str, None] = None, prm_filename: Union[pathlib.Path, str, None] = None, file_name_format: Optional[str] = None, reg_exp: Optional[str] = None, sub_folders: Optional[bool] = True, file_list: Optional[List[str]] = None, with_prefix: Optional[bool] = True, pre_path: Union[cellpy.internals.core.OtherPath, pathlib.Path, str, None] = None) -> Tuple[List[str], str]

   Searches for files (raw-data files and cellpy-files).


   :param run_name: run-file identification.
   :type run_name: str
   :param raw_extension: optional, extension of run-files (without the '.').
   :type raw_extension: str
   :param cellpy_file_extension: optional, extension for cellpy files
                                 (without the '.').
   :type cellpy_file_extension: str
   :param raw_file_dir: optional, directory where to look for run-files
                        (default: read prm-file)
   :type raw_file_dir: path
   :param project_dir: optional, subdirectory in raw_file_dir to look for run-files
   :type project_dir: path
   :param cellpy_file_dir: optional, directory where to look for
                           cellpy-files (default: read prm-file)
   :type cellpy_file_dir: path
   :param prm_filename: optional parameter file can be given.
   :type prm_filename: path
   :param file_name_format: format of raw-file names or a glob pattern
                            (default: YYYYMMDD_[name]EEE_CC_TT_RR).
   :type file_name_format: str
   :param reg_exp: use regular expression instead (defaults to None).
   :type reg_exp: str
   :param sub_folders: perform search also in sub-folders.
   :type sub_folders: bool
   :param file_list: perform the search within a given list
                     of filenames instead of searching the folder(s). The list should
                     not contain the full filepath (only the actual file names). If
                     you want to provide the full path, you will have to modify the
                     file_name_format or reg_exp accordingly.
   :type file_list: list of str
   :param with_prefix: if True, the file list contains full paths to the
                       files (including the prefix and the location).
   :type with_prefix: bool
   :param pre_path: path to prepend the list of files selected
                    from the file_list.
   :type pre_path: path or str

   :returns: run-file names (list of strings) and cellpy-file-name (str of full path).


