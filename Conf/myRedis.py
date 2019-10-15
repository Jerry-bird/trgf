# coding = utf-8
import json
import time
import redis

r = redis.Redis(host='192.168.1.95', port=6379, password='vellgo@123')
k = 'jd_stock:lostocknum_'+'110007548191'+'de4db46a3e424ba951f5bd35a48223'
print(k)
t = r.get(k).decode()
print(t)

print(time.time())
