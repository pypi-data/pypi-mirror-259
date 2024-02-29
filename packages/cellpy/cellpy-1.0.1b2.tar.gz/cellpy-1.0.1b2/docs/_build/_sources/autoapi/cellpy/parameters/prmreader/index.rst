:py:mod:`cellpy.parameters.prmreader`
=====================================

.. py:module:: cellpy.parameters.prmreader


Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.parameters.prmreader.create_custom_init_filename
   cellpy.parameters.prmreader.get_env_file_name
   cellpy.parameters.prmreader.get_user_dir
   cellpy.parameters.prmreader.get_user_dir_and_dst
   cellpy.parameters.prmreader.get_user_name
   cellpy.parameters.prmreader.info
   cellpy.parameters.prmreader.initialize



Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.parameters.prmreader.DEFAULT_FILENAME
   cellpy.parameters.prmreader.DEFAULT_FILENAME_END
   cellpy.parameters.prmreader.DEFAULT_FILENAME_START
   cellpy.parameters.prmreader.ENVIRONMENT_EXAMPLE
   cellpy.parameters.prmreader.USE_MY_DOCUMENTS
   cellpy.parameters.prmreader.yaml


.. py:function:: create_custom_init_filename(user_name=None)

   Creates a custom prms filename


.. py:function:: get_env_file_name()

   Returns the location of the env-file


.. py:function:: get_user_dir()

   Gets the name of the user directory


.. py:function:: get_user_dir_and_dst(init_filename=None)

   Gets the name of the user directory and full prm filepath


.. py:function:: get_user_name()

   Get the username of the current user (cross-platform)


.. py:function:: info()

   This function will show only the 'box'-type
   attributes and their content in the cellpy.prms module


.. py:function:: initialize()

   Initializes cellpy by reading the config file and the environment file


.. py:data:: DEFAULT_FILENAME

   

.. py:data:: DEFAULT_FILENAME_END
   :value: '.conf'

   

.. py:data:: DEFAULT_FILENAME_START
   :value: '.cellpy_prms_'

   

.. py:data:: ENVIRONMENT_EXAMPLE
   :value: Multiline-String

    .. raw:: html

        <details><summary>Show Value</summary>

    .. code-block:: python

        """
        # This is an example of an environment file for cellpy.
        # The environment file is used to set environment variables
        # that are used by cellpy.
        # The environment file should be located in the user directory
        # (i.e. the directory returned by pathlib.Path.home()).
        # The default environment file is named .env_cellpy, but you can
        # change this in your config file.
        # The environment file should contain the following variables:
        # CELLPY_PASSWORD=<password>
        # CELLPY_KEY_FILENAME=<key_filename>
        # CELLPY_HOST=<host>
        # CELLPY_USER=<user>
        """

    .. raw:: html

        </details>

   

.. py:data:: USE_MY_DOCUMENTS
   :value: False

   

.. py:data:: yaml

   

