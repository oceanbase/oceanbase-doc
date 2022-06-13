# 数据截断的相关报错

本文为您介绍数据截断的相关报错及处理方式。

## 报错：ERROR 1265

### 错误码

* OceanBase 错误码：4249

* 兼容 MySQL 错误码：1265

### 错误信息

```sql
ERROR 1265 (01000) : Data truncated for column '%.*s' at row %ld
```

### 示例

在表 `ty` 插入数据时报错。

```sql
obclient> INSERT INTO ty VALUE('1970-01-01');
ERROR 1265 (01000): Data truncated for argument
```

## 如何处理

1. 查看 `ty` 表结构。

   ```sql
   obclient> DESC ty;
   +-------+---------+------+-----+---------+-------+
   | Field | Type    | Null | Key | Default | Extra |
   +-------+---------+------+-----+---------+-------+
   | c1    | year(4) | YES  |     | NULL    |       |
   +-------+---------+------+-----+---------+-------+
   1 row in set
   ```

2. 根据字段类型插入正确的值。

   ```sql
   obclient> INSERT INTO ty VALUE('1970');
   Query OK, 1 row affected
   ```

3. 查看已插入的数据。

   ```sql
   obclient> SELECT * FROM ty;
   +------+
   | c1   |
   +------+
   | 1970 |
   +------+
   1 row in set
   ```
