# VERSION

## 声明

```sql
VERSION()
```

## 说明

返回当前 OceanBase 数据库的版本信息，字符集为 utf8mb4。

## 示例

```sql
obclient> SELECT VERSION();
+-----------+
| VERSION() |
+-----------+
| 3.2.0     |
+-----------+
1 row in set
```
