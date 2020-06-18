import redis
import json

con_host='localhost'
con_port=6379
con_db=3
con_password=''

con = redis.Redis(con_host,con_port,con_db,con_password)


with open('persons.json') as p:
    data = json.load(p)


with con.pipeline() as pipe:
    for index, person in enumerate(data):
        pipe.hsetnx('person',index,str(person))
    pipe.execute()
