import redis

con = redis.Redis('localhost',6379,3,'')

con.set('name1','moein')
con.set('name2','fati')

v1 = con.get('name1')
v2 = con.get('name2')

print(v1)
print(v2)


print(con.client_list())