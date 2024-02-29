:py:mod:`cellpy.exceptions`
===========================

.. py:module:: cellpy.exceptions

.. autoapi-nested-parse::

   Exceptions defined within cellpy



Module Contents
---------------

.. py:exception:: ConfigFileNotRead


   Bases: :py:obj:`Error`

   .. autoapi-inheritance-diagram:: cellpy.exceptions.ConfigFileNotRead
      :parts: 1

   Raised when the configuration file cannot be read

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: ConfigFileNotWritten


   Bases: :py:obj:`Error`

   .. autoapi-inheritance-diagram:: cellpy.exceptions.ConfigFileNotWritten
      :parts: 1

   Raised when the configuration file cannot be written

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: DeprecatedFeature


   Bases: :py:obj:`Error`

   .. autoapi-inheritance-diagram:: cellpy.exceptions.DeprecatedFeature
      :parts: 1

   Raised when the feature is recently deprecated

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: Error


   Bases: :py:obj:`Exception`

   .. autoapi-inheritance-diagram:: cellpy.exceptions.Error
      :parts: 1

   Base class for other exceptions

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: ExportFailed


   Bases: :py:obj:`Error`

   .. autoapi-inheritance-diagram:: cellpy.exceptions.ExportFailed
      :parts: 1

   Raised when exporting data failed

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: FileNotFound


   Bases: :py:obj:`Error`

   .. autoapi-inheritance-diagram:: cellpy.exceptions.FileNotFound
      :parts: 1

   Raised when the given file is not found

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: IOError


   Bases: :py:obj:`Error`

   .. autoapi-inheritance-diagram:: cellpy.exceptions.IOError
      :parts: 1

   Raised when exporting data failed

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: NoDataFound


   Bases: :py:obj:`Error`

   .. autoapi-inheritance-diagram:: cellpy.exceptions.NoDataFound
      :parts: 1

   Raised when there are no cells, but a data is needed.

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: NullData


   Bases: :py:obj:`Error`

   .. autoapi-inheritance-diagram:: cellpy.exceptions.NullData
      :parts: 1

   Raised when required data is missing (e.g. voltage = None or summary_frames are missing)

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: UnderDefined


   Bases: :py:obj:`Error`

   .. autoapi-inheritance-diagram:: cellpy.exceptions.UnderDefined
      :parts: 1

   Raised when trying something that requires you to set
   a missing prm on environment variable first

   Initialize self.  See help(type(self)) for accurate signature.


.. py:exception:: WrongFileVersion


   Bases: :py:obj:`Error`

   .. autoapi-inheritance-diagram:: cellpy.exceptions.WrongFileVersion
      :parts: 1

   Raised when the file version is wrong

   Initialize self.  See help(type(self)) for accurate signature.


