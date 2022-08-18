# __all_virtual_trans_stat
## 功能
`__all_virtual_trans_stat` 视图用于展示正在进行的事务状态信息。
## 字段说明
| 字段名称 | 类型 | NULL | 描述 |
| --- | --- | --- | --- |
| tenant_id | bigint(20) | NO | 租户 ID |
| svr_ip | varchar(32) | NO | IP地址 |
| svr_port | bigint(20) | NO | 端口 |
| session_id | bigint(20) | NO | 会话 ID |
| proxy_id | varchar(512) | NO | proxy ID |
| trans_type | bigint(20) | NO | 事务类型 |
| trans_id | varchar(512) | NO | 事务 ID |
| is_exiting | bigint(20) | NO | 是否退出 |
| is_readonly | bigint(20) | NO | 是否只读 |
| active_memstore_version | varchar(64) | NO | 活跃 memstore 的版本 |
| partition | varchar(64) | NO | 事务记录涉及的分区信息 |
| participants | varchar(1024) | NO | 事务涉及的所有分区 |
| autocommit | bigint(20) | NO | 是否自动提交 |
| trans_consistency | bigint(20) | NO | 事务一致性级别 |
| ctx_create_time | timestamp(6) | YES | ctx 创建时间 |
| expired_time | timestamp(6) | YES | 过期时间 |
| refer | bigint(20) | NO | 上下文的引用计数 |
| sql_no | bigint(20) | NO | SQL 编号 |
| state | bigint(20) | NO | 状态 |

## 常用 SQL
`__all_virtual_trans_stat` 虚拟表统计的是集群内部所有活跃事务的信息。事务涉及 N 个 Partition 的写操作，每个 Partition 产生一条记录。通过该虚拟表可统计耗时长的事务。
统计 `__all_virtual_trans_stat` 虚拟表中耗时超过100 s 的活跃事务。SQL 语法如下：
```sql
select svr_ip, trans_id, `partition` from __all_virtual_trans_stat where tenant_id = xxx and sql_no > 0 and ctx_create_time < date_sub(now(), INTERVAL 100 SECOND);
```
基于查询结果 `trans_id` 中的 `hash` 字段，可以去 `gv$sql_audit` 中搜索本事务内的所有 SQL 及耗时等信息。
`sql_no > 0` 表示 leader 上的上下文信息，`sql_no = 0` 表示备机回放出来的上下文。因此对于长事务的诊断，需要带上 `sql_no > 0` 的约束条件。
