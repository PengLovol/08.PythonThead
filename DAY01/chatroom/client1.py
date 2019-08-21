from socket import *
import sys,os

# 代码编写流程
# 搭建网络连接 --》 创建多进程---》每个进程功能编写--》项目功能模块实现

#进入聊天室
# 客户端 ： 输入姓名  将信息发给服务端（L name）
#           等待服务端回复    根据回复判断是否登录成功


#服务端 ： 接收请求信息  判断请求类型
       #    判断用户名是否存在   如果存在回复不能登录
	  # 如果不存在回复可以登录并插入到数据结构
       #    发送通知给其他用户




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
        name=input("请输入姓名")
        msg="L "+name
        #发送登录请求
        s.sendto(msg.encode(),ADDR)
        #等待服务器回复
        data,addr=s.recvfrom(1024)
        if data.decode()=='OK':
            print('您已进入聊天室')
        else:
            #不成功服务端会回复不允许登录的原因
            print(data.decode())



if __name__=="__mian__":
    main()
