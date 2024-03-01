from typing import Sequence, Any

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.base import ExecutableOption

from sqlgen.repository.base import DatabaseRepository
from sqlgen.repository.object_bound import ObjectBoundRepository
from sqlgen.statement_executor.asynchronous import AsyncStatementExecutor


class AsyncRepository[T](DatabaseRepository, generate=False):

    def __init__(self, session: AsyncSession, *args, **kwargs):
        """
        :param session: the db session used for the queries
        """
        if self.__class__ == AsyncRepository:
            raise ValueError("Cannot instantiate AsyncRepository directly")
        super().__init__(*args, **kwargs)
        self.statement_executor = AsyncStatementExecutor(session)

    async def get_by[T](self, *args, options: list[ExecutableOption] = None,
                        load_all: bool = False, property_name: str = None, **kwargs) -> T | None:
        statement = self.statement_generator.get_by(*args, options=options, load_all=load_all,
                                                    property_name=property_name, **kwargs)
        return await self.statement_executor.one_or_none(statement)

    async def take_by[T](self, *args, options: list[ExecutableOption] = None,
                         load_all: bool = False, property_name: str = None, **kwargs) -> T:
        statement = self.statement_generator.get_by(*args, options=options, load_all=load_all,
                                                    property_name=property_name, **kwargs)
        return await self.statement_executor.one(statement)

    async def get_by_id[T](self, object_id, *args, options: list[ExecutableOption] = None,
                           load_all: bool = False, property_name: str = None, **kwargs) -> T | None:
        statement = self.statement_generator.get_by_id(object_id, *args, options=options, load_all=load_all,
                                                       property_name=property_name, **kwargs)
        return await self.statement_executor.one_or_none(statement)

    async def take_by_id[T](self, object_id, *args, options: list[ExecutableOption] = None,
                            load_all: bool = False, property_name: str = None, **kwargs) -> T:
        statement = self.statement_generator.get_by_id(object_id, *args, options=options, load_all=load_all,
                                                       property_name=property_name, **kwargs)
        return await self.statement_executor.one(statement)

    async def get_all_by[T](self, *args, options: list[ExecutableOption] = None, **kwargs) -> Sequence[T]:
        """
        generic function to get all object of given model
        :param args: filter arguments for sqlalchemy filter function
        :param options: optional options for the query (mostly ofr joinedloads)
        :param kwargs: arguments to filter the model to return
        :return: the list of instances of given model
        """
        statement = self.statement_generator.get_by(*args, options=options, **kwargs)
        return await self.statement_executor.all(statement)

    async def get_all[T](self) -> Sequence[T]:
        """
        generic function to get all object of given model
        :return: the list of instances of given model
        """
        return await self.get_all_by()

    async def create[T](self, **properties) -> T:
        """
        generic function to create a db object
        :param properties: the properties of the model
        :return: the created object
        """
        obj = self.cls(**properties)
        self.statement_executor.store(obj)
        await self.statement_executor.synchronize()
        return obj

    async def update(self, obj: DeclarativeBase | Any, save: bool = False, **properties):
        """
        update a DB object and synchronize the change with the DC
        :param obj: the object to update, or it's ID
        :param save: should we commit the changes? (default to false, flush but no commit)
        :param properties: the properties to update on the object
        """
        if not isinstance(obj, DeclarativeBase):
            obj = await self.take_by_id(obj, load_all=True)
        for prop in properties:
            setattr(obj, prop, properties[prop])
        if save:
            await self.save()
        else:
            await self.synchronize()

    async def synchronize(self):
        """
        synchronize the state of the DB and the python ones
        """
        await self.statement_executor.synchronize()

    async def save(self):
        """
        Save the state of updated objects in DB (do a commit under the hood)
        """
        await self.statement_executor.save()

    async def restore(self):
        """
        restore python object state to the latest save on the DB (rollback internally)
        """
        await self.statement_executor.restore()


class AsyncObjectBoundRepository(AsyncRepository, ObjectBoundRepository, generate=False):
    def __init__(self, session: AsyncSession, bound_object_id):
        """
        :param session: the db session used for the queries
        """
        if self.__class__ == AsyncObjectBoundRepository:
            raise ValueError("Cannot instantiate AsyncObjectBoundRepository directly")
        super().__init__(session=session, bound_object_id=bound_object_id)
