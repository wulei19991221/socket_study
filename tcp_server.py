# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年06月01日11时
# @File: tcp_server.py
from socket import *
from print_color import *


if __name__ == '__main__':
    #  tcp套接字
    tcp = socket(AF_INET, SOCK_STREAM)
    # 绑定固定端口, 服务端必须绑定
    tcp.bind(('', 3256))
    # 监听,套接字由主动变被动, 一般是128
    tcp.listen(128)
    # 连接成功,返回一个客户端套接字
    client_socket, addr = tcp.accept()
    content = client_socket.recv(1024)
    print_c(fred, content.decode())
    client_socket.send(b'ok')
    # 断开客户端
    client_socket.close()
    # 关闭套接字
    tcp.close()


