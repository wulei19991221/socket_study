### socket
1.udp套接字

```
# udp
s = socket(AF_INET, SOCK_DGRAM)
# 绑定端口
# ip_port = ('', 指定端口1024以上)  ''是本地任意ip
# s.bind(ip_port)
# 发送数据
s.sendto(content.encode('utf-8'), (接收方ip, 接收方端口))
# 接收数据
s.recvfrom(接收的字节(例如): 1024)  # 返回类型(bytes, (发送方ip, 发送方端口)) --> 元组
# 关闭udp
s.close()
```

2.tcp套接字 客户端client

```
# udp
s = socket(AF_INET, SOCK_STREAM)
# 连接服务器
s.connect((ip: str, port: int))
# 发送数据
s.send(content.encode('utf-8'))
# 接收数据
content = s.recv(1024)
# 关闭tcp客户端
s.close()
```
3.tcp套接字 服务端serve
```
# udp
s = socket(AF_INET, SOCK_STREAM)
# 连接服务器
s.bind((ip, port))
# 监听
s.listen(128)
# 接入客户端
new_socket, addr = s.accept()
# 发送数据
new_socker.send(content.encode('utf-8'))
# 接收数据
content = new_socket.recv(1024)
# 断开客户端
new_socket.close()
# 关闭tcp客户端
s.close()
```