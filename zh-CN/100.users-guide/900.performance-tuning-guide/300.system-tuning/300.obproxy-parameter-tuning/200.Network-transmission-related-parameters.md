# 网络传输相关参数

| 配置项 | 描述 | 建议 |
| --- | --- | --- |
| server_tcp_user_timeout | OBProxy 与 OBServer 连接的 tcp user timeout，默认值为 0 s | 保持默认值 |
| client_tcp_user_timeout | OBProxy 与 Client 连接的 tcp user timeout，默认值为 0 s | 保持默认值 |
| client_max_connections | OBProxy 所能接受的客户端最大连接数，默认值为 8192 | 保持默认值 |
| connect_observer_max_retries | OBProxy 重连 OBServer 的最大次数，默认值为 3 | 保持默认值 |
| observer_query_timeout_delta | 网络传输延时，给 OBServer 的 `ob_query_timeout` 设置的增量，默认值为 20 s | 保持默认值 |
| sock_option_flag_out | OBProxy 和 OBServer 之间 tcp 的参数，这是个二进制位参数，bit 0 表示否是启用 `no_delay`，bit 1 表示是否启用 `keepalive`。3 的二进制是 11，表示启用 `no_delay` 和 `keepalive`，默认值为 3 | 保持默认值 |
| server_tcp_keepidle | OBProxy 和 OBServer 的 tcp 启动 keepalive 探活前的 idle 时间，默认值为 5 | 保持默认值 |
| server_tcp_keepintvl | OBProxy 和 OBServer 的 tcp 两个 keepalive 探活包之间的时间间隔，默认值为 5 | 保持默认值 |
| server_tcp_keepcnt | OBProxy 和 OBServer 的 tcp 最多发送多少个 keepalive 包，默认值为 5 | 保持默认值 |
| client_sock_option_flag_out | 客户端和 OBProxy 之间 tcp 的参数，这是个二进制位参数，bit 0 表示否是启用 `no_delay`，bit 1 表示是否启用 `keepalive`。3 的二进制是 11，表示启用 `no_delay` 和 `keepalive`，默认值为 2 | 保持默认值 |
| client_tcp_keepidle | 客户端和 OBProxy 的 tcp 启动 keepalive 探活前的 idle 时间，默认值为 5 | 保持默认值 |
| client_tcp_keepintvl | 客户端和 OBProxy 的 tcp 两个 keepalive 探活包之间的时间间隔，默认值为 5 | 保持默认值 |
| client_tcp_keepcnt | 客户端和 OBProxy 的 tcp 最多发送多少个 keepalive 包，默认值为 5 | 保持默认值 |
