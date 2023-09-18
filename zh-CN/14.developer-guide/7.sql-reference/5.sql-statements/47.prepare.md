# PREPARE

## 描述

该语句用于准备一个语句。

## 语法

```sql
PREPARE stmt_name FROM preparable_stmt
```

## 参数解释

|       参数        |        描述        |
|-----------------|------------------|
| stmt_name       | 指定准备语句的名称。       |
| preparable_stmt | 指定要准备执行的 SQL 语句。 |

## 示例

执行准备的语句。

```sql
obclient> PREPARE stmt1 FROM 'SELECT SQRT(POW(?,2) + POW(?,2)) AS hypotenuse';
Query OK, 0 rows affected

obclient> SET @a = 3;
Query OK, 0 rows affected

obclient> SET @b = 4;
Query OK, 0 rows affected

obclient> EXECUTE stmt1 USING @a, @b;
Query OK, 0 rows affected
```

>**说明**
>
>目前，OceanBase 数据库不支持交互客户端显式结果。
