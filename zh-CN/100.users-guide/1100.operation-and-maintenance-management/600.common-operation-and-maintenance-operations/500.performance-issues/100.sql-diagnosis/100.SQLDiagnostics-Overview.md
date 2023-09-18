# SQL 诊断概述

SQL 问题是性能问题中最常见的一类。OCP 的 SQL 诊断功能根据 SQL 运行特征将 SQL 分为可疑 SQL、TopSQL 和 SlowSQL，并提供索引绑定功能，方便您在线优化 SQL。可疑 SQL 为性能下降和执行计划发生变化的 SQL ，您需要重点关注。可疑 SQL 的诊断结果包含性能下降的原因分析等。SlowSQL 将响应时间超过 100ms 的 SQL 进行展示。TopSQL 将全量 SQL 根据平均响应时间进行排序展示。

本章将分篇介绍以下两种 SQL：

* [TopSQL 诊断](3.topsql.md)

* [SlowSQL 诊断](4.SlowSQL.md)
