import os 
import signal 

#向20959发送信号
os.kill(16544,signal.SIGKILL)