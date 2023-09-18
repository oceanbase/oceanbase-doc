# 生态工具概述

本文介绍了社区版 OceanBase 数据库可参考使用的生态工具。

## ob_admin

ob_admin 是 OceanBase 数据库的配套运维工具之一，主要用于排查数据不一致、丢数据、错误数据等问题。详细的使用说明，请参考 [ob_admin 简介](1.ob-admin/1.overview-of-ob_admin.md)。

## OBAgent

OBAgent 是一个监控采集框架，支持推、拉两种数据采集模式，可以满足不同的应用场景。OBAgent 默认支持的插件包括主机数据采集、OceanBase 数据库指标的采集、监控数据标签处理和 Prometheus 协议的 HTTP 服务。详细的使用说明，请参考 [什么是 OBAgent](2.ob-agent/1.about-obagent/1.what-is-obagent.md)。

## ob_error

ob_error 是 OceanBase 数据库的一个错误码解析工具，ob_error 可以根据您输入的错误码返回相对应的原因和解决方案。在 ob_error 的帮助下，您无需查找文档即可获取基本的错误信息。详细的使用说明，请参考 [ob_error](4.cdc/1.overview-of-cdc.md)。

## CDC

CDC （Change Data Capture，即变更数据捕获）能够帮助您识别从上次提取之后发生变化的数据。您可用 CDC 提供的数据做历史库、近实时缓存、提供给消息队列（MQ），用户消费 MQ 做分析和审计等。详细的使用说明，请参考 [CDC 概述](4.cdc/1.overview-of-cdc.md)。

## OBD

OBD 全称为 OceanBase Deployer，是 OceanBase 开源软件的安装部署工具。OBD 同时也是包管理器，可以用来管理 OceanBase 所有的开源软件。详细的使用说明，请参考 [OBD 文档](https://www.oceanbase.com/docs/community/obd-cn/V1.4.0/10000000000436994)。

## TableAPI

TableAPI 提供了对表模型数据的操作接口。同时，在内部，TableAPI 定义了客户端和数据库服务端之间的一组通用的交互协议。详细的使用说明，请参考 [TableAPI 实现介绍](6.tableapi/1.introduction-to-tableapi/1.implementation-of-tableapi.md)。

## DOOBA

DOOBA 是 OceanBase 数据库内部的一个运维脚本，用于性能监控，使用 Python 语言开发，且仅支持 Python 2.7。本文将详细介绍如何使用 DOOBA 对 OceanBase 数据库性能进行监控。详细的使用说明，请参考 [DOOBA](7.dooba.md)。

## HBaseAPI

HBaseAPI 客户端基于 TableAPI 提供的基本接口，在客户端封装了 HBase 兼容的 API 接口（目前已兼容 HBase 0.94 版本的特性）。若您当前有业务使用了原生 HBase 数据操作逻辑，您可以通过安装 OceanBase 数据库集群，在 OBServer 服务端建立 HBase Table，并通过 HBaseAPI 进行数据操作。详细的使用说明，请参考 [HBaseAPI 方案介绍](8.hbaseapi/1.introduction-to-hbaseapi-scheme.md)。

## SQL Diagnoser

SQL Diagnoser 是一款敏捷版 SQL 诊断工具，可直接分析业务集群，找出常见的可疑 SQL 及隐藏的性能问题。详细的使用说明，请参考 [SQL Diagnoser 概述](9.sql_diagnoser/1.overview-of-sql_diagnoser.md)。
