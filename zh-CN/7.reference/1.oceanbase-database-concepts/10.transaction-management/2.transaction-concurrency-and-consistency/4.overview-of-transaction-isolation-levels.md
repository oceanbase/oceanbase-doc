# 事务隔离级别

隔离级别是根据事务并发执行过程中必须防止的现象来定义的。

可防止的现象包括：

* 脏读（Dirty Read）：一个事务读到其他事务尚未提交的数据。

* 不可重复读（Non Repeatable Read）：曾经读到的某行数据，再次查询发现该行数据已经被修改或者删除。例如：`select c2 from test where c1=1；`第一次查询 `c2` 的结果为 `1`，再次查询由于其他事务修改了 `c2` 的值，因此 `c2` 的结果为 `2`。

* 幻读（Phantom Read）：只读请求返回一组满足搜索条件的行，再次执行发现另一个提交的事务已经插入满足条件的行。

基于上述三种现象，ANSI 和 ISO/IEC 定义了四种隔离级别，这四种隔离级别如下：

* 读未提交（Read Uncommitted）

* 读已提交（Read Committed）

* 可重复读（Repeatable Read）

* 可串行化（Serializable）

四种隔离级别比较如下所示。

|   隔离级别   | 脏读 | 不可重复读 | 幻读 |
|----------|----|-------|----|
| **读未提交** | 可能 | 可能    | 可能 |
| **读已提交** | 不会 | 可能    | 可能 |
| **可重复读** | 不会 | 不会    | 可能 |
| **可串行化** | 不会 | 不会    | 不会 |

OceanBase 数据库社区版在 MySQL 模式下，支持两种隔离级别：

* 读已提交（Read Committed）：一个事务执行的查询，只能看到这次查询开始之前提交的数据。读已提交无法防止不可重复读和幻读两种异常现象。如果冲突的事务比较少，简单高效的读已提交隔离级别对应用来说是足够的。

* 可重复读（Repeatable Read）：事务内不同时间读到的同一批数据是一致的。无法防止幻读这种异常现象。

OceanBase 数据库默认的隔离级别为读已提交（Read Committed）。

## 隔离级别设置方法

设置隔离级别有两种方式，分别为全局 Global 级别及 Session 级别。

```sql
SET [GLOBAL | SESSION] TRANSACTION ISOLATION LEVEL REPEATABLE READ
```

## 使用限制

OceanBase 数据库 MySQL 模式的 Repeatable Read 隔离级别的实现，能比 MySQL 数据库防止更多的异常。
