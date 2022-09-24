# 数据库连接报错

本文为您介绍数据库连接报错及解决方式。

## 报错： Got error: 2002

### 错误码

2002

### 错误信息

```sql
Got error: 2002: "Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (2)" when trying to connect
```

### 示例

```sql
[admin@**** /home/admin]
$obclient -h10.10.10.1 -P2881 -uroot@MySQL -p_***2***_ -A
mysql: Got error: 2002: "Can't connect to local MySQL server through socket '/var/lib/mysql/mysql.sock' (2)" when trying to connect
```

## 如何处理

您需要确认连接 OceanBase 数据库的 URL、端口、账号、密码等参数信息是否正确。
