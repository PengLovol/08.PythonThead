from threading import Thread 
from time import sleep,ctime

class MyThread(Thread):
    def __init__(self,target,name = 'tedu',\
        args = (),kwargs = {}):                      #形参有默认值，可传可不传

        super().__init__()                           #继承父类
        self.name = name
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args,**self.kwargs)

def player(song,sec):
    for i in range(2):
        print("Playing %s:%s"%(song,ctime()))
        sleep(sec)

t = MyThread(target = player,args = ('凉凉',),\
    kwargs = {'sec':2})
t.start()
t.join()