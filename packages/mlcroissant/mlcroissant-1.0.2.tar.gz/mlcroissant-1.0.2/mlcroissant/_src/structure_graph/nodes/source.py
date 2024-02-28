"""Source module."""

from __future__ import annotations

import dataclasses
import enum
from typing import Any, Literal

import jsonpath_rw
from jsonpath_rw import lexer

from mlcroissant._src.core import constants
from mlcroissant._src.core.context import Context
from mlcroissant._src.core.json_ld import remove_empty_values
from mlcroissant._src.core.types import Json
from mlcroissant._src.core.uuid import formatted_uuid_to_json
from mlcroissant._src.core.uuid import uuid_from_jsonld


def _find_choice(
    uuids: list[Any], node_types: list[NodeType]
) -> tuple[Any, NodeType | None]:
    """Returns (None, None) if the inputs don't contain exactly 1 non-null value."""
    choices = [
        (uuid, node_type)
        for uuid, node_type in zip(uuids, node_types)
        if uuid is not None
    ]
    if len(choices) != 1:
        return None, None
    return choices[0]


class FileProperty(enum.IntEnum):
    """Lists the intrinsic properties of a file that are accessible from Croissant.

    Notes:
    - Plural indicates a one-to-many relationship (one row gives many rows), while
      singular indicates a one-to-one relationship.
    - We may use camelCase to be conformed with the names in the JSON-LD Croissant
      standard.
    - We use enum.IntEnum (rather than enum.Enum) in order for FileProperty to be usable
      as column names in pd.DataFrames.

    Warning:
    - At the moment there may be an overlap with existing columns if columns
      have one of the following names.
    """

    content = 1
    filename = 2
    filepath = 3
    fullpath = 4
    lines = 5
    lineNumbers = 6


def is_file_property(file_property: str):
    """Checks if a string is a FileProperty (e.g., "content"->FileProperty.content)."""
    for possible_file_property in FileProperty:
        if possible_file_property.name == file_property:
            return True
    return False


@dataclasses.dataclass(frozen=True)
class Extract:
    """Container for possible ways of extracting the data.

    Args:
        column: The column in a columnar format (e.g., CSV).
        file_property: The property of a file to extract.
        json_path: The JSON path if the source is a JSON.
    """

    column: str | None = None
    file_property: FileProperty | None = None
    json_path: str | None = None

    def to_json(self) -> Json:
        """Converts the `Extract` to JSON."""
        return remove_empty_values({
            "column": self.column,
            "fileProperty": self.file_property.name if self.file_property else None,
            "jsonPath": self.json_path,
        })


@dataclasses.dataclass(frozen=True)
class Transform:
    """Container for transformation.

    Args:
        format: The format for a date (e.g. "%Y-%m-%d %H:%M:%S.%f") or for a bounding
            box (e.g., "XYXY").
        regex: A regex pattern with a capturing group to extract information in a
            string.
        replace: A replace pattern, e.g. "pattern_to_remove/pattern_to_add".
        separator: A separator in a string to yield a list.
    """

    format: str | None = None
    json_path: str | None = None
    regex: str | None = None
    replace: str | None = None
    separator: str | None = None

    def to_json(self) -> Json:
        """Converts the `Transform` to JSON."""
        return remove_empty_values({
            "format": self.format,
            "jsonPath": self.json_path,
            "regex": self.regex,
            "replace": self.replace,
            "separator": self.separator,
        })

    @classmethod
    def from_jsonld(cls, ctx: Context, jsonld: Json | list[Json]) -> list[Transform]:
        """Creates a list of `Transform` from JSON-LD."""
        transforms: list[Transform] = []
        if not isinstance(jsonld, list):
            jsonld = [jsonld]
        for transform in jsonld:
            keys = [
                constants.ML_COMMONS_FORMAT(ctx),
                constants.ML_COMMONS_JSON_PATH(ctx),
                constants.ML_COMMONS_REGEX(ctx),
                constants.ML_COMMONS_REPLACE(ctx),
                constants.ML_COMMONS_SEPARATOR(ctx),
            ]
            if not isinstance(transform, dict):
                ctx.issues.add_error(
                    f'Transform "{transform}" should be a dict with the keys'
                    f' {", ".join(keys)}'
                )
                continue
            kwargs = {constants.TO_CROISSANT(ctx)[k]: transform.get(k) for k in keys}
            all_values_are_none = all(v is None for v in kwargs.values())
            if all_values_are_none:
                ctx.issues.add_error(
                    f'Transform "{transform}" should be a dict with at least one key in'
                    f' {", ".join(keys)}'
                )
                continue
            transforms.append(Transform(**kwargs))
        return transforms


NodeType = Literal["distribution", "field", "fileObject", "fileSet"] | None


@dataclasses.dataclass(eq=False)
class Source:
    r"""Python representation of sources and references.

    Croissant accepts several manners to declare sources:

    When the origin is a field:

    ```json
    "source": {
        "field": {"@id": "record_set/name"},
    }
    ```

    When the origin is a FileSet or a FileObject:

    ```json
    "source": {
        "distribution": {"@id": "my-csv"},
        "extract": {
            "column": "my-csv-column"
        }
    }
    ```

    See the specs for all supported parameters by `extract`.

    You can also add one or more transformations with `transform`:

    ```json
    "source": {
        "field": {"@id": "record_set/name"},
        "transform": {
            "format": "yyyy-MM-dd HH:mm:ss.S",
            "regex": "([^\\/]*)\\.jpg",
            "separator": "|"
        }
    }
    ```
    """

    extract: Extract = dataclasses.field(default_factory=Extract)
    transforms: list[Transform] = dataclasses.field(default_factory=list)
    id: str | None = None
    node_type: NodeType = None

    def to_json(self, ctx: Context) -> Json:
        """Converts the `Source` to JSON."""
        transforms = [transform.to_json() for transform in self.transforms]
        if self.node_type is None:
            raise ValueError("node_type should be `distribution` or `field`. Got: None")
        return remove_empty_values({
            self.node_type: formatted_uuid_to_json(ctx, self.id),
            "extract": self.extract.to_json(),
            "transform": transforms[0] if len(transforms) == 1 else transforms,
        })

    @classmethod
    def from_jsonld(cls, ctx: Context, jsonld: Any) -> Source:
        """Creates a new source from a JSON-LD `field` and populates issues."""
        if jsonld is None:
            return Source()
        elif isinstance(jsonld, list):
            if len(jsonld) != 1:
                raise ValueError(f"Field {jsonld} should have one element.")
            return Source.from_jsonld(ctx, jsonld[0])
        elif isinstance(jsonld, dict):
            try:
                transforms = Transform.from_jsonld(
                    ctx, jsonld.get(constants.ML_COMMONS_TRANSFORM(ctx), [])
                )
                # Safely access and check "data_extraction" from JSON-LD.
                data_extraction = jsonld.get(constants.ML_COMMONS_EXTRACT(ctx), {})
                if isinstance(data_extraction, list) and data_extraction:
                    data_extraction = data_extraction[0]
                # Remove the JSON-LD @id property if it exists:
                data_extraction.pop("@id", None)
                if len(data_extraction) > 1:
                    ctx.issues.add_error(
                        f"{constants.ML_COMMONS_EXTRACT(ctx)} should have one of the"
                        f" following properties: {constants.ML_COMMONS_FORMAT(ctx)},"
                        f" {constants.ML_COMMONS_REGEX(ctx)},"
                        f" {constants.ML_COMMONS_REPLACE(ctx)} or"
                        f" {constants.ML_COMMONS_SEPARATOR(ctx)}"
                    )
                # Safely access and check "uuid" from JSON-LD.
                distribution = jsonld.get(constants.SCHEMA_ORG_DISTRIBUTION)
                file_object = jsonld.get(constants.ML_COMMONS_FILE_OBJECT(ctx))
                file_set = jsonld.get(constants.ML_COMMONS_FILE_SET(ctx))
                field = jsonld.get(constants.ML_COMMONS_FIELD(ctx))
                if ctx.is_v0():
                    uuids = [distribution, field]
                    node_types: list[NodeType] = ["distribution", "field"]
                else:
                    uuids = [file_object, file_set, field]
                    node_types = ["fileObject", "fileSet", "field"]
                uuid, node_type = _find_choice(uuids, node_types)
                if isinstance(uuid, dict):
                    uuid = uuid_from_jsonld(uuid)

                if uuid is None or node_type is None:
                    uuid = None
                    node_type = None
                    if ctx.is_v0():
                        mandatory_fields_in_source = [
                            constants.ML_COMMONS_FIELD(ctx),
                            constants.SCHEMA_ORG_DISTRIBUTION,
                        ]
                    else:
                        mandatory_fields_in_source = [
                            constants.ML_COMMONS_FIELD(ctx),
                            constants.ML_COMMONS_FILE_OBJECT(ctx),
                            constants.ML_COMMONS_FILE_SET(ctx),
                        ]
                    ctx.issues.add_error(
                        f"Every {constants.ML_COMMONS_SOURCE(ctx)} should declare"
                        f" either {' or '.join(mandatory_fields_in_source)}"
                    )
                # Safely access and check "file_property" from JSON-LD.
                file_property = data_extraction.get(
                    constants.ML_COMMONS_FILE_PROPERTY(ctx)
                )
                if is_file_property(file_property):
                    file_property = FileProperty[file_property]
                elif file_property is not None:
                    ctx.issues.add_error(
                        f"Property {constants.ML_COMMONS_FILE_PROPERTY(ctx)} can only"
                        " have values in `fullpath`, `filepath` and `content`. Got:"
                        f" {file_property}"
                    )
                # Build the source.
                json_path = data_extraction.get(constants.ML_COMMONS_JSON_PATH(ctx))
                csv_column = data_extraction.get(constants.ML_COMMONS_COLUMN(ctx))
                extract = Extract(
                    column=csv_column,
                    file_property=file_property,
                    json_path=json_path,
                )
                return Source(
                    id=uuid,
                    extract=extract,
                    transforms=transforms,
                    node_type=node_type,
                )
            except TypeError as exception:
                ctx.issues.add_error(
                    f"Malformed `source`: {jsonld}. Got exception: {exception}"
                )
                return Source()
        else:
            ctx.issues.add_error(f"`source` has wrong type: {type(jsonld)} ({jsonld})")
            return Source()

    def __bool__(self):
        """Allows to write `if not node.source` / `if node.source`."""
        return self.uuid is not None

    def __hash__(self):
        """Hashes all immutable arguments."""
        return hash((self.extract, tuple(self.transforms), self.id, self.node_type))

    def __eq__(self, other: Any) -> bool:
        """Overwrites the equality between two sources."""
        if not isinstance(other, Source):
            return False
        return hash(self) == hash(other)

    @property
    def uuid(self) -> str | None:
        """Unique identifier for the source."""
        return self.id

    def get_column(self) -> str | FileProperty:
        """Retrieves the name of the column associated to the source."""
        if self.uuid is None:
            raise ValueError(
                "No UUID! This case already rose an issue and should not happen at run"
                " time."
            )
        if self.extract.column:
            return self.extract.column
        elif self.extract.file_property:
            return self.extract.file_property
        elif self.extract.json_path:
            return self.extract.json_path
        else:
            return self.uuid.split("/")[-1]

    def check_source(self, add_error: Any):
        """Checks if the source is valid and adds error otherwise."""
        if self.extract.json_path:
            try:
                jsonpath_rw.parse(self.extract.json_path)
            except lexer.JsonPathLexerError as exception:
                add_error(
                    "Wrong JSONPath (https://goessner.net/articles/JsonPath/):"
                    f" {exception}"
                )
