from sqlalchemy import Table, Index, Integer, DateTime, String, Column, Text, Boolean, PrimaryKeyConstraint, \
    UniqueConstraint, ForeignKeyConstraint, create_engine

from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import datetime
engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db6")
session = Session(bind=engine)  # сессия для работы с данными
Base = declarative_base()

class User(Base):
    __tablename__ = 'telsprav'  # обязательный атрибут
    id = Column(Integer)    # необязательный
    username = Column(String(100), nullable=False)
    firstname = Column(String(100), nullable=False)
    secondname = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)

    __table_args__ =(
        PrimaryKeyConstraint('id', name='telsprav_pk'),
        UniqueConstraint('username'),
        UniqueConstraint('email'),
        UniqueConstraint('phone')
    )



# Base.metadata.create_all(engine)


u1 = User()
u1.email = "sunshine17892@gmail.com"
u1.phone = "789963334"
u1.username = "Kirill2"
u1.firstname = "Kirill"
u1.secondname = "Morozov"


u2 = User(
    username = "IvanI",
    firstname = "Ivan",
    secondname = "Ivanov",
    phone = "778966523",
    email = "ivanovi@ya.ru"
)


#session.add(u1)
session.add_all([u1, u2])
session.commit()
