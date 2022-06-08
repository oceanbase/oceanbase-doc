# 外键冲突

本文为您介绍外键冲突的相关报错及处理方式。

## 报错：ERROR 1215

### 错误码

* OceanBase 错误码：5317

* 兼容 MySQL 错误码：1215

### 错误信息

```sql
ERROR 1062 (23000) : Duplicate entry \'%s\' for key \'%.*s\'
```

### 示例

`cust` 表创建外键约束时显示关联字段错误。

```sql
obclient> ALTER TABLE cust ADD CONSTRAINT ware FOREIGN KEY (c_w_id) REFERENCES ware(w_name);
ERROR 1215 (HY000): Cannot add foreign key constraint
```

## 如何处理

1. 查看 `ware` 表的表结构，并找到该表主键。

   ```sql
   obclient> DESC WARE;
   +--------+--------------+------+-----+---------+-------+
   | Field  | Type         | Null | Key | Default | Extra |
   +--------+--------------+------+-----+---------+-------+
   | w_id   | int(11)      | NO   | PRI | NULL    |       |
   | w_name | varchar(256) | YES  | UNI | NULL    |       |
   | w_city | varchar(256) | YES  | UNI | NULL    |       |
   +--------+--------------+------+-----+---------+-------+
   3 rows in set
   ```

2. 重新创建外键约束。

   ```sql
   obclient> ALTER TABLE cust ADD CONSTRAINT ware FOREIGN KEY (c_w_id) REFERENCES ware(w_id);
   \Query OK, 0 rows affected
   ```
