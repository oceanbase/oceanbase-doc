# CURRENT_DATE

## 声明

```sql
CURRENT_DATE()
CURRENT_DATE
```

## 说明

返回当前日期，不含时间部分。该函数是 [CURDATE](../1.date-and-time-functions/3.curdate.md) 的别名。

## 示例

```sql
obclient> SELECT CURRENT_DATE;
+--------------+
| CURRENT_DATE |
+--------------+
| 2021-08-23   |
+--------------+
1 row in set

obclient> SELECT CURRENT_DATE();
+----------------+
| CURRENT_DATE() |
+----------------+
| 2021-08-23     |
+----------------+
1 row in set
```
