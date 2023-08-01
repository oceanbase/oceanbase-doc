# Drop an index

Maintenance overhead increases with the number of indexes. We recommend that you drop unnecessary indexes.

## Syntax

```unknow
DROP INDEX [schema.]index_name;
```

### Parameters

| Parameter | Description |
|------------|---------------|
| schema | The name of the schema.  |
| index_name | The name of the index. |

## Examples

1. View the `IDX9` index.

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

2. Drop the `IDX9` index.

   ```unknow
   obclient> DROP INDEX IDX9;
   Query OK, 0 rows affected
   ```

3. View the results.

   ```unknow
   obclient> SELECT INDEX_NAME,INDEX_TYPE, TABLE_OWNER,TABLE_NAME,TABLE_TYPE,UNIQUENESS FROM USER_INDEXES WHERE TABLE_NAME='T_IDX9';
   +------------------------------+------------+-------------+------------+------------+------------+
   | INDEX_NAME                   | INDEX_TYPE | TABLE_OWNER | TABLE_NAME | TABLE_TYPE | UNIQUENESS |
   +------------------------------+------------+-------------+------------+------------+------------+
   | T_IDX9_OBPK_1651134874777227 | NORMAL     | SYS         | T_IDX9     | TABLE      | UNIQUE     |
   +------------------------------+------------+-------------+------------+------------+------------+
   1 row in set
   ```
