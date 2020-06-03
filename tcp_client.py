# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年06月01日10时
# @File: tcp_client.py
from socket import *
from print_color import *


if __name__ == '__main__':
    #  tcp套接字
    tcp = socket(AF_INET, SOCK_STREAM)
    # 绑定固定端口
    # tcp.bind(('', 3256))
    # 连接tcp服务器
    tcp.connect(('127.0.0.1', 3256))
    content = input_c(fgreen, '发送内容: ')
    # 发送数据
    tcp.send(content.encode('utf-8'))
    # 接收数据
    print_c(fgreen, tcp.recv(1024).decode())
    # 关闭套接字
    tcp.close()

