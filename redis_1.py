import redis
r=redis.Redis(host='localhost',port=6379,decode_responses=True)
print(r.ping())#health check
#SET: stores a key/value in Redis’ memory (RAM).
# (Depending on config, Redis can also persist to disk, but it’s primarily an in-memory store.)
r.set('msg','hello')
# GET: reads the value for that key and returns it to your client.
# It’s not really “a copy you keep in Redis” — it’s just the value sent back to your program.
print(r.get('msg'))
# EXPIRE: sets a time-to-live (TTL) on a key (in seconds). When that time runs out, Redis deletes the key automatically.
# r.expire('msg',10)
# TTL: tells you how many seconds are left before the key expires.
# Extra useful detail:
# TTL key = -1 → key exists but no expiry set
# TTL key = -2 → key doesn’t exist (expired or never created)
print(r.ttl('msg'))