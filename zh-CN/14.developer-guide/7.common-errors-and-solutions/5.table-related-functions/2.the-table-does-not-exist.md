# 表不存在

本文为您介绍表不存在的相关报错及处理方式。

## 报错：ERROR 1146

### 错误码

* 错误码：5019

* 兼容 MySQL 错误码：1146

### 错误信息

```sql
ERROR 1146 (42S02) : Table \'%s.%s\' doesn\'t exist
```

### 示例

查询 `student` 表时显示表不存在。

```sql
obclient> desc student;
ERROR 1146 (42S02): Table 'test.student' doesn't exist
```

## 如何处理

1. 如果不存在可以通过 `CREATE TABLE` 来创建需要的表，例如：

   ```sql
   CREATE TABLE student(
   id int,
   name varchar(18),
   sex char(1),
    age int,
    address varchar(200),
     email varchar(100),
    date date,
    PRIMARY KEY (id)
     );
   ```

2. 查询需要的表。

   ```sql
   obclient> desc student;
   +---------+--------------+------+-----+---------+-------+
   | Field   | Type         | Null | Key | Default | Extra |
   +---------+--------------+------+-----+---------+-------+
   | id      | int(11)      | NO   | PRI | NULL    |       |
   | name    | varchar(18)  | YES  |     | NULL    |       |
   | sex     | char(1)      | YES  |     | NULL    |       |
   | age     | int(11)      | YES  |     | NULL    |       |
   | address | varchar(200) | YES  |     | NULL    |       |
   | email   | varchar(100) | YES  |     | NULL    |       |
   | date    | date         | YES  |     | NULL    |       |
   +---------+--------------+------+-----+---------+-------+
   7 rows in set
   ```
