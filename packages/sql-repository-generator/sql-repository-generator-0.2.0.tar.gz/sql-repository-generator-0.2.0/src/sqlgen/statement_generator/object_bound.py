from sqlalchemy import Column, Select
from sqlalchemy.orm import RelationshipProperty
from sqlalchemy.sql.base import ExecutableOption

from sqlgen.statement_generator.base import StatementGenerator


class ObjectBoundStatementGenerator[P, M](StatementGenerator):
    cls: type[M]
    joins: list[RelationshipProperty]
    primary_key: Column

    def __init__(self, bound_object_id: P):
        self.bound_object_id = bound_object_id

    def get_by(self, *args, options: list[ExecutableOption] = None,
               load_all: bool = False, property_name: str = None, **kwargs) -> Select:
        """
        Generate the select query and filter it with the bound object id

        :param args: filter arguments for sqlalchemy filter function
        :param options: optional options for the query (mostly ofr joinedloads)
        :param kwargs: arguments to filter the model to return
        :param load_all: load all relationship on the model when doing the query
        :param property_name: get a property instead of the object
        :return: a sql statement with specified options, filter, ...
        """
        statement = super().get_by(*args, options=options, load_all=load_all, property_name=property_name, **kwargs)

        for join in self.joins:
            statement = statement.join(join)
        return statement.filter(self.primary_key == self.bound_object_id)
