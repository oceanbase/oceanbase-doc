# 闪回被删除的表

OceanBase 支持回收站功能，通过回收站可以闪回已删除的表。默认回收站是开启的，回收站是否开启由租户变量 Recyclebin 控制。

## 前提条件

当前用户具有用户级 SUPER 权限。

## 开启关闭回收站

### 语法

```sql
set global recyclebin = ON | OFF;
```

> **说明**
>
> 修改回收站的开启状态后，只对后续新连接会话生效。

### 示例

将已删除 `dws_ny` 表从回收站恢复。

* 打开回收站。

  ```sql
  set global recyclebin = ON;
  ```

* 删除 `dws_ny` 表。

  ```sql
  obclient> drop table dws_ny;
  Query OK, 0 rows affected (0.01 sec)
  ```

* 查看回收站。

  ```sql
  obclient> show recyclebin\G
  *************************** 1. row ***************************
    OBJECT_NAME: __recycle_$_100051_1647945836520208
  ORIGINAL_NAME: dws_ny
           TYPE: TABLE
     CREATETIME: 2022-03-22 18:43:56.521081
  1 row in set (0.00 sec)
  ```

* 在回收站中恢复 `dws_ny` 表。

  ```unknow
  obclient> flashback table __recycle_$_100051_1647945836520208 to before drop rename to dws_ny;
  ```

* 查看已从回收站恢复的 `dws_ny` 表。

  * `dws_ny` 表结构：

    ```unknow
    obclient> desc dws_ny;
    +-------+--------------+------+-----+---------+-------+
    | Field | Type         | Null | Key | Default | Extra |
    +-------+--------------+------+-----+---------+-------+
    | id    | int(11)      | NO   | PRI | NULL    |       |
    | name  | varchar(200) | YES  |     | NULL    |       |
    | date  | date         | YES  |     | NULL    |       |
    +-------+--------------+------+-----+---------+-------+
    3 rows in set
    ```

  * `dws_ny` 表数据：

    ```unknow
    obclient> select * from dws_ny;
    +----+--------+------------+
    | id | name   | date       |
    +----+--------+------------+
    |  1 | 张三   | 0000-00-00 |
    |  2 | 李四   | 0000-00-00 |
    +----+--------+------------+
    2 rows in set
    ```
