# TEXT 类型

`TEXT` 类型用于存储所有类型的文本数据。

文本类型包括四种，分别是 `TINYTEXT`、`TEXT`、`MEDIUMTEXT` 和 `LONGTEXT`。它们对应于四种 `BLOB` 类型，并且具有相同的最大长度和存储要求。

`TEXT` 值被视为非二进制字符串。它们具有二进制以外的字符集，并且根据字符集的排序规则对值进行排序和比较。

在未启用严格的 SQL 模式时，如果为 `TEXT` 列分配的值超过该列的最大长度，则该值超出长度的部分将被截断并生成告警。在使用严格的 SQL 模式时，如果截断的是非空格字符，会发生错误（而不是告警）并禁止插入值。无论 SQL 模式如何，截断插入到 `TEXT` 列的值中多余的尾部空格时，总是会生成告警。

## TINYTEXT

`TINYTEXT` 是最大长度为 256 个字符的 `TEXT` 类型。如果值中包含多字节字符，则最大有效长度会变小。

每个 `TINYTEXT` 值都使用 1 字节长度的前缀进行存储，该前缀指示值中的字节数。语法如下：

```sql
TINYTEXT [CHARACTER SET charset_name] [COLLATE collation_name]
```

`CHARACTER SET` 用于指定字符集。如果需要，可以使用 `COLLATE` 属性以及其他属性指定字符集的排序规则。如果指定 `CHARACTER SET` 的二进制属性，则会导致将列创建为相应的二进制字符串数据类型，`TEXT` 会变为 `BLOB`。

## TEXT

`TEXT` 列的最大长度为 65,536 个字符。如果值包含多字节字符，则最大有效长度会变小。

每个 `TEXT` 值都使用 2 字节长度的前缀存储，该前缀指示值中的字节数。可以为 `TEXT` 类型指定一个可选的长度 `M`。语法如下：

```sql
TEXT[(M)] [CHARACTER SET charset_name] [COLLATE collation_name]
```

`CHARACTER SET` 用于指定字符集。如果需要，可以使用 `COLLATE` 属性以及其他属性指定字符集的排序规则。 如果指定 `CHARACTER SET` 的二进制属性，则会导致将列创建为相应的二进制字符串数据类型，`TEXT` 会变为 `BLOB`。

## MEDIUMTEXT

`MEDIUMTEXT` 是最大长度为 16,777,216 个字符的 `TEXT` 类型。如果值包含多字节字符，则最大有效长度会变小。

每个 `MEDIUMTEXT` 值都使用 3 字节长度的前缀进行存储，该前缀指示值中的字节数。

语法如下：

```sql
MEDIUMTEXT [CHARACTER SET charset_name] [COLLATE collation_name]
```

`CHARACTER SET` 用于指定字符集。如果需要，可以使用 `COLLATE` 属性以及任何其他属性指定字符集的排序规则。如果指定 `CHARACTER SET` 的二进制属性会导致将列创建为相应的二进制字符串数据类型，`TEXT` 会变为 `BLOB`。

## LONGTEXT

`LONGTEXT` 是最大长度为 50331648 或 48 M 个字符的 `TEXT` 类型。如果值包含多字节字符，则最大有效长度会变小。`LONGTEXT` 列的有效最大长度还取决于客户端/服务器协议中配置的最大数据包大小和可用内存。

每个 `LONGTEXT` 值都使用 4 字节长度的前缀进行存储，该前缀指示值中的字节数。语法如下：

```sql
LONGTEXT [CHARACTER SET charset_name] [COLLATE collation_name]
```

`CHARACTER SET` 用于指定字符集。如果需要，可以使用 `COLLATE` 属性以及其他属性指定字符集的排序规则。如果指定 `CHARACTER SET` 的二进制属性，则会导致将列创建为相应的二进制字符串数据类型，`TEXT` 会变为 `BLOB`。
