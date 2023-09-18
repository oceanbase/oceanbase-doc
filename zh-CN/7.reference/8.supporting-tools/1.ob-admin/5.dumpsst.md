# dumpsst

dumpsst 用来显示 block_file 文件中的内容，例如 super block，macro block，macro block meta，sstable， sstable meta 等。通常用于线上问题调查追溯，定位数据问题等。本文将介绍如何使用 dumpsst。

dumpsst 的命令格式如下：

```bash

Usage: dumpsst command [command args] [options]
commands:
        -d,--dump                     dump, args: [super_block|print_macro|macro_block|macro_meta|sstable|sstable_meta]
        -h,--help                     display this message.
options:
        -f,--data-file-name           data file path
        -a,--macro-id                 macro block index
        -i,--micro-id                 micro block id, -1 means all micro blocks
        -n,--macro-size               macro block size, in bytes
        -q,--quiet                    log level: ERROR
        -t,--table-key                table key: table_type,table_id:partition_id,index_id,base_version:multi_version_start:snapshot_version,start_log_ts:end_log_ts:max_log_ts,major_version
        -s,--skip_replay              skip slog replay, only work for macro_block mode
samples:
  dump all metas and rows in macro:
        ob_admin dumpsst -d pm -f block_file_path -a macro_id -i micro_id
  dump all rows in macro:
        ob_admin dumpsst -d macro_block -f block_file_path -a macro_id -i micro_id: dump rows in macro
```

下面介绍几个 dumpsst 的常见用法。

## super_block

您可使用 dumpsst 打印超级块内容，命令格式通常如下。

```bash
$./ob_admin dumpsst -f /home/admin/ob1.obs0/store -d super_block
$./ob_admin dumpsst -f /home/admin/ob1.obs0/store -d sb
```

其中，`-f` 指定数据文件所在文件夹的绝对路径，`-d` 指定 dump 内容，超级块也可以使用缩写 `sb`。

超级块内容通常如下：

![超级块输入内容](https://help-static-aliyun-doc.aliyuncs.com/assets/img/zh-CN/6606618361/p360259.png)

## macro_block

您可使用以下命令显示 SSTable 数据块内容，包括宏块 common header，sstable header，微块索引信息，微块头和每条数据行。这是一条最常用的命令，格式如下：

```bash
# 本地模式：
./ob_admin dumpsst -f /home/admin/ob1.obs0/store -d mb -a 13 -s
./ob_admin dumpsst -f /home/admin/ob1.obs0/store -d macro_block -a 13 -s
```

其中，`-f` 指定数据文件所在文件夹的绝对路径，`-a` 指定宏块的下标，`-d` 指定 dump 内容。

> **注意**
>
> 您在使用 dumpsst 查看宏块布局时，需要添加 `-s`，否则会显示有错误。

## macro_meta

您可使用以下命令打印宏块元数据，命令格式如下。

```bash
$./ob_admin dumpsst -f /home/admin/ob1.obs0/store -d macro_meta -a 15
$./ob_admin dumpsst -f /home/admin/ob1.obs0/store -d mm -a 15
```

其中，`-f` 指定数据文件所在文件夹的绝对路径，`-a` 指定宏块的下标，`-d` 指定 dump 内容，宏块元数据也可以使用缩写 `mm`。

## sstable

sstable 模式与 macro_block 模式类似，显示输出指定 sstable 相关的所有宏块信息。其输入参数为 -t tablekey。命令格式通常如下。

```bash
./ob_admin dumpsst -d sstable -f ./store/ -t 1,1100611139453777:0,1100611139453777,0:1637564201580068:1637564201580068,0:0:0,4
```

## sstable_meta

sstable_meta 模式与 macro_meta 模式类似，显示输出指定 sstable 相关的所有宏块元数据。其输入参数为 -t tablekey。命令格式通常如下。

```bash
./ob_admin dumpsst -d sstable_meta -f ./store/ -t 1,1100611139453777:0,1100611139453777,0:1637564201580068:1637564201580068,0:0:0,4
```

> **注意**
>
> dumpsst 对 cwd（当前工作目录）有要求，您只能在 OceanBase 的 `home` 目录中执行 ob_admin，即要求 cwd 是 OceanBase 的 `home` 目录。
