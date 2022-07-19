# CHARSET

## 声明

```sql
CHARSET(str)
```

## 说明

返回字符串 `str` 使用的字符集。

## 示例

```sql
obclient> SELECT CHARSET("oceanbase");
+-----------------------+
| CHARSET("oceanbase") |
+-----------------------+
| utf8mb4               |
+-----------------------+
1 row in set

obclient> SELECT CHARSET(CONVERT("oceanbase" USING binary));
+--------------------------------------------+
| CHARSET(CONVERT("oceanbase" USING binary)) |
+--------------------------------------------+
| binary                                     |
+--------------------------------------------+
1 row in set
```
