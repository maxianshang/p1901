"""
P1901socket编程试题(考试时间 2小时):

题目: 实现一个多人聊天室
	要求:  1. 至少实现一个服务端客户端(C/S模式) 的聊天室 服务端和客户端代码 (0-40分)
			2. 能够进行多人同时和服务器收发消息的 服务端和客户端代码 (40-60分)
			3. 能够实现多人同时和服务器收发消息,并且服务器会广播消息的 服务端和客户端代码 (60-70分)

			4. 能够使用线程池来实现上面功能(70-80分)

			5. 能够在完成4要求的情况下考虑到多线程切换的问题,并且对合适的地方上锁,并说明为什么要上锁 (80-90分)

			6. 能够在完成5的要求下实现客户端能顺利关闭退出,并且其他客户端能收到有客户端退出的消息,并且整体代码无bug (90-100分)

	提交方式:将代码发至我微信
	作弊判断规则: 若出现多人代码样视为作弊,多人全部0分
"""

import threading
import socket

def thrad_conn(conn,addr):
    msg = conn.recv(1024)
    while True:
        if len(msg) == 0:break
        return_msg = '{}的用户说:{}'.format(addr,msg.decode('utf-8'))
        for conn in conn_list:
            conn.send(return_msg.encode('utf-8'))
def main():
    # 绑定套接字
    sever_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定端口
    sever_bind = ('127.0.0.1',9099)
    sever_socket.bind(sever_bind)
    # 设置监听
    sever_socket.listen(5)
    # 循环接收信息
    while True:
        conn,addr = sever_socket.accept()
        conn_list.append(conn)
        print('接收到：{}的信息'.format(addr))
        # 创建多线程
        thrad = threading.Thread(target=thrad_conn,args=(conn,addr))
        thrad.start()


if __name__ == '__main__':
    conn_list = []
    main()