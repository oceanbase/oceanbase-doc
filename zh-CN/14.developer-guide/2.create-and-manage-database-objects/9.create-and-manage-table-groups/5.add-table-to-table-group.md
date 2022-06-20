# 向表组中增加表

如果您在表创建的时候没有指定表组，也可以事后加入到表组中。有两种方法：一是修改表的表组属性，二是使用 `ALTER TABLEGROUP ADD` 语法。

## 语法

```sql
ALTER TABLE tblname TABLEGROUP = tablegroupname
```

```sql
ALTER TABLEGROUP tablegroupname ADD [TABLE] tblname [, tblname...]
```

### 参数解释

|     **参数**     |                                                         **描述**                                                         |
|----------------|------------------------------------------------------------------------------------------------------------------------|
| tablegroupname | 指定表组。                                                                                                                  |
| tblname        | 表名。对一个表组增加多张表时，表与表之间以逗号（'，'）分隔。 当添加多个表时，允许表名重复。如果待添加的表已经属于 `tablegroupname`的表格组，系统不报错。 |

## 示例

### 示例 1

修改表的表组属性。

> **说明**
>
> 修改表的表组属性时名字不用单引号，否则会区分大小写。

1. 修改 `ordr` 表的表属性。

   ```sql
   obclient> ALTER TABLE ordr TABLEGROUP=tpcc_group;
   Query OK, 0 rows affected
   ```

2. 查看表组属性。

   ```unknow
   obclient> SHOW TABLEGROUPS;
   +-----------------+------------+---------------+
   | Tablegroup_name | Table_name | Database_name |
   +-----------------+------------+---------------+
   | oceanbase       | NULL       | NULL          |
   | tgh             | NULL       | NULL          |
   | tpcc_group      | ordr       | test          |
   +-----------------+------------+---------------+
   3 rows in set
   ```

### 示例 2

向表组中加入表。

> **说明**
>
> 向表组中加入表的前提是表的分区策略跟表组的分区策略保持一致。

1. 查看当前表组属性。

   ```sql
   obclient> SHOW TABLEGROUPS;
   +-----------------+------------+---------------+
   | Tablegroup_name | Table_name | Database_name |
   +-----------------+------------+---------------+
   | oceanbase       | NULL       | NULL          |
   | tgh             | NULL       | NULL          |
   | tpcc_group      | NULL       | NULL          |
   +-----------------+------------+---------------+
   3 rows in set
   ```

2. 向表组 `tpcc_group` 中增加表。

   ```unknow
   obclient> ALTER TABLEGROUP tpcc_group ADD ordr;
   Query OK, 0 rows affected
   ```

3. 查看当前表组信息。

   ```sql
   obclient> SHOW TABLEGROUPS;
   +-----------------+------------+---------------+
   | Tablegroup_name | Table_name | Database_name |
   +-----------------+------------+---------------+
   | oceanbase       | NULL       | NULL          |
   | tgh             | NULL       | NULL          |
   | tpcc_group      | ordr       | test          |
   +-----------------+------------+---------------+
   3 rows in set
   ```
