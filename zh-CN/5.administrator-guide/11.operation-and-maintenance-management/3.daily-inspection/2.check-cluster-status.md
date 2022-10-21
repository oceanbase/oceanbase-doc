# 检查集群状态

您可以通过 SQL 命令的方式来检查集群状态。

## 检查集群状态

### 通过视图查看

查看所有返回记录中 merge_status 的状态。

```sql
obclient> SELECT info FROM __all_zone where name='merge_status';
```

* 返回结果为 'IDLE' : 集群合并状态健康。

* 返回结果非 'IDLE' : 集群合并状态不正常，需对集群进行处理。
