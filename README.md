
# OceanBase 数据库文档

欢迎访问 OceanBase 数据库文档。您可以在本仓库中查看 OceanBase 数据库的中英文文档。

* `zh-CN` 文件夹下存放的是 OceanBase 数据库的中文文档

* `en-US` 文件夹下存放的是 OceanBase 数据库的英文文档

OceanBase 欢迎大家随时参与到文档的共同建设中，OceanBase 文档的贡献者可以：

* 提交文档问题或者建议

* 优化已有的内容

* 编写新的内容


## 贡献文档

### 开始之前

感谢您对 OceanBase 数据库文档的贡献兴趣。为厘清就个人或实体贡献内容而授予的知识产权许可，我们必须对每位贡献者签署的贡献者许可协议（Contributor Licence Agreement，简称 CLA）（“CLA”）进行归档，以证明就 CLA 达成的一致。点击 [OceanBase CLA](https://cla-assistant.io/oceanbase/oceanbase?pullRequest=108)，点击 **Sign in with GitHub to agree** 按钮签署协议。

### 贡献指南

您可以按照以下步骤提交 Pull Request（简称 PR）：

**步骤 1：Fork 项目仓库**

1. 访问 OceanBase 数据库文档的 [GitHub 地址](https://github.com/oceanbase/oceanbase-doc)。

2. 点击 Fork 按钮创建远程分支。

**步骤 2：克隆分支到本地**

1. 定义工作目录。

   ```bash
   # 定义工作目录
   working_dir=$HOME/Workspace
   ```

2. 配置 GitHub 用户名。

   ```bash
   user={GitHub账户名}
   ```

3. 克隆代码。

   ```bash
   # 克隆代码
   mkdir -p $working_dir
   cd $working_dir
   git clone git@github.com:$user/oceanbase-doc.git
   # 或: git clone https://github.com/$user/oceanbase-doc.git
   
   # 添加上游分支
   cd $working_dir/oceanbase-doc
   git remote add upstream git@github.com:oceanbase/oceanbase-doc.git
   # 或: git remote add upstream https://github.com/oceanbase/oceanbase-doc.git
   
   # 为上游分支设置 no_push
   git remote set-url --push upstream no_push
   
   # 确认远程分支有效
   git remote -v
   ```

**步骤 3：创建新分支**

1. 更新本地分支。

   ```bash
   cd $working_dir/oceanbase-doc
   git fetch upstream
   git checkout $branch
   git rebase upstream/$branch
   ```

2. 基于本地 $branch 分支创建新分支。

   ```bash
   git checkout -b new-branch-name
   ```

**步骤 4：修改/添加/删除文档**

在 `new-branch-name` 上修改文档并保存更改。

**步骤 5：提交更改**

```bash
# 检查本地文件状态
git status

# 添加您希望提交的文件
# 如果您希望提交所有更改，直接使用 `git add .`
git add <file> ... 
git commit -m "commit-message: update the xx"
```

**步骤 6：保持开发分支与上游分支同步**

```bash
# 在开发分支执行以下操作
git fetch upstream
git rebase upstream/branch
```

**步骤 7：推送更改至远程分支**

```bash
# 在开发分支执行以下操作
git push -u origin new-branch-name
```

**步骤 8：创建 PR**

1. 访问您 Fork 的仓库。

2. 单击 `new-branch-name` 分支旁的 `Compare & pull request` 按钮。

以上就是参与 OceanBase 数据库文档共建的步骤，如果在此过程中遇到任何问题，可以加入我们唯一官网钉钉群：41203246，与社区热心的技术大神、热情的贡献者、经验丰富的技术专家一起交流、探讨问题。