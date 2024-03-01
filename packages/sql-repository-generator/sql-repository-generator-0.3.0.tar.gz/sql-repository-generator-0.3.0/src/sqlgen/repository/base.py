import abc
from typing import Any

from sqlgen.statement_generator.base import StatementGenerator
from sqlgen.statement_generator.factories import make_statement_generator_class_for


class DatabaseRepositoryMeta[T](abc.ABCMeta):

    def __new__(cls, name: str, bases: tuple, attrs: dict[str, type[T] | Any], generate: bool = True):
        if generate:
            attrs["statement_generator_factory"] = cls.get_statement_generator_factory(attrs)
        return super().__new__(cls, name, bases, attrs)

    @classmethod
    def get_statement_generator_factory[T](cls, attrs: dict[str, type[T] | Any]) -> type[StatementGenerator[T]]:
        model: type[T] = attrs["cls"]
        return make_statement_generator_class_for(model)


class DatabaseRepository[T](abc.ABC, metaclass=DatabaseRepositoryMeta, generate=False):
    """
    Base class for DatabaseRepositories
    """
    # Metaclass provided
    statement_generator_factory: type[StatementGenerator[T]]
    # Consumer Provided
    cls: type[T]  # this must be set by the child class

    def __init__(self, *args, **kwargs):
        if self.__class__ == DatabaseRepository:
            raise ValueError("Cannot instantiate DatabaseRepository directly")
        self.statement_generator: StatementGenerator[T] = self.statement_generator_factory(*args, **kwargs)
