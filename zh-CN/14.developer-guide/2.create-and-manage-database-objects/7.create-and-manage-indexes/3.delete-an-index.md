# 删除索引

当索引过多时，维护开销会增大，您可以根据需要删除不必要的索引。

## 语法

MySQL 模式下，删除索引的语法格式如下：

### 语法 1

```sql
DROP INDEX index_name idx table_name;
```

参数解释

|    参数     |   描述   |
|-----------|---------|
| indexname | 指定索引名称。 |
| tblname   | 指定表名。   |

### 语法 2

```unknow
ALTER TABLE table_name DROP key|index index_name ;
```

## 示例

### 示例 1

1. 查看 `test` 表的索引。

   ```sql
   obclient> SHOW INDEX FROM test;
   +-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   | Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment   | Index_comment | Visible |
   +-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   | test  |          0 | PRIMARY  |            1 | c1          | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     |
   | test  |          1 | idx      |            1 | c1          | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     |
   | test  |          1 | idx      |            2 | c2          | A         |        NULL | NULL     | NULL   | YES  | BTREE      | available |               | YES     |
   +-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   3 rows in set
   ```

2. 删除 `test` 表的索引 `idx` 。

   ```sql
   obclient> DROP INDEX idx on test;
   Query OK, 0 rows affected
   ```

3. 查询 `test` 表的索引。

   ```sql
   obclient> SHOW INDEX FROM test;
   +-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   | Table | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment   | Index_comment | Visible |
   +-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   | test  |          0 | PRIMARY  |            1 | c1          | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     |
   +-------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   1 row in set
   ```

### 示例 2

1. 查看 `t_idx1` 表的索引。

   ```unknow
   obclient> SHOW INDEX FROM t_idx1;
   +--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   | Table  | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment   | Index_comment | Visible |
   +--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   | t_idx1 |          0 | PRIMARY  |            1 | id          | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     |
   | t_idx1 |          1 | idx      |            1 | date        | A         |        NULL | NULL     | NULL   | YES  | BTREE      | available |               | YES     |
   +--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   2 rows in set
   ```

2. 删除 `t_idx1` 表的索引。

   ```unknow
   obclient> ALTER TABLE t_idx1 DROP INDEX idx ;
   Query OK, 0 rows affected
   ```

3. 再次查看 `t_idx1` 表的索引。

   ```unknow
   obclient> SHOW INDEX FROM t_idx1;
   +--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   | Table  | Non_unique | Key_name | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment   | Index_comment | Visible |
   +--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   | t_idx1 |          0 | PRIMARY  |            1 | id          | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     |
   +--------+------------+----------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   1 row in set
   ```
