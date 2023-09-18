# RANK

## 声明

```sql
RANK() OVER ([ query_partition_clause ] order_by_clause
```

## 说明

计算每一行数据在某列的秩，该列由 `order_by_clause` 中的列决定。

对于秩相同的行，返回值会产生跳跃。

## 示例

```sql
obclient> CREATE TABLE EXPLOYEES(LAST_NAME CHAR(10), SALARY DECIMAL, JOB_ID CHAR(32));
INSERT INTO EXPLOYEES VALUES('JIM', 2000, 'CLEANER');
INSERT INTO EXPLOYEES VALUES('MIKE', 12000, 'ENGINEERING');
INSERT INTO EXPLOYEES VALUES('LILY', 13000, 'ENGINEERING');
INSERT INTO EXPLOYEES VALUES('IRIS', 11000, 'ENGINEERING');
INSERT INTO EXPLOYEES VALUES('TOM', 11000, 'ENGINEERING');
COMMIT;
Query OK, 1 row affected

obclient> SELECT LAST_NAME, RANK() OVER(PARTITION BY JOB_ID ORDER BY SALARY) RANK, DENSE_RANK() OVER(PARTITION BY JOB_ID ORDER BY SALARY) DENSE_RANK, PERCENT_RANK() OVER(PARTITION BY JOB_ID ORDER BY SALARY) PERCENT_RANK FROM EXPLOYEES;
+-----------+------+------------+----------------------------------+
| LAST_NAME | RANK | DENSE_RANK | PERCENT_RANK                     |
+-----------+------+------------+----------------------------------+
| JIM       |    1 |          1 | 0.000000000000000000000000000000 |
| TOM       |    1 |          1 | 0.000000000000000000000000000000 |
| IRIS      |    1 |          1 | 0.000000000000000000000000000000 |
| MIKE      |    3 |          2 | 0.666666666666666666666666666667 |
| LILY      |    4 |          3 | 1.000000000000000000000000000000 |
+-----------+------+------------+----------------------------------+
5 rows in set
```
