from multiprocessing import Event 

#创建事件对象
e = Event()

e.set()  #设置事件,变为非阻塞

print(e.is_set())

e.wait(3)

#e.clear()
#e.wait()