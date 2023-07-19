# DROP TENANT

## 描述

该语句用于删除一个 OceanBase 数据库租户。

>**注意**
>
>只有用 root 用户连接到 sys 租户才能执行 `DROP TENANT` 去删除租户。

## 语法

```sql
drop_tenant_stmt:
DROP TENANT [IF EXISTS] tenant_name [PURGE|FORCE];
```

## 参数解释

|   **参数**    |                **描述**                |
|-------------|--------------------------------------|
| tenant_name | 指定要删除的租户名。                           |
| PURGE       | 表示仅延迟删除租户，且无论回收站功能是否开启，删除的租户均不进入回收站。 |
| FORCE       | 表示无论回收站功能是否开启，均可以立刻删除租户。             |

## 示例

删除租户 `test_tenant1` 。

```sql
obclient> DROP TENANT test_tenant1;
```
