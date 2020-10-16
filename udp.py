# !/usr/bin/python3
# --coding:utf-8--
# @Author:ACHIEVE_DREAM
# @Time: 2020年05月30日16时
# @File: socket.py
from socket import *
from print_color import *


def send():
    text = input_c(fpurple, '请输入你要发送的内容: ')
    s.sendto(text.encode('utf-8'), ('192.168.159.1', 8080))


def receive():
    result = s.recvfrom(1024*10)
    print(result[0].decode('utf-8'))


if __name__ == '__main__':
    # udp
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('', 3256))
    receive()
    s.close()
