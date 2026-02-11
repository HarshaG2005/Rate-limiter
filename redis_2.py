import redis 
r=redis.Redis(host='localhost',port=6379,decode_responses=True)
#Micro-lab B: Counter (rate limiting foundation)
#DEL/delete=Removes a key (and its value) from Redis.
r.delete('hits')
print(r.incr('hits'))
#incr=Increments the value stored at key by 1, but only if it’s an integer (or doesn’t exist)
print(r.incr('hits'))
print(r.incr('hits',10))
#DECR-decrements the value stored at key by 1, but only if it’s an integer (or doesn’t exist)
print(r.decr('hits',5))
print(r.get('hits'))