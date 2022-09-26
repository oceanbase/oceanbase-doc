# DROP USER

## 描述

该语句用于删除一个或多个数据库用户。

注意事项：

* 必须拥有全局的 `CREATE USER` 权限，才可以使用 `DROP USER` 命令。

* 不能通过 `DELETE` 方式对 `mysql.user` 表进行删除操作，只能通过 `DROP` 命令删除。

* 成功删除用户后，该用户的所有权限也会被一同删除。

## 语法

```sql
DROP USER user_name [, user_name...];
```

## 参数解释

|    参数     |          描述           |
|-----------|-----------------------|
| user_name | 用户名。同时删除多个用户时，用","隔开。 |

## 示例

删除名为 `sqluser01` 的用户。

```sql
obclient>DROP USER sqluser01;
Query OK, 0 rows affected
```
