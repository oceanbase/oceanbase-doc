# I/O 相关参数
| 配置项 | 描述 | 建议 |
| --- | --- | --- |
| syslog_io_bandwidth_limit | 限制打印程序日志的带宽 | 默认为 30 MB，建议调整为10 MB |
| syslog_level | 系统日志的日志级别 | 性能场景调整为 PERF |
| clog_sync_time_warn_threshold | 日志同步耗时超过一定阈值，打印报警日志，阈值可以通过该配置项调整 | 建议调大，但是需要注意，调大可能会影响 Clog 同步慢问题的调查 |
| trace_log_slow_query_watermark | 事务执行时间超过一定的阈值，打印 slow trans 日志，阈值可以通过该配置项调整 | 建议调大，这样可以避免打印 Slow Query 的 Trace 日志 |
| max_syslog_file_count | observer.log 最大允许数量，超过会自动回收 | 根据磁盘容量进行调整 |
| merge_thread_count | 合并调度线程数量，默认是 10 | 根据实际情况酌情调大 |
| enable_sql_operator_dump | 允许 SQL 层操作（ 比如：hash join ）dump 中间结果，避免由于超出内存大小限制而报错 | AP 测试建议开启 |
| _temporary_file_io_area_size | SQL 中间结果（ 比如：hash join ）在存储层能使用的总大小 | AP 测试建议调大 |
| builtin_db_data_verify_cycle | 宏块巡检周期参数，当设置为0时关闭巡检 | 建议性能相关场景设置成0 |
| data_copy_concurrency | 数据迁移复制任务的最大并发数 | 在进行备份恢复或者迁移复制任务的时候调大 |
| server_data_copy_in_concurrency | 副本迁入的线程数 | 在进行备份恢复或者迁移复制任务的时候调大 |
| server_data_copy_out_concurrency | 副本迁出的线程数 | 在进行备份恢复或者迁移复制任务的时候调大 |
| disk_io_thread_count | 磁盘 I/O 线程数，须为偶数 | 根据 I/O 压力适当调整 |
| enable_async_syslog | 开启异步日志 | 性能场景建议设置为 True |
| fuse_row_cache_priority | 融合行缓存在 KV cache 中的优先级，所谓融合缓存就是 OceanBase 数据库多级存储架构下，如果一行的多个列存在于 memstore ，mini sstable ，minor sstable ，sstable 中，那么在查询该行时，需要将多个列做融合（ fuse )，此时用 fuse row cache 来缓存该行，避免在下次查询时继续做融合操作。对性能有一定影响 | 建议调整为大于 1，可以避免此 Cache 过早被淘汰替换 |
| merge_stat_sampling_ratio | 合并时候数据列统计信息的采样率,当设置为 0 时则关闭统计信息采集 | 性能场景可以设置成 0 或 1，减少合并时进行采样 |
| micro_block_merge_verify_level | 宏块验证级别，0 表示不做任何校验 | 性能场景可以设置成 0，但生产系统不建议修改 |
| sys_bkgd_io_high_percentage | 系统后台 I/O 最高占用百分比 | 保证转储合并等后台任务的正常进行，后台 I/O 拥有至少 128 MB 写入带宽 |
| sys_bkgd_io_low_percentage | 系统后台 I/O 最少占用的百分比 | 保证转储合并等后台任务的正常进行，后台 I/O 拥有至少 128 MB 写入带宽 |
