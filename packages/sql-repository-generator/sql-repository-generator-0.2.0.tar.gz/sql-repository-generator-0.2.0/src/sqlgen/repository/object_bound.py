from typing import Any

from sqlgen.repository.base import DatabaseRepositoryMeta, DatabaseRepository
from sqlgen.statement_generator.factories import make_object_bound_statement_generator_class_for
from sqlgen.statement_generator.object_bound import ObjectBoundStatementGenerator


class ObjectBoundRepositoryMeta[T, D](DatabaseRepositoryMeta):
    @classmethod
    def get_statement_generator_factory(
            cls,
            attrs: dict[str, type[T] | type[D] | Any]
    ) -> type[ObjectBoundStatementGenerator[T, D]]:
        model: type[T] = attrs["cls"]
        bound_model: type[D] = attrs["bound_model"]
        return make_object_bound_statement_generator_class_for(model, bound_model)


class ObjectBoundRepository[D](DatabaseRepository, metaclass=ObjectBoundRepositoryMeta, generate=False):
    bound_model: type[D]

    def __init__(self, bound_object_id, *args, **kwargs):
        if self.__class__ == ObjectBoundRepository:
            raise ValueError("Cannot instantiate ObjectBoundRepository directly")
        super().__init__(*args, bound_object_id=bound_object_id, **kwargs)
