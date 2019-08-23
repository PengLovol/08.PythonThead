import os 
from multiprocessing import Process 

filename = "./byte.png"
#获取文件大小
size = os.path.getsize(filename)

#如果子进程使用父进程的对象,那么相互之间有偏移量的影响
# f = open(filename,'rb')

#复制前半部分
def copy1():
    f = open(filename,'rb')
    n = size // 2
    fw = open('file1.png','wb') 

    while True:
        if n < 1024:             #如果一次性读取n，那么会占用大量的内存，为了解决这个问题，可以一次读取1024个字节，直到当n减少到小于1024后直接读取n
            data = f.read(n)
            fw.write(data)
            break
        data = f.read(1024)
        fw.write(data)
        n -= 1024
    f.close()
    fw.close()

#复制下半部分
def copy2():
    f = open(filename,'rb')
    fw = open('file2.png','wb')

    f.seek(size//2,0)   #将文件读取的偏移量后移一半．
    while True:
        data = f.read(1024)
        if not data:
            break 
        fw.write(data)
    fw.close()
    f.close()

p1 = Process(target = copy1)
p2 = Process(target = copy2)
p1.start()
p2.start()
p1.join()
p2.join()