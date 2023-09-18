# 查看表组信息

本文介绍如何查看表组信息。

## 语法

使用命令 `SHOW TABLEGROUPS` 和 `SHOW CREATE TABLE` 来查看表组信息。

## 示例

### 示例 1

查看 `tablegroups` 表组信息。

```sql
obclient> SHOW TABLEGROUPS;
+-----------------+------------+---------------+
| Tablegroup_name | Table_name | Database_name |
+-----------------+------------+---------------+
| oceanbase       | NULL       | NULL          |
| tpcc_group      | ordr       | test          |
+-----------------+------------+---------------+
2 rows in set
```

### 示例 2

查看 `tablegroups` 表组定义。

```sql
obclient> SHOW CREATE TABLEGROUP tpcc_group\G
*************************** 1. row ***************************
       Tablegroup: tpcc_group
Create Tablegroup: CREATE TABLEGROUP IF NOT EXISTS `tpcc_group`  BINDING = FALSE
  partition by hash partitions 6
1 row in set
```
