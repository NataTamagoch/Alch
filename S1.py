from sqlalchemy import create_engine
from table_str import telsprav, ed
engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db6")

connection = engine.connect()
#sel1 = telsprav.select()
#print(sel1.compile())
#result = connection.execute(sel1)
#print(result.fetchall()) #все записи
#print(result.fetchone()) #одну запись

sel1 = telsprav.select().where(telsprav.c.id < 2)
print(sel1.compile())
result = connection.execute(sel1)
print(result.fetchall())
print(result.rowcount)


