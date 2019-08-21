from socket import *
import sys,os

# 代码编写流程
# 搭建网络连接 --》 创建多进程---》每个进程功能编写--》项目功能模块实现

#功能模块:聊天 客户端 ： 创建父子进程   发送聊天请求/接收聊天信息 服务端 ： 接收请求信息  将消息转发给其他客户端

#发送消息
def send_msg(s,name,addr):
    while True:
        text=input("发言:")
        msg='C %s %s'%(name,text)
        s.sendto(msg.encode(),addr)

#接收消息
def recv_msg(s):
    while True:
        data,addr=s.recvfrom(20485)
        print(data.decode())

#创建网络,创建进程,调用功能函数
def main():
    # 从命令行获取服务端地址
    if len(sys.argv)<3:
        print("argv is error")
        return
    HOST=sys.argv[1]
    PORT=int(sys.argv[2])
    ADDR=(HOST,PORT)

    #创建套接字
    s = socket(AF_INET, SOCK_DGRAM)

    #一次输入不成功可以连续输入

    while True:
        name = input("请输入姓名:")
        msg = "L " + name
        #发送登录请求
        s.sendto(msg.encode(),ADDR)
        #等待服务器回复
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("您已进入聊天室")
            break
        else:
            #不成功服务端会回复不允许登录原因
            print(data.decode())
    pid=os.fork()
    if pid<0:
        sys.exit("创建子进程失败")
    elif pid==0:
        send_msg(s,name,ADDR)
    else:
        recv_msg(s)



if __name__=="__main__":
    main()



