:py:mod:`cellpy.internals.core`
===============================

.. py:module:: cellpy.internals.core

.. autoapi-nested-parse::

   This module contains div classes etc that are not really connected to cellpy.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.internals.core.ExternalStatResult
   cellpy.internals.core.OtherPath




Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.internals.core.ENV_VAR_CELLPY_KEY_FILENAME
   cellpy.internals.core.ENV_VAR_CELLPY_PASSWORD
   cellpy.internals.core.IMPLEMENTED_PROTOCOLS
   cellpy.internals.core.S
   cellpy.internals.core.URI_PREFIXES


.. py:class:: ExternalStatResult


   Mock of os.stat_result.

   .. py:attribute:: st_atime
      :type: int
      :value: 0

      

   .. py:attribute:: st_ctime
      :type: Optional[int]

      

   .. py:attribute:: st_mtime
      :type: int
      :value: 0

      

   .. py:attribute:: st_size
      :type: int
      :value: 0

      


.. py:class:: OtherPath(*args, **kwargs)


   Bases: :py:obj:`pathlib.Path`

   .. autoapi-inheritance-diagram:: cellpy.internals.core.OtherPath
      :parts: 1

   A pathlib.Path subclass that can handle external paths.

   .. attribute:: is_external

      is True if the path is external.

      :type: bool

   .. attribute:: location

      the location of the external path (e.g. a server name).

      :type: str

   .. attribute:: uri_prefix

      the prefix of the external path (e.g. scp:// or sftp://).

      :type: str

   .. attribute:: raw_path

      the path without any uri_prefix or location.

      :type: str

   .. attribute:: original

      the original path string.

      :type: str

   .. attribute:: full_path

      the full path (including uri_prefix and location).

      :type: str

   .. method:: copy (method)

      a method for copying the file to a local path.

   .. method:: glob (method)

      a method for globbing external paths if ``is_external`` is True.

   .. method:: rglob (method)

      a method for 'recursive' globbing external paths (max one extra level deep) if ``is_external`` is True.
      

   Construct a PurePath from one or several strings and or existing
   PurePath objects.  The strings and path objects are combined so as
   to yield a canonicalized path, which is incorporated into the
   new PurePath object.

   .. py:property:: full_path
      :type: str


   .. py:property:: is_external
      :type: bool


   .. py:property:: location
      :type: str

      Return the location of the external path (e.g ``user@server.com``).

   .. py:property:: name

      Return the parent directory of the path.

   .. py:property:: original
      :type: str


   .. py:property:: owner

      Return the login name of the file owner.

   .. py:property:: parent
      :type: S

      Return the parent directory of the path.

   .. py:property:: parents

      A sequence of this path's logical parents.

   .. py:property:: pathlike_location
      :type: S

      Return the location of the external path as a pathlike object.

   .. py:property:: raw_path
      :type: str


   .. py:property:: stem
      :type: str

      Return the stem of the path.

   .. py:property:: suffix
      :type: str

      Return the suffix of the path.

   .. py:property:: suffixes
      :type: List[str]

      Return the suffixes of the path.

   .. py:property:: uri_prefix
      :type: str

      Return the uri prefix for the external path (e.g ``ssh://``).

   .. py:method:: absolute() -> S

      Return an absolute version of this path by prepending the current
      working directory. No normalization or symlink resolution is performed.

      Use resolve() to get the canonical path to a file.


   .. py:method:: as_uri() -> str

      Return the path as a uri (e.g. ``scp://user@server.com/home/data/my_file.txt``).


   .. py:method:: connection_info(testing: bool = False) -> Tuple[Dict, str]

      Return a dictionary with connection information.


   .. py:method:: copy(destination: Optional[pathlib.Path] = None, testing=False) -> pathlib.Path

      Copy the file to a destination.


   .. py:method:: cwd()

      Return a new path pointing to the current working directory
      (as returned by os.getcwd()).


   .. py:method:: exists(*args, **kwargs) -> bool

      Check if path exists.


   .. py:method:: glob(glob_str: str, *args, **kwargs) -> Generator

      Iterate over this subtree and yield all existing files (of any
      kind, including directories) matching the given relative pattern.


   .. py:method:: group()

      Return the group name of the file gid.


   .. py:method:: is_dir(*args, **kwargs) -> bool

      Check if path is a directory.


   .. py:method:: is_file(*args, **kwargs) -> bool

      Check if path is a file.


   .. py:method:: iterdir(*args, **kwargs)

      Iterate over the files in this directory.  Does not yield any
      result for the special paths '.' and '..'.


   .. py:method:: joinpath(*args, **kwargs)

      Combine this path with one or several arguments, and return a
      new path representing either a subpath (if all arguments are relative
      paths) or a totally different path (if one of the arguments is
      anchored).


   .. py:method:: lchmod(*args, **kwargs)

      Like chmod(), except if the path points to a symlink, the symlink's
      permissions are changed, rather than its target's.


   .. py:method:: listdir(levels: int = 1, **kwargs) -> Generator

      List the contents of the directory.

      :param levels: How many sublevels to list:

                     - If you want to list all sublevels, use ``listdir(levels=-1)``.
                     - If you want to list only the current level (no subdirectories),
                       use ``listdir(levels=0)``.
      :type levels: int, optional

      :returns: Generator of ``OtherPath`` objects.
      :rtype: Generator


   .. py:method:: match(*args, **kwargs)

      Return True if this path matches the given pattern.


   .. py:method:: readlink(*args, **kwargs)

      Return the path to which the symbolic link points.


   .. py:method:: resolve(*args, **kwargs) -> S

      Resolve the path.


   .. py:method:: rglob(glob_str: str, *args, **kwargs) -> Generator

      Recursively yield all existing files (of any kind, including
      directories) matching the given relative pattern, anywhere in
      this subtree.


   .. py:method:: samefile(other_path: Union[str, pathlib.Path, S]) -> bool

      Return whether other_path is the same or not as this file
      (as returned by os.path.samefile()).


   .. py:method:: stat(*args, **kwargs)

      Return the result of the stat() system call on this path, like
      os.stat() does.


   .. py:method:: with_name(name: str) -> S

      Return a new path with the name changed.


   .. py:method:: with_stem(stem: str) -> S

      Return a new path with the stem changed.


   .. py:method:: with_suffix(suffix: str) -> S

      Return a new path with the suffix changed.



.. py:data:: ENV_VAR_CELLPY_KEY_FILENAME
   :value: 'CELLPY_KEY_FILENAME'

   

.. py:data:: ENV_VAR_CELLPY_PASSWORD
   :value: 'CELLPY_PASSWORD'

   

.. py:data:: IMPLEMENTED_PROTOCOLS
   :value: ['ssh:', 'sftp:', 'scp:']

   

.. py:data:: S

   

.. py:data:: URI_PREFIXES
   :value: ['ssh:', 'sftp:', 'scp:', 'http:', 'https:', 'ftp:', 'ftps:', 'smb:']

   

