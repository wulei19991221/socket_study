# !/usr/bin/python3
# --coding:utf-8--
# @Author:吴磊
# @Time: 2019年12月19日16时
# @File: 远程发送与接受.py
import socket
import threading
import sys


def socket_service():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 防止socket server重启后端口被占用（socket.error: [Errno 98] Address already in use）
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('10.25.64.240', 6666))
        s.listen(10)
    except socket.error as msg:
        print(msg)
        sys.exit(1)
    print('Waiting connection...')

    while 1:
        conn, addr = s.accept()
        t = threading.Thread(target=deal_data, args=(conn, addr))
        t.start()


def deal_data(conn, addr):
    print('Accept new connection from {0}'.format(addr))
    conn.send(b'Hi, Welcome to the server!')
    while 1:
        data = conn.recv(1024)
        print('new message: ' + str(data, encoding='utf-8'))
        if data == 'exit' or not data:
            print('{0} connection close'.format(addr))
            conn.send('Connection closed!')
            break
        msg = input('your message: ')
        conn.send(bytes(msg, encoding='utf-8'))
    conn.close()


if __name__ == '__main__':
    socket_service()
