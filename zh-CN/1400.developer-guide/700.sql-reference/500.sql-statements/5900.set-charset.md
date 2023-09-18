# SET CHARSET

## 描述

该语句用于设置客户端与结果字符集。

## 语法

```sql
SET {CHARSET | CHARACTER SET} {DEFAULT | charset_name};
```

## 参数解释

|      参数      |    解释     |
|--------------|------------------------------------------------|
| charset_name | 指定客户端与结果字符集，可使用的字符集包括：`utf8mb4`、`binary` 。 |
| DEFAULT      | 使用系统默认字符集。      |

## 示例

使用 `SET CHARSET` 设置客户端字符集, 会同时修改 `character_set_client` 和 `character_set_results`。

```sql
OceanBase(root@oceanbase)>set charset binary;
Query OK, 0 rows affected

OceanBase(root@oceanbase)>show variables like '%char%';
+--------------------------------------+---------+
| Variable_name        | Value   |
+--------------------------------------+---------+
| character_set_client | binary  |
| character_set_connection     | utf8mb4 |
| character_set_database       | utf8mb4 |
| character_set_filesystem     | binary  |
| character_set_results        | binary  |
| character_set_server | utf8mb4 |
| character_set_system | utf8mb4 |
| validate_password_special_char_count | 0       |
+--------------------------------------+---------+
8 rows in set
```
