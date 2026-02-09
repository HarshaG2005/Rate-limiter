from time import time,sleep
class FixedWindow:
    def __init__(self,capacity,forward_callback,backward_callback):
        self.capacity=capacity
        self.allowance=capacity
        self.forward_callback=forward_callback
        self.backward_callback=backward_callback
        self.current_time=int(time())

    def handle(self,packet):
        if int(time()) != self.current_time:
            self.current_time=int(time())
            self.allowance=self.capacity
        if self.allowance < 1 :
           return self.backward_callback(packet)
            
        self.allowance -= 1
        return self.forward_callback(packet)
        
def forward(packet):
    print(f'forward packet:{packet}')
def drop(packet):
    print(f'drop packet:{packet}')
x=FixedWindow(2,forward,drop)
packet=0
while packet<10:
    sleep(0.2)
    x.handle(packet)
    packet+=1
      
