from uuid import UUID, uuid4

from logic.apps.example.models.example import Example
from logic.libs.sqliteAlchemy import sqliteAlchemy
from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ExampleEntity(Base):
    __tablename__ = 'examples'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=True)
    string = Column(String)
    integer = Column(Integer)
    date_time = Column(DateTime)
    double = Column(Float)
    uuid = Column(String)

    def to_model(self) -> Example:
        return Example(
            id=self.id,
            string=self.string,
            integer=self.integer,
            date_time=self.date_time,
            double=self.double,
            uuid=UUID(self.uuid)
        )

    @staticmethod
    def from_model(m: Example) -> 'ExampleEntity':
        return ExampleEntity(
            id=m.id,
            string=m.string,
            integer=m.integer,
            date_time=m.date_time,
            double=m.double,
            uuid=str(m.uuid)
        )


Base.metadata.create_all(sqliteAlchemy.get_engine())
