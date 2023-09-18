# 查询中使用字符串连接符

在 OceanBase 数据库 MySQL 模式下，字符串连接函数包括 CONCAT() 和 CONCAT_WS() 等。 '\|\|' 默认是表示逻辑运算符"或"，在指定 sql_mode 下，'\|\|' 也可以当作字符串连接符使用。

本文通过具体示例介绍如何在查询中使用字符串连接符。

## 示例 1：查看示例表 `cust` 的客户姓名

在 OceanBase 数据库 MySQL 模式下的SQL 语句示例如下：

```sql
/*创建示例表并录入合适的数据*/
obclient> CREATE TABLE cust (
       c_id        INTEGER,
       c_first     VARCHAR(20),
       c_last      VARCHAR(20),
       c_credit    DECIMAL(10, 2)
 );
Query OK, 0 rows affected

obclient> INSERT INTO cust VALUES(101,'Ann','Smith',16.10);
1 row affected
obclient> INSERT INTO cust VALUES(102,'Madeleine','Johnson',23.00);
1 row affected
obclient> INSERT INTO cust VALUES(103,'Michael','Brown',9.05);
1 row affected

obclient> SELECT CONCAT_WS(' ', c_first, c_last) full_name FROM cust ORDER BY c_last LIMIT 2;
+-------------------+
| full_name         |
+-------------------+
| Michael Brown     |
| Madeleine Johnson |
+-------------------+
2 rows in set
```

## 示例 2："\|\|"作为字符串连接符

如果把 MySQL 模式下的变量 `sql_mode` 值增加一个选项 `PIPES_AS_CONCAT` ，则 '\|\|' 也会当作字符串连接符。SQL 语句示例如下：

```sql
obclient> SET SESSION sql_mode='PIPES_AS_CONCAT,STRICT_TRANS_TABLES,STRICT_ALL_TABLES';
Query OK, 0 rows affected

obclient> SELECT c_first || ' ' || c_last  full_name FROM cust ORDER BY c_last LIMIT 2;
+-------------------+
| full_name         |
+-------------------+
| Michael Brown     |
| Madeleine Johnson |
+-------------------+
2 rows in set
```
