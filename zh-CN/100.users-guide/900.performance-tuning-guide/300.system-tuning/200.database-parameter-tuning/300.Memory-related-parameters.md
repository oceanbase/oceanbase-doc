# 内存相关参数

| 配置项 | 描述 | 建议 |
| --- | --- | --- |
| memory_chunk_cache_size | Observer cache 2 M 内存块的大小 | 默认值为 0，建议保持默认值 |
| minor_warm_up_duration_time | memtable 预热时间 | 设置为 0，转储 sstable 预热时间，转储完成后到预热时间内，所有对应 Partition 的流量会逐步从 Memtable 过渡到 sstable。设置为 0，转储之后流量马上切到 sstable，使得 Memtable 快速释放，内存释放更快 |
| _enable_parallel_minor_merge | 分区内并行转储 | 提高大分区转储效率，建议开启 |
| minor_merge_concurrency | 转储线程数 | 增大转储的线程数，期望提高转储的速度 |
| memory_limit_percentage | OceanBase 数据库占系统总内存的比例 | 提高 OceanBase 数据库可用的内存量 |
| memstore_limit_percentage | memstore 占租户的内存比，本内存不独占 | 尽量增大 Memstore 的空间。如果过大可能会存在写入过大的场景，即存在由于转储速度跟不上写入速度导致内存超限的风险 |
| freeze_trigger_percentage | 触发转储的时机 | 在写入压力比较大的系统，建议可以调整到 30~50，尽快触发转储，防止内存不足。触发转储会带来额外的 CPU 和 I/O 开销，且频繁触发转储后，mini sstable 的个数会增加，增加了查询路径，对性能产生一定影响 |
| minor_freeze_times | 指定多少次转储后触发大版本合并 | 增加 minor freeze 的次数，尽量不在测试期间触发 major freeze |
| _mini_merge_concurrency | mini merge 线程数 | 建议增加 mini merge 的线程数，期望提高 mini merge 的速度 |
| _flush_clog_aggregation_buffer_timeout | 控制刷新 clog 日志聚合 buffer 的超时时间 | 建议调整为 2 ms |
| _clog_aggregation_buffer_amount | clog 日志聚合 buffer 大小 | 建议设置为 4 |
| system_memory | 500 租户预留内存大小 | 建议保持默认值 |
| use_large_pages | 开启内存大页 |  需要在OS端开启内存大页功能，此功能才会生效，开启后可以提高内存页表查询效率 |
