# Qwen Chatbot 作业

本项目调用阿里云 **DashScope** 的 `qwen-plus` 模型实现简单对话。

## 🛠️ 配置说明（脱敏版）

### 1. 获取 API Key
- 登录 [DashScope 控制台](https://dashscope.console.aliyun.com/)
- 进入「API Key 管理」页面
- 创建或复制你的 API Key（格式如：`sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`）

### 2. 设置环境变量

#### Linux / macOS
```bash
export DASHSCOPE_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
python main.py