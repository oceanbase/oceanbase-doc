删除索引 
=========================

当索引过多时，维护开销会增大，您可以根据需要删除不必要的索引。

语法 
-----------------------

```unknow
DROP INDEX [schema.]index_name;
```



### 参数解释 



|     参数     |      描述       |
|------------|---------------|
| schema     | 指定 Schema 名称。 |
| index_name | 指定索引名称        |



示例 
-----------------------

1. 查看 `IDX9` 索引。

   ```unknow
   obclient> SELECT INDEX_NAME,INDEX_TYPE, TABLE_OWNER,TABLE_NAME,TABLE_TYPE,UNIQUENESS FROM USER_INDEXES WHERE TABLE_NAME='T_IDX9';
   +------------------------------+------------+-------------+------------+------------+------------+
   | INDEX_NAME                   | INDEX_TYPE | TABLE_OWNER | TABLE_NAME | TABLE_TYPE | UNIQUENESS |
   +------------------------------+------------+-------------+------------+------------+------------+
   | T_IDX9_OBPK_1651134874777227 | NORMAL     | SYS         | T_IDX9     | TABLE      | UNIQUE     |
   | IDX9                         | NORMAL     | SYS         | T_IDX9     | TABLE      | NONUNIQUE  |
   +------------------------------+------------+-------------+------------+------------+------------+
   2 rows in set
   ```

   

2. 删除 `IDX9` 索引。

   ```unknow
   obclient> DROP INDEX IDX9;
   Query OK, 0 rows affected
   ```

   

3. 查看运行结果。

   ```unknow
   obclient> SELECT INDEX_NAME,INDEX_TYPE, TABLE_OWNER,TABLE_NAME,TABLE_TYPE,UNIQUENESS FROM USER_INDEXES WHERE TABLE_NAME='T_IDX9';
   +------------------------------+------------+-------------+------------+------------+------------+
   | INDEX_NAME                   | INDEX_TYPE | TABLE_OWNER | TABLE_NAME | TABLE_TYPE | UNIQUENESS |
   +------------------------------+------------+-------------+------------+------------+------------+
   | T_IDX9_OBPK_1651134874777227 | NORMAL     | SYS         | T_IDX9     | TABLE      | UNIQUE     |
   +------------------------------+------------+-------------+------------+------------+------------+
   1 row in set
   ```

   



