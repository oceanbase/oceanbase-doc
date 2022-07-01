# 关于 DELETE 语句

DELETE 语句用来删除表中的记录，本文介绍了相关语句的使用方法和示例。

## DELETE 语句

简单的 `DELETE` 语句格式如下：

```sql
DELETE FROM table_name [ WHERE condition ] ;
```

|          参数           | 是否必填 |                描述                |     示例     |
|-----------------------|------|----------------------------------|------------|
| table_name            | 是    | 指定需要删除数据的表                       | table1     |
| \[ WHERE condition \] | 否    | 条件子句指定要删除的数据必须满足的条件，如果没有提供就全表删除。 | where id=3 |

>**说明**
>
>如果表记录数多达几百万以上，会形成大事务，可能会有性能问题。建议带上 `WHERE` 条件分批删除，或者使用 `TRUNCATE TABLE` 语句。

## 示例

### 删除表中数据

删除 ordr 表中符合 `o_w_id=2` 的所有行数据。

```sql
DELETE FROM ordr WHERE o_w_id=2;
```

删除 ordr 表中所有行数据。

```sql
DELETE FROM ordr;
```

>**说明**
>
>除了 `DELETE` 语句外，`REPLACE INTO` 语句也可能会删除数据。

### 分批删除表中数据

当表中数据记录多达百万以上，一次性执行删除可能会出现性能问题，建议根据表内的信息进行分批删除。以下示例通过筛选表中 o_w_id 列数据，分批删除 `o_w_id < 100000`，`o_w_id < 200000`，`o_w_id < 300000` 的数据。

```sql
DELETE FROM ordr WHERE o_w_id < 100000;
DELETE FROM ordr WHERE o_w_id < 200000;
DELETE FROM ordr WHERE o_w_id < 300000;
```

### 清空表数据

`TRUNCATE TABLE` 语句用于完全清空指定表，但是保留表结构，包括表中定义的分区信息。从逻辑上说，该语句与用于删除所有行的 `DELETE FROM` 语句相同。以下示例通过 `TRUNCATE TABLE` 语句清空表 ordr。

```sql
obclient> TRUNCATE TABLE ordr;
```
