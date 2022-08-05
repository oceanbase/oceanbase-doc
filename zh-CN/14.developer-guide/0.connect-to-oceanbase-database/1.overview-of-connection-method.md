# 连接方式概述

本文主要介绍 MySQL 模式下连接和访问 OceanBase 数据库的途径，包括 MySQL 客户端（mysql）、OceanBase 客户端（OBClient）、OceanBase 开发者中心（ODC）。

## MySQL 客户端（mysql）

mysql 是 MySQL 数据库命令行下客户端，需要单独安装。OceanBase 数据库的 MySQL 租户可以通过 mysql 连接。

连接 OceanBase 数据库后，在 mysql 的命令行环境里，可以运行 mysql 运维命令和 SQL 语句来执行一下任务：

* 计算、存储和打印查询结果。

* 创建数据库对象、检查和修改对象定义。

* 执行数据库管理和修改参数等 。

## OceanBase 客户端（OBClient）

OBClient 是一个交互式和批处理查询工具，需要单独安装。它是一个命令行用户界面，在连接到数据库时充当客户端，支持 OceanBase 数据库的 MySQL 租户。

OBClient 运行时需要指定 OceanBase 数据库租户的连接信息。连接上 OceanBase 数据库后，通过 OBClient 可以运行一些数据库命令（包含常用的 MySQL 命令）、SQL 语句和 PL 语句，可以实现以下任务：

* 计算、存储和打印查询结果。

* 创建数据库对象、检查和修改对象定义。

* 开发和运行批处理脚本。

* 执行数据库管理和修改参数等。

## OceanBase 开发者中心（ODC）

OceanBase 开发者中心（OceanBase Developer Center，ODC）是为 OceanBase 数据库量身打造的企业级数据库开发平台。

ODC 支持连接 OceanBase 数据库的 MySQL 租户，同时为数据库开发者提供了数据库日常开发操作、WebSQL、SQL 诊断、会话管理和数据导入导出等功能。
