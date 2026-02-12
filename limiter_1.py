import redis
from time import time,sleep
from math import floor
class FixedWindow:
    def __init__(self,user,window,capacity,forward,drop):
        self.user=user
        self.window=window
        self.capacity=capacity
        self.forward=forward
        self.drop=drop
        self.r=redis.Redis(host='localhost',port=6379,decode_responses=True)
    def handle(self):
        window_id=floor(time()/self.window)
        key=f'rl:{self.user}_{window_id}'
        count=self.r.incr(key)
        if count==1:
            self.r.expire(key,self.window)
        if count>self.capacity:
            return self.drop(window_id)
        return self.forward(window_id)
def forward(window_id):
    print(f'got the packet at the window-id:{window_id}')
def drop(window_id):
    print(f'drop the packet sorry!!!the window-id:{window_id}')
x=FixedWindow(f'harsha',5,2,forward,drop)
for i in range(5):
    sleep(0.2)
    x.handle()
