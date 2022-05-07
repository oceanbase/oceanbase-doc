# OBServer 安装目录结构

OBServer 工作目录下通常有 audit、bin、etc、etc2、etc3、log、run、store 这 8 个目录，但这 8 个目录并非都是安装必须的。在启动 OBServer 前我们需要保证 etc、log、run、store 这 4 的目录存在，同时 store 下应该有clog、ilog、slog、sstable 这 4 个目录。etc2、etc3 是备份配置文件用的，由 OBServer 创建。audit 下存放的是审计日志，也由 OBServer 创建。bin 目录用于存放 observer binary 文件，方便后续定位。

![安装目录结构](https://obbusiness-private.oss-cn-shanghai.aliyuncs.com/doc/img/observer/V3.1.3/zh-CN/oceanbase-database-overview/observer-architecture/1.structure-of-observer-installation-directory-OBServer%E5%AE%89%E8%A3%85%E7%9B%AE%E5%BD%95%E7%BB%93%E6%9E%84.png)

## 配置文件目录

etc、etc2、etc3 都是配置文件目录。这三个目录里的内容是完全一致的，区别是后两个目录是 OBServer 创建的，第一个目录是启动前需要准备的。etc2 和 etc3 是配置文件额外保存的目录，由配置项 config_additional_dir 控制。当配置修改以后，除了会写标准的 etc/observer.config.bin 以外，还会额外在这些目录创建配置项文件。server 启动不会读取额外目录的配置项文件，只是作为额外备份。额外目录如果有权限会自动创建，没有权限则日志中报 ERROR。

配置文件中储存了集群和租户级配置项的增量信息。集群配置可以通过连接到数据库上执行 alter system 修改，也可以通过命令行传入配置项。命令行传入配置项会覆盖原有配置。命令行可以通过以下参数修改 OBServer 配置项：

```javascript
-z,--zone ZONE           zone name 节点所在的zone的名字
-p,--mysql_port PORT     mysql port SQL服务协议端口号
-P,--rpc_port PORT       rpc port 集群内部通信的端口号
-n,--appname APPNAME     application name 本OceanBase集群名
-c,--cluster_id ID       cluster id 本OceanBase集群ID
-d,--data_dir DIR        OceanBase data directory 存储sstable等数据的目录
-i,--devname DEV         net dev interface 服务进程绑定的网卡设备名
-r,--rs_list RS_LIST     root service list root service列表
-l,--log_level LOG_LEVEL server log level 系统日志级别
-o,--optstr OPTSTR       extra options string 额外配置项格式为 配置名=新值,配置名=新值
```

## 日志文件目录

log 目录是存放运行日志的目录，里面包含了 observer 日志、RS 日志和选举日志。单个日志文件大小为 256M。

当 `enable_syslog_recycle` 设置为 true、`max_syslog_file_count` 大于 0 时日志文件会自动回收。其中，`enable_syslog_recycle` 用于设置是否开启自动回收，`max_syslog_file_count` 用于设置每种日志的最大日志数量。

## 数据文件目录

store 是数据文件目录，包含了 clog、ilog、slog、sstable 这 4 个子目录。其中 clog、ilog、slog 是事务日志目录，slog 存储静态数据写入的事务日志，clog 存储动态数据写入的事务日志，ilog 存储日志目录。sstable 是基线数据目录。sstable 目录下会有一个 block_file，这个文件在 observer 启动后就会被创建，文件的大小由 `datafile_size` 或 `datafile_disk_percentage` 控制。
>**说明**
>
>* `datafile_size` 用于设置数据文件的大小。
>* `datafile_disk_percentage` 表示占用 `data_dir` 所在磁盘（ `data_dir` 所在磁盘将被 OceanBase 数据库系统初始化用于存储数据）总空间的百分比。

有关两个配置项的详细介绍，参见《OceanBase 数据库参考指南》中的 **系统配置项** 章节。
