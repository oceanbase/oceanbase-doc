# 唯一键冲突

本文为您介绍唯一键冲突的相关报错及处理方式。

## 报错：ERROR 1062

### 错误码

* OceanBase 错误码：5024

* 兼容 MySQL 错误码：1062

### 错误信息

```sql
ERROR 1062 (23000) : Duplicate entry \'%s\' for key \'%.*s\'
```

### 示例

`t_insert` 表插入数据时显示主键值 `3` 重复。

```sql
obclient> INSERT INTO t_insert(id, name, value) VALUES (3,'UK', 10003),(4, 'JP', 10004);
ERROR 1062 (23000): Duplicate entry '3' for key 'PRIMARY'
```

## 如何处理

### 方式 1

通过 INSERT IGNORE INTO 避免约束冲突，IGNORE 关键字可以忽略由于约束冲突导致的 INSERT 失败的影响。

1. 在 `t_insert` 表插入数据时添加 IGNORE 关键字。

   ```sql
   obclient> INSERT IGNORE INTO t_insert(id, name, value) VALUES (3,'UK', 10003),(4, 'JP', 10004);
   Query OK, 1 row affected
   ```

2. 再次查看 `t_insert` 表的数据。

   ```sql
   obclient> select * from t_insert;
   +----+------+-------+---------------------+
   | id | name | value | gmt_create          |
   +----+------+-------+---------------------+
   |  1 | CN   | 10001 | 1970-01-01 16:05:45 |
   |  2 | US   | 10002 | 1970-01-01 16:05:54 |
   |  3 | EN   | 10003 | 1970-01-01 16:05:54 |
   |  4 | JP   | 10004 | 1970-01-01 16:06:08 |
   +----+------+-------+---------------------+
   4 rows in set
   ```

### 方式 2

通过 INSERT INTO ON DUPLICATE KEY UPDATE 避免约束冲突，可以指定对重复主键或唯一键的后续处理，以下示例对冲突行内容进行了更新。

>**说明**
>
>* 指定 ON DUPLICATE KEY UPDATE：当要插入的主键或唯一键有重复时，会用配置值替换待插入的值。
>
>* 不指定 ON DUPLICATE KEY UPDATE：当要插入的主键或唯一键有重复时，插入报错。

1. 在 `t_insert` 表插入数据时通过 INSERT INTO ON DUPLICATE KEY UPDATE 避免约束冲突。

   ```sql
   obclient> INSERT INTO t_insert(id, name, value) VALUES (3,'UK', 10003),(4, 'JP', 10004) ON DUPLICATE KEY UPDATE name=VALUES(name);
   Query OK, 1 row affected
   ```

2. 再次查看 `t_insert` 表的数据。

   ```sql
   obclient> select * from t_insert;
   +----+------+-------+---------------------+
   | id | name | value | gmt_create          |
   +----+------+-------+---------------------+
   |  1 | CN   | 10001 | 1970-01-01 16:05:45 |
   |  2 | US   | 10002 | 1970-01-01 16:05:54 |
   |  3 | UK   | 10003 | 1970-01-01 16:05:54 |
   |  4 | JP   | 10004 | 1970-01-01 16:06:08 |
   +----+------+-------+---------------------+
   4 rows in set
   ```
