# 事务超时报错

本文为您介绍事务超时的相关报错及处理方式。

## 事务空闲超时

### 报错：ERROR 6002

OceanBase 错误码：6002

### 报错信息

```sql
ERROR 6002 (40000) : transaction is rolled back
```

### 示例

begin 后 `120` 秒内未操作。

```sql
obclient> delete from t_insert where id=2;
ERROR 6002 (25000): transaction needs rollback
```

### 处理方法

1. 查看 ob_trx_idle_timeout 参数值，确认操作的超时时间是否超过了设置的值。

   ```sql
   obclient> show variables like 'ob_trx_idle_timeout';
   +---------------------+-----------+
   | VARIABLE_NAME       | VALUE     |
   +---------------------+-----------+
   | ob_trx_idle_timeout | 120000000 |
   +---------------------+-----------+
   1 row in set
   ```

2. 使用 `rollback` 恢复操作。

   ```sql
   obclient> rollback;
   Query OK, 0 rows affected
   ```

3. 再次清除 `t_insert` 表中 `id=2` 的数据。

   ```sql
   obclient> delete from t_insert where id=2;
   Query OK, 1 row affected
   ```

4. 查询运行结果。

   ```sql
   obclient> select * from t_insert;
   +----+------+-------+---------------------+
   | id | name | value | gmt_create          |
   +----+------+-------+---------------------+
   |  3 | US   |  NULL | 2022-03-31 17:04:55 |
   +----+------+-------+---------------------+
   1 row in set
   ```

## 事务未提交超时

### 报错：ERROR 4012

* OceanBase 错误码：6210

* 兼容 MySQL 错误码：4012

### 示例

begin 后 `100` 秒内未操作。

```sql
obclient> select now(), t.* from t_insert t ;
ERROR 4012 (25000): Transaction is timeout
obclient> commit;
ERROR 4012 (25000): Transaction is timeout
```

### 处理方法

1. 查看 ob_trx_timeout 参数值，确认事务超时时间是否超过了设置的值。

   ```sql
   obclient> show variables like 'ob_trx_timeout';
   +----------------+-----------+
   | Variable_name  | Value     |
   +----------------+-----------+
   | ob_trx_timeout | 100000000 |
   +----------------+-----------+
   1 row in set
   ```

2. 使用 `rollback` 恢复操作。

   ```sql
   obclient> rollback;
   Query OK, 0 rows affected
   ```

3. 再次查询 `t_insert` 表数据。

   ```sql
   obclient> select now(), t.* from t_insert t ;
   +---------------------+----+------+-------+---------------------+
   | now()               | id | name | value | gmt_create          |
   +---------------------+----+------+-------+---------------------+
   | 2022-04-02 14:14:09 |  1 | CN   |  NULL | 2022-04-02 14:03:31 |
   | 2022-04-02 14:14:09 |  2 | UK   |  NULL | 2022-04-02 14:03:31 |
   | 2022-04-02 14:14:09 |  3 | US   |  NULL | 2022-03-31 17:04:55 |
   +---------------------+----+------+-------+---------------------+
   3 rows in set
   ```
