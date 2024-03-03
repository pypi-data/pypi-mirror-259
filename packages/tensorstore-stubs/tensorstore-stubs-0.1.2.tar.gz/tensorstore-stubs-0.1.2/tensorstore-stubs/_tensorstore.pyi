import asyncio
from enum import Enum
from numbers import Real
from typing import (
    Any,
    Callable,
    Generic,
    List,
    Literal,
    Optional,
    Sequence,
    Tuple,
    TypeAlias,
    TypeVar,
    Union,
)

import numpy
import numpy.typing

T = TypeVar("T")
_bool: TypeAlias = bool
DimSelectionLike = int | str | None

class ChunkLayout:
    class Grid:
        @property
        def aspect_ratio(
            arg0: ChunkLayout.Grid,
        ) -> Optional[Tuple[Optional[float], ...]]: ...
        @property
        def aspect_ratio_soft_constraint(
            arg0: ChunkLayout.Grid,
        ) -> Optional[Tuple[Optional[float], ...]]: ...
        @property
        def elements(arg0: ChunkLayout.Grid) -> Optional[int]: ...
        @property
        def elements_soft_constraint(arg0: ChunkLayout.Grid) -> Optional[int]: ...
        @property
        def ndim(arg0: ChunkLayout.Grid) -> Optional[int]: ...
        @property
        def rank(arg0: ChunkLayout.Grid) -> Optional[int]: ...
        @property
        def shape(arg0: ChunkLayout.Grid) -> Optional[Tuple[Optional[int], ...]]: ...
        @property
        def shape_soft_constraint(
            arg0: ChunkLayout.Grid,
        ) -> Optional[Tuple[Optional[int], ...]]: ...
        def to_json(self: ChunkLayout.Grid, include_defaults: _bool = False) -> Any:
            """Converts to the :json:schema:`JSON representation<ChunkLayout/Grid>`."""
            ...

        def update(
            self: ChunkLayout.Grid,
            *,
            rank: Optional[int] = None,
            shape: Optional[Sequence[Optional[int]]] = None,
            shape_soft_constraint: Optional[Sequence[Optional[int]]] = None,
            aspect_ratio: Optional[Sequence[Optional[float]]] = None,
            aspect_ratio_soft_constraint: Optional[Sequence[Optional[float]]] = None,
            elements: Optional[int] = None,
            elements_soft_constraint: Optional[int] = None,
            grid: Optional[ChunkLayout.Grid] = None,
            grid_soft_constraint: Optional[ChunkLayout.Grid] = None,
        ) -> None:
            """Adds additional constraints.

            Args:
              rank: Specifies the number of dimensions.
              shape: Hard constraints on the chunk size for each dimension.  Corresponds to
                :json:schema:`ChunkLayout/Grid.shape`.
              shape_soft_constraint: Soft constraints on the chunk size for each dimension.  Corresponds to
                :json:schema:`ChunkLayout/Grid.shape_soft_constraint`.
              aspect_ratio: Aspect ratio for each dimension.  Corresponds to
                :json:schema:`ChunkLayout/Grid.aspect_ratio`.
              aspect_ratio_soft_constraint: Soft constraints on the aspect ratio for each dimension.  Corresponds to
                :json:schema:`ChunkLayout/Grid.aspect_ratio_soft_constraint`.
              elements: Target number of elements per chunk.  Corresponds to
                :json:schema:`ChunkLayout/Grid.elements`.
              elements_soft_constraint: Soft constraint on the target number of elements per chunk.  Corresponds to
                :json:schema:`ChunkLayout/Grid.elements_soft_constraint`.
              grid: Other grid constraints to merge in.  Hard and soft constraints in
                :py:param:`.grid` are retained as hard and soft constraints, respectively.
              grid_soft_constraint: Other grid constraints to merge in as soft constraints.
            """
            ...

    @property
    def codec_chunk(arg0: ChunkLayout) -> ChunkLayout.Grid: ...
    @property
    def grid_origin(arg0: ChunkLayout) -> Optional[Tuple[Optional[int], ...]]: ...
    @property
    def grid_origin_soft_constraint(
        arg0: ChunkLayout,
    ) -> Optional[Tuple[Optional[int], ...]]: ...
    @property
    def inner_order(arg0: ChunkLayout) -> Optional[Tuple[int, ...]]: ...
    @property
    def inner_order_soft_constraint(arg0: ChunkLayout) -> Optional[Tuple[int, ...]]: ...
    @property
    def ndim(arg0: ChunkLayout) -> int: ...
    @property
    def rank(arg0: ChunkLayout) -> int: ...
    @property
    def read_chunk(arg0: ChunkLayout) -> ChunkLayout.Grid: ...
    @property
    def read_chunk_template(arg0: ChunkLayout) -> IndexDomain: ...
    def to_json(self: ChunkLayout) -> Any:
        """Converts to the :json:schema:`JSON representation<ChunkLayout>`.

        Example:

            >>> layout = ts.ChunkLayout(
            ...     inner_order=[0, 2, 1],
            ...     write_chunk_shape_soft_constraint=[100, None, 200],
            ...     read_chunk_elements=1000000)
            >>> layout.to_json()
            {'inner_order': [0, 2, 1],
             'read_chunk': {'elements': 1000000},
             'write_chunk': {'shape_soft_constraint': [100, None, 200]}}

        Group:
          Accessors
        """
        ...

    def update(
        self: ChunkLayout,
        *,
        rank: Optional[int] = None,
        inner_order: Optional[Sequence[int]] = None,
        inner_order_soft_constraint: Optional[Sequence[int]] = None,
        grid_origin: Optional[Sequence[Optional[int]]] = None,
        grid_origin_soft_constraint: Optional[Sequence[Optional[int]]] = None,
        chunk: Optional[ChunkLayout.Grid] = None,
        write_chunk: Optional[ChunkLayout.Grid] = None,
        read_chunk: Optional[ChunkLayout.Grid] = None,
        codec_chunk: Optional[ChunkLayout.Grid] = None,
        chunk_shape: Optional[Sequence[Optional[int]]] = None,
        chunk_shape_soft_constraint: Optional[Sequence[Optional[int]]] = None,
        write_chunk_shape: Optional[Sequence[Optional[int]]] = None,
        write_chunk_shape_soft_constraint: Optional[Sequence[Optional[int]]] = None,
        read_chunk_shape: Optional[Sequence[Optional[int]]] = None,
        read_chunk_shape_soft_constraint: Optional[Sequence[Optional[int]]] = None,
        codec_chunk_shape: Optional[Sequence[Optional[int]]] = None,
        codec_chunk_shape_soft_constraint: Optional[Sequence[Optional[int]]] = None,
        chunk_aspect_ratio: Optional[Sequence[Optional[float]]] = None,
        chunk_aspect_ratio_soft_constraint: Optional[Sequence[Optional[float]]] = None,
        write_chunk_aspect_ratio: Optional[Sequence[Optional[float]]] = None,
        write_chunk_aspect_ratio_soft_constraint: Optional[
            Sequence[Optional[float]]
        ] = None,
        read_chunk_aspect_ratio: Optional[Sequence[Optional[float]]] = None,
        read_chunk_aspect_ratio_soft_constraint: Optional[
            Sequence[Optional[float]]
        ] = None,
        codec_chunk_aspect_ratio: Optional[Sequence[Optional[float]]] = None,
        codec_chunk_aspect_ratio_soft_constraint: Optional[
            Sequence[Optional[float]]
        ] = None,
        chunk_elements: Optional[int] = None,
        chunk_elements_soft_constraint: Optional[int] = None,
        write_chunk_elements: Optional[int] = None,
        write_chunk_elements_soft_constraint: Optional[int] = None,
        read_chunk_elements: Optional[int] = None,
        read_chunk_elements_soft_constraint: Optional[int] = None,
        codec_chunk_elements: Optional[int] = None,
        codec_chunk_elements_soft_constraint: Optional[int] = None,
        finalize: Optional[_bool] = None,
    ) -> None:
        """Adds additional constraints.

        Args:
          rank: Specifies the number of dimensions.
          inner_order: Permutation specifying the element storage order within the innermost chunks.
            Corresponds to the JSON :json:schema:`ChunkLayout.inner_order` member.  This
            must be a permutation of ``[0, 1, ..., rank-1]``.  Lexicographic order (i.e. C
            order/row-major order) is specified as ``[0, 1, ..., rank-1]``, while
            colexicographic order (i.e. Fortran order/column-major order) is specified as
            ``[rank-1, ..., 1, 0]``.
          inner_order_soft_constraint: Specifies a preferred value for :py:obj:`~ChunkLayout.inner_order` rather than a
            hard constraint.  Corresponds to the JSON
            :json:schema:`ChunkLayout.inner_order_soft_constraint` member.  If
            :py:obj:`~ChunkLayout.inner_order` is also specified, it takes precedence.
          grid_origin: Hard constraints on the origin of the chunk grid.
            Corresponds to the JSON :json:schema:`ChunkLayout.grid_origin` member.
          grid_origin_soft_constraint: Soft constraints on the origin of the chunk grid.  Corresponds to the JSON
            :json:schema:`ChunkLayout.grid_origin_soft_constraint` member.
          chunk: Common constraints on write, read, and codec chunks.  Corresponds to the JSON
            :json:schema:`ChunkLayout.chunk` member.  The :py:obj:`~ChunkLayout.Grid.shape`
            and :py:obj:`~ChunkLayout.Grid.elements` constraints apply only to write and
            read chunks, while the :py:obj:`~ChunkLayout.Grid.aspect_ratio` constraints
            apply to write, read, and codec chunks.
          write_chunk: Constraints on write chunks.  Corresponds to the JSON
            :json:schema:`ChunkLayout.write_chunk` member.
          read_chunk: Constraints on read chunks.  Corresponds to
            the JSON :json:schema:`ChunkLayout.read_chunk` member.
          codec_chunk: Constraints on codec chunks.  Corresponds to
            the JSON :json:schema:`ChunkLayout.codec_chunk` member.
          chunk_shape: Hard constraints on both the write and read chunk shape.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.shape` member of
            :json:schema:`ChunkLayout.chunk`.  Equivalent to specifying both
            :py:param:`.write_chunk_shape` and :py:param:`.read_chunk_shape`.
          chunk_shape_soft_constraint: Soft constraints on both the write and read chunk shape.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.shape_soft_constraint` member of
            :json:schema:`ChunkLayout.chunk`.  Equivalent to specifying both
            :py:param:`.write_chunk_shape_soft_constraint` and
            :py:param:`.read_chunk_shape_soft_constraint`.
          write_chunk_shape: Hard constraints on the write chunk shape.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.shape` member of
            :json:schema:`ChunkLayout.write_chunk`.
          write_chunk_shape_soft_constraint: Soft constraints on the write chunk shape.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.shape_soft_constraint` member of
            :json:schema:`ChunkLayout.write_chunk`.
          read_chunk_shape: Hard constraints on the read chunk shape.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.shape` member of
            :json:schema:`ChunkLayout.read_chunk`.
          read_chunk_shape_soft_constraint: Soft constraints on the read chunk shape.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.shape_soft_constraint` member of
            :json:schema:`ChunkLayout.read_chunk`.
          codec_chunk_shape: Soft constraints on the codec chunk shape.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.shape` member of
            :json:schema:`ChunkLayout.codec_chunk`.
          codec_chunk_shape_soft_constraint: Soft constraints on the codec chunk shape.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.shape_soft_constraint` member of
            :json:schema:`ChunkLayout.codec_chunk`.
          chunk_aspect_ratio: Hard constraints on the write, read, and codec chunk aspect ratio.  Corresponds
            to the JSON :json:schema:`~ChunkLayout/Grid.aspect_ratio` member of
            :json:schema:`ChunkLayout.chunk`.  Equivalent to specifying
            :py:param:`.write_chunk_aspect_ratio`, :py:param:`.read_chunk_aspect_ratio`, and
            :py:param:`.codec_chunk_aspect_ratio`.
          chunk_aspect_ratio_soft_constraint: Soft constraints on the write, read, and codec chunk aspect ratio.  Corresponds
            to the :json:schema:`~ChunkLayout/Grid.aspect_ratio_soft_constraint` member of
            :json:schema:`ChunkLayout.chunk`.  Equivalent to specifying
            :py:param:`.write_chunk_aspect_ratio_soft_constraint`,
            :py:param:`.read_chunk_aspect_ratio_soft_constraint`, and
            :py:param:`.codec_chunk_aspect_ratio_soft_constraint`.
          write_chunk_aspect_ratio: Hard constraints on the write chunk aspect ratio.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.aspect_ratio` member of
            :json:schema:`ChunkLayout.write_chunk`.
          write_chunk_aspect_ratio_soft_constraint: Soft constraints on the write chunk aspect ratio.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.aspect_ratio_soft_constraint` member of
            :json:schema:`ChunkLayout.write_chunk`.
          read_chunk_aspect_ratio: Hard constraints on the read chunk aspect ratio.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.aspect_ratio` member of
            :json:schema:`ChunkLayout.read_chunk`.
          read_chunk_aspect_ratio_soft_constraint: Soft constraints on the read chunk aspect ratio.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.aspect_ratio_soft_constraint` member of
            :json:schema:`ChunkLayout.read_chunk`.
          codec_chunk_aspect_ratio: Soft constraints on the codec chunk aspect ratio.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.aspect_ratio` member of
            :json:schema:`ChunkLayout.codec_chunk`.
          codec_chunk_aspect_ratio_soft_constraint: Soft constraints on the codec chunk aspect ratio.  Corresponds to the
            JSON :json:schema:`~ChunkLayout/Grid.aspect_ratio_soft_constraint` member of
            :json:schema:`ChunkLayout.codec_chunk`.
          chunk_elements: Hard constraints on the target number of elements for write and read chunks.
            Corresponds to the JSON :json:schema:`~ChunkLayout/Grid.elements` member of
            :json:schema:`ChunkLayout.chunk`.  Equivalent to specifying both
            :py:param:`.write_chunk_elements` and :py:param:`.read_chunk_elements`.
          chunk_elements_soft_constraint: Soft constraints on the target number of elements for write and read chunks.
            Corresponds to the JSON
            :json:schema:`~ChunkLayout/Grid.elements_soft_constraint` member of
            :json:schema:`ChunkLayout.chunk`.  Equivalent to specifying both
            :py:param:`.write_chunk_elements_soft_constraint` and
            :py:param:`.read_chunk_elements_soft_constraint`.
          write_chunk_elements: Hard constraints on the target number of elements for write chunks.  Corresponds
            to the JSON :json:schema:`~ChunkLayout/Grid.elements` member of
            :json:schema:`ChunkLayout.write_chunk`.
          write_chunk_elements_soft_constraint: Soft constraints on the target number of elements for write chunks.  Corresponds
            to the JSON :json:schema:`~ChunkLayout/Grid.elements_soft_constraint` member
            of :json:schema:`ChunkLayout.write_chunk`.
          read_chunk_elements: Hard constraints on the target number of elements for read chunks.  Corresponds
            to the JSON :json:schema:`~ChunkLayout/Grid.elements` member of
            :json:schema:`ChunkLayout.read_chunk`.
          read_chunk_elements_soft_constraint: Soft constraints on the target number of elements for read chunks.  Corresponds
            to the JSON :json:schema:`~ChunkLayout/Grid.elements_soft_constraint` member
            of :json:schema:`ChunkLayout.read_chunk`.
          codec_chunk_elements: Hard constraints on the target number of elements for codec chunks.  Corresponds
            to the JSON :json:schema:`~ChunkLayout/Grid.elements` member of
            :json:schema:`ChunkLayout.codec_chunk`.
          codec_chunk_elements_soft_constraint: Soft constraints on the target number of elements for codec chunks.  Corresponds
            to the JSON :json:schema:`~ChunkLayout/Grid.elements_soft_constraint` member
            of :json:schema:`ChunkLayout.codec_chunk`.
          finalize: Validates and converts the layout into a *precise* chunk
            layout.

            - All dimensions of :py:obj:`~ChunkLayout.grid_origin` must be specified as hard
              constraints.

            - Any write/read/codec chunk :py:obj:`~ChunkLayout.Grid.shape` soft constraints
              are cleared.

            - Any unspecified dimensions of the read chunk shape are set from the
              write chunk shape.

            - Any write/read/codec chunk :py:obj:`~ChunkLayout.Grid.aspect_ratio` or
              :py:obj:`~ChunkLayout.Grid.elements` constraints are cleared.


        Group:
          Setters
        """
        ...

    @property
    def write_chunk(arg0: ChunkLayout) -> ChunkLayout.Grid: ...
    @property
    def write_chunk_template(arg0: ChunkLayout) -> IndexDomain: ...

class CodecSpec:
    def to_json(self: CodecSpec, include_defaults: _bool = False) -> Any:
        """Converts to the :json:schema:`JSON representation<Codec>`."""
        ...

class Context:
    class Resource:
        def to_json(self: Context.Resource, include_defaults: _bool = False) -> Any:
            """Returns the :json:schema:`JSON representation<ContextResource>` of the context resource.

            Example:

                >>> context = ts.Context(
                ...     {'cache_pool#a': {
                ...         'total_bytes_limit': 10000000
                ...     }})
                >>> context['cache_pool#a'].to_json()
                {'total_bytes_limit': 10000000}

            Group:
              Accessors
            """
            ...

    class Spec:
        def to_json(self: Context.Spec, include_defaults: _bool = False) -> Any:
            """Returns the :json:schema:`JSON representation<Context>`.

            Args:
              include_defaults: Indicates whether to include members even if they are equal to the default value.

            Group:
              Accessors
            """
            ...

    @property
    def parent(arg0: Context) -> Context: ...
    @property
    def spec(arg0: Context) -> Context.Spec: ...

class Dim:
    @property
    def empty(arg0: Dim) -> _bool: ...
    @property
    def exclusive_max(arg0: Dim) -> int: ...
    @property
    def exclusive_min(arg0: Dim) -> int: ...
    @property
    def finite(arg0: Dim) -> _bool: ...
    def hull(self: Dim, other: Dim) -> Dim:
        """Hull with another Dim.

        The ``implicit`` flag that corresponds to the selected bound is propagated.
        The :py:obj:`.label` field, if non-empty, must match, and will be propagated.

        Args:
          other: Object to hull with.

        Example:

            >>> a = ts.Dim(inclusive_min=1, exclusive_max=5, label='x')
            >>> a.hull(ts.Dim(size=3))
            Dim(inclusive_min=0, exclusive_max=5, label="x")
        """
        ...

    @property
    def implicit_lower(arg0: Dim) -> _bool: ...
    @property
    def implicit_upper(arg0: Dim) -> _bool: ...
    @property
    def inclusive_max(arg0: Dim) -> int: ...
    @property
    def inclusive_min(arg0: Dim) -> int: ...
    def intersect(self: Dim, other: Dim) -> Dim:
        """Intersect with another Dim.

        The ``implicit`` flag that corresponds to the selected bound is propagated.
        The :py:obj:`.label`  field, if non-empty, must match, and will be propagated.

        Args:
          other: Object to intersect with.

        Example:

            >>> a = ts.Dim(inclusive_min=1, exclusive_max=5, label='x')
            >>> a.intersect(ts.Dim(size=3))
            Dim(inclusive_min=1, exclusive_max=3, label="x")
        """
        ...

    @property
    def label(arg0: Dim) -> str: ...
    @property
    def size(arg0: Dim) -> int: ...

class DimExpression:
    @property
    def diagonal(arg0: DimExpression) -> DimExpression: ...
    @property
    def label(arg0: object) -> DimExpression: ...
    @property
    def mark_bounds_implicit(arg0: object) -> DimExpression: ...
    @property
    def oindex(arg0: object) -> DimExpression: ...
    @property
    def stride(arg0: object) -> DimExpression: ...
    @property
    def translate_backward_by(arg0: object) -> DimExpression: ...
    @property
    def translate_by(arg0: object) -> DimExpression: ...
    @property
    def translate_to(arg0: object) -> DimExpression: ...
    @property
    def transpose(arg0: object) -> DimExpression: ...
    @property
    def vindex(arg0: object) -> DimExpression: ...

class Future(Generic[T]):
    def add_done_callback(self: Future, callback: Callable[[Future], None]) -> None:
        """Registers a callback to be invoked upon completion of the asynchronous operation.

        Args:
          callback: Callback to invoke with :python:`self` when this future becomes
            ready.

        .. warning::

           Unlike :py:obj:`python:asyncio.Future.add_done_callback`, but like
           :py:obj:`python:concurrent.futures.Future.add_done_callback`, the
           :py:param:`.callback` may be invoked from any thread.  If using
           :py:mod:`asyncio` and :py:param:`.callback` needs to be invoked from a
           particular event loop, wrap :py:param:`.callback` with
           :py:obj:`python:asyncio.loop.call_soon_threadsafe`.

        Group:
          Callback interface
        """
        ...

    def cancel(self: Future) -> _bool:
        """Requests cancellation of the asynchronous operation.

        If the operation has not already completed, it is marked as unsuccessfully
        completed with an instance of :py:obj:`asyncio.CancelledError`.
        """
        ...

    def cancelled(self: Future) -> _bool:
        """Queries whether the asynchronous operation has been cancelled.

        Example:

            >>> promise, future = ts.Promise.new()
            >>> future.cancelled()
            False
            >>> future.cancel()
            >>> future.cancelled()
            True
            >>> future.exception()
            Traceback (most recent call last):
                ...
            ...CancelledError...

        Group:
          Accessors
        """
        ...

    def done(self: Future) -> _bool:
        """Queries whether the asynchronous operation has completed or been cancelled.

        Group:
          Accessors
        """
        ...

    def exception(
        self: Future, timeout: Optional[float] = None, deadline: Optional[float] = None
    ) -> object:
        """Blocks until asynchronous operation completes, and returns the error if any.

        Args:
          timeout: Maximum number of seconds to block.
          deadline: Deadline in seconds since the Unix epoch.

        Returns:

          The error that was produced by the asynchronous operation, or :py:obj:`None`
          if the operation completed successfully.

        Raises:

          TimeoutError: If the result did not become ready within the specified
            :py:param:`.timeout` or :py:param:`.deadline`.

          KeyboardInterrupt: If running on the main thread and a keyboard interrupt is
            received.

        Group:
          Blocking interface
        """
        ...

    def force(self: Future) -> None:
        """Ensures the asynchronous operation begins executing.

        This is called automatically by :py:obj:`.result` and :py:obj:`.exception`, but
        must be called explicitly when using :py:obj:`.add_done_callback`.
        """
        ...

    def remove_done_callback(self: Future, callback: Callable[[Future], None]) -> int:
        """Unregisters a previously-registered callback.

        Group:
          Callback interface
        """
        ...

    def result(
        self: Future, timeout: Optional[float] = None, deadline: Optional[float] = None
    ) -> T:
        """Blocks until the asynchronous operation completes, and returns the result.

        If the asynchronous operation completes unsuccessfully, raises the error that
        was produced.

        Args:
          timeout: Maximum number of seconds to block.
          deadline: Deadline in seconds since the Unix epoch.

        Returns:
          The result of the asynchronous operation, if successful.

        Raises:

          TimeoutError: If the result did not become ready within the specified
            :py:param:`.timeout` or :py:param:`.deadline`.

          KeyboardInterrupt: If running on the main thread and a keyboard interrupt is
            received.

        Group:
          Blocking interface
        """
        ...

class FutureLike(Generic[T]):
    pass

class IndexDomain:
    @property
    def T(arg0: IndexDomain) -> IndexDomain: ...
    @property
    def exclusive_max(arg0: IndexDomain) -> Tuple[int, ...]: ...
    def hull(self: IndexDomain, other: IndexDomain) -> IndexDomain:
        """Computes the hull (minimum containing box) with another domain.

        The ``implicit`` flag that corresponds to the selected bound is propagated.

        Args:
          other: Object to hull with.

        Example:

            >>> a = ts.IndexDomain(inclusive_min=[1, 2, 3],
            ...                    exclusive_max=[4, 5, 6],
            ...                    labels=['x', 'y', ''])
            >>> a.hull(ts.IndexDomain(shape=[2, 3, 4]))
            { "x": [0, 4), "y": [0, 5), [0, 6) }

        Group:
          Geometric operations
        """
        ...

    @property
    def implicit_lower_bounds(arg0: IndexDomain) -> Tuple[_bool, ...]: ...
    @property
    def implicit_upper_bounds(arg0: IndexDomain) -> Tuple[_bool, ...]: ...
    @property
    def inclusive_max(arg0: IndexDomain) -> Tuple[int, ...]: ...
    @property
    def inclusive_min(arg0: IndexDomain) -> Tuple[int, ...]: ...
    @property
    def index_exp(arg0: IndexDomain) -> Tuple[slice, ...]: ...
    def intersect(self: IndexDomain, other: IndexDomain) -> IndexDomain:
        """Intersects with another domain.

        The ``implicit`` flag that corresponds to the selected bound is propagated.

        Args:
          other: Object to intersect with.

        Example:

            >>> a = ts.IndexDomain(inclusive_min=[1, 2, 3],
            ...                    exclusive_max=[4, 5, 6],
            ...                    labels=['x', 'y', ''])
            >>> a.intersect(ts.IndexDomain(shape=[2, 3, 4]))
            { "x": [1, 2), "y": [2, 3), [3, 4) }

        Group:
          Geometric operations
        """
        ...

    @property
    def label(arg0: object) -> IndexDomain: ...
    @property
    def labels(arg0: IndexDomain) -> Tuple[str, ...]: ...
    @property
    def mark_bounds_implicit(arg0: object) -> IndexDomain: ...
    @property
    def ndim(arg0: IndexDomain) -> int: ...
    @property
    def origin(arg0: IndexDomain) -> Tuple[int, ...]: ...
    @property
    def rank(arg0: IndexDomain) -> int: ...
    @property
    def shape(arg0: IndexDomain) -> Tuple[int, ...]: ...
    @property
    def size(arg0: IndexDomain) -> int: ...
    def to_json(self: IndexDomain) -> Any:
        """Returns the :json:schema:`JSON representation<IndexDomain>`.

        Group:
          Accessors
        """
        ...

    @property
    def translate_backward_by(arg0: object) -> IndexDomain: ...
    @property
    def translate_by(arg0: object) -> IndexDomain: ...
    @property
    def translate_to(arg0: object) -> IndexDomain: ...
    def transpose(
        self: IndexDomain, axes: Optional[DimSelectionLike] = None
    ) -> IndexDomain:
        """Returns a view with a transposed domain.

        This is equivalent to :python:`self[ts.d[axes].transpose[:]]`.

        Args:

          axes: Specifies the existing dimension corresponding to each dimension of the
            new view.  Dimensions may be specified either by index or label.  Specifying
            `None` is equivalent to specifying :python:`[rank-1, ..., 0]`, which
            reverses the dimension order.

        Raises:

          ValueError: If :py:param:`.axes` does not specify a valid permutation.

        See also:
          - `tensorstore.DimExpression.transpose`
          - :py:obj:`.T`

        Group:
          Indexing
        """
        ...

class IndexTransform:
    @property
    def T(arg0: IndexTransform) -> IndexTransform: ...
    @property
    def domain(arg0: IndexTransform) -> IndexDomain: ...
    @property
    def implicit_lower_bounds(arg0: IndexTransform) -> Tuple[_bool, ...]: ...
    @property
    def implicit_upper_bounds(arg0: IndexTransform) -> Tuple[_bool, ...]: ...
    @property
    def input_exclusive_max(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def input_inclusive_max(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def input_inclusive_min(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def input_labels(arg0: IndexTransform) -> Tuple[str, ...]: ...
    @property
    def input_origin(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def input_rank(arg0: IndexTransform) -> int: ...
    @property
    def input_shape(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def label(arg0: object) -> IndexTransform: ...
    @property
    def mark_bounds_implicit(arg0: object) -> IndexTransform: ...
    @property
    def ndim(arg0: IndexTransform) -> int: ...
    @property
    def oindex(arg0: object) -> IndexTransform: ...
    @property
    def origin(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def output(arg0: IndexTransform) -> OutputIndexMaps: ...
    @property
    def output_rank(arg0: IndexTransform) -> int: ...
    @property
    def shape(arg0: IndexTransform) -> Tuple[int, ...]: ...
    @property
    def size(arg0: IndexTransform) -> int: ...
    def to_json(self: IndexTransform) -> Any:
        """Returns the :json:schema:`JSON representation<IndexTransform>` of the transform.

        Example:

           >>> transform = ts.IndexTransform(
           ...     input_inclusive_min=[1, 2, -1],
           ...     implicit_lower_bounds=[1, 0, 0],
           ...     input_shape=[3, 2, 2],
           ...     implicit_upper_bounds=[0, 1, 0],
           ...     input_labels=['x', 'y', 'z'],
           ...     output=[
           ...         ts.OutputIndexMap(offset=7, stride=13, input_dimension=1),
           ...         ts.OutputIndexMap(offset=8),
           ...         ts.OutputIndexMap(
           ...             offset=1,
           ...             stride=-2,
           ...             index_array=[[[1, 2]]],
           ...             index_range=ts.Dim(inclusive_min=-3, exclusive_max=10),
           ...         ),
           ...     ],
           ... )
           >>> transform.to_json()
           {'input_exclusive_max': [4, [4], 1],
            'input_inclusive_min': [[1], 2, -1],
            'input_labels': ['x', 'y', 'z'],
            'output': [{'input_dimension': 1, 'offset': 7, 'stride': 13},
                       {'offset': 8},
                       {'index_array': [[[1, 2]]], 'offset': 1, 'stride': -2}]}

        Group:
          Accessors
        """
        ...

    @property
    def translate_backward_by(arg0: object) -> IndexTransform: ...
    @property
    def translate_by(arg0: object) -> IndexTransform: ...
    @property
    def translate_to(arg0: object) -> IndexTransform: ...
    def transpose(
        self: IndexTransform, axes: Optional[DimSelectionLike] = None
    ) -> IndexTransform:
        """Returns a view with a transposed domain.

        This is equivalent to :python:`self[ts.d[axes].transpose[:]]`.

        Args:

          axes: Specifies the existing dimension corresponding to each dimension of the
            new view.  Dimensions may be specified either by index or label.  Specifying
            `None` is equivalent to specifying :python:`[rank-1, ..., 0]`, which
            reverses the dimension order.

        Raises:

          ValueError: If :py:param:`.axes` does not specify a valid permutation.

        See also:
          - `tensorstore.DimExpression.transpose`
          - :py:obj:`.T`

        Group:
          Indexing
        """
        ...

    @property
    def vindex(arg0: object) -> IndexTransform: ...

class Indexable:
    pass

class KvStore:
    class KeyRange:
        def copy(self: KvStore.KeyRange) -> KvStore.KeyRange:
            """Returns a copy of the range.

            Group:
              Accessors
            """
            ...

        @property
        def empty(arg0: KvStore.KeyRange) -> _bool: ...
        @property
        def exclusive_max(arg0: KvStore.KeyRange) -> str: ...
        @property
        def inclusive_min(arg0: KvStore.KeyRange) -> str: ...

    class ReadResult:
        @property
        def stamp(arg0: KvStore.ReadResult) -> KvStore.TimestampedStorageGeneration: ...
        @property
        def state(
            arg0: KvStore.ReadResult,
        ) -> Literal["unspecified", "missing", "value"]: ...
        @property
        def value(arg0: KvStore.ReadResult) -> bytes: ...

    class Spec:
        @property
        def base(arg0: KvStore.Spec) -> Optional[KvStore.Spec]: ...
        def copy(self: KvStore.Spec) -> KvStore.Spec:
            """Returns a copy of the key-value store spec.

            Example:

              >>> a = ts.KvStore.Spec({'driver': 'file', 'path': 'tmp/data/'})
              >>> b = a.copy()
              >>> a.path = 'tmp/data/abc/'
              >>> a
              KvStore.Spec({'driver': 'file', 'path': 'tmp/data/abc/'})
              >>> b
              KvStore.Spec({'driver': 'file', 'path': 'tmp/data/'})

            Group:
              Accessors
            """
            ...

        @property
        def path(arg0: KvStore.Spec) -> str: ...
        def to_json(self: KvStore.Spec, include_defaults: _bool = False) -> Any:
            """Converts to the :json:schema:`JSON representation<KvStore>`.

            Example:

              >>> spec = ts.KvStore.Spec({'driver': 'file', 'path': 'tmp/dataset/'})
              >>> spec /= 'abc/'
              >>> spec.to_json()
              {'driver': 'file', 'path': 'tmp/dataset/abc/'}
              >>> spec.to_json(include_defaults=True)
              {'context': {},
               'driver': 'file',
               'file_io_concurrency': 'file_io_concurrency',
               'file_io_sync': 'file_io_sync',
               'path': 'tmp/dataset/abc/'}

            Group:
              Accessors
            """
            ...

        def update(
            self: KvStore.Spec,
            *,
            unbind_context: Optional[_bool] = None,
            strip_context: Optional[_bool] = None,
            context: Optional[Context] = None,
        ) -> None:
            """Modifies a spec.

            Example:

                >>> spec = ts.KvStore.Spec({
                ...     'driver': 'memory',
                ...     'path': 'abc/',
                ...     'memory_key_value_store': 'memory_key_value_store#a'
                ... })
                >>> spec.update(context=ts.Context({'memory_key_value_store#a': {}}))
                >>> spec
                KvStore.Spec({
                  'context': {'memory_key_value_store#a': {}},
                  'driver': 'memory',
                  'memory_key_value_store': ['memory_key_value_store#a'],
                  'path': 'abc/',
                })
                >>> spec.update(unbind_context=True)
                >>> spec
                KvStore.Spec({
                  'context': {'memory_key_value_store#a': {}},
                  'driver': 'memory',
                  'memory_key_value_store': 'memory_key_value_store#a',
                  'path': 'abc/',
                })
                >>> spec.update(strip_context=True)
                >>> spec
                KvStore.Spec({'driver': 'memory', 'path': 'abc/'})

            Args:

              unbind_context: Convert any bound context resources to context resource specs that fully capture
                the graph of shared context resources and interdependencies.

                Re-binding/re-opening the resultant spec will result in a new graph of new
                context resources that is isomorphic to the original graph of context resources.
                The resultant spec will not refer to any external context resources;
                consequently, binding it to any specific context will have the same effect as
                binding it to a default context.

                Specifying a value of :python:`False` has no effect.
              strip_context: Replace any bound context resources and unbound context resource specs by
                default context resource specs.

                If the resultant :py:obj:`~tensorstore.KvStore.Spec` is re-opened with, or
                re-bound to, a new context, it will use the default context resources specified
                by that context.

                Specifying a value of :python:`False` has no effect.
              context: Bind any context resource specs using the specified shared resource context.

                Any already-bound context resources remain unchanged.  Additionally, any context
                resources specified by a nested :json:schema:`KvStore.context` spec will be
                created as specified, but won't be overridden by :py:param:`.context`.


            Group:
              Mutators
            """
            ...

        @property
        def url(arg0: KvStore.Spec) -> str: ...

    class TimestampedStorageGeneration:
        @property
        def generation(arg0: KvStore.TimestampedStorageGeneration) -> bytes: ...
        @property
        def time(arg0: KvStore.TimestampedStorageGeneration) -> float: ...

    @property
    def base(arg0: KvStore) -> Optional[KvStore]: ...
    def copy(self: KvStore) -> KvStore:
        """Returns a copy of the key-value store.

        Example:

          >>> a = await ts.KvStore.open({'driver': 'file', 'path': 'tmp/data/'})
          >>> b = a.copy()
          >>> a.path = 'tmp/data/abc/'
          >>> a
          KvStore({
            'context': {'file_io_concurrency': {}, 'file_io_sync': True},
            'driver': 'file',
            'path': 'tmp/data/abc/',
          })
          >>> b
          KvStore({
            'context': {'file_io_concurrency': {}, 'file_io_sync': True},
            'driver': 'file',
            'path': 'tmp/data/',
          })

        Group:
          Accessors
        """
        ...

    def delete_range(self: KvStore, range: KvStore.KeyRange) -> Future[None]:
        """Deletes a key range.

        Example:

            >>> store = await ts.KvStore.open({'driver': 'memory'})
            >>> await store.write(b'a', b'value')
            >>> await store.write(b'b', b'value')
            >>> await store.write(b'c', b'value')
            >>> await store.list()
            [b'a', b'b', b'c']
            >>> await store.delete_range(ts.KvStore.KeyRange(b'aa', b'cc'))
            >>> await store.list()
            [b'a']

        Args:

          range: Key range to delete.  This is relative to the existing :py:obj:`.path`,
            if any.

        Returns:

          - If no :py:obj:`.transaction` is specified, returns a :py:obj:`Future` that
            becomes ready when the delete operation has completed and durability is
            guaranteed (to the extent supported by the
            :ref:`driver<key-value-store-drivers>`).

          - If a :py:obj:`.transaction` is specified, returns a :py:obj:`Future` that
            becomes ready when the delete operation is recorded in the transaction.  The
            delete operation is not actually performed until the transaction is
            committed.

        Group:
          I/O
        """
        ...

    def experimental_copy_range_to(
        self: KvStore,
        target: KvStore,
        source_range: Optional[KvStore.KeyRange] = None,
        source_staleness_bound: Optional[float] = None,
    ) -> Future[None]:
        """Copies a range of keys.

        .. warning::

           This API is experimental and subject to change.

        Example:

            >>> store = await ts.KvStore.open({
            ...     'driver': 'ocdbt',
            ...     'base': 'memory://'
            ... })
            >>> await store.write(b'x/a', b'value')
            >>> await store.write(b'x/b', b'value')
            >>> await store.list()
            [b'x/a', b'x/b']
            >>> await (store / "x/").experimental_copy_range_to(store / "y/")
            >>> await store.list()
            [b'x/a', b'x/b', b'y/a', b'y/b']

        .. note::

           Depending on the kvstore implementation, this operation may be able to
           perform the copy without actually re-writing the data.

        Args:

          target: Target key-value store.

            .. warning::

               This may refer to the same kvstore as ``self``, but the target key range
               must not overlap with ``self``.  If this requirement is violated, the
               behavior is unspecified.

          source_range: Key range to include.  This is relative to the existing
            :py:obj:`.path`, if any.  If not specified, all keys under :py:obj:`.path`
            are copied.
          source_staleness_bound: Specifies a time in (fractional) seconds since the
            Unix epoch.  If specified, data that is cached internally by the kvstore
            implementation may be used without validation if not older than the
            :py:param:`.source_staleness_bound`.  Cached data older than
            :py:param:`.source_staleness_bound` must be validated before being returned.
            A value of :python:`float('inf')` indicates that the result must be current
            as of the time the :py:obj:`.read` request was made, i.e. it is equivalent
            to specifying a value of :python:`time.time()`.  A value of
            :python:`float('-inf')` indicates that cached data may be returned without
            validation irrespective of its age.

        Returns:

          - If no :py:obj:`.transaction` is specified for :py:param:`.target`, returns a
            :py:obj:`Future` that becomes ready when the copy operation has completed
            and durability is guaranteed (to the extent supported by the
            :ref:`driver<key-value-store-drivers>`).

          - If a :py:obj:`.transaction` is specified for :py:param:`.target`, returns a
            :py:obj:`Future` that becomes ready when the copy operation is recorded in
            the transaction.  The copy operation is not actually performed until the
            transaction is committed.

        Group:
          I/O
        """
        ...

    def list(
        self: KvStore,
        range: Optional[KvStore.KeyRange] = None,
        strip_prefix_length: int = 0,
    ) -> Future[List[bytes]]:
        """Lists the keys in the key-value store.

        Example:

            >>> store = ts.KvStore.open({'driver': 'memory'}).result()
            >>> store[b'a'] = b'value'
            >>> store[b'b'] = b'value'
            >>> store.list().result()
            [b'a', b'b']
            >>> store.list(ts.KvStore.KeyRange(inclusive_min=b'b')).result()
            [b'b']

        Args:

          range: If specified, restricts to the specified key range.

          strip_prefix_length: Strips the specified number of bytes from the start of
            the returned keys.

        Returns:

          Future that resolves to the list of matching keys, in an unspecified order.

        Raises:

          ValueError: If a :py:obj:`.transaction` is specified.

        Warning:

          This returns all keys within :py:param:`range` as a single :py:obj:`list`.  If
          there are a large number of matching keys, this can consume a large amount of
          memory.

        Group:
          I/O
        """
        ...

    def open(
        spec: Union[KvStore.Spec, Any],
        *,
        context: Optional[Context] = None,
        transaction: Optional[Transaction] = None,
    ) -> Future[KvStore]:
        """Opens a key-value store.

        Example of opening from a :json:schema:`JSON KvStore spec<KvStore>`:

            >>> kvstore = await ts.KvStore.open({'driver': 'memory', 'path': 'abc/'})
            >>> await kvstore.write(b'x', b'y')
            KvStore.TimestampedStorageGeneration(b'...', ...)
            >>> await kvstore.read(b'x')
            KvStore.ReadResult(state='value', value=b'y', stamp=KvStore.TimestampedStorageGeneration(b'...', ...))

        Example of opening from a :json:schema:`URL<KvStoreUrl>`:

            >>> kvstore = await ts.KvStore.open('memory://abc/')
            >>> kvstore.spec()
            KvStore.Spec({'driver': 'memory', 'path': 'abc/'})

        Example of opening from an existing :py:obj:`KvStore.Spec`:

            >>> spec = ts.KvStore.Spec({'driver': 'memory', 'path': 'abc/'})
            >>> kvstore = await ts.KvStore.open(spec)
            >>> kvstore.spec()
            KvStore.Spec({'driver': 'memory', 'path': 'abc/'})

        Args:

          spec: Key-value store spec to open.  May also be specified as
            :json:schema:`JSON<KvStore>` or a :json:schema:`URL<KvStoreUrl>`.

          context: Bind any context resource specs using the specified shared resource context.

            Any already-bound context resources remain unchanged.  Additionally, any context
            resources specified by a nested :json:schema:`KvStore.context` spec will be
            created as specified, but won't be overridden by :py:param:`.context`.
          transaction: Transaction to use for read/write operations.  By default, operations are
            non-transactional.

            .. note::

               To perform transactional operations using a :py:obj:`KvStore` that was
               previously opened without a transaction, use
               :py:obj:`KvStore.with_transaction`.


        Group:
          Constructors
        """
        ...

    @property
    def path(arg0: KvStore) -> str: ...
    def read(
        self: KvStore,
        key: str,
        *,
        if_not_equal: Optional[str] = None,
        staleness_bound: Optional[float] = None,
    ) -> Future[KvStore.ReadResult]:
        """Reads the value of a single key.

        A missing key is not treated as an error; instead, a :py:obj:`.ReadResult` with
        :py:obj:`.ReadResult.state` set to :python:`'missing'` is returned.

        Note:

          The behavior in the case of a missing key differs from that of
          :py:obj:`.__getitem__`, which raises :py:obj:`KeyError` to indicate a missing
          key.

        Example:

            >>> store = await ts.KvStore.open({'driver': 'memory'})
            >>> await store.write(b'a', b'value')
            KvStore.TimestampedStorageGeneration(...)
            >>> await store.read(b'a')
            KvStore.ReadResult(state='value', value=b'value', stamp=KvStore.TimestampedStorageGeneration(...))
            >>> store[b'a']
            b'value'
            >>> await store.read(b'b')
            KvStore.ReadResult(state='missing', value=b'', stamp=KvStore.TimestampedStorageGeneration(...))
            >>> store[b'b']
            Traceback (most recent call last):
                ...
            KeyError...

            >>> store[b'a'] = b'value'
            >>> store[b'b'] = b'value'
            >>> store.list().result()

        If a :py:obj:`.transaction` is bound, the read reflects any writes made within
        the transaction, and the commit of the transaction will fail if the value
        associated with :py:param:`key` changes after the read due to external writes,
        i.e. consistent reads are guaranteed.

        Args:

          key: The key to read.  This is appended (without any separator) to the
            existing :py:obj:`.path`, if any.

          if_not_equal: If specified, the read is aborted if the generation associated
            with :py:param:`key` matches :py:param:`if_not_equal`.  An aborted read due
            to this condition is indicated by a :py:obj:`.ReadResult.state` of
            :python:`'unspecified'`.  This may be useful for validating a cached value
            cache validation at a higher level.

          staleness_bound: Specifies a time in (fractional) seconds since the Unix
            epoch.  If specified, data that is cached internally by the kvstore
            implementation may be used without validation if not older than the
            :py:param:`staleness_bound`.  Cached data older than
            :py:param:`staleness_bound` must be validated before being returned.  A
            value of :python:`float('inf')` indicates that the result must be current as
            of the time the :py:obj:`.read` request was made, i.e. it is equivalent to
            specifying a value of :python:`time.time()`.  A value of
            :python:`float('-inf')` indicates that cached data may be returned without
            validation irrespective of its age.

        Returns:
          Future that resolves when the read operation completes.

        See also:

          - :py:obj:`.write`
          - :py:obj:`.__getitem__`
          - :py:obj:`.__setitem__`
          - :py:obj:`.__delitem__`

        Group:
          I/O
        """
        ...

    def spec(
        self: KvStore,
        *,
        retain_context: Optional[_bool] = None,
        unbind_context: Optional[_bool] = None,
    ) -> KvStore.Spec:
        """Spec that may be used to re-open or re-create the key-value store.

        Example:

            >>> kvstore = await ts.KvStore.open({'driver': 'memory', 'path': 'abc/'})
            >>> kvstore.spec()
            KvStore.Spec({'driver': 'memory', 'path': 'abc/'})
            >>> kvstore.spec(unbind_context=True)
            KvStore.Spec({'context': {'memory_key_value_store': {}}, 'driver': 'memory', 'path': 'abc/'})
            >>> kvstore.spec(retain_context=True)
            KvStore.Spec({
              'context': {'memory_key_value_store': {}},
              'driver': 'memory',
              'memory_key_value_store': ['memory_key_value_store'],
              'path': 'abc/',
            })

        Args:

          retain_context: Retain all bound context resources (e.g. specific concurrency pools, specific
            cache pools).

            The resultant :py:obj:`~tensorstore.KvStore.Spec` may be used to re-open the
            :py:obj:`~tensorstore.KvStore` using the identical context resources.

            Specifying a value of :python:`False` has no effect.
          unbind_context: Convert any bound context resources to context resource specs that fully capture
            the graph of shared context resources and interdependencies.

            Re-binding/re-opening the resultant spec will result in a new graph of new
            context resources that is isomorphic to the original graph of context resources.
            The resultant spec will not refer to any external context resources;
            consequently, binding it to any specific context will have the same effect as
            binding it to a default context.

            Specifying a value of :python:`False` has no effect.


        Group:
          Accessors
        """
        ...

    @property
    def transaction(arg0: KvStore) -> Optional[Transaction]: ...
    @property
    def url(arg0: KvStore) -> str: ...
    def with_transaction(self: KvStore, transaction: Optional[Transaction]) -> KvStore:
        """Returns a transaction-bound view of this key-value store.

        The returned view may be used to perform transactional read/write operations.

        Example:

            >>> store = await ts.KvStore.open({'driver': 'memory'})
            >>> txn = ts.Transaction()
            >>> await store.with_transaction(txn).write(b'a', b'value')
            >>> (await store.with_transaction(txn).read(b'a')).value
            b'value'
            >>> await txn.commit_async()

        Group:
          Transactions
        """
        ...

    def write(
        self: KvStore, key: str, value: Optional[str], *, if_equal: Optional[str] = None
    ) -> Future[KvStore.TimestampedStorageGeneration]:
        """Writes or deletes a single key.

        Example:

            >>> store = await ts.KvStore.open({'driver': 'memory'})
            >>> await store.write(b'a', b'value')
            KvStore.TimestampedStorageGeneration(...)
            >>> await store.read(b'a')
            KvStore.ReadResult(state='value', value=b'value', stamp=KvStore.TimestampedStorageGeneration(...))
            >>> await store.write(b'a', None)
            KvStore.TimestampedStorageGeneration(...)
            >>> await store.read(b'a')
            KvStore.ReadResult(state='missing', value=b'', stamp=KvStore.TimestampedStorageGeneration(...))

        Args:

          key: Key to write/delete.  This is appended (without any separator) to the
            existing :py:obj:`.path`, if any.

          value: Value to store, or :py:obj:`None` to delete.

          if_equal: If specified, indicates a conditional write operation.  The write is
            performed only if the existing generation associated with :py:param:`key`
            matches :py:param:`if_equal`.

        Returns:

          - If no :py:obj:`.transaction` is specified, returns a :py:obj:`Future` that
            resolves to the new storage generation for :py:param:`key` once the write
            operation completes and durability is guaranteed (to the extent supported by
            the :ref:`driver<key-value-store-drivers>`).

          - If a :py:obj:`.transaction` is specified, returns a :py:obj:`Future` that
            resolves to an empty storage generation once the write operation is recorded
            in the transaction.  The write operation is not actually performed until the
            transaction is committed.

        See also:

          - :py:obj:`.__setitem__`
          - :py:obj:`.__delitem__`

        Group:
          I/O
        """
        ...

class OpenMode:
    @property
    def assume_cached_metadata(arg0: OpenMode) -> _bool: ...
    @property
    def assume_metadata(arg0: OpenMode) -> _bool: ...
    @property
    def create(arg0: OpenMode) -> _bool: ...
    @property
    def delete_existing(arg0: OpenMode) -> _bool: ...
    @property
    def open(arg0: OpenMode) -> _bool: ...

class OutputIndexMap:
    @property
    def index_array(arg0: OutputIndexMap) -> Optional[numpy.typing.ArrayLike]: ...
    @property
    def index_range(arg0: OutputIndexMap) -> Optional[Dim]: ...
    @property
    def input_dimension(arg0: OutputIndexMap) -> Optional[int]: ...
    @property
    def method(arg0: OutputIndexMap) -> OutputIndexMethod: ...
    @property
    def offset(arg0: OutputIndexMap) -> int: ...
    @property
    def stride(arg0: OutputIndexMap) -> Optional[int]: ...

class OutputIndexMaps:
    @property
    def rank(arg0: OutputIndexMaps) -> int: ...

class OutputIndexMethod(Enum):
    constant = 0
    single_input_dimension = 1
    array = 2

    @property
    def name(self) -> str: ...
    @property
    def value(arg0: OutputIndexMethod) -> int: ...
    def __str__(self) -> str: ...

class Promise:
    def new(self) -> Tuple[Promise, Future]:
        """Creates a linked promise and future pair.

        Group:
          Constructors
        """
        ...

    def set_exception(self: Promise, exception: object) -> None:
        """Marks the linked future as unsuccessfully completed with the specified error.

        Example:

            >>> promise, future = ts.Promise.new()
            >>> future.done()
            False
            >>> promise.set_exception(Exception(5))
            >>> future.done()
            True
            >>> future.result()
            Traceback (most recent call last):
                ...
            Exception: 5
        """
        ...

    def set_result(self: Promise, result: object) -> None:
        """Marks the linked future as successfully completed with the specified result.

        Example:

            >>> promise, future = ts.Promise.new()
            >>> future.done()
            False
            >>> promise.set_result(5)
            >>> future.done()
            True
            >>> future.result()
            5
        """
        ...

class Schema:
    @property
    def T(arg0: Schema) -> Schema: ...
    @property
    def chunk_layout(arg0: Schema) -> ChunkLayout: ...
    @property
    def codec(arg0: Schema) -> Optional[CodecSpec]: ...
    def copy(self: Schema) -> Schema:
        """Returns a copy of the schema.

        Example:

          >>> a = ts.Schema(dtype=ts.uint8)
          >>> b = a.copy()
          >>> a.update(rank=2)
          >>> b.update(rank=3)
          >>> a
          Schema({'dtype': 'uint8', 'rank': 2})
          >>> b
          Schema({'dtype': 'uint8', 'rank': 3})

        Group:
          Accessors
        """
        ...

    @property
    def dimension_units(arg0: Schema) -> Optional[Tuple[Optional[Unit], ...]]: ...
    @property
    def domain(arg0: Schema) -> Optional[IndexDomain]: ...
    @property
    def dtype(arg0: Schema) -> Optional[dtype]: ...
    @property
    def fill_value(arg0: Schema) -> Optional[numpy.typing.ArrayLike]: ...
    @property
    def label(arg0: object) -> Schema: ...
    @property
    def mark_bounds_implicit(arg0: object) -> Schema: ...
    @property
    def ndim(arg0: Schema) -> Optional[int]: ...
    @property
    def oindex(arg0: object) -> Schema: ...
    @property
    def origin(arg0: Schema) -> Tuple[int, ...]: ...
    @property
    def rank(arg0: Schema) -> Optional[int]: ...
    @property
    def shape(arg0: Schema) -> Tuple[int, ...]: ...
    @property
    def size(arg0: Schema) -> int: ...
    def to_json(self: Schema, include_defaults: _bool = False) -> Any:
        """Converts to the :json:schema:`JSON representation<Schema>`.

        Example:

          >>> schema = ts.Schema(dtype=ts.uint8,
          ...                    chunk_layout=ts.ChunkLayout(grid_origin=[0, 0, 0],
          ...                                                inner_order=[0, 2, 1]))
          >>> schema.to_json()
          {'chunk_layout': {'grid_origin': [0, 0, 0], 'inner_order': [0, 2, 1]},
           'dtype': 'uint8',
           'rank': 3}

        Group:
          Accessors
        """
        ...

    @property
    def translate_backward_by(arg0: object) -> Schema: ...
    @property
    def translate_by(arg0: object) -> Schema: ...
    @property
    def translate_to(arg0: object) -> Schema: ...
    def transpose(self: Schema, axes: Optional[DimSelectionLike] = None) -> Schema:
        """Returns a view with a transposed domain.

        This is equivalent to :python:`self[ts.d[axes].transpose[:]]`.

        Args:

          axes: Specifies the existing dimension corresponding to each dimension of the
            new view.  Dimensions may be specified either by index or label.  Specifying
            `None` is equivalent to specifying :python:`[rank-1, ..., 0]`, which
            reverses the dimension order.

        Raises:

          ValueError: If :py:param:`.axes` does not specify a valid permutation.

        See also:
          - `tensorstore.DimExpression.transpose`
          - :py:obj:`.T`

        Group:
          Indexing
        """
        ...

    def update(
        self: Schema,
        *,
        rank: Optional[int] = None,
        dtype: Optional[dtype] = None,
        domain: Optional[IndexDomain] = None,
        shape: Optional[Sequence[int]] = None,
        chunk_layout: Optional[ChunkLayout] = None,
        codec: Optional[CodecSpec] = None,
        fill_value: Optional[numpy.typing.ArrayLike] = None,
        dimension_units: Optional[
            Sequence[Optional[Union[Unit, str, Real, Tuple[Real, str]]]]
        ] = None,
        schema: Optional[Schema] = None,
    ) -> None:
        """Adds additional constraints.

        Example:

          >>> schema = ts.Schema(rank=3)
          >>> schema
          Schema({'rank': 3})
          >>> schema.update(dtype=ts.uint8)
          >>> schema
          Schema({'dtype': 'uint8', 'rank': 3})

        Args:
          rank: Constrains the rank of the TensorStore.  If there is an index transform, the
            rank constraint must match the rank of the *input* space.
          dtype: Constrains the data type of the TensorStore.  If a data type has already been
            set, it is an error to specify a different data type.
          domain: Constrains the domain of the TensorStore.  If there is an existing
            domain, the specified domain is merged with it as follows:

            1. The rank must match the existing rank.

            2. All bounds must match, except that a finite or explicit bound is permitted to
               match an infinite and implicit bound, and takes precedence.

            3. If both the new and existing domain specify non-empty labels for a dimension,
               the labels must be equal.  If only one of the domains specifies a non-empty
               label for a dimension, the non-empty label takes precedence.

            Note that if there is an index transform, the domain must match the *input*
            space, not the output space.
          shape: Constrains the shape and origin of the TensorStore.  Equivalent to specifying a
            :py:param:`domain` of :python:`ts.IndexDomain(shape=shape)`.

            .. note::

               This option also constrains the origin of all dimensions to be zero.
          chunk_layout: Constrains the chunk layout.  If there is an existing chunk layout constraint,
            the constraints are merged.  If the constraints are incompatible, an error
            is raised.
          codec: Constrains the codec.  If there is an existing codec constraint, the constraints
            are merged.  If the constraints are incompatible, an error is raised.
          fill_value: Specifies the fill value for positions that have not been written.

            The fill value data type must be convertible to the actual data type, and the
            shape must be :ref:`broadcast-compatible<index-domain-alignment>` with the
            domain.

            If an existing fill value has already been set as a constraint, it is an
            error to specify a different fill value (where the comparison is done after
            normalization by broadcasting).
          dimension_units: Specifies the physical units of each dimension of the domain.

            The *physical unit* for a dimension is the physical quantity corresponding to a
            single index increment along each dimension.

            A value of :python:`None` indicates that the unit is unknown.  A dimension-less
            quantity can be indicated by a unit of :python:`""`.
          schema: Additional schema constraints to merge with existing constraints.


        Group:
          Mutators
        """
        ...

    @property
    def vindex(arg0: object) -> Schema: ...

class Spec:
    @property
    def T(arg0: Spec) -> Spec: ...
    @property
    def base(arg0: Spec) -> Optional[Spec]: ...
    @property
    def chunk_layout(arg0: Spec) -> ChunkLayout: ...
    @property
    def codec(arg0: Spec) -> Optional[CodecSpec]: ...
    def copy(self: Spec) -> Spec:
        """Returns a copy of the spec.

        Example:

          >>> a = ts.Spec({'driver': 'n5', 'kvstore': {'driver': 'memory'}})
          >>> b = a.copy()
          >>> a.update(dtype=ts.uint8)
          >>> b.update(dtype=ts.uint16)
          >>> a
          Spec({'driver': 'n5', 'dtype': 'uint8', 'kvstore': {'driver': 'memory'}})
          >>> b
          Spec({'driver': 'n5', 'dtype': 'uint16', 'kvstore': {'driver': 'memory'}})

        Group:
          Accessors
        """
        ...

    @property
    def dimension_units(arg0: Spec) -> Optional[Tuple[Optional[Unit], ...]]: ...
    @property
    def domain(arg0: Spec) -> Optional[IndexDomain]: ...
    @property
    def dtype(arg0: Spec) -> Optional[dtype]: ...
    @property
    def fill_value(arg0: Spec) -> Optional[numpy.typing.ArrayLike]: ...
    @property
    def kvstore(arg0: Spec) -> Optional[KvStore.Spec]: ...
    @property
    def label(arg0: object) -> Spec: ...
    @property
    def mark_bounds_implicit(arg0: object) -> Spec: ...
    @property
    def ndim(arg0: Spec) -> Optional[int]: ...
    @property
    def oindex(arg0: object) -> Spec: ...
    @property
    def open_mode(arg0: Spec) -> OpenMode: ...
    @property
    def origin(arg0: Spec) -> Tuple[int, ...]: ...
    @property
    def rank(arg0: Spec) -> Optional[int]: ...
    @property
    def schema(arg0: Spec) -> Schema: ...
    @property
    def shape(arg0: Spec) -> Tuple[int, ...]: ...
    @property
    def size(arg0: Spec) -> int: ...
    def to_json(self: Spec, include_defaults: _bool = False) -> Any:
        """Converts to the :json:schema:`JSON representation<TensorStore>`.

        Example:

          >>> spec = ts.Spec({
          ...     'driver': 'n5',
          ...     'kvstore': {
          ...         'driver': 'memory'
          ...     },
          ...     'metadata': {
          ...         'dimensions': [100, 200]
          ...     }
          ... })
          >>> spec = spec[ts.d[0].translate_by[5]]
          >>> spec.to_json()
          {'driver': 'n5',
           'kvstore': {'driver': 'memory'},
           'metadata': {'dimensions': [100, 200]},
           'transform': {'input_exclusive_max': [[105], [200]],
                         'input_inclusive_min': [5, 0],
                         'output': [{'input_dimension': 0, 'offset': -5},
                                    {'input_dimension': 1}]}}

        Group:
          Accessors
        """
        ...

    @property
    def transform(arg0: Spec) -> Optional[IndexTransform]: ...
    @property
    def translate_backward_by(arg0: object) -> Spec: ...
    @property
    def translate_by(arg0: object) -> Spec: ...
    @property
    def translate_to(arg0: object) -> Spec: ...
    def transpose(self: Spec, axes: Optional[DimSelectionLike] = None) -> Spec:
        """Returns a view with a transposed domain.

        This is equivalent to :python:`self[ts.d[axes].transpose[:]]`.

        Args:

          axes: Specifies the existing dimension corresponding to each dimension of the
            new view.  Dimensions may be specified either by index or label.  Specifying
            `None` is equivalent to specifying :python:`[rank-1, ..., 0]`, which
            reverses the dimension order.

        Raises:

          ValueError: If :py:param:`.axes` does not specify a valid permutation.

        See also:
          - `tensorstore.DimExpression.transpose`
          - :py:obj:`.T`

        Group:
          Indexing
        """
        ...

    def update(
        self: Spec,
        *,
        open_mode: Optional[OpenMode] = None,
        open: Optional[_bool] = None,
        create: Optional[_bool] = None,
        delete_existing: Optional[_bool] = None,
        assume_metadata: Optional[_bool] = None,
        assume_cached_metadata: Optional[_bool] = None,
        unbind_context: Optional[_bool] = None,
        strip_context: Optional[_bool] = None,
        context: Optional[Context] = None,
        kvstore: Optional[KvStore.Spec] = None,
        rank: Optional[int] = None,
        dtype: Optional[dtype] = None,
        domain: Optional[IndexDomain] = None,
        shape: Optional[Sequence[int]] = None,
        chunk_layout: Optional[ChunkLayout] = None,
        codec: Optional[CodecSpec] = None,
        fill_value: Optional[numpy.typing.ArrayLike] = None,
        dimension_units: Optional[
            Sequence[Optional[Union[Unit, str, Real, Tuple[Real, str]]]]
        ] = None,
        schema: Optional[Schema] = None,
    ) -> None:
        """Adds additional constraints or changes the open mode.

        Example:

          >>> spec = ts.Spec({'driver': 'n5', 'kvstore': {'driver': 'memory'}})
          >>> spec.update(shape=[100, 200, 300])
          >>> spec
          Spec({
            'driver': 'n5',
            'kvstore': {'driver': 'memory'},
            'schema': {
              'domain': {'exclusive_max': [100, 200, 300], 'inclusive_min': [0, 0, 0]},
            },
            'transform': {
              'input_exclusive_max': [[100], [200], [300]],
              'input_inclusive_min': [0, 0, 0],
            },
          })

        Args:
          open_mode: Overrides the existing open mode.
          open: Allow opening an existing TensorStore.  Overrides the existing open mode.
          create: Allow creating a new TensorStore.  Overrides the existing open mode.  To open or
            create, specify :python:`create=True` and :python:`open=True`.
          delete_existing: Delete any existing data before creating a new array.  Overrides the existing
            open mode.  Must be specified in conjunction with :python:`create=True`.
          assume_metadata: Neither read nor write stored metadata.  Instead, just assume any necessary
            metadata based on constraints in the spec, using the same defaults for any
            unspecified metadata as when creating a new TensorStore.  The stored metadata
            need not even exist.  Operations such as resizing that modify the stored
            metadata are not supported.  Overrides the existing open mode.  Requires that
            :py:param:`.open` is `True` and :py:param:`.delete_existing` is `False`.  This
            option takes precedence over `.assume_cached_metadata` if that option is also
            specified.

            .. warning::

               This option can lead to data corruption if the assumed metadata does
               not match the stored metadata, or multiple concurrent writers use
               different assumed metadata.

            .. seealso:

               - :ref:`python-open-assume-metadata`
          assume_cached_metadata: Skip reading the metadata when opening.  Instead, just assume any necessary
            metadata based on constraints in the spec, using the same defaults for any
            unspecified metadata as when creating a new TensorStore.  The stored metadata
            may still be accessed by subsequent operations that need to re-validate or
            modify the metadata.  Requires that :py:param:`.open` is `True` and
            :py:param:`.delete_existing` is `False`.  The :py:param:`.assume_metadata`
            option takes precedence if also specified.

            .. warning::

               This option can lead to data corruption if the assumed metadata does
               not match the stored metadata, or multiple concurrent writers use
               different assumed metadata.

            .. seealso:

               - :ref:`python-open-assume-metadata`
          unbind_context: Convert any bound context resources to context resource specs that fully capture
            the graph of shared context resources and interdependencies.

            Re-binding/re-opening the resultant spec will result in a new graph of new
            context resources that is isomorphic to the original graph of context resources.
            The resultant spec will not refer to any external context resources;
            consequently, binding it to any specific context will have the same effect as
            binding it to a default context.

            Specifying a value of :python:`False` has no effect.
          strip_context: Replace any bound context resources and unbound context resource specs by
            default context resource specs.

            If the resultant :py:obj:`~tensorstore.Spec` is re-opened with, or re-bound to,
            a new context, it will use the default context resources specified by that
            context.

            Specifying a value of :python:`False` has no effect.
          context: Bind any context resource specs using the specified shared resource context.

            Any already-bound context resources remain unchanged.  Additionally, any context
            resources specified by a nested :json:schema:`TensorStore.context` spec will be
            created as specified, but won't be overridden by :py:param:`.context`.
          kvstore: Sets the associated key-value store used as the underlying storage.

            If the :py:obj:`~tensorstore.Spec.kvstore` has already been set, it is
            overridden.

            It is an error to specify this if the TensorStore driver does not use a
            key-value store.
          rank: Constrains the rank of the TensorStore.  If there is an index transform, the
            rank constraint must match the rank of the *input* space.
          dtype: Constrains the data type of the TensorStore.  If a data type has already been
            set, it is an error to specify a different data type.
          domain: Constrains the domain of the TensorStore.  If there is an existing
            domain, the specified domain is merged with it as follows:

            1. The rank must match the existing rank.

            2. All bounds must match, except that a finite or explicit bound is permitted to
               match an infinite and implicit bound, and takes precedence.

            3. If both the new and existing domain specify non-empty labels for a dimension,
               the labels must be equal.  If only one of the domains specifies a non-empty
               label for a dimension, the non-empty label takes precedence.

            Note that if there is an index transform, the domain must match the *input*
            space, not the output space.
          shape: Constrains the shape and origin of the TensorStore.  Equivalent to specifying a
            :py:param:`domain` of :python:`ts.IndexDomain(shape=shape)`.

            .. note::

               This option also constrains the origin of all dimensions to be zero.
          chunk_layout: Constrains the chunk layout.  If there is an existing chunk layout constraint,
            the constraints are merged.  If the constraints are incompatible, an error
            is raised.
          codec: Constrains the codec.  If there is an existing codec constraint, the constraints
            are merged.  If the constraints are incompatible, an error is raised.
          fill_value: Specifies the fill value for positions that have not been written.

            The fill value data type must be convertible to the actual data type, and the
            shape must be :ref:`broadcast-compatible<index-domain-alignment>` with the
            domain.

            If an existing fill value has already been set as a constraint, it is an
            error to specify a different fill value (where the comparison is done after
            normalization by broadcasting).
          dimension_units: Specifies the physical units of each dimension of the domain.

            The *physical unit* for a dimension is the physical quantity corresponding to a
            single index increment along each dimension.

            A value of :python:`None` indicates that the unit is unknown.  A dimension-less
            quantity can be indicated by a unit of :python:`""`.
          schema: Additional schema constraints to merge with existing constraints.


        Group:
          Mutators
        """
        ...

    @property
    def vindex(arg0: object) -> Spec: ...

class TensorStore:
    class StorageStatistics:
        @property
        def fully_stored(arg0: TensorStore.StorageStatistics) -> Optional[_bool]: ...
        @property
        def not_stored(arg0: TensorStore.StorageStatistics) -> Optional[_bool]: ...

    @property
    def T(arg0: TensorStore) -> TensorStore: ...
    def astype(self: TensorStore, dtype: dtype) -> TensorStore:
        """Returns a read/write view as the specified data type.

        Example:

          >>> store = ts.array([1, 2, 3], dtype=ts.uint32)
          >>> store.astype(ts.string)
          TensorStore({
            'base': {'array': [1, 2, 3], 'driver': 'array', 'dtype': 'uint32'},
            'context': {'data_copy_concurrency': {}},
            'driver': 'cast',
            'dtype': 'string',
            'transform': {'input_exclusive_max': [3], 'input_inclusive_min': [0]},
          })

        Group:
          Data type
        """
        ...

    @property
    def base(arg0: TensorStore) -> Optional[TensorStore]: ...
    @property
    def chunk_layout(arg0: TensorStore) -> ChunkLayout: ...
    @property
    def codec(arg0: TensorStore) -> Optional[CodecSpec]: ...
    @property
    def dimension_units(arg0: TensorStore) -> Tuple[Optional[Unit], ...]: ...
    @property
    def domain(arg0: TensorStore) -> IndexDomain: ...
    @property
    def dtype(arg0: TensorStore) -> dtype: ...
    @property
    def fill_value(arg0: TensorStore) -> Optional[numpy.typing.ArrayLike]: ...
    @property
    def kvstore(arg0: TensorStore) -> Optional[KvStore]: ...
    @property
    def label(arg0: object) -> TensorStore: ...
    @property
    def mark_bounds_implicit(arg0: object) -> TensorStore: ...
    @property
    def mode(arg0: TensorStore) -> str: ...
    @property
    def ndim(arg0: TensorStore) -> int: ...
    @property
    def oindex(arg0: object) -> TensorStore: ...
    @property
    def origin(arg0: TensorStore) -> Tuple[int, ...]: ...
    @property
    def rank(arg0: TensorStore) -> int: ...
    def read(
        self: TensorStore, order: Literal["C", "F"] = "C"
    ) -> Future[numpy.typing.ArrayLike]:
        """Reads the data within the current domain.

        Example:

            >>> dataset = await ts.open(
            ...     {
            ...         'driver': 'zarr',
            ...         'kvstore': {
            ...             'driver': 'memory'
            ...         }
            ...     },
            ...     dtype=ts.uint32,
            ...     shape=[70, 80],
            ...     create=True)
            >>> await dataset[5:10, 8:12].read()
            array([[0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0],
                   [0, 0, 0, 0]], dtype=uint32)

        .. tip::

           Depending on the cache behavior of the driver, the read may be satisfied by
           the cache and not require any I/O.

        When *not* using a :py:obj:`.transaction`, the
        read result only reflects committed data; the result never includes uncommitted
        writes.

        When using a transaction, the read result reflects all writes completed (but not
        yet committed) to the transaction.

        Args:
          order: Contiguous layout order of the returned array:

            :python:`'C'`
              Specifies C order, i.e. lexicographic/row-major order.

            :python:`'F'`
              Specifies Fortran order, i.e. colexicographic/column-major order.

        Returns:
          A future representing the asynchronous read result.

        .. tip::

           Synchronous reads (blocking the current thread) may be performed by calling
           :py:obj:`Future.result` on the returned future:

           >>> dataset[5:10, 8:12].read().result()
           array([[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]], dtype=uint32)

        See also:

          - :py:obj:`.__array__`

        Group:
          I/O
        """
        ...

    @property
    def readable(arg0: TensorStore) -> _bool: ...
    def resize(
        self: TensorStore,
        inclusive_min: Optional[Sequence[Optional[int]]] = None,
        exclusive_max: Optional[Sequence[Optional[int]]] = None,
        resize_metadata_only: _bool = False,
        resize_tied_bounds: _bool = False,
        expand_only: _bool = False,
        shrink_only: _bool = False,
    ) -> Future[TensorStore]:
        """Resizes the current domain, persistently modifying the stored representation.

        Depending on the :py:param`resize_metadata_only`, if the bounds are shrunk,
        existing elements outside of the new bounds may be deleted. If the bounds are
        expanded, elements outside the existing bounds will initially contain either the
        fill value, or existing out-of-bounds data remaining after a prior resize
        operation.

        Example:

            >>> dataset = await ts.open(
            ...     {
            ...         'driver': 'zarr',
            ...         'kvstore': {
            ...             'driver': 'memory'
            ...         }
            ...     },
            ...     dtype=ts.uint32,
            ...     shape=[3, 3],
            ...     create=True)
            >>> await dataset.write(np.arange(9, dtype=np.uint32).reshape((3, 3)))
            >>> dataset = await dataset.resize(exclusive_max=(3, 2))
            >>> await dataset.read()
            array([[0, 1],
                   [3, 4],
                   [6, 7]], dtype=uint32)

        Args:

          inclusive_min: Sequence of length :python:`self.rank()` specifying the new
            inclusive min bounds.  A bound of :python:`None` indicates no change.
          exclusive_max: Sequence of length :python:`self.rank()` specifying the new
            exclusive max bounds.  A bound of :python:`None` indicates no change.
          resize_metadata_only: Requests that, if applicable, the resize operation
            affect only the metadata but not delete data chunks that are outside of the
            new bounds.
          resize_tied_bounds: Requests that the resize be permitted even if other
            bounds tied to the specified bounds must also be resized.  This option
            should be used with caution.
          expand_only: Fail if any bounds would be reduced.
          shrink_only: Fail if any bounds would be increased.

        Returns:

          Future that resolves to a copy of :python:`self` with the updated bounds, once
          the resize operation completes.

        Group:
          I/O
        """
        ...

    def resolve(
        self: TensorStore, fix_resizable_bounds: _bool = False
    ) -> Future[TensorStore]:
        """Obtains updated bounds, subject to the cache policy.

        Group:
          I/O
        """
        ...

    @property
    def schema(arg0: TensorStore) -> Schema: ...
    @property
    def shape(arg0: TensorStore) -> Tuple[int, ...]: ...
    @property
    def size(arg0: TensorStore) -> int: ...
    def spec(
        self: TensorStore,
        *,
        open_mode: Optional[OpenMode] = None,
        open: Optional[_bool] = None,
        create: Optional[_bool] = None,
        delete_existing: Optional[_bool] = None,
        assume_metadata: Optional[_bool] = None,
        assume_cached_metadata: Optional[_bool] = None,
        minimal_spec: Optional[_bool] = None,
        retain_context: Optional[_bool] = None,
        unbind_context: Optional[_bool] = None,
    ) -> Spec:
        """Spec that may be used to re-open or re-create the TensorStore.

        Example:

            >>> dataset = await ts.open(
            ...     {
            ...         'driver': 'zarr',
            ...         'kvstore': {
            ...             'driver': 'memory'
            ...         }
            ...     },
            ...     dtype=ts.uint32,
            ...     shape=[70, 80],
            ...     create=True)
            >>> dataset.spec()
            Spec({
              'driver': 'zarr',
              'dtype': 'uint32',
              'kvstore': {'driver': 'memory'},
              'metadata': {
                'chunks': [70, 80],
                'compressor': {
                  'blocksize': 0,
                  'clevel': 5,
                  'cname': 'lz4',
                  'id': 'blosc',
                  'shuffle': -1,
                },
                'dimension_separator': '.',
                'dtype': '<u4',
                'fill_value': None,
                'filters': None,
                'order': 'C',
                'shape': [70, 80],
                'zarr_format': 2,
              },
              'transform': {
                'input_exclusive_max': [[70], [80]],
                'input_inclusive_min': [0, 0],
              },
            })
            >>> dataset.spec(minimal_spec=True)
            Spec({
              'driver': 'zarr',
              'dtype': 'uint32',
              'kvstore': {'driver': 'memory'},
              'transform': {
                'input_exclusive_max': [[70], [80]],
                'input_inclusive_min': [0, 0],
              },
            })
            >>> dataset.spec(minimal_spec=True, unbind_context=True)
            Spec({
              'context': {
                'cache_pool': {},
                'data_copy_concurrency': {},
                'memory_key_value_store': {},
              },
              'driver': 'zarr',
              'dtype': 'uint32',
              'kvstore': {'driver': 'memory'},
              'transform': {
                'input_exclusive_max': [[70], [80]],
                'input_inclusive_min': [0, 0],
              },
            })

        If neither :py:param:`.retain_context` nor :py:param:`.unbind_context` is
        specified, the returned :py:obj:`~tensorstore.Spec` does not include any context
        resources, equivalent to specifying
        :py:param:`tensorstore.Spec.update.strip_context`.

        Args:

          open_mode: Overrides the existing open mode.
          open: Allow opening an existing TensorStore.  Overrides the existing open mode.
          create: Allow creating a new TensorStore.  Overrides the existing open mode.  To open or
            create, specify :python:`create=True` and :python:`open=True`.
          delete_existing: Delete any existing data before creating a new array.  Overrides the existing
            open mode.  Must be specified in conjunction with :python:`create=True`.
          assume_metadata: Neither read nor write stored metadata.  Instead, just assume any necessary
            metadata based on constraints in the spec, using the same defaults for any
            unspecified metadata as when creating a new TensorStore.  The stored metadata
            need not even exist.  Operations such as resizing that modify the stored
            metadata are not supported.  Overrides the existing open mode.  Requires that
            :py:param:`.open` is `True` and :py:param:`.delete_existing` is `False`.  This
            option takes precedence over `.assume_cached_metadata` if that option is also
            specified.

            .. warning::

               This option can lead to data corruption if the assumed metadata does
               not match the stored metadata, or multiple concurrent writers use
               different assumed metadata.

            .. seealso:

               - :ref:`python-open-assume-metadata`
          assume_cached_metadata: Skip reading the metadata when opening.  Instead, just assume any necessary
            metadata based on constraints in the spec, using the same defaults for any
            unspecified metadata as when creating a new TensorStore.  The stored metadata
            may still be accessed by subsequent operations that need to re-validate or
            modify the metadata.  Requires that :py:param:`.open` is `True` and
            :py:param:`.delete_existing` is `False`.  The :py:param:`.assume_metadata`
            option takes precedence if also specified.

            .. warning::

               This option can lead to data corruption if the assumed metadata does
               not match the stored metadata, or multiple concurrent writers use
               different assumed metadata.

            .. seealso:

               - :ref:`python-open-assume-metadata`
          minimal_spec: Indicates whether to include in the returned :py:obj:`~tensorstore.Spec` the
            metadata necessary to re-create the :py:obj:`~tensorstore.TensorStore`.  By
            default, the returned :py:obj:`~tensorstore.Spec` includes the full metadata,
            but it is skipped if :py:param:`.minimal_spec` is set to :python:`True`.
          retain_context: Retain all bound context resources (e.g. specific concurrency pools, specific
            cache pools).

            The resultant :py:obj:`~tensorstore.Spec` may be used to re-open the
            :py:obj:`~tensorstore.TensorStore` using the identical context resources.

            Specifying a value of :python:`False` has no effect.
          unbind_context: Convert any bound context resources to context resource specs that fully capture
            the graph of shared context resources and interdependencies.

            Re-binding/re-opening the resultant spec will result in a new graph of new
            context resources that is isomorphic to the original graph of context resources.
            The resultant spec will not refer to any external context resources;
            consequently, binding it to any specific context will have the same effect as
            binding it to a default context.

            Specifying a value of :python:`False` has no effect.


        Group:
          Accessors
        """
        ...

    def storage_statistics(
        self: TensorStore,
        *,
        query_not_stored: _bool = False,
        query_fully_stored: _bool = False,
    ) -> Future[TensorStore.StorageStatistics]:
        """Obtains statistics of the data stored for the :py:obj:`.domain`.

        Only the specific information indicated by the parameters will be returned.  If
        no query options are specified, no information will be computed.

        Example:

            >>> store = await ts.open({
            ...     "driver": "zarr",
            ...     "kvstore": "memory://"
            ... },
            ...                       shape=(100, 200),
            ...                       dtype=ts.uint32,
            ...                       create=True)
            >>> await store.storage_statistics(query_not_stored=True)
            TensorStore.StorageStatistics(not_stored=True, fully_stored=None)
            >>> await store[10:20, 30:40].write(5)
            >>> await store.storage_statistics(query_not_stored=True)
            TensorStore.StorageStatistics(not_stored=False, fully_stored=None)
            >>> await store.storage_statistics(query_not_stored=True,
            ...                                query_fully_stored=True)
            TensorStore.StorageStatistics(not_stored=False, fully_stored=True)
            >>> await store[10:20, 30:40].storage_statistics(query_fully_stored=True)
            TensorStore.StorageStatistics(not_stored=None, fully_stored=True)

        Args:

          query_not_stored: Check whether there is data stored for *any* element of the
            :py:obj:`.domain`.

          query_fully_stored: Check whether there is data stored for *all* elements of
            the :py:obj:`.domain`.

            .. warning::

                 Enabling this option may significantly increase the cost of the
                 :py:obj:`.storage_statistics` query.

        Returns:
          The requested statistics.

        Raises:
          NotImplementedError: If the :ref:`driver<tensorstore-drivers>` does not
            support this operation.

        Group:
          I/O
        """
        ...

    @property
    def transaction(arg0: TensorStore) -> Optional[Transaction]: ...
    @property
    def translate_backward_by(arg0: object) -> TensorStore: ...
    @property
    def translate_by(arg0: object) -> TensorStore: ...
    @property
    def translate_to(arg0: object) -> TensorStore: ...
    def transpose(
        self: TensorStore, axes: Optional[DimSelectionLike] = None
    ) -> TensorStore:
        """Returns a view with a transposed domain.

        This is equivalent to :python:`self[ts.d[axes].transpose[:]]`.

        Args:

          axes: Specifies the existing dimension corresponding to each dimension of the
            new view.  Dimensions may be specified either by index or label.  Specifying
            `None` is equivalent to specifying :python:`[rank-1, ..., 0]`, which
            reverses the dimension order.

        Raises:

          ValueError: If :py:param:`.axes` does not specify a valid permutation.

        See also:
          - `tensorstore.DimExpression.transpose`
          - :py:obj:`.T`

        Group:
          Indexing
        """
        ...

    @property
    def vindex(arg0: object) -> TensorStore: ...
    def with_transaction(
        self: TensorStore, transaction: Optional[Transaction]
    ) -> TensorStore:
        """Returns a transaction-bound view of this TensorStore.

        The returned view may be used to perform transactional read/write operations.

        Group:
          Transactions
        """
        ...

    @property
    def writable(arg0: TensorStore) -> _bool: ...
    def write(
        self: TensorStore, source: Union[TensorStore, numpy.typing.ArrayLike]
    ) -> WriteFutures:
        """Writes to the current domain.

        Example:

            >>> dataset = await ts.open(
            ...     {
            ...         'driver': 'zarr',
            ...         'kvstore': {
            ...             'driver': 'memory'
            ...         }
            ...     },
            ...     dtype=ts.uint32,
            ...     shape=[70, 80],
            ...     create=True)
            >>> await dataset[5:10, 6:8].write(42)
            >>> await dataset[0:10, 0:10].read()
            array([[ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                   [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
                   [ 0,  0,  0,  0,  0,  0, 42, 42,  0,  0],
                   [ 0,  0,  0,  0,  0,  0, 42, 42,  0,  0],
                   [ 0,  0,  0,  0,  0,  0, 42, 42,  0,  0],
                   [ 0,  0,  0,  0,  0,  0, 42, 42,  0,  0],
                   [ 0,  0,  0,  0,  0,  0, 42, 42,  0,  0]], dtype=uint32)
            >>> await dataset[5:10, 6:8].write([1, 2])
            >>> await dataset[5:10, 6:8].read()
            array([[1, 2],
                   [1, 2],
                   [1, 2],
                   [1, 2],
                   [1, 2]], dtype=uint32)

        Args:

          source: Source array, :ref:`broadcast-compatible<index-domain-alignment>` with
            :python:`self.domain` and with a data type convertible to
            :python:`self.dtype`.  May be an existing :py:obj:`TensorStore` or any
            :py:obj:`~numpy.typing.ArrayLike`, including a scalar.

        Returns:

          Future representing the asynchronous result of the write operation.

        Logically there are two steps to the write operation:

        1. reading/copying from the :python:`source`, and

        2. waiting for the write to be committed, such that it will be reflected in
           subsequent reads.

        The completion of these two steps can be tracked separately using the returned
        :py:obj:`WriteFutures.copy` and :py:obj:`WriteFutures.commit` futures,
        respectively:

        Waiting on the returned `WriteFutures` object itself waits for
        the entire write operation to complete, and is equivalent to waiting on the
        :py:obj:`WriteFutures.commit` future.  The returned
        :py:obj:`WriteFutures.copy` future becomes ready once the data has been fully
        read from :python:`source`.  After this point, :python:`source` may be safely
        modified without affecting the write operation.

        .. warning::

           You must either synchronously or asynchronously wait on the returned future
           in order to ensure the write actually completes.  If all references to the
           future are dropped without waiting on it, the write may be cancelled.

        Group:
          I/O

        Non-transactional semantics
        ---------------------------

        When *not* using a :py:obj:`Transaction`, the returned `WriteFutures.commit`
        future becomes ready only once the data has been durably committed by the
        underlying storage layer.  The precise durability guarantees depend on the
        driver, but for example:

        - when using the :ref:`file-kvstore-driver`, the data is only considered
          committed once the ``fsync`` system call completes, which should normally
          guarantee that it will survive a system crash;

        - when using the :ref:`gcs-kvstore-driver`, the data is only considered
          committed once the write is acknowledged and durability is guaranteed by
          Google Cloud Storage.

        Because committing a write often has significant latency, it is advantageous to
        issue multiple writes concurrently and then wait on all of them jointly:

            >>> dataset = await ts.open(
            ...     {
            ...         'driver': 'zarr',
            ...         'kvstore': {
            ...             'driver': 'memory'
            ...         }
            ...     },
            ...     dtype=ts.uint32,
            ...     shape=[70, 80],
            ...     create=True)
            >>> await asyncio.wait([
            ...     asyncio.ensure_future(dataset[i * 5].write(i)) for i in range(10)
            ... ])

        This can also be accomplished with synchronous blocking:

            >>> dataset = ts.open({
            ...     'driver': 'zarr',
            ...     'kvstore': {
            ...         'driver': 'memory'
            ...     }
            ... },
            ...                   dtype=ts.uint32,
            ...                   shape=[70, 80],
            ...                   create=True).result()
            >>> futures = [dataset[i * 5].write(i) for i in range(10)]
            >>> for f in futures:
            ...     f.result()

        Note:

          When issuing writes asynchronously, keep in mind that uncommitted writes are
          never reflected in non-transactional reads.

        For most drivers, data is written in fixed-size
        :ref:`write chunks<chunk-layout>` arranged in a regular grid.  When concurrently
        issuing multiple writes that are not perfectly aligned to disjoint write chunks,
        specifying a :json:schema:`Context.cache_pool` enables writeback caching, which
        can improve efficiency by coalescing multiple writes to the same chunk.

        Alternatively, for more explicit control over writeback behavior, you can use a
        :py:obj:`Transaction`.

        Transactional semantics
        -----------------------

        Transactions provide explicit control over writeback, and allow uncommitted
        writes to be read:

            >>> txn = ts.Transaction()
            >>> dataset = await ts.open(
            ...     {
            ...         'driver': 'zarr',
            ...         'kvstore': {
            ...             'driver': 'memory'
            ...         }
            ...     },
            ...     dtype=ts.uint32,
            ...     shape=[70, 80],
            ...     create=True)
            >>> await dataset.with_transaction(txn)[5:10, 6:8].write([1, 2])
            >>> # Transactional read reflects uncommitted write
            >>> await dataset.with_transaction(txn)[5:10, 6:8].read()
            array([[1, 2],
                   [1, 2],
                   [1, 2],
                   [1, 2],
                   [1, 2]], dtype=uint32)
            >>> # Non-transactional read does not reflect uncommitted write
            >>> await dataset[5:10, 6:8].read()
            array([[0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0],
                   [0, 0]], dtype=uint32)
            >>> await txn.commit_async()
            >>> # Now, non-transactional read reflects committed write
            >>> await dataset[5:10, 6:8].read()
            array([[1, 2],
                   [1, 2],
                   [1, 2],
                   [1, 2],
                   [1, 2]], dtype=uint32)

        .. warning::

           When using a :py:obj:`Transaction`, the returned `WriteFutures.commit` future
           does *not* indicate that the data is durably committed by the underlying
           storage layer.  Instead, it merely indicates that the write will be reflected
           in any subsequent reads *using the same transaction*.  The write is only
           durably committed once the *transaction* is committed successfully.
        """
        ...

class Transaction:
    def abort(self: Transaction) -> None:
        """Aborts the transaction.

        Has no effect if :py:meth:`.commit_async` or :py:meth:`.abort` has already been
        called.

          - :py:obj:`.commit_async`

        Group:
          Operations
        """
        ...

    @property
    def aborted(arg0: Transaction) -> _bool: ...
    @property
    def atomic(arg0: Transaction) -> _bool: ...
    def commit_async(self: Transaction) -> Future[None]:
        """Asynchronously commits the transaction.

        Has no effect if :py:meth:`.commit_async` or :py:meth:`.abort` has already been
        called.

        Returns the associated :py:obj:`.future`, which may be used to check if the
        commit was successful.

        See also:

          - :py:obj:`.commit_sync`
          - :py:obj:`.abort`

        Group:
          Operations
        """
        ...

    @property
    def commit_started(arg0: Transaction) -> _bool: ...
    def commit_sync(self: Transaction) -> None:
        """Synchronously commits the transaction.

        Equivalent to :python:`self.commit_async().result()`.

        Returns:

           :py:obj:`None` if the commit is successful, and raises an error otherwise.

        See also:

          - :py:obj:`.commit_async`
          - :py:obj:`.abort`

        Group:
          Operations
        """
        ...

    @property
    def future(arg0: Transaction) -> Future[None]: ...
    @property
    def open(arg0: Transaction) -> _bool: ...

class Unit:
    @property
    def base_unit(arg0: Unit) -> str: ...
    @property
    def multiplier(arg0: Unit) -> float: ...
    def to_json(self: Unit) -> Any:
        """Converts to the :json:schema:`JSON representation<Unit>`.

        Example:

          >>> ts.Unit('3nm').to_json()
          [3.0, 'nm']

        Group:
          Accessors
        """
        ...

class VirtualChunkedReadParameters:
    @property
    def if_not_equal(arg0: VirtualChunkedReadParameters) -> bytes: ...
    @property
    def staleness_bound(arg0: VirtualChunkedReadParameters) -> float: ...

class VirtualChunkedWriteParameters:
    @property
    def if_equal(arg0: VirtualChunkedWriteParameters) -> bytes: ...

class WriteFutures:
    def add_done_callback(
        self: WriteFutures, callback: Callable[[Future], None]
    ) -> None:
        """ """
        ...

    def cancel(self: WriteFutures) -> _bool:
        """ """
        ...

    def cancelled(self: WriteFutures) -> _bool:
        """ """
        ...

    @property
    def commit(arg0: WriteFutures) -> Future[None]: ...
    @property
    def copy(arg0: WriteFutures) -> Future[None]: ...
    def done(self: WriteFutures) -> _bool:
        """ """
        ...

    def exception(
        self: WriteFutures,
        timeout: Optional[float] = None,
        deadline: Optional[float] = None,
    ) -> object:
        """ """
        ...

    def remove_done_callback(
        self: WriteFutures, callback: Callable[[Future], None]
    ) -> int:
        """ """
        ...

    def result(
        self: WriteFutures,
        timeout: Optional[float] = None,
        deadline: Optional[float] = None,
    ) -> object:
        """ """
        ...

def array(
    array: numpy.typing.ArrayLike,
    dtype: Optional[dtype] = None,
    context: Context = None,
) -> TensorStore:
    """Returns a TensorStore that reads/writes from an in-memory array.

    Args:
      array: Source array.
      dtype: Data type to which :python:`array` will be converted.
      context: Context to use.

    Group:
      Views
    """
    ...

bfloat16 = dtype("bfloat16")
bool = dtype("bool")
byte = dtype("byte")

def cast(*args, **kwargs):
    """Overloaded function.

    1. cast(base: tensorstore.TensorStore, dtype: tensorstore.dtype) -> tensorstore.TensorStore


    Returns a read/write view with the data type converted.

    Example:

        >>> array = ts.array([1.5, 2.5, 3.5, 4.5, 5.5], dtype=ts.float32)
        >>> view = ts.cast(array, ts.uint32)
        >>> view
        TensorStore({
          'base': {
            'array': [1.5, 2.5, 3.5, 4.5, 5.5],
            'driver': 'array',
            'dtype': 'float32',
          },
          'context': {'data_copy_concurrency': {}},
          'driver': 'cast',
          'dtype': 'uint32',
          'transform': {'input_exclusive_max': [5], 'input_inclusive_min': [0]},
        })
        >>> await view.read()
        array([1, 2, 3, 4, 5], dtype=uint32)

    Overload:
      store

    Group:
      Views


    2. cast(base: tensorstore.Spec, dtype: tensorstore.dtype) -> tensorstore.Spec


    Returns a view with the data type converted.

    Example:

        >>> base = ts.Spec({"driver": "zarr", "kvstore": "memory://"})
        >>> view = ts.cast(base, ts.uint32)
        >>> view
        Spec({
          'base': {'driver': 'zarr', 'kvstore': {'driver': 'memory'}},
          'driver': 'cast',
          'dtype': 'uint32',
        })

    Overload:
      spec

    Group:
      Views
    """
    ...

char = dtype("char")
complex128 = dtype("complex128")
complex64 = dtype("complex64")

def concat(
    layers: Sequence[Union[TensorStore, Spec]],
    axis: Union[int, str],
    *,
    read: Optional[_bool] = None,
    write: Optional[_bool] = None,
    context: Optional[Context] = None,
    transaction: Optional[Transaction] = None,
    rank: Optional[int] = None,
    dtype: Optional[dtype] = None,
    domain: Optional[IndexDomain] = None,
    shape: Optional[Sequence[int]] = None,
    dimension_units: Optional[
        Sequence[Optional[Union[Unit, str, Real, Tuple[Real, str]]]]
    ] = None,
    schema: Optional[Schema] = None,
) -> TensorStore:
    """Virtually concatenates a sequence of :py:obj:`TensorStore` layers along an existing dimension.

        >>> store = ts.concat([
        ...     ts.array([1, 2, 3, 4], dtype=ts.uint32),
        ...     ts.array([5, 6, 7, 8], dtype=ts.uint32)
        ... ],
        ...                   axis=0)
        >>> store
        TensorStore({
          'context': {'data_copy_concurrency': {}},
          'driver': 'stack',
          'dtype': 'uint32',
          'layers': [
            {
              'array': [1, 2, 3, 4],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {'input_exclusive_max': [4], 'input_inclusive_min': [0]},
            },
            {
              'array': [5, 6, 7, 8],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {
                'input_exclusive_max': [8],
                'input_inclusive_min': [4],
                'output': [{'input_dimension': 0, 'offset': -4}],
              },
            },
          ],
          'schema': {'domain': {'exclusive_max': [8], 'inclusive_min': [0]}},
          'transform': {'input_exclusive_max': [8], 'input_inclusive_min': [0]},
        })
        >>> await store.read()
        array([1, 2, 3, 4, 5, 6, 7, 8], dtype=uint32)
        >>> store = ts.concat([
        ...     ts.array([[1, 2, 3], [4, 5, 6]], dtype=ts.uint32),
        ...     ts.array([[7, 8, 9], [10, 11, 12]], dtype=ts.uint32)
        ... ],
        ...                   axis=0)
        >>> store
        TensorStore({
          'context': {'data_copy_concurrency': {}},
          'driver': 'stack',
          'dtype': 'uint32',
          'layers': [
            {
              'array': [[1, 2, 3], [4, 5, 6]],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {
                'input_exclusive_max': [2, 3],
                'input_inclusive_min': [0, 0],
              },
            },
            {
              'array': [[7, 8, 9], [10, 11, 12]],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {
                'input_exclusive_max': [4, 3],
                'input_inclusive_min': [2, 0],
                'output': [
                  {'input_dimension': 0, 'offset': -2},
                  {'input_dimension': 1},
                ],
              },
            },
          ],
          'schema': {'domain': {'exclusive_max': [4, 3], 'inclusive_min': [0, 0]}},
          'transform': {'input_exclusive_max': [4, 3], 'input_inclusive_min': [0, 0]},
        })
        >>> await store.read()
        array([[ 1,  2,  3],
               [ 4,  5,  6],
               [ 7,  8,  9],
               [10, 11, 12]], dtype=uint32)
        >>> store = ts.concat([
        ...     ts.array([[1, 2, 3], [4, 5, 6]], dtype=ts.uint32),
        ...     ts.array([[7, 8, 9], [10, 11, 12]], dtype=ts.uint32)
        ... ],
        ...                   axis=-1)
        >>> store
        TensorStore({
          'context': {'data_copy_concurrency': {}},
          'driver': 'stack',
          'dtype': 'uint32',
          'layers': [
            {
              'array': [[1, 2, 3], [4, 5, 6]],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {
                'input_exclusive_max': [2, 3],
                'input_inclusive_min': [0, 0],
              },
            },
            {
              'array': [[7, 8, 9], [10, 11, 12]],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {
                'input_exclusive_max': [2, 6],
                'input_inclusive_min': [0, 3],
                'output': [
                  {'input_dimension': 0},
                  {'input_dimension': 1, 'offset': -3},
                ],
              },
            },
          ],
          'schema': {'domain': {'exclusive_max': [2, 6], 'inclusive_min': [0, 0]}},
          'transform': {'input_exclusive_max': [2, 6], 'input_inclusive_min': [0, 0]},
        })
        >>> await store.read()
        array([[ 1,  2,  3,  7,  8,  9],
               [ 4,  5,  6, 10, 11, 12]], dtype=uint32)
        >>> await ts.concat([
        ...     ts.array([[1, 2, 3], [4, 5, 6]], dtype=ts.uint32).label["x", "y"],
        ...     ts.array([[7, 8, 9], [10, 11, 12]], dtype=ts.uint32)
        ... ],
        ...                 axis="y").read()
        array([[ 1,  2,  3,  7,  8,  9],
               [ 4,  5,  6, 10, 11, 12]], dtype=uint32)

    Args:

      layers: Sequence of layers to concatenate.  If a layer is specified as a
        :py:obj:`Spec` rather than a :py:obj:`TensorStore`, it must have a known
        :py:obj:`~Spec.domain` and will be opened on-demand as needed for individual
        read and write operations.

      axis: Existing dimension along which to concatenate.  A negative number counts
        from the end.  May also be specified by a
        :ref:`dimension label<dimension-labels>`.
      read: Allow read access.  Defaults to `True` if neither ``read`` nor ``write`` is specified.
      write: Allow write access.  Defaults to `True` if neither ``read`` nor ``write`` is specified.
      context: Shared resource context.  Defaults to a new (unshared) context with default
        options, as returned by :py:meth:`tensorstore.Context`.  To share resources,
        such as cache pools, between multiple open TensorStores, you must specify a
        context.
      transaction: Transaction to use for opening/creating, and for subsequent operations.  By
        default, the open is non-transactional.

        .. note::

           To perform transactional operations using a :py:obj:`TensorStore` that was
           previously opened without a transaction, use
           :py:obj:`TensorStore.with_transaction`.
      rank: Constrains the rank of the TensorStore.  If there is an index transform, the
        rank constraint must match the rank of the *input* space.
      dtype: Constrains the data type of the TensorStore.  If a data type has already been
        set, it is an error to specify a different data type.
      domain: Constrains the domain of the TensorStore.  If there is an existing
        domain, the specified domain is merged with it as follows:

        1. The rank must match the existing rank.

        2. All bounds must match, except that a finite or explicit bound is permitted to
           match an infinite and implicit bound, and takes precedence.

        3. If both the new and existing domain specify non-empty labels for a dimension,
           the labels must be equal.  If only one of the domains specifies a non-empty
           label for a dimension, the non-empty label takes precedence.

        Note that if there is an index transform, the domain must match the *input*
        space, not the output space.
      shape: Constrains the shape and origin of the TensorStore.  Equivalent to specifying a
        :py:param:`domain` of :python:`ts.IndexDomain(shape=shape)`.

        .. note::

           This option also constrains the origin of all dimensions to be zero.
      dimension_units: Specifies the physical units of each dimension of the domain.

        The *physical unit* for a dimension is the physical quantity corresponding to a
        single index increment along each dimension.

        A value of :python:`None` indicates that the unit is unknown.  A dimension-less
        quantity can be indicated by a unit of :python:`""`.
      schema: Additional schema constraints to merge with existing constraints.


    See also:
      - :py:obj:`numpy.concatenate`
      - :ref:`stack-driver`
      - :py:obj:`tensorstore.overlay`
      - :py:obj:`tensorstore.stack`

    Group:
      Views
    """
    ...

class d:
    @property
    def diagonal(arg0: DimExpression) -> DimExpression: ...
    @property
    def label(arg0: object) -> DimExpression: ...
    @property
    def mark_bounds_implicit(arg0: object) -> DimExpression: ...
    @property
    def oindex(arg0: object) -> DimExpression: ...
    @property
    def stride(arg0: object) -> DimExpression: ...
    @property
    def translate_backward_by(arg0: object) -> DimExpression: ...
    @property
    def translate_by(arg0: object) -> DimExpression: ...
    @property
    def translate_to(arg0: object) -> DimExpression: ...
    @property
    def transpose(arg0: object) -> DimExpression: ...
    @property
    def vindex(arg0: object) -> DimExpression: ...

def downsample(*args, **kwargs):
    """Overloaded function.

    1. downsample(base: tensorstore.TensorStore, downsample_factors: List[int], method: DownsampleMethod) -> tensorstore.TensorStore


    Returns a virtual :ref:`downsampled view<driver/downsample>` of a :py:obj:`TensorStore`.

    Group:
      Views

    Overload:
      store


    2. downsample(base: tensorstore.Spec, downsample_factors: List[int], method: DownsampleMethod) -> tensorstore.Spec


    Returns a virtual :ref:`downsampled view<driver/downsample>` view of a :py:obj:`Spec`.

    Group:
      Views

    Overload:
      spec
    """
    ...

class dtype:
    def __init__(self, name: str) -> None: ...
    @property
    def name(arg0: dtype) -> str: ...
    @property
    def numpy_dtype(arg0: dtype) -> dtype: ...
    def to_json(self: dtype) -> str:
        """ """
        ...

    @property
    def type(arg0: dtype) -> object: ...

def experimental_collect_matching_metrics(
    metric_prefix: str = "", include_zero_metrics: _bool = False
) -> List[Any]:
    """Collects metrics with a matching prefix.

    Args:
      metric_prefix: Prefix of the metric names to collect.
      include_zero_metrics: Indicate whether zero-valued metrics are included.

    Returns:
      :py:obj:`list` of a :py:obj:`dict` of metrics.

    Group:
      Experimental
    """
    ...

def experimental_collect_prometheus_format_metrics(
    metric_prefix: str = "",
) -> List[str]:
    """Collects metrics in prometheus exposition format.
    See: https://prometheus.io/docs/instrumenting/exposition_formats/

    Args:
      metric_prefix: Prefix of the metric names to collect.

    Returns:
      :py:obj:`list` of a :py:obj:`str` of prometheus exposition format metrics.

    Group:
      Experimental
    """
    ...

def experimental_push_metrics_to_prometheus(
    pushgateway: str = "", job: str = "", instance: str = "", metric_prefix: str = ""
) -> Future[int]:
    """Publishes metrics to the prometheus pushgateway.
    See: https://github.com/prometheus/pushgateway

    Args:
      pushgateway: prometheus pushgateway url, like 'http://localhost:1234/'
      job: prometheus job name
      instance: prometheus instance identifier
      metric_prefix: Prefix of the metric names to publish.

    Returns:
      A future with the response status code.

    Group:
      Experimental
    """
    ...

float16 = dtype("float16")
float32 = dtype("float32")
float64 = dtype("float64")
float8_e4m3b11fnuz = dtype("float8_e4m3b11fnuz")
float8_e4m3fn = dtype("float8_e4m3fn")
float8_e4m3fnuz = dtype("float8_e4m3fnuz")
float8_e5m2 = dtype("float8_e5m2")
float8_e5m2fnuz = dtype("float8_e5m2fnuz")
inf = 4611686018427387903
int16 = dtype("int16")
int32 = dtype("int32")
int4 = dtype("int4")
int64 = dtype("int64")
int8 = dtype("int8")
json = dtype("json")
newaxis = None

def open(
    spec: Union[Spec, Any],
    *,
    read: Optional[_bool] = None,
    write: Optional[_bool] = None,
    open_mode: Optional[OpenMode] = None,
    open: Optional[_bool] = None,
    create: Optional[_bool] = None,
    delete_existing: Optional[_bool] = None,
    assume_metadata: Optional[_bool] = None,
    assume_cached_metadata: Optional[_bool] = None,
    context: Optional[Context] = None,
    transaction: Optional[Transaction] = None,
    kvstore: Optional[KvStore.Spec] = None,
    rank: Optional[int] = None,
    dtype: Optional[dtype] = None,
    domain: Optional[IndexDomain] = None,
    shape: Optional[Sequence[int]] = None,
    chunk_layout: Optional[ChunkLayout] = None,
    codec: Optional[CodecSpec] = None,
    fill_value: Optional[numpy.typing.ArrayLike] = None,
    dimension_units: Optional[
        Sequence[Optional[Union[Unit, str, Real, Tuple[Real, str]]]]
    ] = None,
    schema: Optional[Schema] = None,
) -> Future[TensorStore]:
    """Opens or creates a :py:class:`TensorStore` from a :py:class:`Spec`.

        >>> store = await ts.open(
        ...     {
        ...         'driver': 'zarr',
        ...         'kvstore': {
        ...             'driver': 'memory'
        ...         }
        ...     },
        ...     create=True,
        ...     dtype=ts.int32,
        ...     shape=[1000, 2000, 3000],
        ...     chunk_layout=ts.ChunkLayout(inner_order=[2, 1, 0]),
        ... )
        >>> store
        TensorStore({
          'context': {
            'cache_pool': {},
            'data_copy_concurrency': {},
            'memory_key_value_store': {},
          },
          'driver': 'zarr',
          'dtype': 'int32',
          'kvstore': {'driver': 'memory'},
          'metadata': {
            'chunks': [101, 101, 101],
            'compressor': {
              'blocksize': 0,
              'clevel': 5,
              'cname': 'lz4',
              'id': 'blosc',
              'shuffle': -1,
            },
            'dimension_separator': '.',
            'dtype': '<i4',
            'fill_value': None,
            'filters': None,
            'order': 'F',
            'shape': [1000, 2000, 3000],
            'zarr_format': 2,
          },
          'transform': {
            'input_exclusive_max': [[1000], [2000], [3000]],
            'input_inclusive_min': [0, 0, 0],
          },
        })

    Args:
      spec: TensorStore Spec to open.  May also be specified as :json:schema:`JSON<TensorStore>`.

      read: Allow read access.  Defaults to `True` if neither ``read`` nor ``write`` is specified.
      write: Allow write access.  Defaults to `True` if neither ``read`` nor ``write`` is specified.
      open_mode: Overrides the existing open mode.
      open: Allow opening an existing TensorStore.  Overrides the existing open mode.
      create: Allow creating a new TensorStore.  Overrides the existing open mode.  To open or
        create, specify :python:`create=True` and :python:`open=True`.
      delete_existing: Delete any existing data before creating a new array.  Overrides the existing
        open mode.  Must be specified in conjunction with :python:`create=True`.
      assume_metadata: Neither read nor write stored metadata.  Instead, just assume any necessary
        metadata based on constraints in the spec, using the same defaults for any
        unspecified metadata as when creating a new TensorStore.  The stored metadata
        need not even exist.  Operations such as resizing that modify the stored
        metadata are not supported.  Overrides the existing open mode.  Requires that
        :py:param:`.open` is `True` and :py:param:`.delete_existing` is `False`.  This
        option takes precedence over `.assume_cached_metadata` if that option is also
        specified.

        .. warning::

           This option can lead to data corruption if the assumed metadata does
           not match the stored metadata, or multiple concurrent writers use
           different assumed metadata.

        .. seealso:

           - :ref:`python-open-assume-metadata`
      assume_cached_metadata: Skip reading the metadata when opening.  Instead, just assume any necessary
        metadata based on constraints in the spec, using the same defaults for any
        unspecified metadata as when creating a new TensorStore.  The stored metadata
        may still be accessed by subsequent operations that need to re-validate or
        modify the metadata.  Requires that :py:param:`.open` is `True` and
        :py:param:`.delete_existing` is `False`.  The :py:param:`.assume_metadata`
        option takes precedence if also specified.

        .. warning::

           This option can lead to data corruption if the assumed metadata does
           not match the stored metadata, or multiple concurrent writers use
           different assumed metadata.

        .. seealso:

           - :ref:`python-open-assume-metadata`
      context: Shared resource context.  Defaults to a new (unshared) context with default
        options, as returned by :py:meth:`tensorstore.Context`.  To share resources,
        such as cache pools, between multiple open TensorStores, you must specify a
        context.
      transaction: Transaction to use for opening/creating, and for subsequent operations.  By
        default, the open is non-transactional.

        .. note::

           To perform transactional operations using a :py:obj:`TensorStore` that was
           previously opened without a transaction, use
           :py:obj:`TensorStore.with_transaction`.
      kvstore: Sets the associated key-value store used as the underlying storage.

        If the :py:obj:`~tensorstore.Spec.kvstore` has already been set, it is
        overridden.

        It is an error to specify this if the TensorStore driver does not use a
        key-value store.
      rank: Constrains the rank of the TensorStore.  If there is an index transform, the
        rank constraint must match the rank of the *input* space.
      dtype: Constrains the data type of the TensorStore.  If a data type has already been
        set, it is an error to specify a different data type.
      domain: Constrains the domain of the TensorStore.  If there is an existing
        domain, the specified domain is merged with it as follows:

        1. The rank must match the existing rank.

        2. All bounds must match, except that a finite or explicit bound is permitted to
           match an infinite and implicit bound, and takes precedence.

        3. If both the new and existing domain specify non-empty labels for a dimension,
           the labels must be equal.  If only one of the domains specifies a non-empty
           label for a dimension, the non-empty label takes precedence.

        Note that if there is an index transform, the domain must match the *input*
        space, not the output space.
      shape: Constrains the shape and origin of the TensorStore.  Equivalent to specifying a
        :py:param:`domain` of :python:`ts.IndexDomain(shape=shape)`.

        .. note::

           This option also constrains the origin of all dimensions to be zero.
      chunk_layout: Constrains the chunk layout.  If there is an existing chunk layout constraint,
        the constraints are merged.  If the constraints are incompatible, an error
        is raised.
      codec: Constrains the codec.  If there is an existing codec constraint, the constraints
        are merged.  If the constraints are incompatible, an error is raised.
      fill_value: Specifies the fill value for positions that have not been written.

        The fill value data type must be convertible to the actual data type, and the
        shape must be :ref:`broadcast-compatible<index-domain-alignment>` with the
        domain.

        If an existing fill value has already been set as a constraint, it is an
        error to specify a different fill value (where the comparison is done after
        normalization by broadcasting).
      dimension_units: Specifies the physical units of each dimension of the domain.

        The *physical unit* for a dimension is the physical quantity corresponding to a
        single index increment along each dimension.

        A value of :python:`None` indicates that the unit is unknown.  A dimension-less
        quantity can be indicated by a unit of :python:`""`.
      schema: Additional schema constraints to merge with existing constraints.


    Examples
    ========

    Opening an existing TensorStore
    -------------------------------

    To open an existing TensorStore, you can use a *minimal* :py:class:`.Spec` that
    specifies required driver-specific options, like the storage location.
    Information that can be determined automatically from the existing metadata,
    like the data type, domain, and chunk layout, may be omitted:

        >>> store = await ts.open(
        ...     {
        ...         'driver': 'neuroglancer_precomputed',
        ...         'kvstore': {
        ...             'driver': 'gcs',
        ...             'bucket': 'neuroglancer-janelia-flyem-hemibrain',
        ...             'path': 'v1.2/segmentation/',
        ...         },
        ...     },
        ...     read=True)
        >>> store
        TensorStore({
          'context': {
            'cache_pool': {},
            'data_copy_concurrency': {},
            'gcs_request_concurrency': {},
            'gcs_request_retries': {},
            'gcs_user_project': {},
          },
          'driver': 'neuroglancer_precomputed',
          'dtype': 'uint64',
          'kvstore': {
            'bucket': 'neuroglancer-janelia-flyem-hemibrain',
            'driver': 'gcs',
            'path': 'v1.2/segmentation/',
          },
          'multiscale_metadata': {'num_channels': 1, 'type': 'segmentation'},
          'scale_index': 0,
          'scale_metadata': {
            'chunk_size': [64, 64, 64],
            'compressed_segmentation_block_size': [8, 8, 8],
            'encoding': 'compressed_segmentation',
            'key': '8.0x8.0x8.0',
            'resolution': [8.0, 8.0, 8.0],
            'sharding': {
              '@type': 'neuroglancer_uint64_sharded_v1',
              'data_encoding': 'gzip',
              'hash': 'identity',
              'minishard_bits': 6,
              'minishard_index_encoding': 'gzip',
              'preshift_bits': 9,
              'shard_bits': 15,
            },
            'size': [34432, 39552, 41408],
            'voxel_offset': [0, 0, 0],
          },
          'transform': {
            'input_exclusive_max': [34432, 39552, 41408, 1],
            'input_inclusive_min': [0, 0, 0, 0],
            'input_labels': ['x', 'y', 'z', 'channel'],
          },
        })

    Creating a new TensorStore
    --------------------------

    To create a new TensorStore, you must specify required driver-specific options,
    like the storage location, as well as :py:class:`Schema` constraints like the
    data type and domain.  Suitable defaults are chosen automatically for schema
    properties that are left unconstrained:

        >>> store = await ts.open(
        ...     {
        ...         'driver': 'zarr',
        ...         'kvstore': {
        ...             'driver': 'memory'
        ...         },
        ...     },
        ...     create=True,
        ...     dtype=ts.float32,
        ...     shape=[1000, 2000, 3000],
        ...     fill_value=42)
        >>> store
        TensorStore({
          'context': {
            'cache_pool': {},
            'data_copy_concurrency': {},
            'memory_key_value_store': {},
          },
          'driver': 'zarr',
          'dtype': 'float32',
          'kvstore': {'driver': 'memory'},
          'metadata': {
            'chunks': [101, 101, 101],
            'compressor': {
              'blocksize': 0,
              'clevel': 5,
              'cname': 'lz4',
              'id': 'blosc',
              'shuffle': -1,
            },
            'dimension_separator': '.',
            'dtype': '<f4',
            'fill_value': 42.0,
            'filters': None,
            'order': 'C',
            'shape': [1000, 2000, 3000],
            'zarr_format': 2,
          },
          'transform': {
            'input_exclusive_max': [[1000], [2000], [3000]],
            'input_inclusive_min': [0, 0, 0],
          },
        })

    Partial constraints may be specified on the chunk layout, and the driver will
    determine a matching chunk layout automatically:

        >>> store = await ts.open(
        ...     {
        ...         'driver': 'zarr',
        ...         'kvstore': {
        ...             'driver': 'memory'
        ...         },
        ...     },
        ...     create=True,
        ...     dtype=ts.float32,
        ...     shape=[1000, 2000, 3000],
        ...     chunk_layout=ts.ChunkLayout(
        ...         chunk_shape=[10, None, None],
        ...         chunk_aspect_ratio=[None, 2, 1],
        ...         chunk_elements=10000000,
        ...     ),
        ... )
        >>> store
        TensorStore({
          'context': {
            'cache_pool': {},
            'data_copy_concurrency': {},
            'memory_key_value_store': {},
          },
          'driver': 'zarr',
          'dtype': 'float32',
          'kvstore': {'driver': 'memory'},
          'metadata': {
            'chunks': [10, 1414, 707],
            'compressor': {
              'blocksize': 0,
              'clevel': 5,
              'cname': 'lz4',
              'id': 'blosc',
              'shuffle': -1,
            },
            'dimension_separator': '.',
            'dtype': '<f4',
            'fill_value': None,
            'filters': None,
            'order': 'C',
            'shape': [1000, 2000, 3000],
            'zarr_format': 2,
          },
          'transform': {
            'input_exclusive_max': [[1000], [2000], [3000]],
            'input_inclusive_min': [0, 0, 0],
          },
        })

    The schema constraints allow key storage characteristics to be specified
    independent of the driver/format:

        >>> store = await ts.open(
        ...     {
        ...         'driver': 'n5',
        ...         'kvstore': {
        ...             'driver': 'memory'
        ...         },
        ...     },
        ...     create=True,
        ...     dtype=ts.float32,
        ...     shape=[1000, 2000, 3000],
        ...     chunk_layout=ts.ChunkLayout(
        ...         chunk_shape=[10, None, None],
        ...         chunk_aspect_ratio=[None, 2, 1],
        ...         chunk_elements=10000000,
        ...     ),
        ... )
        >>> store
        TensorStore({
          'context': {
            'cache_pool': {},
            'data_copy_concurrency': {},
            'memory_key_value_store': {},
          },
          'driver': 'n5',
          'dtype': 'float32',
          'kvstore': {'driver': 'memory'},
          'metadata': {
            'blockSize': [10, 1414, 707],
            'compression': {
              'blocksize': 0,
              'clevel': 5,
              'cname': 'lz4',
              'shuffle': 1,
              'type': 'blosc',
            },
            'dataType': 'float32',
            'dimensions': [1000, 2000, 3000],
          },
          'transform': {
            'input_exclusive_max': [[1000], [2000], [3000]],
            'input_inclusive_min': [0, 0, 0],
          },
        })

    Driver-specific constraints can be used in combination with, or instead of,
    schema constraints:

        >>> store = await ts.open(
        ...     {
        ...         'driver': 'zarr',
        ...         'kvstore': {
        ...             'driver': 'memory'
        ...         },
        ...         'metadata': {
        ...             'dtype': '>f4'
        ...         },
        ...     },
        ...     create=True,
        ...     shape=[1000, 2000, 3000])
        >>> store
        TensorStore({
          'context': {
            'cache_pool': {},
            'data_copy_concurrency': {},
            'memory_key_value_store': {},
          },
          'driver': 'zarr',
          'dtype': 'float32',
          'kvstore': {'driver': 'memory'},
          'metadata': {
            'chunks': [101, 101, 101],
            'compressor': {
              'blocksize': 0,
              'clevel': 5,
              'cname': 'lz4',
              'id': 'blosc',
              'shuffle': -1,
            },
            'dimension_separator': '.',
            'dtype': '>f4',
            'fill_value': None,
            'filters': None,
            'order': 'C',
            'shape': [1000, 2000, 3000],
            'zarr_format': 2,
          },
          'transform': {
            'input_exclusive_max': [[1000], [2000], [3000]],
            'input_inclusive_min': [0, 0, 0],
          },
        })

    .. _python-open-assume-metadata:

    Using :py:param:`.assume_metadata` for improved concurrent open efficiency
    --------------------------------------------------------------------------

    Normally, when opening or creating a chunked format like
    :ref:`zarr<zarr-driver>`, TensorStore first attempts to read the existing
    metadata (and confirms that it matches any specified constraints), or (if
    creating is allowed) creates a new metadata file based on any specified
    constraints.

    When the same TensorStore stored on a distributed filesystem or cloud storage is
    opened concurrently from many machines, the simultaneous requests to read and
    write the metadata file by every machine can create contention and result in
    high latency on some distributed filesystems.

    The :py:param:`.assume_metadata` open mode allows redundant reading and writing
    of the metadata file to be avoided, but requires careful use to avoid data
    corruption.

    .. admonition:: Example of skipping reading the metadata when opening an existing array
       :class: example

       >>> context = ts.Context()
       >>> # First create the array normally
       >>> store = await ts.open({
       ...     "driver": "zarr",
       ...     "kvstore": "memory://"
       ... },
       ...                       context=context,
       ...                       dtype=ts.float32,
       ...                       shape=[5],
       ...                       create=True)
       >>> # Note that the .zarray metadata has been written.
       >>> await store.kvstore.list()
       [b'.zarray']
       >>> await store.write([1, 2, 3, 4, 5])
       >>> spec = store.spec()
       >>> spec
       Spec({
         'driver': 'zarr',
         'dtype': 'float32',
         'kvstore': {'driver': 'memory'},
         'metadata': {
           'chunks': [5],
           'compressor': {
             'blocksize': 0,
             'clevel': 5,
             'cname': 'lz4',
             'id': 'blosc',
             'shuffle': -1,
           },
           'dimension_separator': '.',
           'dtype': '<f4',
           'fill_value': None,
           'filters': None,
           'order': 'C',
           'shape': [5],
           'zarr_format': 2,
         },
         'transform': {'input_exclusive_max': [[5]], 'input_inclusive_min': [0]},
       })
       >>> # Re-open later without re-reading metadata
       >>> store2 = await ts.open(spec,
       ...                        context=context,
       ...                        open=True,
       ...                        assume_metadata=True)
       >>> # Read data using the unverified metadata from `spec`
       >>> await store2.read()

    .. admonition:: Example of skipping writing the metadata when creating a new array
       :class: example

       >>> context = ts.Context()
       >>> spec = ts.Spec(json={"driver": "zarr", "kvstore": "memory://"})
       >>> spec.update(dtype=ts.float32, shape=[5])
       >>> # Open the array without writing the metadata.  If using a distributed
       >>> # filesystem, this can safely be executed on multiple machines concurrently,
       >>> # provided that the `spec` is identical and the metadata is either fully
       >>> # constrained, or exactly the same TensorStore version is used to ensure the
       >>> # same defaults are applied.
       >>> store = await ts.open(spec,
       ...                       context=context,
       ...                       open=True,
       ...                       create=True,
       ...                       assume_metadata=True)
       >>> await store.write([1, 2, 3, 4, 5])
       >>> # Note that the data chunk has been written but not the .zarray metadata
       >>> await store.kvstore.list()
       [b'0']
       >>> # From a single machine, actually write the metadata to ensure the array
       >>> # can be re-opened knowing the metadata.  This can be done in parallel with
       >>> # any other writing.
       >>> await ts.open(spec, context=context, open=True, create=True)
       >>> # Metadata has now been written.
       >>> await store.kvstore.list()
       [b'.zarray', b'0']

    Group:
      Core
    """
    ...

def overlay(
    layers: Sequence[Union[TensorStore, Spec]],
    *,
    read: Optional[_bool] = None,
    write: Optional[_bool] = None,
    context: Optional[Context] = None,
    transaction: Optional[Transaction] = None,
    rank: Optional[int] = None,
    dtype: Optional[dtype] = None,
    domain: Optional[IndexDomain] = None,
    shape: Optional[Sequence[int]] = None,
    dimension_units: Optional[
        Sequence[Optional[Union[Unit, str, Real, Tuple[Real, str]]]]
    ] = None,
    schema: Optional[Schema] = None,
) -> TensorStore:
    """Virtually overlays a sequence of :py:obj:`TensorStore` layers within a common domain.

        >>> store = ts.overlay([
        ...     ts.array([1, 2, 3, 4], dtype=ts.uint32),
        ...     ts.array([5, 6, 7, 8], dtype=ts.uint32).translate_to[3]
        ... ])
        >>> store
        TensorStore({
          'context': {'data_copy_concurrency': {}},
          'driver': 'stack',
          'dtype': 'uint32',
          'layers': [
            {
              'array': [1, 2, 3, 4],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {'input_exclusive_max': [4], 'input_inclusive_min': [0]},
            },
            {
              'array': [5, 6, 7, 8],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {
                'input_exclusive_max': [7],
                'input_inclusive_min': [3],
                'output': [{'input_dimension': 0, 'offset': -3}],
              },
            },
          ],
          'schema': {'domain': {'exclusive_max': [7], 'inclusive_min': [0]}},
          'transform': {'input_exclusive_max': [7], 'input_inclusive_min': [0]},
        })
        >>> await store.read()
        array([1, 2, 3, 5, 6, 7, 8], dtype=uint32)

    Args:

      layers: Sequence of layers to overlay.  Later layers take precedence.  If a
        layer is specified as a :py:obj:`Spec` rather than a :py:obj:`TensorStore`,
        it must have a known :py:obj:`~Spec.domain` and will be opened on-demand as
        neneded for individual read and write operations.

      read: Allow read access.  Defaults to `True` if neither ``read`` nor ``write`` is specified.
      write: Allow write access.  Defaults to `True` if neither ``read`` nor ``write`` is specified.
      context: Shared resource context.  Defaults to a new (unshared) context with default
        options, as returned by :py:meth:`tensorstore.Context`.  To share resources,
        such as cache pools, between multiple open TensorStores, you must specify a
        context.
      transaction: Transaction to use for opening/creating, and for subsequent operations.  By
        default, the open is non-transactional.

        .. note::

           To perform transactional operations using a :py:obj:`TensorStore` that was
           previously opened without a transaction, use
           :py:obj:`TensorStore.with_transaction`.
      rank: Constrains the rank of the TensorStore.  If there is an index transform, the
        rank constraint must match the rank of the *input* space.
      dtype: Constrains the data type of the TensorStore.  If a data type has already been
        set, it is an error to specify a different data type.
      domain: Constrains the domain of the TensorStore.  If there is an existing
        domain, the specified domain is merged with it as follows:

        1. The rank must match the existing rank.

        2. All bounds must match, except that a finite or explicit bound is permitted to
           match an infinite and implicit bound, and takes precedence.

        3. If both the new and existing domain specify non-empty labels for a dimension,
           the labels must be equal.  If only one of the domains specifies a non-empty
           label for a dimension, the non-empty label takes precedence.

        Note that if there is an index transform, the domain must match the *input*
        space, not the output space.
      shape: Constrains the shape and origin of the TensorStore.  Equivalent to specifying a
        :py:param:`domain` of :python:`ts.IndexDomain(shape=shape)`.

        .. note::

           This option also constrains the origin of all dimensions to be zero.
      dimension_units: Specifies the physical units of each dimension of the domain.

        The *physical unit* for a dimension is the physical quantity corresponding to a
        single index increment along each dimension.

        A value of :python:`None` indicates that the unit is unknown.  A dimension-less
        quantity can be indicated by a unit of :python:`""`.
      schema: Additional schema constraints to merge with existing constraints.


    See also:
      - :ref:`stack-driver`
      - :py:obj:`tensorstore.stack`
      - :py:obj:`tensorstore.concat`

    Group:
      Views
    """
    ...

def stack(
    layers: Sequence[Union[TensorStore, Spec]],
    axis: int = 0,
    *,
    read: Optional[_bool] = None,
    write: Optional[_bool] = None,
    context: Optional[Context] = None,
    transaction: Optional[Transaction] = None,
    rank: Optional[int] = None,
    dtype: Optional[dtype] = None,
    domain: Optional[IndexDomain] = None,
    shape: Optional[Sequence[int]] = None,
    dimension_units: Optional[
        Sequence[Optional[Union[Unit, str, Real, Tuple[Real, str]]]]
    ] = None,
    schema: Optional[Schema] = None,
) -> TensorStore:
    """Virtually stacks a sequence of :py:obj:`TensorStore` layers along a new dimension.

        >>> store = ts.stack([
        ...     ts.array([1, 2, 3, 4], dtype=ts.uint32),
        ...     ts.array([5, 6, 7, 8], dtype=ts.uint32)
        ... ])
        >>> store
        TensorStore({
          'context': {'data_copy_concurrency': {}},
          'driver': 'stack',
          'dtype': 'uint32',
          'layers': [
            {
              'array': [1, 2, 3, 4],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {
                'input_exclusive_max': [1, 4],
                'input_inclusive_min': [0, 0],
                'output': [{'input_dimension': 1}],
              },
            },
            {
              'array': [5, 6, 7, 8],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {
                'input_exclusive_max': [2, 4],
                'input_inclusive_min': [1, 0],
                'output': [{'input_dimension': 1}],
              },
            },
          ],
          'schema': {'domain': {'exclusive_max': [2, 4], 'inclusive_min': [0, 0]}},
          'transform': {'input_exclusive_max': [2, 4], 'input_inclusive_min': [0, 0]},
        })
        >>> await store.read()
        array([[1, 2, 3, 4],
               [5, 6, 7, 8]], dtype=uint32)
        >>> store = ts.stack([
        ...     ts.array([1, 2, 3, 4], dtype=ts.uint32),
        ...     ts.array([5, 6, 7, 8], dtype=ts.uint32)
        ... ],
        ...                  axis=-1)
        >>> store
        TensorStore({
          'context': {'data_copy_concurrency': {}},
          'driver': 'stack',
          'dtype': 'uint32',
          'layers': [
            {
              'array': [1, 2, 3, 4],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {
                'input_exclusive_max': [4, 1],
                'input_inclusive_min': [0, 0],
                'output': [{'input_dimension': 0}],
              },
            },
            {
              'array': [5, 6, 7, 8],
              'driver': 'array',
              'dtype': 'uint32',
              'transform': {
                'input_exclusive_max': [4, 2],
                'input_inclusive_min': [0, 1],
                'output': [{'input_dimension': 0}],
              },
            },
          ],
          'schema': {'domain': {'exclusive_max': [4, 2], 'inclusive_min': [0, 0]}},
          'transform': {'input_exclusive_max': [4, 2], 'input_inclusive_min': [0, 0]},
        })
        >>> await store.read()
        array([[1, 5],
               [2, 6],
               [3, 7],
               [4, 8]], dtype=uint32)

    Args:

      layers: Sequence of layers to stack.  If a layer is specified as a
        :py:obj:`Spec` rather than a :py:obj:`TensorStore`, it must have a known
        :py:obj:`~Spec.domain` and will be opened on-demand as needed for individual
        read and write operations.

      axis: New dimension along which to stack.  A negative number counts from the end.
      read: Allow read access.  Defaults to `True` if neither ``read`` nor ``write`` is specified.
      write: Allow write access.  Defaults to `True` if neither ``read`` nor ``write`` is specified.
      context: Shared resource context.  Defaults to a new (unshared) context with default
        options, as returned by :py:meth:`tensorstore.Context`.  To share resources,
        such as cache pools, between multiple open TensorStores, you must specify a
        context.
      transaction: Transaction to use for opening/creating, and for subsequent operations.  By
        default, the open is non-transactional.

        .. note::

           To perform transactional operations using a :py:obj:`TensorStore` that was
           previously opened without a transaction, use
           :py:obj:`TensorStore.with_transaction`.
      rank: Constrains the rank of the TensorStore.  If there is an index transform, the
        rank constraint must match the rank of the *input* space.
      dtype: Constrains the data type of the TensorStore.  If a data type has already been
        set, it is an error to specify a different data type.
      domain: Constrains the domain of the TensorStore.  If there is an existing
        domain, the specified domain is merged with it as follows:

        1. The rank must match the existing rank.

        2. All bounds must match, except that a finite or explicit bound is permitted to
           match an infinite and implicit bound, and takes precedence.

        3. If both the new and existing domain specify non-empty labels for a dimension,
           the labels must be equal.  If only one of the domains specifies a non-empty
           label for a dimension, the non-empty label takes precedence.

        Note that if there is an index transform, the domain must match the *input*
        space, not the output space.
      shape: Constrains the shape and origin of the TensorStore.  Equivalent to specifying a
        :py:param:`domain` of :python:`ts.IndexDomain(shape=shape)`.

        .. note::

           This option also constrains the origin of all dimensions to be zero.
      dimension_units: Specifies the physical units of each dimension of the domain.

        The *physical unit* for a dimension is the physical quantity corresponding to a
        single index increment along each dimension.

        A value of :python:`None` indicates that the unit is unknown.  A dimension-less
        quantity can be indicated by a unit of :python:`""`.
      schema: Additional schema constraints to merge with existing constraints.


    See also:
      - :py:obj:`numpy.stack`
      - :ref:`stack-driver`
      - :py:obj:`tensorstore.overlay`
      - :py:obj:`tensorstore.concat`

    Group:
      Views
    """
    ...

string = dtype("string")
uint16 = dtype("uint16")
uint32 = dtype("uint32")
uint64 = dtype("uint64")
uint8 = dtype("uint8")
ustring = dtype("ustring")

def virtual_chunked(
    read_function: Optional[
        Callable[
            [IndexDomain, numpy.typing.ArrayLike, VirtualChunkedReadParameters],
            FutureLike[Optional[KvStore.TimestampedStorageGeneration]],
        ]
    ] = None,
    write_function: Optional[
        Callable[
            [IndexDomain, numpy.typing.ArrayLike, VirtualChunkedWriteParameters],
            FutureLike[Optional[KvStore.TimestampedStorageGeneration]],
        ]
    ] = None,
    *,
    loop: Optional[asyncio.AbstractEventLoop] = None,
    rank: Optional[int] = None,
    dtype: Optional[dtype] = None,
    domain: Optional[IndexDomain] = None,
    shape: Optional[Sequence[int]] = None,
    chunk_layout: Optional[ChunkLayout] = None,
    dimension_units: Optional[
        Sequence[Optional[Union[Unit, str, Real, Tuple[Real, str]]]]
    ] = None,
    schema: Optional[Schema] = None,
    context: Optional[Context] = None,
    transaction: Optional[Transaction] = None,
) -> TensorStore:
    """Creates a :py:obj:`.TensorStore` where the content is read/written chunk-wise by an arbitrary function.

    Example (read-only):

        >>> a = ts.array([[1, 2, 3], [4, 5, 6]], dtype=ts.uint32)
        >>> async def do_read(domain: ts.IndexDomain, array: np.ndarray,
        ...                   read_params: ts.VirtualChunkedReadParameters):
        ...     print(f'Computing content for: {domain}')
        ...     array[...] = (await a[domain].read()) + 100
        >>> t = ts.virtual_chunked(do_read, dtype=a.dtype, domain=a.domain)
        >>> await t.read()
        Computing content for: { [0, 2), [0, 3) }
        array([[101, 102, 103],
               [104, 105, 106]], dtype=uint32)

    Example (read/write):

        >>> array = np.zeros(shape=[4, 5], dtype=np.uint32)
        >>> array[1] = 50
        >>> def do_read(domain, chunk, read_context):
        ...     chunk[...] = array[domain.index_exp]
        >>> def do_write(domain, chunk, write_context):
        ...     array[domain.index_exp] = chunk
        >>> t = ts.virtual_chunked(
        ...     do_read,
        ...     do_write,
        ...     dtype=array.dtype,
        ...     shape=array.shape,
        ...     chunk_layout=ts.ChunkLayout(read_chunk_shape=(2, 3)))
        >>> await t.read()
        array([[ 0,  0,  0,  0,  0],
               [50, 50, 50, 50, 50],
               [ 0,  0,  0,  0,  0],
               [ 0,  0,  0,  0,  0]], dtype=uint32)
        >>> t[1:3, 1:3] = 42
        >>> array
        array([[ 0,  0,  0,  0,  0],
               [50, 42, 42, 50, 50],
               [ 0, 42, 42,  0,  0],
               [ 0,  0,  0,  0,  0]], dtype=uint32)

    Args:

      read_function: Callback that handles chunk read requests.  Must be specified
        to create a virtual view that supports reads.  To create a write-only view,
        leave this unspecified (as :py:obj:`None`).

        This function should assign to the array the content for the specified
        :py:obj:`~tensorstore.IndexDomain`.

        The returned :py:obj:`~tensorstore.KvStore.TimestampedStorageGeneration`
        identifies the version of the content, for caching purposes.  If versioning
        is not applicable, :py:obj:`None` may be returned to indicate a value that
        may be cached indefinitely.

        If it returns a :ref:`coroutine<python:async>`, the coroutine will be
        executed using the event loop indicated by :py:param:`.loop`.

      write_function: Callback that handles chunk write requests.  Must be specified
        to create a virtual view that supports writes.  To create a read-only view,
        leave this unspecified (as :py:obj:`None`).

        This function store the content of the array for the specified
        :py:obj:`~tensorstore.IndexDomain`.

        The returned :py:obj:`~tensorstore.KvStore.TimestampedStorageGeneration`
        identifies the stored version of the content, for caching purposes.  If
        versioning is not applicable, :py:obj:`None` may be returned to indicate a
        value that may be cached indefinitely.

        If it returns a :ref:`coroutine<python:async>`, the coroutine will be
        executed using the event loop indicated by :py:param:`.loop`.

      loop: Event loop on which to execute :py:param:`.read_function` and/or
        :py:param:`.write_function` if they are
        :ref:`async functions<python:async def>`.  If not specified (or
        :py:obj:`None` is specified), defaults to the loop returned by
        :py:obj:`asyncio.get_running_loop` (in the context of the call to
        :py:obj:`.virtual_chunked`).  If :py:param:`.loop` is not specified and
        there is no running event loop, it is an error for
        :py:param:`.read_function` or :py:param:`.write_function` to return a
        coroutine.

      rank: Constrains the rank of the TensorStore.  If there is an index transform, the
        rank constraint must match the rank of the *input* space.
      dtype: Constrains the data type of the TensorStore.  If a data type has already been
        set, it is an error to specify a different data type.
      domain: Constrains the domain of the TensorStore.  If there is an existing
        domain, the specified domain is merged with it as follows:

        1. The rank must match the existing rank.

        2. All bounds must match, except that a finite or explicit bound is permitted to
           match an infinite and implicit bound, and takes precedence.

        3. If both the new and existing domain specify non-empty labels for a dimension,
           the labels must be equal.  If only one of the domains specifies a non-empty
           label for a dimension, the non-empty label takes precedence.

        Note that if there is an index transform, the domain must match the *input*
        space, not the output space.
      shape: Constrains the shape and origin of the TensorStore.  Equivalent to specifying a
        :py:param:`domain` of :python:`ts.IndexDomain(shape=shape)`.

        .. note::

           This option also constrains the origin of all dimensions to be zero.
      chunk_layout: Constrains the chunk layout.  If there is an existing chunk layout constraint,
        the constraints are merged.  If the constraints are incompatible, an error
        is raised.
      dimension_units: Specifies the physical units of each dimension of the domain.

        The *physical unit* for a dimension is the physical quantity corresponding to a
        single index increment along each dimension.

        A value of :python:`None` indicates that the unit is unknown.  A dimension-less
        quantity can be indicated by a unit of :python:`""`.
      schema: Additional schema constraints to merge with existing constraints.
      context: Shared resource context.  Defaults to a new (unshared) context with default
        options, as returned by :py:meth:`tensorstore.Context`.  To share resources,
        such as cache pools, between multiple open TensorStores, you must specify a
        context.
      transaction: Transaction to use for opening/creating, and for subsequent operations.  By
        default, the open is non-transactional.

        .. note::

           To perform transactional operations using a TensorStore that was previously
           opened without a transaction, use :py:obj:`TensorStore.with_transaction`.



    Warning:

      Neither :py:param:`.read_function` nor :py:param:`.write_function` should
      block synchronously while waiting for another TensorStore operation; blocking
      on another operation that uses the same
      :json:schema:`Context.data_copy_concurrency` resource may result in deadlock.
      Instead, it is better to specify a :ref:`coroutine function<python:async def>`
      for :py:param:`.read_function` and :py:param:`.write_function` and use
      :ref:`await<python:await>` to wait for the result of other TensorStore
      operations.

    Group:
      Virtual views

    Caching
    -------

    By default, the computed content of chunks is not cached, and will be
    recomputed on every read.  To enable caching:

    - Specify a :py:obj:`~tensorstore.Context` that contains a
      :json:schema:`~Context.cache_pool` with a non-zero size limit, e.g.:
      :json:`{"cache_pool": {"total_bytes_limit": 100000000}}` for 100MB.

    - Additionally, if the data is not immutable, the :py:param:`read_function`
      should return a unique generation and a timestamp that is not
      :python:`float('inf')`.  When a cached chunk is re-read, the
      :py:param:`read_function` will be called with
      :py:obj:`~tensorstore.VirtualChunkedReadParameters.if_not_equal` specified.
      If the generation specified by
      :py:obj:`~tensorstore.VirtualChunkedReadParameters.if_not_equal` is still
      current, the :py:param:`read_function` may leave the output array unmodified
      and return a :py:obj:`~tensorstore.KvStore.TimestampedStorageGeneration` with
      an appropriate
      :py:obj:`~tensorstore.KvStore.TimestampedStorageGeneration.time` but
      :py:obj:`~tensorstore.KvStore.TimestampedStorageGeneration.generation` left
      unspecified.

    Pickle support
    --------------

    The returned :py:obj:`.TensorStore` supports pickling if, and only if, the
    :py:param:`.read_function` and :py:param:`.write_function` support pickling.

    .. note::

       The :py:mod:`pickle` module only supports global functions defined in named
       modules.  For broader function support, you may wish to use
       `cloudpickle <https://github.com/cloudpipe/cloudpickle>`__.

    .. warning::

       The specified :py:param:`.loop` is not preserved when the returned
       :py:obj:`.TensorStore` is pickled, since it is a property of the current
       thread.  Instead, when unpickled, the resultant :py:obj:`.TensorStore` will
       use the running event loop (as returned by
       :py:obj:`asyncio.get_running_loop`) of the thread used for unpickling, if
       there is one.

    Transaction support
    -------------------

    Transactional reads and writes are supported on virtual_chunked views.  A
    transactional write simply serves to buffer the write in memory until it is
    committed.  Transactional reads will observe prior writes made using the same
    transaction.  However, when the transaction commit is initiated, the
    :py:param:`.write_function` is called in exactly the same way as for a
    non-transactional write, and if more than one chunk is affected, the commit will
    be non-atomic.  If the transaction is atomic, it is an error to write to more
    than one chunk in the same transaction.

    You are also free to use transactional operations, e.g. operations on a
    :py:class:`.KvStore` or another :py:class:`.TensorStore`, within the
    :py:param:`.read_function` or :py:param:`.write_function`.

    - For read-write views, you should not attempt to use the same transaction
      within the :py:param:`.read_function` or :py:param:`.write_function` that is
      also used for read or write operations on the virtual view directly, because
      both :py:param:`.write_function` and :py:param:`.read_function` may be called
      after the commit starts, and any attempt to perform new operations using the
      same transaction once it is already being committed will fail; instead, any
      transactional operations performed within the :py:param:`.read_function` or
      :py:param:`.write_function` should use a different transaction.

    - For read-only views, it is possible to use the same transaction within the
      :py:param:`.read_function` as is also used for read operations on the virtual
      view directly, though this may not be particularly useful.

    Specifying a transaction directly when creating the virtual chunked view is no
    different than binding the transaction to an existing virtual chunked view.
    """
    ...
