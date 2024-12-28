# 学习进度跟踪器

[English README available here](README.md)

## 该项目是以下三个项目的整合版本
- **[entodo](https://github.com/yzwbeast/entodo)**：[基于每周计划跟踪学习进度，包含阅读、写作、听力、口语和词汇任务。记录进度，查看成就，并可视化完成情况。](https://github.com/yzwbeast/entodo/blob/main/README.md)
   - 关键改动点
     1. 嵌套字典：将任务标签设计为嵌套字典，使多级选择成为可能。
     2. 递归菜单：select_tag() 函数支持递归选择子标签。
     3. 动态新增标签：用户可以在任何层级新增自定义标签。
   - 示例运行
     1. 用户选择 `3. Tech`。
     2. 接着选择 `1. Web`。
     3. 最终返回 `Web` 作为标签。
- **[pomodoro](https://github.com/yzwbeast/pomodoro)**：[帮助你使用番茄工作法管理任务，支持设置计时器、添加标签，并查看统计数据和图表。支持英语和简体中文，并提供数据备份功能。](https://github.com/yzwbeast/pomodoro/blob/main/README.md)
- **[read-log](https://github.com/yzwbeast/read-log)**：[简单高效的读书记录程序，用于记录和管理您的阅读记录。](https://github.com/yzwbeast/read-log/blob/main/README.md)

## 安装步骤
1. 克隆仓库，进入项目目录：
   ```bash
   git clone https://github.com/yzwbeast/focus-flow.git
   cd focus-flow
   ```

1. 创建虚拟环境

   <details>
   <summary>为什么推荐使用虚拟环境</summary>

   >当你遇到 “**externally-managed-environment**” 错误时，可能是操作系统 使用 APT 安装的 Python 版本对系统环境进行了严格管理，防止用户通过 pip 修改系统级的 Python 包。<br />
   >要解决这个问题，**推荐方法**：<br />使用虚拟环境是最干净、安全的方法。它不会影响系统的 Python 环境，同时方便你自由管理依赖。
   </details>

   在项目目录下运行：
   ```bash
   python3 -m venv flow
   ```
   - `flow` 是虚拟环境的名称，可以替换为任意名字。
2. 激活虚拟环境：
   ```bash
   source flow/bin/activate
   ```
3. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```
4. 运行脚本：
   ```bash
   python x.py
   ```
5. 退出虚拟环境：使用完后，可退出环境：
   ```bash
   deactivate 
   ```
6. 删除虚拟环境
直接删除 my_env 文件夹即可：
   ```bash
   rm -rf flow
   ```

## 许可证
本项目基于 MIT 许可证，详情请参阅 [LICENSE](LICENSE) 文件。

[English README available here](README.md)
