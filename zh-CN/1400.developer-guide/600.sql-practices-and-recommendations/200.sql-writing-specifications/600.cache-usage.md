# cache 的使用规范

本文介绍在 OceanBase 数据库关于 cache 的使用规范。

* 业务上对某个字段频繁的重复写，推荐使用写缓存机制，如计数器的写入

* 执行计划所占内存超过 20M 时，不会加入计划缓存。

* 如果该计划为分布式执行计划且涉及多个表，不会加入计划缓存。

* 使用 hint 控制计划缓存

  * `/+ USE_PLAN_CACHE(NONE)/` 表示不使用计划缓存。

  * `/+USE_PLAN_CACHE(DEFAULT)/` 表示使用计划缓存。

* SQL 语句禁止使用提示，如 `force index`，`ignore index`，`straight_join`，`SQL_no_cache` 等。
