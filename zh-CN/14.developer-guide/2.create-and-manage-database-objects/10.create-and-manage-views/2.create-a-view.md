# 创建视图

本文为您介绍如何创建普通视图。

## 语法

可以使用 `CREATE VIEW` 语句来创建视图。

```sql
create_view_stmt:
  CREATE [OR REPLACE] VIEW view_name [(column_name_list)] AS select_stmt;

column_name_list:
    column_name [, column_name ...]
```

### 参数解释

|      **参数**      |                                                                                                                 **描述**                                                                                                                 |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OR REPLACE       | 表示如果要创建的同义词名称已存在，则使用新的定义重新创建同义词。                                                                                                                                                                                                       |
| view_name        | 视图名。                                                                                                                                                                                                                                   |
| select_stmt      | 是一种 SELECT 语句。它给出了视图的定义。该语句可以从基表或其他视图进行选择。                                                                                                                                                                                             |
| column_name_list | 视图必须具有唯一的列名，不得有重复，就像基表那样。默认情况下，由 SELECT 语句检索的列名将用作视图列名。 要想为视图列定义明确的名称，可使用可选的 column_name_list 子句，列出由逗号隔开的 ID。column_name_list 中的名称数目必须等于SELECT语句检索的列数。 SELECT 语句检索的列可以是对表列的简单引用。也可以是使用函数、常量值、操作符等的表达式。 |

## 示例

根据 `t1` 和 `t2` 两张表，创建两表关联查询视图 `v` 。

1. 创建 `t1` 表。

   ```sql
   obclient> CREATE TABLE t1 (id1 int,name varchar(256),sex varchar(256));
   Query OK, 0 rows affected
   ```

2. 创建 `t2` 表。

   ```sql
   obclient> CREATE TABLE t2 (id2 int,age int,date date);
   Query OK, 0 rows affected
   ```

3. 创建视图 `v` 。

   ```sql
   obclient> CREATE VIEW v
                     AS
                     SELECT
                     id1 as id,name, date, age, sex
                     FROM t1 a, t2 b
                     WHERE a.id1 = b.id2;
   Query OK, 0 rows affected
   ```

4. 查看视图 `v`。

   ```sql
   obclient> DESC v;
   +-------+--------------+------+-----+---------+-------+
   | Field | Type         | Null | Key | Default | Extra |
   +-------+--------------+------+-----+---------+-------+
   | id    | int(11)      | YES  |     | NULL    |       |
   | name  | varchar(256) | YES  |     | NULL    |       |
   | date  | date         | YES  |     | NULL    |       |
   | age   | int(11)      | YES  |     | NULL    |       |
   | sex   | varchar(256) | YES  |     | NULL    |       |
   +-------+--------------+------+-----+---------+-------+
   5 rows in set
   ```
