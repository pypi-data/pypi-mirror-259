"""Spaces."""

from __future__ import annotations

import dataclasses
import functools
from collections.abc import Iterable
from typing import Any, Final, TypeAlias

from typing_extensions import Self

from corvic import orm, system
from corvic.model.default_client import get_default_client
from corvic.model.sources import Source, SourceID
from corvic.model.wrapped_orm import WrappedOrmObject
from corvic.result import BadArgumentError
from corvic.table import RowFilter, Table, feature_type, row_filter

SpaceID: TypeAlias = orm.SpaceID
SpaceSourceID: TypeAlias = orm.SpaceID


class Column:
    """A logical representation of a column to use in filter predicates.

    Columns are identified by name.
    """

    _column_name: Final[str]

    def __init__(self, column_name: str):
        """Creates a new instance of Column.

        Args:
            column_name: Name of the column
        """
        self._column_name = column_name

    def eq(self, value: Any) -> RowFilter:
        """Return rows where column is equal to a value."""
        return row_filter.eq(column_name=self._column_name, literal=value)

    def ne(self, value: Any) -> RowFilter:
        """Return rows where column is not equal to a value."""
        return row_filter.ne(column_name=self._column_name, literal=value)

    def gt(self, value: Any) -> RowFilter:
        """Return rows where column is greater than a value."""
        return row_filter.gt(column_name=self._column_name, literal=value)

    def lt(self, value: Any) -> RowFilter:
        """Return rows where column is less than a value."""
        return row_filter.lt(column_name=self._column_name, literal=value)

    def ge(self, value: Any) -> RowFilter:
        """Return rows where column is greater than or equal to a value."""
        return row_filter.ge(column_name=self._column_name, literal=value)

    def le(self, value: Any) -> RowFilter:
        """Return rows where column is less than or equal to a value."""
        return row_filter.le(column_name=self._column_name, literal=value)

    def in_(self, value: list[Any]) -> RowFilter:
        """Return rows where column matches any in a list of values."""
        return row_filter.in_(column_name=self._column_name, literals=value)


@dataclasses.dataclass(frozen=True)
class Relationship:
    """A connection between two sources within a space."""

    from_source_id: Final[SourceID]
    to_source_id: Final[SourceID]
    directional: Final[bool]
    space: Final[Space]
    from_foreign_key_name: Final[str | None]
    to_foreign_key_name: Final[str | None]

    @property
    def from_space_source(self):
        return self.space.get_space_source(self.from_source_id)

    @property
    def to_space_source(self):
        return self.space.get_space_source(self.to_source_id)

    def edge_list(self) -> Iterable[tuple[Any, Any]]:
        from_table = self.from_space_source.table
        to_table = self.to_space_source.table

        from_primary_key = from_table.schema.get_primary_key()
        to_primary_key = to_table.schema.get_primary_key()
        if not from_primary_key or not to_primary_key:
            raise BadArgumentError(
                "both sources must have a primary key to produce an edge list"
            )

        # pick column names that the table doesn't have. these names don't matter
        # except we have to be really sure that they don't conflict
        edge_start_name = "__corvic_edge_start"
        while from_table.schema.has_column(
            edge_start_name
        ) or to_table.schema.has_column(edge_start_name):
            edge_start_name = "_" + edge_start_name

        edge_end_name = "__corvic_edge_end"
        while from_table.schema.has_column(edge_end_name) or to_table.schema.has_column(
            edge_end_name
        ):
            edge_end_name = "_" + edge_start_name

        from_table = from_table.rename_columns({from_primary_key.name: edge_start_name})
        to_table = to_table.rename_columns({to_primary_key.name: edge_end_name})

        if self.from_foreign_key_name:
            from_table = from_table.rename_columns(
                {self.from_foreign_key_name: edge_end_name}
            )
            result_table = from_table.join(
                to_table,
                left_on=edge_end_name,
                right_on=edge_end_name,
                how="inner",
            )
        elif self.to_foreign_key_name:
            to_table = to_table.rename_columns(
                {self.to_foreign_key_name: edge_start_name}
            )
            result_table = from_table.join(
                to_table,
                left_on=edge_start_name,
                right_on=edge_start_name,
                how="inner",
            )
        else:
            raise BadArgumentError("no foreign key relationship")

        result_table = result_table.select([edge_start_name, edge_end_name])
        for row in result_table.to_dicts().unwrap_or_raise():
            yield (row[edge_start_name], row[edge_end_name])


class SpaceSource(WrappedOrmObject[SpaceSourceID, orm.SpaceSource]):
    """A table from a source with some extra operations defined by a space."""

    _source: Final[Source]

    def __init__(
        self,
        client: system.Client,
        orm_self: orm.SpaceSource,
        derived_from_id: SpaceSourceID,
        source: Source | None = None,
    ):
        super().__init__(client, orm_self, derived_from_id)
        if source is None:
            if not orm_self.source_id:
                raise BadArgumentError("could not determine the source")
            source = Source.from_id(
                SourceID.from_orm(orm_self.source_id), self._client
            ).unwrap_or_raise()
        self._source = source

    def _sub_orm_objects(self, orm_object: orm.SpaceSource) -> Iterable[orm.Base]:
        _ = (orm_object,)
        return []

    def _make(self, orm_self: orm.SpaceSource, derived_from_id: SpaceSourceID) -> Self:
        return type(self)(
            self._client,
            orm_self,
            derived_from_id,
            self._source,
        )

    @functools.cached_property
    def table(self):
        return Table.from_bytes(self._client, self._orm_self.table_op_graph)

    @property
    def source(self):
        return self._source


class Space(WrappedOrmObject[SpaceID, orm.Space]):
    """Spaces describe how Sources should be modeled to create a feature space.

    Example:
    >>> Space.create()
    >>>    .with_entity(
    >>>        customer_source.id,
    >>>        row_filter=Column("customer_name").eq("Denis").or_(Column("id").lt(3)),
    >>>        drop_disconnected=True,
    >>>    )
    >>>    .with_entity(
    >>>        order_source,
    >>>        include_columns=["id", "ordered_item"],
    >>>    )
    >>>    .wth_relationship(customer_source.id, order_source.id, directional=False)
    """

    _space_sources: Final[dict[SourceID, SpaceSource]]
    _relationships: Final[list[Relationship]]

    def __init__(
        self,
        client: system.Client,
        orm_self: orm.Space,
        derived_from_id: SpaceID,
        space_sources: dict[SourceID, SpaceSource],
        relationships: list[Relationship],
    ):
        super().__init__(client, orm_self, derived_from_id)
        self._space_sources = space_sources
        self._relationships = [
            dataclasses.replace(rel, space=self) for rel in relationships
        ]

    def _make(self, orm_self: orm.Space, derived_from_id: SpaceID) -> Self:
        return type(self)(
            self._client,
            orm_self,
            derived_from_id,
            self._space_sources,
            self._relationships,
        )

    def _sub_orm_objects(self, orm_object: orm.Space) -> Iterable[orm.Base]:
        _ = (orm_object,)
        return []

    @property
    def relationships(self) -> list[Relationship]:
        return self._relationships

    @classmethod
    def create(cls, client: system.Client | None = None) -> Space:
        """Create a Space."""
        orm_space = orm.Space()
        client = client or get_default_client()
        return Space(client, orm_space, SpaceID(), space_sources={}, relationships=[])

    def get_space_source(self, source_id: SourceID) -> SpaceSource:
        return self._space_sources[source_id]

    @property
    def space_sources(self) -> list[SpaceSource]:
        return list(self._space_sources.values())

    def with_source(
        self,
        source_id: SourceID,
        *,
        row_filter: RowFilter | None = None,
        drop_disconnected: bool = False,
        include_columns: list[str] | None = None,
    ) -> Space:
        """Define a source to be considered in Space.

        Args:
            source_id: The if of the source to be considered in the space
            row_filter: Row level filters to be applied on source
            drop_disconnected: Filter orphan nodes in source
            include_columns: Column level filters to be applied on source

        Example:
        >>> with_entity(
        >>>     customer_source_id,
        >>>     row_filter=Column("customer_name").eq("Denis"),
        >>>     drop_disconnected=True,
        >>>     include_columns=["id", "customer_name"],
        >>> )
        """
        # TODO(thunt): Reminder that these new table ops should start
        # from loading the source
        source = Source.from_id(source_id, self._client).unwrap_or_raise()
        new_table = source.table
        if row_filter:
            new_table = new_table.filter_rows(row_filter)
        if include_columns:
            new_table = new_table.select(include_columns)

        orm_space_source = orm.SpaceSource(
            table_op_graph=new_table.op_graph.to_bytes(),
            drop_disconnected=drop_disconnected,
        )

        space_sources = self._space_sources.copy()
        space_sources.update(
            {
                source.id: SpaceSource(
                    self._client, orm_space_source, SpaceSourceID(), source
                )
            }
        )

        return Space(
            self._client,
            dataclasses.replace(self._orm_self, id=None),
            derived_from_id=self.derived_from_id,
            space_sources=space_sources,
            relationships=self._relationships,
        )

    def _check_or_infer_foreign_keys(
        self,
        from_source_id: SourceID,
        to_source_id: SourceID,
        from_foreign_key: str | None,
        to_foreign_key: str | None,
    ) -> tuple[str | None, str | None]:
        frm = self._space_sources[from_source_id]
        to = self._space_sources[to_source_id]

        if from_foreign_key:
            match frm.table.schema[from_foreign_key].ftype:
                case feature_type.ForeignKey(referenced_source_id):
                    if referenced_source_id != to.source.id:
                        raise BadArgumentError(
                            "from_foreign_key does not reference to_source_id",
                            to_source_id=str(to.source.id),
                            referenced_source_id=str(referenced_source_id),
                        )
                case _:
                    raise BadArgumentError(
                        "the provided from_foreign_key is not a ForeignKey feature"
                    )

        if to_foreign_key:
            match to.table.schema[to_foreign_key].ftype:
                case feature_type.ForeignKey(referenced_source_id):
                    if referenced_source_id != frm.source.id:
                        raise BadArgumentError(
                            "to_foreign_key does not reference from_source_id",
                            from_source_id=str(frm.source.id),
                            referenced_source_id=str(referenced_source_id),
                        )
                case _:
                    raise BadArgumentError(
                        "the provided to_foreign_key is not a ForeignKey feature"
                    )

        if not from_foreign_key and not to_foreign_key:
            from_foreign_keys = [
                field.name for field in frm.table.schema.get_foreign_keys(to.source.id)
            ]
            to_foreign_keys = [
                field.name for field in to.table.schema.get_foreign_keys(frm.source.id)
            ]

            if (
                (from_foreign_keys and to_foreign_keys)
                or len(from_foreign_keys) > 1
                or len(to_foreign_keys) > 1
            ):
                raise BadArgumentError(
                    "relationship is ambiguous:"
                    + "provide from_foreign_key or to_foreign_key to disambiguate",
                    from_foreign_keys=from_foreign_keys,
                    to_foreign_keys=to_foreign_keys,
                )
            if from_foreign_keys:
                from_foreign_key = from_foreign_keys[0]
            if to_foreign_keys:
                to_foreign_key = to_foreign_keys[0]

        return (from_foreign_key, to_foreign_key)

    def with_relationship(
        self,
        from_source_id: SourceID,
        to_source_id: SourceID,
        *,
        from_foreign_key: str | None = None,
        to_foreign_key: str | None = None,
        directional: bool = False,
    ) -> Space:
        """Define relationship between two sources.

        Args:
            from_source_id: The ID of the source on the "from" side (if dircectional)
            to_source_id: The ID of the source on the "to" side (if dircectional)
            from_foreign_key: The foreign key to use to match on the "from"
                source. Required if there is more than one foreign key relationship
                linking the sources. Cannot be used with "to_foreign_key".
            to_foreign_key: The foreign key to use to match on the "to"
                source. Required if there is more than one foreign key relationship
                linking the sources. Cannot be used with "from_foreign_key"
            directional: Whether to load graph as directional

        Example:
        >>> with_relationship(customer_source.id, order_source.id, directional=False)
        """
        if from_source_id not in self._space_sources:
            raise BadArgumentError(
                "from_source_id does not match any source in this space",
                from_source_id=str(from_source_id),
            )
        if to_source_id not in self._space_sources:
            raise BadArgumentError(
                "to_source_id does not match any source in this space",
                to_source_id=str(to_source_id),
            )

        if from_foreign_key and to_foreign_key:
            raise BadArgumentError(
                "only one of from_foreign_key and to_foreign_key may be provided",
                to_source_id=str(to_source_id),
            )

        from_foreign_key, to_foreign_key = self._check_or_infer_foreign_keys(
            from_source_id, to_source_id, from_foreign_key, to_foreign_key
        )

        if not from_foreign_key and not to_foreign_key:
            raise BadArgumentError(
                "foreign key relationship was not provided and could not be inferred"
            )

        relationships = [
            dataclasses.replace(val)
            for val in self._relationships
            if val.from_source_id != from_source_id and val.to_source_id != to_source_id
        ]
        relationships.append(
            Relationship(
                from_source_id=from_source_id,
                to_source_id=to_source_id,
                directional=directional,
                space=self,
                from_foreign_key_name=from_foreign_key,
                to_foreign_key_name=to_foreign_key,
            )
        )

        return Space(
            self._client,
            dataclasses.replace(self._orm_self, id=None),
            derived_from_id=self.derived_from_id,
            space_sources=self._space_sources,
            relationships=relationships,
        )
