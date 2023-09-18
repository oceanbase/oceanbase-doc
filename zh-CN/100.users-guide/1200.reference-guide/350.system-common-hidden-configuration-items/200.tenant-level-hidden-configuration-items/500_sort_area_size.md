# _sort_area_size

`_sort_area_size` 用于设置 SORT 可以使用的最大内存大小。

<main id="notice" type='explain'>
  <h4>说明</h4>
  <p>该配置项仅在 <code>workarea_size_policy = MANUAL</code> 时生效，配置项 <code>workarea_size_policy</code> 用于设置手动或者自动调整 SQL 工作区大小的策略，更多详细信息，参考 <a href="../../300.system-configuration-items/21400.workarea_size_policy.md">workarea_size_policy</a>。</p>
</main>

| **属性** | **描述** |
| --- | --- |
| 参数类型 | 容量单位 |
| 默认值 | 128M |
| 取值范围 | [2M,  +∞) |
| 是否重启 OBServer 节点生效 | 否 |
