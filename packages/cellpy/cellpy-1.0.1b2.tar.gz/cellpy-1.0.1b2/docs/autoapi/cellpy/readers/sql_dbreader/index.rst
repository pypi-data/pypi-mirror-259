:py:mod:`cellpy.readers.sql_dbreader`
=====================================

.. py:module:: cellpy.readers.sql_dbreader

.. autoapi-nested-parse::

   This module is an example of how to implement a custom database reader for the batch utility in cellpy.



Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   cellpy.readers.sql_dbreader.Base
   cellpy.readers.sql_dbreader.Batch
   cellpy.readers.sql_dbreader.Cell
   cellpy.readers.sql_dbreader.RawData
   cellpy.readers.sql_dbreader.SQLReader




Attributes
~~~~~~~~~~

.. autoapisummary::

   cellpy.readers.sql_dbreader.DB_FILE_EXCEL
   cellpy.readers.sql_dbreader.DB_FILE_SQLITE
   cellpy.readers.sql_dbreader.DB_URI
   cellpy.readers.sql_dbreader.HEADER_ROW
   cellpy.readers.sql_dbreader.TABLE_NAME_EXCEL
   cellpy.readers.sql_dbreader.UNIT_ROW
   cellpy.readers.sql_dbreader.batch_cell_association_table
   cellpy.readers.sql_dbreader.hdr_journal


.. py:class:: Base


   Bases: :py:obj:`sqlalchemy.orm.DeclarativeBase`

   .. autoapi-inheritance-diagram:: cellpy.readers.sql_dbreader.Base
      :parts: 1

   Base class used for declarative class definitions.

   The :class:`_orm.DeclarativeBase` allows for the creation of new
   declarative bases in such a way that is compatible with type checkers::


       from sqlalchemy.orm import DeclarativeBase

       class Base(DeclarativeBase):
           pass


   The above ``Base`` class is now usable as the base for new declarative
   mappings.  The superclass makes use of the ``__init_subclass__()``
   method to set up new classes and metaclasses aren't used.

   When first used, the :class:`_orm.DeclarativeBase` class instantiates a new
   :class:`_orm.registry` to be used with the base, assuming one was not
   provided explicitly. The :class:`_orm.DeclarativeBase` class supports
   class-level attributes which act as parameters for the construction of this
   registry; such as to indicate a specific :class:`_schema.MetaData`
   collection as well as a specific value for
   :paramref:`_orm.registry.type_annotation_map`::

       from typing_extensions import Annotated

       from sqlalchemy import BigInteger
       from sqlalchemy import MetaData
       from sqlalchemy import String
       from sqlalchemy.orm import DeclarativeBase

       bigint = Annotated[int, "bigint"]
       my_metadata = MetaData()

       class Base(DeclarativeBase):
           metadata = my_metadata
           type_annotation_map = {
               str: String().with_variant(String(255), "mysql", "mariadb"),
               bigint: BigInteger()
           }

   Class-level attributes which may be specified include:

   :param metadata: optional :class:`_schema.MetaData` collection.
    If a :class:`_orm.registry` is constructed automatically, this
    :class:`_schema.MetaData` collection will be used to construct it.
    Otherwise, the local :class:`_schema.MetaData` collection will supercede
    that used by an existing :class:`_orm.registry` passed using the
    :paramref:`_orm.DeclarativeBase.registry` parameter.
   :param type_annotation_map: optional type annotation map that will be
    passed to the :class:`_orm.registry` as
    :paramref:`_orm.registry.type_annotation_map`.
   :param registry: supply a pre-existing :class:`_orm.registry` directly.

   .. versionadded:: 2.0  Added :class:`.DeclarativeBase`, so that declarative
      base classes may be constructed in such a way that is also recognized
      by :pep:`484` type checkers.   As a result, :class:`.DeclarativeBase`
      and other subclassing-oriented APIs should be seen as
      superseding previous "class returned by a function" APIs, namely
      :func:`_orm.declarative_base` and :meth:`_orm.registry.generate_base`,
      where the base class returned cannot be recognized by type checkers
      without using plugins.

   **__init__ behavior**

   In a plain Python class, the base-most ``__init__()`` method in the class
   hierarchy is ``object.__init__()``, which accepts no arguments. However,
   when the :class:`_orm.DeclarativeBase` subclass is first declared, the
   class is given an ``__init__()`` method that links to the
   :paramref:`_orm.registry.constructor` constructor function, if no
   ``__init__()`` method is already present; this is the usual declarative
   constructor that will assign keyword arguments as attributes on the
   instance, assuming those attributes are established at the class level
   (i.e. are mapped, or are linked to a descriptor). This constructor is
   **never accessed by a mapped class without being called explicitly via
   super()**, as mapped classes are themselves given an ``__init__()`` method
   directly which calls :paramref:`_orm.registry.constructor`, so in the
   default case works independently of what the base-most ``__init__()``
   method does.

   .. versionchanged:: 2.0.1  :class:`_orm.DeclarativeBase` has a default
      constructor that links to :paramref:`_orm.registry.constructor` by
      default, so that calls to ``super().__init__()`` can access this
      constructor. Previously, due to an implementation mistake, this default
      constructor was missing, and calling ``super().__init__()`` would invoke
      ``object.__init__()``.

   The :class:`_orm.DeclarativeBase` subclass may also declare an explicit
   ``__init__()`` method which will replace the use of the
   :paramref:`_orm.registry.constructor` function at this level::

       class Base(DeclarativeBase):
           def __init__(self, id=None):
               self.id = id

   Mapped classes still will not invoke this constructor implicitly; it
   remains only accessible by calling ``super().__init__()``::

       class MyClass(Base):
           def __init__(self, id=None, name=None):
               self.name = name
               super().__init__(id=id)

   Note that this is a different behavior from what functions like the legacy
   :func:`_orm.declarative_base` would do; the base created by those functions
   would always install :paramref:`_orm.registry.constructor` for
   ``__init__()``.




.. py:class:: Batch


   Bases: :py:obj:`Base`

   .. autoapi-inheritance-diagram:: cellpy.readers.sql_dbreader.Batch
      :parts: 1

   Base class used for declarative class definitions.

   The :class:`_orm.DeclarativeBase` allows for the creation of new
   declarative bases in such a way that is compatible with type checkers::


       from sqlalchemy.orm import DeclarativeBase

       class Base(DeclarativeBase):
           pass


   The above ``Base`` class is now usable as the base for new declarative
   mappings.  The superclass makes use of the ``__init_subclass__()``
   method to set up new classes and metaclasses aren't used.

   When first used, the :class:`_orm.DeclarativeBase` class instantiates a new
   :class:`_orm.registry` to be used with the base, assuming one was not
   provided explicitly. The :class:`_orm.DeclarativeBase` class supports
   class-level attributes which act as parameters for the construction of this
   registry; such as to indicate a specific :class:`_schema.MetaData`
   collection as well as a specific value for
   :paramref:`_orm.registry.type_annotation_map`::

       from typing_extensions import Annotated

       from sqlalchemy import BigInteger
       from sqlalchemy import MetaData
       from sqlalchemy import String
       from sqlalchemy.orm import DeclarativeBase

       bigint = Annotated[int, "bigint"]
       my_metadata = MetaData()

       class Base(DeclarativeBase):
           metadata = my_metadata
           type_annotation_map = {
               str: String().with_variant(String(255), "mysql", "mariadb"),
               bigint: BigInteger()
           }

   Class-level attributes which may be specified include:

   :param metadata: optional :class:`_schema.MetaData` collection.
    If a :class:`_orm.registry` is constructed automatically, this
    :class:`_schema.MetaData` collection will be used to construct it.
    Otherwise, the local :class:`_schema.MetaData` collection will supercede
    that used by an existing :class:`_orm.registry` passed using the
    :paramref:`_orm.DeclarativeBase.registry` parameter.
   :param type_annotation_map: optional type annotation map that will be
    passed to the :class:`_orm.registry` as
    :paramref:`_orm.registry.type_annotation_map`.
   :param registry: supply a pre-existing :class:`_orm.registry` directly.

   .. versionadded:: 2.0  Added :class:`.DeclarativeBase`, so that declarative
      base classes may be constructed in such a way that is also recognized
      by :pep:`484` type checkers.   As a result, :class:`.DeclarativeBase`
      and other subclassing-oriented APIs should be seen as
      superseding previous "class returned by a function" APIs, namely
      :func:`_orm.declarative_base` and :meth:`_orm.registry.generate_base`,
      where the base class returned cannot be recognized by type checkers
      without using plugins.

   **__init__ behavior**

   In a plain Python class, the base-most ``__init__()`` method in the class
   hierarchy is ``object.__init__()``, which accepts no arguments. However,
   when the :class:`_orm.DeclarativeBase` subclass is first declared, the
   class is given an ``__init__()`` method that links to the
   :paramref:`_orm.registry.constructor` constructor function, if no
   ``__init__()`` method is already present; this is the usual declarative
   constructor that will assign keyword arguments as attributes on the
   instance, assuming those attributes are established at the class level
   (i.e. are mapped, or are linked to a descriptor). This constructor is
   **never accessed by a mapped class without being called explicitly via
   super()**, as mapped classes are themselves given an ``__init__()`` method
   directly which calls :paramref:`_orm.registry.constructor`, so in the
   default case works independently of what the base-most ``__init__()``
   method does.

   .. versionchanged:: 2.0.1  :class:`_orm.DeclarativeBase` has a default
      constructor that links to :paramref:`_orm.registry.constructor` by
      default, so that calls to ``super().__init__()`` can access this
      constructor. Previously, due to an implementation mistake, this default
      constructor was missing, and calling ``super().__init__()`` would invoke
      ``object.__init__()``.

   The :class:`_orm.DeclarativeBase` subclass may also declare an explicit
   ``__init__()`` method which will replace the use of the
   :paramref:`_orm.registry.constructor` function at this level::

       class Base(DeclarativeBase):
           def __init__(self, id=None):
               self.id = id

   Mapped classes still will not invoke this constructor implicitly; it
   remains only accessible by calling ``super().__init__()``::

       class MyClass(Base):
           def __init__(self, id=None, name=None):
               self.name = name
               super().__init__(id=id)

   Note that this is a different behavior from what functions like the legacy
   :func:`_orm.declarative_base` would do; the base created by those functions
   would always install :paramref:`_orm.registry.constructor` for
   ``__init__()``.



   .. py:attribute:: cells
      :type: sqlalchemy.orm.Mapped[List[Cell]]

      

   .. py:attribute:: comment
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: name
      :type: sqlalchemy.orm.Mapped[str]

      

   .. py:attribute:: pk
      :type: sqlalchemy.orm.Mapped[int]

      


.. py:class:: Cell


   Bases: :py:obj:`Base`

   .. autoapi-inheritance-diagram:: cellpy.readers.sql_dbreader.Cell
      :parts: 1

   Base class used for declarative class definitions.

   The :class:`_orm.DeclarativeBase` allows for the creation of new
   declarative bases in such a way that is compatible with type checkers::


       from sqlalchemy.orm import DeclarativeBase

       class Base(DeclarativeBase):
           pass


   The above ``Base`` class is now usable as the base for new declarative
   mappings.  The superclass makes use of the ``__init_subclass__()``
   method to set up new classes and metaclasses aren't used.

   When first used, the :class:`_orm.DeclarativeBase` class instantiates a new
   :class:`_orm.registry` to be used with the base, assuming one was not
   provided explicitly. The :class:`_orm.DeclarativeBase` class supports
   class-level attributes which act as parameters for the construction of this
   registry; such as to indicate a specific :class:`_schema.MetaData`
   collection as well as a specific value for
   :paramref:`_orm.registry.type_annotation_map`::

       from typing_extensions import Annotated

       from sqlalchemy import BigInteger
       from sqlalchemy import MetaData
       from sqlalchemy import String
       from sqlalchemy.orm import DeclarativeBase

       bigint = Annotated[int, "bigint"]
       my_metadata = MetaData()

       class Base(DeclarativeBase):
           metadata = my_metadata
           type_annotation_map = {
               str: String().with_variant(String(255), "mysql", "mariadb"),
               bigint: BigInteger()
           }

   Class-level attributes which may be specified include:

   :param metadata: optional :class:`_schema.MetaData` collection.
    If a :class:`_orm.registry` is constructed automatically, this
    :class:`_schema.MetaData` collection will be used to construct it.
    Otherwise, the local :class:`_schema.MetaData` collection will supercede
    that used by an existing :class:`_orm.registry` passed using the
    :paramref:`_orm.DeclarativeBase.registry` parameter.
   :param type_annotation_map: optional type annotation map that will be
    passed to the :class:`_orm.registry` as
    :paramref:`_orm.registry.type_annotation_map`.
   :param registry: supply a pre-existing :class:`_orm.registry` directly.

   .. versionadded:: 2.0  Added :class:`.DeclarativeBase`, so that declarative
      base classes may be constructed in such a way that is also recognized
      by :pep:`484` type checkers.   As a result, :class:`.DeclarativeBase`
      and other subclassing-oriented APIs should be seen as
      superseding previous "class returned by a function" APIs, namely
      :func:`_orm.declarative_base` and :meth:`_orm.registry.generate_base`,
      where the base class returned cannot be recognized by type checkers
      without using plugins.

   **__init__ behavior**

   In a plain Python class, the base-most ``__init__()`` method in the class
   hierarchy is ``object.__init__()``, which accepts no arguments. However,
   when the :class:`_orm.DeclarativeBase` subclass is first declared, the
   class is given an ``__init__()`` method that links to the
   :paramref:`_orm.registry.constructor` constructor function, if no
   ``__init__()`` method is already present; this is the usual declarative
   constructor that will assign keyword arguments as attributes on the
   instance, assuming those attributes are established at the class level
   (i.e. are mapped, or are linked to a descriptor). This constructor is
   **never accessed by a mapped class without being called explicitly via
   super()**, as mapped classes are themselves given an ``__init__()`` method
   directly which calls :paramref:`_orm.registry.constructor`, so in the
   default case works independently of what the base-most ``__init__()``
   method does.

   .. versionchanged:: 2.0.1  :class:`_orm.DeclarativeBase` has a default
      constructor that links to :paramref:`_orm.registry.constructor` by
      default, so that calls to ``super().__init__()`` can access this
      constructor. Previously, due to an implementation mistake, this default
      constructor was missing, and calling ``super().__init__()`` would invoke
      ``object.__init__()``.

   The :class:`_orm.DeclarativeBase` subclass may also declare an explicit
   ``__init__()`` method which will replace the use of the
   :paramref:`_orm.registry.constructor` function at this level::

       class Base(DeclarativeBase):
           def __init__(self, id=None):
               self.id = id

   Mapped classes still will not invoke this constructor implicitly; it
   remains only accessible by calling ``super().__init__()``::

       class MyClass(Base):
           def __init__(self, id=None, name=None):
               self.name = name
               super().__init__(id=id)

   Note that this is a different behavior from what functions like the legacy
   :func:`_orm.declarative_base` would do; the base created by those functions
   would always install :paramref:`_orm.registry.constructor` for
   ``__init__()``.



   .. py:attribute:: active_material_mass_fraction
      :type: sqlalchemy.orm.Mapped[Optional[float]]

      

   .. py:attribute:: area
      :type: sqlalchemy.orm.Mapped[Optional[float]]

      

   .. py:attribute:: argument
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: batches
      :type: sqlalchemy.orm.Mapped[Optional[List[Batch]]]

      

   .. py:attribute:: cell_design
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: cell_exists
      :type: sqlalchemy.orm.Mapped[Optional[bool]]

      

   .. py:attribute:: cell_group
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: cell_type
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: cellpy_file_name
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: channel
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: comment_cell
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: comment_general
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: comment_history
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: comment_slurry
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: electrolyte
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: experiment_type
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: formation
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: frozen
      :type: sqlalchemy.orm.Mapped[Optional[bool]]

      

   .. py:attribute:: inactive_additive_mass
      :type: sqlalchemy.orm.Mapped[Optional[float]]

      

   .. py:attribute:: instrument
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: label
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: loading_active
      :type: sqlalchemy.orm.Mapped[Optional[float]]

      

   .. py:attribute:: mass_active
      :type: sqlalchemy.orm.Mapped[Optional[float]]

      

   .. py:attribute:: mass_total
      :type: sqlalchemy.orm.Mapped[Optional[float]]

      

   .. py:attribute:: material_class
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: material_group_label
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: material_label
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: material_pre_processing
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: material_solvent
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: material_sub_label
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: material_surface_processing
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: name
      :type: sqlalchemy.orm.Mapped[str]

      

   .. py:attribute:: nominal_capacity
      :type: sqlalchemy.orm.Mapped[Optional[float]]

      

   .. py:attribute:: pasting_thickness
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: pk
      :type: sqlalchemy.orm.Mapped[int]

      

   .. py:attribute:: project
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: raw_data
      :type: sqlalchemy.orm.Mapped[List[RawData]]

      

   .. py:attribute:: schedule
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: selected
      :type: sqlalchemy.orm.Mapped[Optional[bool]]

      

   .. py:attribute:: separator
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: solvent_solid_ratio
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      

   .. py:attribute:: temperature
      :type: sqlalchemy.orm.Mapped[Optional[float]]

      

   .. py:attribute:: test_date
      :type: sqlalchemy.orm.Mapped[Optional[str]]

      


.. py:class:: RawData


   Bases: :py:obj:`Base`

   .. autoapi-inheritance-diagram:: cellpy.readers.sql_dbreader.RawData
      :parts: 1

   Base class used for declarative class definitions.

   The :class:`_orm.DeclarativeBase` allows for the creation of new
   declarative bases in such a way that is compatible with type checkers::


       from sqlalchemy.orm import DeclarativeBase

       class Base(DeclarativeBase):
           pass


   The above ``Base`` class is now usable as the base for new declarative
   mappings.  The superclass makes use of the ``__init_subclass__()``
   method to set up new classes and metaclasses aren't used.

   When first used, the :class:`_orm.DeclarativeBase` class instantiates a new
   :class:`_orm.registry` to be used with the base, assuming one was not
   provided explicitly. The :class:`_orm.DeclarativeBase` class supports
   class-level attributes which act as parameters for the construction of this
   registry; such as to indicate a specific :class:`_schema.MetaData`
   collection as well as a specific value for
   :paramref:`_orm.registry.type_annotation_map`::

       from typing_extensions import Annotated

       from sqlalchemy import BigInteger
       from sqlalchemy import MetaData
       from sqlalchemy import String
       from sqlalchemy.orm import DeclarativeBase

       bigint = Annotated[int, "bigint"]
       my_metadata = MetaData()

       class Base(DeclarativeBase):
           metadata = my_metadata
           type_annotation_map = {
               str: String().with_variant(String(255), "mysql", "mariadb"),
               bigint: BigInteger()
           }

   Class-level attributes which may be specified include:

   :param metadata: optional :class:`_schema.MetaData` collection.
    If a :class:`_orm.registry` is constructed automatically, this
    :class:`_schema.MetaData` collection will be used to construct it.
    Otherwise, the local :class:`_schema.MetaData` collection will supercede
    that used by an existing :class:`_orm.registry` passed using the
    :paramref:`_orm.DeclarativeBase.registry` parameter.
   :param type_annotation_map: optional type annotation map that will be
    passed to the :class:`_orm.registry` as
    :paramref:`_orm.registry.type_annotation_map`.
   :param registry: supply a pre-existing :class:`_orm.registry` directly.

   .. versionadded:: 2.0  Added :class:`.DeclarativeBase`, so that declarative
      base classes may be constructed in such a way that is also recognized
      by :pep:`484` type checkers.   As a result, :class:`.DeclarativeBase`
      and other subclassing-oriented APIs should be seen as
      superseding previous "class returned by a function" APIs, namely
      :func:`_orm.declarative_base` and :meth:`_orm.registry.generate_base`,
      where the base class returned cannot be recognized by type checkers
      without using plugins.

   **__init__ behavior**

   In a plain Python class, the base-most ``__init__()`` method in the class
   hierarchy is ``object.__init__()``, which accepts no arguments. However,
   when the :class:`_orm.DeclarativeBase` subclass is first declared, the
   class is given an ``__init__()`` method that links to the
   :paramref:`_orm.registry.constructor` constructor function, if no
   ``__init__()`` method is already present; this is the usual declarative
   constructor that will assign keyword arguments as attributes on the
   instance, assuming those attributes are established at the class level
   (i.e. are mapped, or are linked to a descriptor). This constructor is
   **never accessed by a mapped class without being called explicitly via
   super()**, as mapped classes are themselves given an ``__init__()`` method
   directly which calls :paramref:`_orm.registry.constructor`, so in the
   default case works independently of what the base-most ``__init__()``
   method does.

   .. versionchanged:: 2.0.1  :class:`_orm.DeclarativeBase` has a default
      constructor that links to :paramref:`_orm.registry.constructor` by
      default, so that calls to ``super().__init__()`` can access this
      constructor. Previously, due to an implementation mistake, this default
      constructor was missing, and calling ``super().__init__()`` would invoke
      ``object.__init__()``.

   The :class:`_orm.DeclarativeBase` subclass may also declare an explicit
   ``__init__()`` method which will replace the use of the
   :paramref:`_orm.registry.constructor` function at this level::

       class Base(DeclarativeBase):
           def __init__(self, id=None):
               self.id = id

   Mapped classes still will not invoke this constructor implicitly; it
   remains only accessible by calling ``super().__init__()``::

       class MyClass(Base):
           def __init__(self, id=None, name=None):
               self.name = name
               super().__init__(id=id)

   Note that this is a different behavior from what functions like the legacy
   :func:`_orm.declarative_base` would do; the base created by those functions
   would always install :paramref:`_orm.registry.constructor` for
   ``__init__()``.



   .. py:attribute:: cell
      :type: sqlalchemy.orm.Mapped[Cell]

      

   .. py:attribute:: cell_pk
      :type: sqlalchemy.orm.Mapped[int]

      

   .. py:attribute:: is_file
      :type: sqlalchemy.orm.Mapped[bool]

      

   .. py:attribute:: name
      :type: sqlalchemy.orm.Mapped[str]

      

   .. py:attribute:: pk
      :type: sqlalchemy.orm.Mapped[int]

      


.. py:class:: SQLReader(db_connection: str = None, batch: str = None, **kwargs)


   Bases: :py:obj:`cellpy.readers.core.BaseDbReader`

   .. autoapi-inheritance-diagram:: cellpy.readers.sql_dbreader.SQLReader
      :parts: 1

   Base class for database readers.

   Initialize the SQLReader.

   .. py:method:: add_batch_object(batch: Batch) -> None

      Add a batch object to the database.

      For this to work, you will have to create a batch object first, then populate it with
      data (including the cell objects that the batch refers to, see .add_cell_object),
      and finally add it to the database using this method.

      .. rubric:: Examples

      >>> from cellpy.readers import sql_dbreader
      >>> db = sql_dbreader.SQLReader()
      >>> db.open_db("my_db.sqlite")

      >>> # create a batch object:
      >>> batch = sql_dbreader.Batch()
      >>> batch.name = "my_batch"
      >>> batch.comment = "my_comment"

      >>> # add the cells to the batch:
      >>> batch.cells = [cell1, cell2, cell3]

      >>> db.add_batch_object(batch)


   .. py:method:: add_cell_object(cell: Cell) -> None

      Add a cell object to the database.

      For this to work, you will have to create a cell object first, then populate it with
      data, and finally add it to the database using this method.

      .. rubric:: Examples

      >>> from cellpy.readers import sql_dbreader
      >>> cell = sql_dbreader.Cell()
      >>> cell.name = "my_cell"
      >>> cell.label = "my_label"
      >>> cell.project = "my_project"
      >>> cell.cell_group = "my_cell_group"
      >>> # ...and so on...

      >>> db = sql_dbreader.SQLReader()
      >>> db.open_db("my_db.sqlite")
      >>> db.add_cell_object(cell)

      :param cell: cellpy.readers.sql_dbreader.Cell object

      :returns: None


   .. py:method:: add_raw_data_object(raw_data: RawData) -> None


   .. py:method:: create_db(db_uri: str = DB_URI, echo: bool = False, **kwargs) -> None


   .. py:method:: extract_date_from_cell_name(force=False)


   .. py:method:: from_batch(batch_name: str, include_key: bool = False, include_individual_arguments: bool = False) -> dict


   .. py:method:: get_area(pk: int) -> float


   .. py:method:: get_args(pk: int) -> dict


   .. py:method:: get_by_column_label(pk: int, name: str) -> Any


   .. py:method:: get_cell_name(pk: int) -> str


   .. py:method:: get_cell_type(pk: int) -> str


   .. py:method:: get_comment(pk: int) -> str


   .. py:method:: get_experiment_type(pk: int) -> str


   .. py:method:: get_group(pk: int) -> str


   .. py:method:: get_instrument(pk: int) -> str


   .. py:method:: get_label(pk: int) -> str


   .. py:method:: get_loading(pk: int) -> float


   .. py:method:: get_mass(pk: int) -> float


   .. py:method:: get_nom_cap(pk: int) -> float


   .. py:method:: get_total_mass(pk: int) -> float


   .. py:method:: import_cells_from_excel_sqlite(db_path: str = None, echo: bool = False, allow_duplicates: bool = False, allow_updates: bool = True, process_batches=True, clear=False) -> None

      Import cells from old db to new db.

      :param db_path: path to old db (if not provided, it will use the already loaded db if it exists).
      :param echo: will echo sql statements (if loading, i.e. if db_path is provided).
      :param allow_duplicates: will not import if cell already exists in new db.
      :param allow_updates: will update existing cells in new db.
      :param process_batches: will process batches (if any) in old db.
      :param clear: will clear all rows in new db before importing (asks for confirmation).

      :returns: None


   .. py:method:: inspect_hd5f_fixed(pk: int) -> int


   .. py:method:: load_excel_sqlite(db_path: str, echo: bool = False) -> None

      Load an old sqlite cellpy database created from an Excel file.

      You can use the cellpy.utils.batch_tools.sqlite_from_excel.run() function to
      convert an Excel file to a sqlite database.



   .. py:method:: open_db(db_uri: str = DB_URI, echo: bool = False, **kwargs) -> None


   .. py:method:: select_batch(batch_name: str) -> List[int]


   .. py:method:: view_old_excel_sqlite_table_columns() -> None

      Prints the columns of the old sqlite database.



.. py:data:: DB_FILE_EXCEL

   

.. py:data:: DB_FILE_SQLITE

   

.. py:data:: DB_URI

   

.. py:data:: HEADER_ROW

   

.. py:data:: TABLE_NAME_EXCEL

   

.. py:data:: UNIT_ROW

   

.. py:data:: batch_cell_association_table

   

.. py:data:: hdr_journal

   

