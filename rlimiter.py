import redis
import time
r=redis.Redis(host='localhost',port=6379,decode_responses=True)
def allowed(identity:str,limit=3,window=10):
    key=f'rl:{identity}'
    count=r.incr(key)
    if count==1:
        r.expire(key,window)
    ttl=r.ttl(key)
    return (count<=limit),count,ttl
for i in range(1, 6):
    time.sleep(1)
    ok, count, ttl = allowed("harsha")
    print(i, ok, "count=", count, "reset_in=", ttl)
    