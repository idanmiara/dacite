from dataclasses import Field, MISSING, _FIELDS, _FIELD, _FIELD_INITVAR  # type: ignore
from typing import Type, Any, TypeVar, List

from dacite.data import Data
from dacite.types import is_optional

T = TypeVar("T", bound=Any)


class DefaultValueNotFoundError(Exception):
    pass


def get_default_value_for_field(field: Field, allow_missing_fields_as_none: bool = False) -> Any:
    if field.default != MISSING:
        return field.default
    elif field.default_factory != MISSING:
        return field.default_factory()
    elif is_optional(field.type) or allow_missing_fields_as_none:
        return None
    raise DefaultValueNotFoundError()


def create_instance(data_class: Type[T], init_values: Data, post_init_values: Data) -> T:
    instance: T = data_class(**init_values)
    for key, value in post_init_values.items():
        setattr(instance, key, value)
    return instance


def get_fields(data_class: Type[T]) -> List[Field]:
    fields = getattr(data_class, _FIELDS)
    return [f for f in fields.values() if f._field_type is _FIELD or f._field_type is _FIELD_INITVAR]
