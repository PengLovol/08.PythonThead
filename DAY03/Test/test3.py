from test import * 
import multiprocessing 
import time 

def io():
    write()
    read()

counts = []
t = time.time()
for x in range(10):                                              #CPU
    p = multiprocessing.Process(target = count,args = (1,1))
    counts.append(p)
    p.start()


# for x in range(10):                                             #IO
#     p = multiprocessing.Process(target=io)
#     counts.append(p)
#     p.start()

for i in counts:
    i.join()
print("Process  cpu:",time.time() - t)
#print("Process  IO:",time.time() - t)