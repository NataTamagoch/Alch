from sqlalchemy import create_engine, MetaData, insert

from table_str import metadata, telsprav, ed

# engine = create_engine("mysql+pymysql://alch:123456@10.10.101.193:3306/mydb")
engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db6")


connection = engine.connect()
metadata.create_all(engine)

#ins = telsprav.insert().values(
#    name='Nikolay',
#    surname='Romanov',
#    phone='345345',
#    about='imperator',
#    address='Dvortsovaya sq'
#)

#block_insert = insert(telsprav)

#result = connection.execute(block_insert, [
 #   {
#        "name": 'Ivan',
#        "surname": 'Ivanov',
#        "phone": '5423525',
#        "address": 'Nevskyi'
#    },
#    {
#        "surname": 'petrov',
#        "phone": '757575',
#        "about": 'vodotel',
#        "address": 'Sennaya sq'
#    }
#])

#items = [
#    {
#        "surname": 'Drakula',
#        "phone": '5437363',
#        "about": 'vampir',
#        "address": 'Karpaty'
#    },
#    {
#        "name": 'Ivan',
#        "surname": 'Grozny',
#        "phone": '000000000',
#        "about": 'tcar',
#        "address": 'Horomy'
#    }
#]

#result2 = connection.execute(block_insert, items)

#print(ins)!
#print(ins.compile().params)
#execute_result = connection.execute(ins)
#print(execute_result)
#print(execute_result.inserted_primary_key)
#print(execute_result.is_insert)
#print(execute_result)

#connection.commit()

print(engine)

ed_block_insert = insert(ed)
ed_items = [
    {
        "id":3,
        "age":1000,
        "heigest":200,
        "country":"Romania",
        "City":"Sigishuara",
        "businessman":True
    }

]

result3 = connection.execute(ed_block_insert, ed_items)
connection.commit()