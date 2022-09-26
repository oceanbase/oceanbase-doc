# Primary Zone

OceanBase 数据库支持通过设置 Primary Zone 来设置 Leader 副本的偏好。

## 基本概念

Primary Zone 表示 Leader 副本的偏好位置。指定 Primary Zone 实际上是指定了 Leader 更趋向于被调度到哪个 Zone 上，即假设某张表 `t1` 的 `primary_zone="zone1"`，则 RS 会尽量将 `t1` 表的 Leader 调度到 `zone1` 上来。

## 引申概念

Primary Zone 实际上是一个 Zone 的列表，列表中包含多个 Zone。该列表用使用如下方式为 Zone 配置了优先级。

当 Primary Zone 列表包含多个 Zone 时，用 `;` 分隔的具有从高到底的优先级；`,` 分隔的具有相同优先级。例如：`'hz1,hz2;sh1,sh2;sz1'` 表示 `hz1` 和 `hz2` 具有相同的优先级，并且优先级高于 `sh1`/`sh2` 和 `sz1`；`sh1` 和 `sh2` 具有相同优先级，并且优先级高于 `sz1`。

## Region 信息

在 OceanBase 数据库中，Zone 有一个 Region 属性，表示该 Zone 所处的地区，每个 Zone 仅能配置一个 Region，但一个 Region 内可包含多个 Zone。Primary Zone 的设置隐含的包含了 Leader 偏好的 Region 位置。具体指用户设置 primary_zone 包含两层语义：

* 被指定的 Primary Zone 为 Leader 的偏好 Zone 的位置。

* 被指定 Primary Zone 所在的 Region 为 Leader 偏好的 Region。

具体地，Leader 会被优先调度到最高优先级的 Zone 上去，如果最高优先级的 Zone 上的副本不能成为 Leader，会优先选择同一个 Region 内的其他 Zone 作为 Leader 的位置。

## Primary Zone 改写

用户设置的 Primary Zone 会由 OceanBase 数据库内部，基于各个 Zone 所在的 Region 进行改写，改写规则如下：

* 将用户设置的 Primary Zone 中的所有 Zone 对应的 Region 列出。例如：primary_zone 为 `'hz1,hz2;sh1,sh2;sz1'` 对应的 primary_region 的列表为 `'hz,hz;sh,sh;sz'`。

* 将 primary_region 中重复的 Region 去掉，去掉规则为保留第一个出现的 Region，其他 Region 后续重复的 Region 移除，则上述 primary_region 转化为 primary_region 列表 `'hz;sh;sz'`。

* 依据 primary_region 中各 Region 的优先级，对 primary_zone 进行补充，补充规则如下：将 Primary Zone 中各 Region 对应的 Zone 都取出，重新排列，高优先级 Region 内 Zone 比低优先级 Region 内 Zone 的优先级高，同一 Region 内 Zone 的优先级高低参考原始 Primary Zone 中的优先级。

## 继承关系

当前有 Table 级、Table Group 级、Database 级以及 Tenant 级 primary_zone。

除 Tenant 级别外，每个级别均可以自由指定 primary_zone 的分布情况，如果不指定那么默认向上继承，Tenant 维度必须指定 primary_zone（此处的必须指定含义是租户级的 primary_zone 不能为空，如果创建时未指定 primary_zone，默认填写为 RANDOM，表示各个 Zone 优先级相同）。

* Table 级

  * 首先看自身的 primary_zone，若不为空，则使用自身的 primary_zone。

  * 若为空，判断是否属于 Table Group。若属于则查看 Table Group 的 primary_zone 是否为空，若不为空，则使用 Table Group 的 primary_zone。

  * 若 Table Group 为空或不属于 Table Group，那么查看 Database 的 primary_zone 是否为空，若不为空，则使用 Database 的primary_zone。

  * 若均为空，那么使用 Tenant 级的 primary_zone。

* Table Group 级

  * 检查自身 primary_zone，若不为空，则使用自身的 primary_zone。

  * 若为空，则使用 Tenant 的 primary_zone。

* Database 级

  * 检查自身 primary_zone，若不为空，则使用自身的 primary_zone。

  * 若为空，则使用 Tenant 的 primary_zone。

## 示例

假设共有 9 个 Zone，`sh1`、`sh2`、`sh3` 三个 Zone 在 Region `SH`，`hz1`、`hz2`、`hz3` 三个 Zone 在 Region `HZ`，`sz1`、`sz2`、`sz3` 三个 Zone 在 Region `SZ`。

### 示例 1

用户设置的 primary_zone 为 `'sh1;hz1;hz2;sz1';` 按照改写规则 1 得到 primary_region 为 `'SH;HZ;HZ;SZ'`。按照改写规则 2 得到 primary_zone 为 `'SH;HZ;SZ'`。按规则 3 得到改写后 primary_zone 为 `'sh1;sh2,sh3;hz1;hz2;hz3;sz1;sz2,sz3'`。

解释如下：

三个 Region 的优先级为 `SH` \> `HZ` \> `SZ`。Region `SH` 中的 Zone 的优先级高于 Region `HZ` 和 Region `SZ` 中 Zone 的优先级。Region `HZ` 中的 Zone 的优先级高于 Region `SZ` 中 Zone 的优先级。各 Region 内每个 Zone 的优先级为：在 Region `SH` 中 `sh1` \> `sh2` = `sh3`，在 Region `HZ` 中 `hz1` \> `hz2` \> `hz3`，在 Region `SZ` 中 `sz1` \> `sz2` = `sz3`。因此最终得到新的 Primary Zone 为 `'sh1;sh2,sh3;hz1;hz2;hz3;sz1;sz2,sz3'`。Leader 会优先分布在 `sh1` 上，当 `sh1` 发生故障时，Leader 会依照上面的 Primary Zone 优先级依次分布在 `sh2` 和 `sh3`。

### 示例 2

用户设置的 primary_zone 为 `'sh1,sh2;hz1;hz2;sz1';` 按照改写规则 1 得到 primary_region 为 `'SH,SH;HZ;HZ;SZ'`。按照改写规则 2 得到 primary_zone 为 `'SH;HZ;SZ'`。按规则 3 得到改写后 primary_zone 为 `'sh1,sh2;sh3;hz1;hz2;hz3;sz1;sz2,sz3'`。

解释如下：

三个 Region 的优先级为 `SH` \> `HZ` \> `SZ`。Region `SH` 中的 Zone 的优先级高于 Region `HZ` 和 Region `SZ` 中 Zone 的优先级。Region `HZ` 中的 Zone 的优先级高于 Region `SZ` 中 Zone 的优先级。各 Region 内每个 Zone的优先级为：在 Region `SH` 中 `sh1` = `sh2` \> `sh3`，在 Region `HZ` 中 `hz1` \> `hz2` \> `hz3`，在 Region `SZ` 中 `sz1` \> `sz2` = `sz3`。因此最终得到新的 Primary Zone 为 `'sh1,sh2;sh3;hz1;hz2;hz3;sz1;sz2,sz3'`。Leader 会优先平均分布在 `sh1` 和 `sh2` 上，当 `sh1` 和 `sh2` 发生故障时，Leader 会依照上面 Primary Zone 优先级依次分布在 `sh3`。

### 示例 3

用户设置的 primary_zone 为 `'sh1,hz1;hz2;sz1';` 按照改写规则 1 得到 primary_region 为 `'SH,HZ;HZ;SZ'`。按照改写规则 2 得到 primary_zone 为 `'SH,HZ;SZ'`。按规则 3 得到改写后 primary_zone 为 `'sh1,hz1;hz2;sh2,sh3,hz3;sz1;sz2,sz3'`。

解释如下：

三个 Region 的优先级为 `SH` = `HZ` \> `SZ`。Region `SH` 和 Region `HZ` 中的 Zone 的优先级高于 Region SZ 中 Zone 的优先级。`sh1` = `hz1` \> `hz2` \> `sh2` = `sh3` = `hz3` \> `sz1` \> `sz2` = `sz3`。因此最终得到新的 Primary Zone 为 `'sh1,hz1;hz2;sh2,sh3,hz3;sz1;sz2,sz3'`。Leader 会优先平均分布在 `sh1` 和 `hz1` 上，当 `sh1`和 `hz1` 发生故障时，Leader 会依照上面 Primary Zone 优先级依次分布在 `hz2`。
