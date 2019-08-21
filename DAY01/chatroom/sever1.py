#!/usr/bin/env python3
#coding=utf-8

#功能模块:

from socket  import *
import sys,os

#登录判断
def do_login(s,user,name,addr):
    if (name in user) or name=='管理员':
        s.sendto('该用户已存在'.encode(),addr)
        return
    s.sendto(b'OK',addr)

    #通知其他人
    msg="欢迎 %s 进入聊天室"%name
    for i in user:
        s.sendto(msg.encode(),user[i])

    #插入新用户
    user[name]=addr


#接收客户端请求
def do_parent(s):
    user={}
    while True:
        msg,addr=s.recvfrom(1024)
        msfList=msg.decode().split(' ')

        #区分请求类型
        if msfList[0]=='L':
            do_login(s,user,msfList[1],addr)

#做管理员喊话
def do_child():
    pass

#创建网络,创建进程,调用功能函数
def main():
    #sever address
    ADDR=('0.0.0.0',8888)

    #创建套接字
    s=socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    # 创建一个单独的进程处理管理员喊话功能
    pid=os.fork()
    if pid<0:
        sys.exit("创建进程失败")
    elif pid==0:
        do_child()
    else:
        do_parent(s)

if __name__=="__main__":
    main()