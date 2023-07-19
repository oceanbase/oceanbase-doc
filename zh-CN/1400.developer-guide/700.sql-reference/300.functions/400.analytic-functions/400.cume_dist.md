# CUME_DIST

## 声明

```sql
CUME_DIST() OVER ([ query_partition_clause ] order_by_clause)
```

## 说明

该函数计算一个值的分布，返回值为大于 `0` 小于等于 `1` 的值。作为一个分析函数，`CUME_DIST()` 在升序情况下计算比当前行的特定列数值小的数据的占比。

## 示例

按 `job_id` 分组并在薪水升序排列的情况下，每行数据在窗口内的排序列上的占比。

```sql
obclient> CREATE TABLE EXPLOYEES(LAST_NAME CHAR(10), SALARY DECIMAL, JOB_ID CHAR(32));
INSERT INTO EXPLOYEES VALUES('JIM', 2000, 'CLEANER');
INSERT INTO EXPLOYEES VALUES('MIKE', 12000, 'ENGINEERING');
INSERT INTO EXPLOYEES VALUES('LILY', 13000, 'ENGINEERING');
INSERT INTO EXPLOYEES VALUES('IRIS', 11000, 'ENGINEERING');
INSERT INTO EXPLOYEES VALUES('TOM', 11000, 'ENGINEERING');
COMMIT;
Query OK, 1 row affected

obclient> SELECT LAST_NAME, CUME_DIST() OVER(PARTITION BY JOB_ID ORDER BY SALARY) CUME_DIST FROM EXPLOYEES;
+-----------+----------------------------------+
| LAST_NAME | CUME_DIST                        |
+-----------+----------------------------------+
| JIM       | 1.000000000000000000000000000000 |
| TOM       | 0.500000000000000000000000000000 |
| IRIS      | 0.500000000000000000000000000000 |
| MIKE      | 0.750000000000000000000000000000 |
| LILY      | 1.000000000000000000000000000000 |
+-----------+----------------------------------+
5 rows in set
```
