# 小林 x 图解计算机基础

![](https://cdn.jsdelivr.net/gh/xiaolincoder/ImageHost4@main/网站封面.png)

👉 **点击**：[图解计算机基础在线阅读](https://xiaolincoding.com/)

本站所有文章都是我[公众号：小林 coding](https://mp.weixin.qq.com/s/FYH1I8CRsuXDSybSGY_AFA)
的原创文章，内容包含图解计算机网络、操作系统、计算机组成、数据库，共 1000 张图 + 50
万字，破除晦涩难懂的计算机基础知识，让天下没有难懂的八股文（口嗨一下，大家不要当真哈哈）！🚀

曾经我也苦恼于那些晦涩难弄的计算机基础知识，但在我啃了一本又一本的书，看了一个又一个的视频后，终于对这些“家伙”有了认识。我想着，这世界上肯定有一些朋友也跟我有一样的苦恼，为此下决心，用图解 +
通熟易懂的讲解来帮助大家理解，利用工作之余，坚持输出图解文章两年之久，这才有了今天的网站！

## :open_book:《图解网络》

- **介绍**:point_down:：
  - [图解网络介绍](https://xiaolincoding.com/network/)
- **网络基础篇** :point_down:
  - [TCP/IP 网络模型有哪几层？](https://xiaolincoding.com/network/1_base/tcp_ip_model.html)
  - [键入网址到网页显示，期间发生了什么？](https://xiaolincoding.com/network/1_base/what_happen_url.html)
  - [Linux 系统是如何收发网络包的？](https://xiaolincoding.com/network/1_base/how_os_deal_network_package.html)
- **HTTP 篇** :point_down:
  - [HTTP 常见面试题](https://xiaolincoding.com/network/2_http/http_interview.html)
  - [HTTP/1.1 如何优化？](https://xiaolincoding.com/network/2_http/http_optimize.html)
  - [HTTPS RSA 握手解析](https://xiaolincoding.com/network/2_http/https_rsa.html)
  - [HTTPS ECDHE 握手解析](https://xiaolincoding.com/network/2_http/https_ecdhe.html)
  - [HTTPS 如何优化？](https://xiaolincoding.com/network/2_http/https_optimize.html)
  - [HTTP/2 牛逼在哪？](https://xiaolincoding.com/network/2_http/http2.html)
  - [HTTP/3 强势来袭](https://xiaolincoding.com/network/2_http/http3.html)
  - [既然有 HTTP 协议，为什么还要有 RPC？](https://xiaolincoding.com/network/2_http/http_rpc.html)
  - [既然有 HTTP 协议，为什么还要有 WebSocket？](https://xiaolincoding.com/network/2_http/http_websocket.html)
- **TCP 篇** :point_down:
  - [TCP 三次握手与四次挥手面试题](https://xiaolincoding.com/network/3_tcp/tcp_interview.html)
  - [TCP 重传、滑动窗口、流量控制、拥塞控制](https://xiaolincoding.com/network/3_tcp/tcp_feature.html)
  - [TCP 实战抓包分析](https://xiaolincoding.com/network/3_tcp/tcp_tcpdump.html)
  - [TCP 半连接队列和全连接队列](https://xiaolincoding.com/network/3_tcp/tcp_queue.html)
  - [如何优化 TCP?](https://xiaolincoding.com/network/3_tcp/tcp_optimize.html)
  - [如何理解是 TCP 面向字节流协议？](https://xiaolincoding.com/network/3_tcp/tcp_stream.html)
  - [为什么 TCP 每次建立连接时，初始化序列号都要不一样呢？](https://xiaolincoding.com/network/3_tcp/isn_deff.html)
  - [SYN 报文什么时候情况下会被丢弃？](https://xiaolincoding.com/network/3_tcp/syn_drop.html)
  - [四次挥手中收到乱序的 FIN 包会如何处理？](https://xiaolincoding.com/network/3_tcp/out_of_order_fin.html)
  - [在 TIME_WAIT 状态的 TCP 连接，收到 SYN 后会发生什么？](https://xiaolincoding.com/network/3_tcp/time_wait_recv_syn.html)
  - [TCP 连接，一端断电和进程崩溃有什么区别？](https://xiaolincoding.com/network/3_tcp/tcp_down_and_crash.html)
  - [拔掉网线后，原本的 TCP 连接还存在吗？](https://xiaolincoding.com/network/3_tcp/tcp_unplug_the_network_cable.html)
  - [tcp_tw_reuse 为什么默认是关闭的？](https://xiaolincoding.com/network/3_tcp/tcp_tw_reuse_close.html)
  - [HTTPS 中 TLS 和 TCP 能同时握手吗？](https://xiaolincoding.com/network/3_tcp/tcp_tls.html)
  - [TCP Keepalive 和 HTTP Keep-Alive 是一个东西吗？](https://xiaolincoding.com/network/3_tcp/tcp_http_keepalive.html)
  - [TCP 协议有什么缺陷？](https://xiaolincoding.com/network/3_tcp/tcp_problem.html)
  - [如何基于 UDP 协议实现可靠传输？](https://xiaolincoding.com/network/3_tcp/quic.html)
  - [TCP 和 UDP 可以使用同一个端口吗？](https://xiaolincoding.com/network/3_tcp/port.html)
  - [服务端没有 listen，客户端发起连接建立，会发生什么？](https://xiaolincoding.com/network/3_tcp/tcp_no_listen.html)
  - [没有 accept，可以建立 TCP 连接吗？](https://xiaolincoding.com/network/3_tcp/tcp_no_accpet.html)
  - [用了 TCP 协议，数据一定不会丢吗？](https://xiaolincoding.com/network/3_tcp/tcp_drop.html)
  - [TCP 四次挥手，可以变成三次吗？](https://xiaolincoding.com/network/3_tcp/tcp_three_fin.html)
  - [TCP 序列号和确认号是如何变化的？](https://xiaolincoding.com/network/3_tcp/tcp_seq_ack.html)
- **IP 篇** :point_down:
  - [IP 基础知识全家桶](https://xiaolincoding.com/network/4_ip/ip_base.html)
  - [ping 的工作原理](https://xiaolincoding.com/network/4_ip/ping.html)
  - [断网了，还能 ping 通 127.0.0.1 吗？](https://xiaolincoding.com/network/4_ip/ping_lo.html)
- **学习心得** :point_down:
  - [计算机网络怎么学？](https://xiaolincoding.com/network/5_learn/learn_network.html)
  - [画图经验分享](https://xiaolincoding.com/network/5_learn/draw.html)
