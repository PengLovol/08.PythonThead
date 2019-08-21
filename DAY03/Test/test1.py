from test import * 
import time 

t = time.time()
# for i in range(10):   #cpu
#     count(1,1)

for i in range(10):    #io
    write()
    read()

#print("Line cpu:",time.time() - t)
print("Line IO:",time.time() - t)