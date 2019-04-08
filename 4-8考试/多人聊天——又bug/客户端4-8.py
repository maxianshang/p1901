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
import socket
import threading
def main():
    clert_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 拨号
    clert_connect = ('127.0.0.1',9099)
    clert_socket.connect(clert_connect)
    t1 = threading.Thread(target=clert_recv,args=(clert_socket,))
    t2 = threading.Thread(target=clert_send,args=(clert_socket,))
    t1.start()
    t2.start()
    print('服务启动')
    t1.join()
    t2.join()

def clert_recv(clert_socket):
    while 1:
        retun_msg = clert_socket.recv(1024).decode
        if len(retun_msg) == 0:break
        try:
            print(retun_msg.decode())
        except Exception:
            break

    clert_socket.close()
def clert_send(clert_socket):

    while True:
        msg = input('>>:')
        try:
            clert_socket.send(msg.encode())
        except Exception:
            break
    clert_socket.close()

    # while True:
    #     msg = input('>>:')
    #     if msg == 0:break
    #     # 发送数据
    #     clert_socket.send(msg.encode('utf-8'))
    #     # 接收数据
    #     msgs = clert_socket.recv(1024)
    #     print(msgs.decode('utf-8'))
    # clert_socket.close()
    #


if __name__ == '__main__':
    main()
