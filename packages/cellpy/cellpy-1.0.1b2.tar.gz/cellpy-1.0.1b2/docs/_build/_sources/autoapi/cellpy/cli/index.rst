:py:mod:`cellpy.cli`
====================

.. py:module:: cellpy.cli


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.cli.cli
   cellpy.cli.dump_env_file
   cellpy.cli.echo_missing_modules
   cellpy.cli.edit
   cellpy.cli.get_default_config_file_path
   cellpy.cli.get_dst_file
   cellpy.cli.get_package_prm_dir
   cellpy.cli.info
   cellpy.cli.new
   cellpy.cli.pull
   cellpy.cli.run
   cellpy.cli.save_prm_file
   cellpy.cli.serve
   cellpy.cli.setup



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.cli.DEFAULT_EDITOR
   cellpy.cli.DIFFICULT_MISSING_MODULES
   cellpy.cli.EDITORS
   cellpy.cli.GITHUB_PWD_VAR_NAME
   cellpy.cli.REPO
   cellpy.cli.USER
   cellpy.cli.VERSION


.. py:function:: cli()

   cellpy - command line interface.


.. py:function:: dump_env_file(env_filename)

   saves (writes) the env to file


.. py:function:: echo_missing_modules()

   prints out the missing modules


.. py:function:: edit(name, default_editor, debug, silent)

   Edit your cellpy config or database files.

   You can use this to edit the configuration file, the database file, or the
   environment file. If you do not specify which file to edit, the configuration
   file will be opened.

   .. rubric:: Examples

   edit your cellpy configuration file

       cellpy edit config

   or just

       cellpy edit

   edit your cellpy database file

       cellpy edit db

   edit your cellpy environment file using notepad.exe (on Windows)

       cellpy edit env -e notepad.exe


.. py:function:: get_default_config_file_path(init_filename=None)

   gets the path to the default config-file


.. py:function:: get_dst_file(user_dir, init_filename)

   gets the destination path for the config-file


.. py:function:: get_package_prm_dir()

   gets the folder where the cellpy package lives


.. py:function:: info(version, configloc, params, check)

   This will give you some valuable information about your cellpy.


.. py:function:: new(template, directory, project, experiment, local_user_template, serve_, run_, lab, jupyter_executable, list_)

   Set up a batch experiment (might need git installed).


.. py:function:: pull(tests, examples, clone, directory, password)

   Download examples or tests from the big internet (needs git).


.. py:function:: run(journal, key, folder, cellpy_project, debug, silent, raw, cellpyfile, minimal, nom_cap, batch_col, project, list_, name)

   Run a cellpy process (for example a batch-job).

   You can use this to launch specific applications.

   .. rubric:: Examples

   run a batch job described in a journal file

      cellpy run -j my_experiment.json


.. py:function:: save_prm_file(prm_filename)

   saves (writes) the prms to file


.. py:function:: serve(lab, directory, executable)

   Start a Jupyter server.


.. py:function:: setup(interactive, not_relative, dry_run, reset, root_dir, folder_name, test_user, silent, no_deps)

   This will help you to set up cellpy.


.. py:data:: DEFAULT_EDITOR
   :value: 'vim'

   

.. py:data:: DIFFICULT_MISSING_MODULES

   

.. py:data:: EDITORS

   

.. py:data:: GITHUB_PWD_VAR_NAME
   :value: 'GD_PWD'

   

.. py:data:: REPO
   :value: 'jepegit/cellpy'

   

.. py:data:: USER
   :value: 'jepegit'

   

.. py:data:: VERSION

   

