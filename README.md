# 作业二（hw02）说明

## • 任务一：论文导读生成与配图
- **论文来源**：选自知网上的公开期刊论文《当机器成为“智能体”——人智协作新范式的提出与展望》（南开管理评论，2025-12-08）
- **导读生成方式**：使用千问-Qwen3-Max模型对论文摘要和引言部分进行理解，并生成一段约1000字的中文导读。
- **配图方式**：使用wps提取图表插入进文档中。

## • 任务二：AI 对话系统实现
- **采用的 API/平台**：阿里云千问平台的qwen-plus文本生成模型。
- **运行方式**：
  1. 安装依赖：`pip install requests`
  2. 设置环境变量：  
     ```bash
     export DASHSCOPE_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # 脱敏示例
     ```
  3. 执行脚本：`python chatbot.py`
- **注意事项**：
  - 未配置 API Key 时程序自动进入演示模式，仅输出模拟回复；
  - 首次使用需在 [DashScope 控制台](https://dashscope.console.aliyun.com/) 开通`qwen-plus`模型权限；
  - 代码中不包含真实密钥，符合脱敏要求。
