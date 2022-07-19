# 字符集

OceanBase 数据库默认的字符集是 `utf8mb4`。

OceanBase 数据库目前支持如下字符集：

* `binary`

* `utf8mb4`

>**说明**
>
>* 为支持无缝迁移，OceanBase在语法上将 `UTF8` 视为 `UTF8MB4` 的同义词。
>
>* 数据库字符集暂不支持修改。

要显示可用的字符集，请使用如下 `SHOW CHARACTER SET` 语句。

```sql
obclient> SHOW CHARACTER SET;
+---------+-----------------------+--------------------+--------+
| Charset | Description           | Default collation  | Maxlen |
+---------+-----------------------+--------------------+--------+
| binary  | Binary pseudo charset | binary             |      1 |
| utf8mb4 | UTF-8 Unicode         | utf8mb4_general_ci |      4 |
+---------+-----------------------+--------------------+--------+
2 rows in set
```

OceanBase 数据库支持指定非默认字符集与服务器通信。例如，要使用 `binary` 字符集，在连接到服务器后执行以下语句：

```sql
obclient> SET NAMES binary;
Query OK, 0 rows affected
```
