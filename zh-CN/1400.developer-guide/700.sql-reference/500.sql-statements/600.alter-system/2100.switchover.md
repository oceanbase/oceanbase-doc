# SWITCHOVER

## 描述

计划内的集群角色切换语法，可以将主集群无损切换为备集群，备集群切换成主集群。

最大保护模式和最大可用模式下，执行 Switchover 前，要求将主集群配置为 `SYNC` 模式，保证 Switchover 之后，仍然存在一个 `SYNC` 模式的备集群。

在切换集群角色前，可以通过 `V$OB_CLUSTER` 视图的 `SWITCHOVER_STATUS` 列，查看是否可以切换。如果为 `NOT ALLOWED` 或其他值，说明当前不满足切换条件。

```sql
obclient> SELECT SWITCHOVER_STATUS, SWITCHOVER_INFO FROM V$OB_CLUSTER;
+-------------------+------------------------------+
| SWITCHOVER_STATUS | SWITCHOVER_INFO              |
+-------------------+------------------------------+
| TO STANDBY        | SYNCED STANDBY CLUSTERS: 2,3 |
+-------------------+------------------------------+
```

## 语法

```sql
ALTER SYSTEM commit_switchover_clause;

commit_switchover_clause：
    COMMIT TO SWITCHOVER TO PRIMARY
    | COMMIT TO SWITCHOVER TO PHYSICAL STANDBY
```

## 参数解释

|                  **参数**                  |       **描述**       |
|------------------------------------------|--------------------|
| COMMIT TO SWITCHOVER TO PRIMARY          | 备集群切换为主集群，在备集群上执行。 |
| COMMIT TO SWITCHOVER TO PHYSICAL STANDBY | 主集群切换为备集群，在主集群上执行。 |

## 示例

* 主集群切换成备集群。

  ```sql
  obclient> ALTER SYSTEM COMMIT TO SWITCHOVER TO PHYSICAL STANDBY；
  ```

* 备集群切换成主集群。

  ```sql
  obclient> ALTER SYSTEM COMMIT TO SWITCHOVER TO PRIMARY；
  ```
