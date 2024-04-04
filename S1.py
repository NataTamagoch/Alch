from sqlalchemy import create_engine, asc, desc, select
from table_str import telsprav, ed

engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db6")
connection = engine.connect()

# Выборка без фильтров

# sel1 = telsprav.select()
# print(sel1.compile())
# result = connection.execute(sel1)
# print(result.fetchall()) # все записи
# print(result.fetchone()) # одну запись
# print(result.fetchmany(3))
# print(result.rowcount)

# sel1 = telsprav.select().where((telsprav.c.id < 100) & ((telsprav.c.name == "Ivan") | (telsprav.c.name == "Petr")))
# sel1 = telsprav.select().where(telsprav.c.surname.like('Romanov%'))
# sel1 = telsprav.select().where(telsprav.c.id.between(1,8)).order_by(desc(telsprav.c.id))
# sel1 = telsprav.select().where(telsprav.c.name.notin_(["Ivan", "Petr", "Nikolay"]))
# sel1 = telsprav.select().limit(3).offset(5)
sel1 = select(telsprav.c.phone, telsprav.c.about)
print(sel1.compile())
print(sel1.compile().params)
result = connection.execute(sel1)
print(result.fetchall())  # все записи
# print(result.fetchone()) # одну запись
# print(result.fetchmany(3)) # выберет определенное кол-во записей
print(result.rowcount)
