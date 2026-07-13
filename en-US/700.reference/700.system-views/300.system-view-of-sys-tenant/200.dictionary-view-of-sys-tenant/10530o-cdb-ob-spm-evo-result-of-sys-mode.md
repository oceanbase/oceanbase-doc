|description||
|---|---|
|keywords||
|dir-name||
|dir-name-en||
|tenant-type||
|machine-translation|en,ja-marker|
|slug|o-cdb-ob-spm-evo-result-of-sys-tenant|

# oceanbase.CDB_OB_SPM_EVO_RESULT

<main id="notice" type='explain'>
<h4>Note</h4>
<p>This view is available starting with V4.2.5. </p>
</main>

## Purpose

Displays the SPM plan evolution information for all tenants.

## Columns

| **Column** | **Type** | **Nullable** | **Description** |
| --- | --- | --- | --- |
| TENANT_ID | bigint(20) | NO | Tenant ID. |
| OWNER | varchar(128) | NO | The user who executes the evolution task. |
| RECORD_TIME | timestamp(6) | NO | The time when the evolution result was recorded. |
| SVR_IP | varchar(46) | NO | The IP address of the server that executes the evolution task. |
| SVR_PORT | bigint(20) | NO | The server port for executing the evolution task. |
| SQL_ID | varchar(32) | NO | SQL ID for executing the evolution task. |
| TYPE | varchar(32) | NO | Record type:<ul><li>`OnlineEvolve`: Indicates that the Online Evolution mode records the results of evolution tasks. The following fields are valid only when their type is the current value.</li><li>`FirstBaseline`: Indicates that the SQL statement generated the first baseline. </li><li>`UnReproducible`: Indicates that none of the current SQL's baselines can be reproduced. </li><li>`BaselineFirst`: Indicates that a new plan was generated in baseline-first mode, but the baseline plan was restored and used.</li><li>`BestBaseline`: Indicates that the optimal baseline plan was generated and used.</li><li>`FixedBaseline`: Indicates that a fixed baseline plan is used. </li></ul> |
| START_TIME | timestamp(6) | YES | The start time of the evolution task. |
| END_TIME | timestamp(6) | YES | The end time of the evolution task. |
| STATUS | varchar(7) | YES | Evolution task status:<ul><li>`success`: The evolution task has ended normally. </li><li>`timeout`: The evolution task timed out. In this case, the plan that executed better during the evolution period is chosen. |
| NEW_PLAN_BETTER | tinyint(4) | YES | Whether the evolution plan is better. |
| EVO_PLAN_EXEC_COUNT | bigint(20) | YES | Number of times the evolution plan is executed during the evolution period. |
| EVO_PLAN_CPU_TIME | bigint(20) | YES | The average CPU overhead of the evolution plan during evolution. |
| BASELINE_EXEC_COUNT | bigint(20) | YES | Number of times the baseline plan is executed during the evolution period. |
| BASELINE_CPU_TIME | bigint(20) | YES | The average CPU cost of the baseline plan during the evolution period. |

## Sample query

Query the SPM plan evolution information for all tenants under the sys tenant.

```shell
obclient [oceanbase]> SELECT * FROM oceanbase.CDB_OB_SPM_EVO_RESULT;
```
