from test import * 
import threading 
import time 

def io():
    write()
    read()

counts = []
t = time.time()

for x in range(10):
    th=threading.Thread(target=count,args=(1,1))
    counts.append(th)
    th.start()




# for x in range(10):
#     th = threading.Thread(target = io)
#     counts.append(th)
#     th.start()

for i in counts:
    i.join()
#print("thread  IO:",time.time() - t)
print("thread  cpu:",time.time() - t)