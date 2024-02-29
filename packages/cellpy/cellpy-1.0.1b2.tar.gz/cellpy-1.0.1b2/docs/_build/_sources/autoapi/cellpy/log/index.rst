:py:mod:`cellpy.log`
====================

.. py:module:: cellpy.log

.. autoapi-nested-parse::

   Set up logger instance



Module Contents
---------------


Functions
~~~~~~~~~

.. autoapisummary::

   cellpy.log.setup_logging



.. py:function:: setup_logging(default_level=None, default_json_path=None, env_key='LOG_CFG', custom_log_dir=None, reset_big_log=False, max_size=5000000, testing=False)

   Setup logging configuration.

   :param default_level: default log-level to screen (std.out).
   :param default_json_path: path to config file for setting up logging.
   :param env_key: use this environment prm to try to get default_json_path.
   :type env_key: str
   :param custom_log_dir: path for saving logs.
   :param reset_big_log: reset log if too big (max_size).
   :type reset_big_log: bool
   :param max_size: if reset_log, this is the max limit.
   :type max_size: int
   :param testing: set as True if testing, and you don't want to create any .log files
   :type testing: bool


