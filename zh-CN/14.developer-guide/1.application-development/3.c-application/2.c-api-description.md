# C 相关 API 介绍

本文主要介绍常用的 C API 函数和示例。

## C API 函数概览

当前版本 OceanBase Connector/C 所有可用的 C API 函数如下表所示。

有关各接口详细信息，请参见官网文档《[OceanBase Connector/C](https://www.oceanbase.com/docs/community/connector-c-cn/V1.0.0/10000000000017244)》 中的 **C API 函数** 章节。

|                                     **名称**                                      |                         **描述**                          |
|---------------------------------------------------------------------------------|---------------------------------------------------------|
| my_init()                        | 初始化 OceanBase 库的全局变量。                                   |
| mysql_affected_rows()            | 返回上一次由 `UPDATE`、`DELETE` 或 `INSERT` 语句进行更改、删除或插入的行数。    |
| mysql_autocommit()               | 设置自动提交模式。                                               |
| mysql_change_user()              | 在打开的连接上更改用户和数据库。                                        |
| mysql_character_set_name()       | 返回当前连接的默认字符集名称。                                         |
| mysql_client_find_plugin()       | 返回指向插件的指针。                                              |
| mysql_client_register_plugin()   | 注册一个插件。                                                 |
| mysql_close()                    | 关闭与服务器的连接。                                              |
| mysql_commit()                   | 提交事务。                                                   |
| mysql_connect()                  | 连接服务器。此功能已弃用。                                           |
| mysql_create_db()                | 创建数据库。此功能已弃用。                                           |
| mysql_data_seek()                | 在结果集中查找任意行号。                                            |
| mysql_debug()                    | 使用给定的字符串执行 `DBUG_PUSH`。                                 |
| mysql_drop_db()                  | 删除数据库。此功能已弃用。                                           |
| mysql_dump_debug_info()          | 引发服务器将调试信息写入错误日志。                                       |
| mysql_eof()                      | 判断结果集的最后一行是否已经被读取。此功能已弃用。                               |
| mysql_errno()                    | 返回最近调用的 API 函数的错误码。                                     |
| mysql_error()                    | 返回最近调用的 API 函数的错误信息。                                    |
| mysql_escape_string()            | 转义字符串中的特殊字符，使其可以在 SQL 语句中使用。                            |
| mysql_fetch_field()              | 返回下一个表字段的类型。                                            |
| mysql_fetch_field_direct()       | 返回指定字段编号的字段类型。                                          |
| mysql_fetch_fields()             | 返回包含所有字段结构的数组。                                          |
| mysql_fetch_lengths()            | 返回当前行中所有列的长度。                                           |
| mysql_fetch_row()                | 获取结果集的下一行。                                              |
| mysql_field_count()              | 返回最近查询结果的列数。                                            |
| mysql_field_seek()               | 查找结果集行中的列。                                              |
| mysql_field_tell()               | 最后一次调用 `mysql_fetch_field()` 的字段位置。                     |
| mysql_free_result()              | 释放结果集内存。                                                |
| mysql_get_character_set_info()   | 返回关于默认字符集的信息。                                           |
| mysql_get_client_info()          | 返回 OceanBase 客户端版本信息（字符串）。                              |
| mysql_get_client_version()       | 返回 OceanBase 客户端版本信息（整数型）。                              |
| mysql_get_host_info()            | 返回包括服务器主机名的相关连接信息。                                      |
| mysql_get_proto_info()           | 返回连接所使用的协议版本。                                           |
| mysql_get_server_info()          | 返回服务器版本号（字符串）。                                          |
| mysql_get_server_version()       | 返回服务器版本号（整数型）。                                          |
| mysql_get_ssl_cipher()           | 返回当前的 SSL 密码。                                           |
| mysql_hex_string()               | 以十六进制格式编码字符串。                                           |
| mysql_info()                     | 返回最近执行语句的有关信息。                                          |
| mysql_init()                     | 获取或初始化一个连接结构。                                           |
| mysql_insert_id()                | 返回上一条语句为 `AUTO_INCREMENT` 列生成的 ID 值。                    |
| mysql_kill()                     | 杀死一个线程。此功能已弃用。                                          |
| mysql_library_end()              | 结束使用 C API 库。                                           |
| mysql_library_init()             | 初始化 C API 库。                                            |
| mysql_list_dbs()                 | 返回匹配正则表达式的数据库名称。                                        |
| mysql_list_fields()              | 返回匹配正则表达式的字段名称。                                         |
| mysql_list_processes()           | 返回当前服务器的线程列表。                                           |
| mysql_list_tables()              | 返回匹配正则表达式的表名。                                           |
| mysql_load_plugin()              | 加载插件。                                                   |
| mysql_load_plugin_v()            | 加载插件。                                                   |
| mysql_more_results()             | 检查是否存在更多的结果。                                            |
| mysql_next_result()              | 在多结果执行中返回或启动下一个结果。                                      |
| mysql_num_fields()               | 返回结果集中的列数。                                              |
| mysql_num_rows()                 | 返回结果集中的行数。                                              |
| mysql_options()                  | 在连接前设置选项。                                               |
| mysql_options4()                 | 在连接前设置选项。                                               |
| mysql_ping()                     | Ping 服务器。                                               |
| mysql_plugin_options()           | 设置插件选项。                                                 |
| mysql_query()                    | 执行 SQL 语句。                                              |
| mysql_real_connect()             | 连接到服务器。                                                 |
| mysql_real_escape_string()       | 对语句的字符串中的特殊字符进行编码。                                      |
| mysql_real_query()               | 执行语句。                                                   |
| mysql_refresh()                  | 刷新或重置表和缓存。                                              |
| mysql_reload()                   | 重新加载授权表。此功能已弃用。                                         |
| mysql_rollback()                 | 回滚事务。                                                   |
| mysql_row_seek()                 | 在查询结果集中查找任意行。                                           |
| mysql_row_tell()                 | 返回结果集行游标的当前位置。                                          |
| mysql_select_db()                | 选择数据库。                                                  |
| mysql_server_end()               | 结束使用 C API 库。                                           |
| mysql_server_init()              | 初始化 C API 库。                                            |
| mysql_set_character_set()        | 设置当前连接默认字符集。                                            |
| mysql_set_local_infile_default() | 将 `LOAD DATA LOCAL` 句柄回调到默认值。                           |
| mysql_set_local_infile_handler() | 安装指定应用程序的 `LOAD DATA LOCAL` 句柄回调。                       |
| mysql_set_server_option()        | 设置当前连接的选项。                                              |
| mysql_shutdown()                 | 关闭服务器。                                                  |
| mysql_sqlstate()                 | 返回最近调用函数的 `SQLSTATE` 值。                                 |
| mysql_ssl_set()                  | 准备与服务器建立 SSL 连接。                                        |
| mysql_stat()                     | 返回服务器状态。                                                |
| mysql_stmt_affected_rows()       | 返回使用上次准备的 `UPDATE`、`DELETE` 或 `INSERT` 语句进行更改、删除或插入的行数。 |
| mysql_stmt_attr_get()            | 获取 Prepared Statement 的属性值。                             |
| mysql_stmt_attr_set()            | 设置 Prepared Statement 属性值。                              |
| mysql_stmt_bind_param()          | 将应用程序数据缓冲器与 Prepared Statement 中的参数标记相关联。               |
| mysql_stmt_bind_result()         | 将应用程序数据缓冲器与结果集中的列相关联。                                   |
| mysql_stmt_close()               | 释放 Prepared Statement 所使用的内存。                           |
| mysql_stmt_data_seek()           | 在 Prepared Statement 的结果集中查找任意行号。                       |
| mysql_stmt_errno()               | 最近调用的 Prepared Statement API 函数的错误号。                    |
| mysql_stmt_error()               | 最近调用的 Prepared Statement API 函数的错误信息。                   |
| mysql_stmt_execute()             | 执行 Prepared Statement 。                                 |
| mysql_stmt_fetch()               | 获取结果集的下一行并返回所有绑定列的数据。                                   |
| mysql_stmt_fetch_column()        | 获取当前结果集行的一列。                                            |
| mysql_stmt_field_count()         | 最近 Prepared Statement 执行结果的列数。                          |
| mysql_stmt_free_result()         | 释放分配给语句句柄的资源。                                           |
| mysql_stmt_init()                | 为 `STMT` 结构分配和初始化内存。                                    |
| mysql_stmt_insert_id()           | 由先前的 Prepared Statement 所生成的 `AUTO_INCREMENT` 列的 ID。    |
| mysql_stmt_next_result()         | 在多结果 Prepared Statement 执行中返回或启动下一个结果。                  |
| mysql_stmt_num_rows()            | 缓冲语句结果集中的行数。                                            |
| mysql_stmt_param_count()         | 返回 Prepared Statement 中的参数数量。                           |
| mysql_stmt_param_metadata()      | 将参数元数据作为结果集返回。                                          |
| mysql_stmt_prepare()             | 准备执行语句。                                                 |
| mysql_stmt_reset()               | 在服务器端重置语句缓冲器。                                           |
| mysql_stmt_result_metadata()     | 将 Prepared Statement 的元数据作为结果集返回。                       |
| mysql_stmt_row_seek()            | 在 Prepared Statement 结果集中寻找任意行。                         |
| mysql_stmt_row_tell()            | 返回 Prepared Statement 结果集行游标的当前位置。                      |
| mysql_stmt_send_long_data()      | 将长数据分块发送到服务器。                                           |
| mysql_stmt_sqlstate()            | 返回最近调用的 Prepared Statement API 函数的 `SQLSTATE` 值。        |
| mysql_stmt_store_result()        | 检索并存储整个结果集。                                             |
| mysql_store_result()             | 检索并存储整个结果集。                                             |
| mysql_thread_end()               | 结束使用线程句柄。                                               |
| mysql_thread_id()                | 返回当前线程 ID。                                              |
| mysql_thread_init()              | 初始化线程句柄。                                                |
| mysql_thread_safe()              | 指示客户端库的编译是否为线程安全的。                                      |
| mysql_use_result()               | 开始逐行检索结果集。                                              |
| mysql_warning_count()            | 返回上一条语句的告警计数。                                           |

## 示例

使用基础接口连接数据库，并创建表和更改数据。

```c
mysql_library_init(0, NULL, NULL);
MYSQL *mysql = mysql_init(NULL);

/* 使用 CLIENT_MULTI_STATEMENTS 选项连接服务器 */
if (mysql_real_connect (mysql, host_name, user_name, password,
    db_name, port_num, socket_name, CLIENT_MULTI_STATEMENTS) == NULL)
{
  printf("mysql_real_connect() failed\n");
  mysql_close(mysql);
  mysql_library_end();
  exit(1);
}

/*执行多条语句 */
status = mysql_query(mysql,
                     "DROP TABLE IF EXISTS tbl1;\
                      CREATE TABLE tbl1(id INT);\
                      INSERT INTO tbl1 VALUES(110);\
                      UPDATE tbl1 SET id=120 WHERE id=110;\
                      SELECT * FROM tbl1;\
                      DROP TABLE tbl1");
if (status)
{
  printf("Could not execute statement(s)");
  mysql_close(mysql);
  mysql_library_end();
  exit(0);
}

/* 处理每个语句的结果 */
do {
  /* 当前语句是否返回数据? */
  result = mysql_store_result(mysql);
  if (result)
  {
    /* 是的; 则处理行并释放结果集 */
    process_result_set(mysql, result);
    mysql_free_result(result);
  }
  else          /* 没有结果集或报错 */
  {
    if (mysql_field_count(mysql) == 0)
    {
      printf("%lld rows affected\n",
            mysql_affected_rows(mysql));
    }
    else  /* 发生报错 */
    {
      printf("Could not retrieve result set\n");
      break;
    }
  }
  /* 判断是否有更多结果？ -1 表示否，大于 0 表示报错，等于 0 表示是（即继续循环）*/
  if ((status = mysql_next_result(mysql)) > 0)
    printf("Could not execute statement\n");
} while (status == 0);

mysql_close(mysql);
mysql_library_end();
```
