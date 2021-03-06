from abc import ABCMeta, abstractmethod
from typing import TypeVar, Type, Union
from common.database import Database

T = TypeVar("T", bound="Model")

class Model(metaclass=ABCMeta):

    def save_to_mongo(self):
        Database.update(self.collection, {"_id": self._id}, self.json())

    def remove_from_mongo(self):
        Database.remove(self.collection, {"_id": self._id})

    @classmethod
    def get_by_id(cls: Type[T], _id: str) -> T:
        return cls.find_one_by("_id", _id)

    @abstractmethod
    def json(self) -> dict:
        raise NotImplementedError

    @classmethod
    def all(cls: Type[T]) -> list[T]:
        elements_from_db = Database.find(cls.collection, {})
        return [cls(**elem) for elem in elements_from_db]

    @classmethod
    def find_one_by(cls: Type[T], attribute: str, value: Union[str, dict]) -> T:
        return cls(**Database.find_one(cls.collection, {attribute: value}))

    @classmethod
    def find_many_by(cls: Type[T], attribute: str, value: str) -> list[T]:
        return [cls(**elem) for elem in Database.find(cls.collection, {attribute: value})]