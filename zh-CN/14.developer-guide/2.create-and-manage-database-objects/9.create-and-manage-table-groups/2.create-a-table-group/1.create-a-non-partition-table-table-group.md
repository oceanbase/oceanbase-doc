# 创建非分区表表组

本文内容主要介绍非分区表组的创建。

## 语法

```sql
CREATE TABLEGROUP [IF NOT EXISTS] tablegroupname [opt_tablegroup_option_list]

opt_tablegroup_option_list:
tablegroup_option [tablegroup_option]

tablegroup_option:
LOCALITY [=] locality_name
| PRIMARY_ZONE [=] primary_zone_name
```

## 参数解释

|     **参数**      |                                                                 **描述**                                                                  |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| tablegroup_name | 表组名称，最长 64 个字符，字符只能有大小写英文字母，数字和下划线，而且必须以字母或下划线开头，并且不能使用 OceanBase 数据库的关键字。 如果要创建的表组名称已存在，并且没有指定 `IF NOT EXISTS`，则会出现错误。 |

## 示例

1. 创建表组 `tgn`。

   ```sql
   obclient> CREATE TABLEGROUP tgn;
   Query OK, 0 rows affected
   ```

2. 查看已新建的 `tgn` 表组信息。

   ```sql
   obclient> SHOW TABLEGROUPS WHERE Tablegroup_name='tgn';
   +-----------------+------------+---------------+
   | Tablegroup_name | Table_name | Database_name |
   +-----------------+------------+---------------+
   | tgn             | NULL       | NULL          |
   +-----------------+------------+---------------+
   1 row in set
   ```

3. 查看已新建的 `tgn` 表组信息。

   ```sql
   obclient> SHOW CREATE Tablegroup tgn\G
   *************************** 1. row ***************************
          Tablegroup: tgn
   Create Tablegroup: CREATE TABLEGROUP IF NOT EXISTS `tgn`  BINDING = FALSE
     partition by hash partitions 10
   1 row in set
   ```
