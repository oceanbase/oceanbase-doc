# 分区表使用建议

本文介绍OceanBase数据库 中的 MySQL 模式下分区表的使用建议。

## 背景信息

通常当表的数据量非常大，以致于可能使数据库空间紧张，或者由于表非常大导致相关 SQL 查询性能变慢时，可以考虑使用分区表。

使用分区表时要选择合适的拆分键以及拆分策略。如果是日志类型的大表，根据时间类型的列做 RANGE 分区是最合适的。如果是并发访问非常高的表，结合业务特点选择能满足绝大部分核心业务查询的列作为拆分键是最合适的。无论选哪个列做为分区键，都不大可能满足所有的查询性能。

分区表中的全局唯一性需求可以通过主键约束和唯一约束实现。OceanBase 数据库的分区表的主键约束和局部唯一索引必须包含拆分键。唯一约束也是一个全局索引。全局唯一的需求也可以通过本地唯一索引实现，只需要在唯一索引里包含拆分键。

## 示例

创建有唯一性约束的分区表

1. 创建 `account` 表。

   ```sql
   CREATE TABLE account(
            id bigint NOT NULL PRIMARY KEY
            , name varchar(50) NOT NULL
            , value number NOT NULL
            , gmt_create timestamp DEFAULT current_timestamp NOT NULL
            , gmt_modified timestamp DEFAULT current_timestamp NOT NULL
        ) PARTITION BY HASH(id) PARTITIONS 16;
   ```

2. 创建索引 `account_uk` 。

   ```sql
    CREATE UNIQUE INDEX account_uk ON account(name, id) LOCAL ;
   ```

3. 查看 `account` 表索引。

   ```sql
   obclient> show indexes from account;
   +---------+------------+------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   | Table   | Non_unique | Key_name   | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment   | Index_comment | Visible |
   +---------+------------+------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   | account |          0 | PRIMARY    |            1 | id          | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     |
   | account |          0 | account_uk |            1 | name        | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     |
   | account |          0 | account_uk |            2 | id          | A         |        NULL | NULL     | NULL   |      | BTREE      | available |               | YES     |
   +---------+------------+------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+-----------+---------------+---------+
   3 rows in set
   ```

4. 查看分区表中的约束与索引信息。

   ```sql
   obclient>  SELECT * FROM information_schema.`TABLE_CONSTRAINTS` WHERE table_schema='data_ny' AND table_name='ACCOUNT';
   +--------------------+-------------------+-----------------+--------------+------------+-----------------+
   | CONSTRAINT_CATALOG | CONSTRAINT_SCHEMA | CONSTRAINT_NAME | TABLE_SCHEMA | TABLE_NAME | CONSTRAINT_TYPE |
   +--------------------+-------------------+-----------------+--------------+------------+-----------------+
   | def                | data_ny           | PRIMARY         | data_ny      | account    | PRIMARY KEY     |
   | def                | data_ny           | account_uk      | data_ny      | account    | UNIQUE          |
   +--------------------+-------------------+-----------------+--------------+------------+-----------------+
   2 rows in set
   ```
