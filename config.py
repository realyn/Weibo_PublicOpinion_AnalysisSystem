# -*- coding: utf-8 -*-
"""
微舆配置文件
"""

# ============================== 数据库配置 ==============================
# 配置这些值以连接到您的MySQL实例。
DB_HOST = "your_db_host"  # 例如："localhost" 或 "127.0.0.1"
DB_PORT = 3306
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_NAME = "your_db_name"
DB_CHARSET = "utf8mb4"
# 我们也提供云数据库资源便捷配置，日均10w+数据，可免费申请，联系我们：670939375@qq.com
# NOTE：为进行数据合规性审查与服务升级，云数据库自2025年10月1日起暂停接收新的使用申请


# ============================== LLM配置 ==============================
# 您可以更改每个部分LLM使用的API，🚩只要兼容OpenAI请求格式都可以，定义好KEY、BASE_URL与MODEL_NAME即可正常使用。
# 重要提醒：我们强烈推荐您先使用推荐的配置申请API，先跑通再进行您的更改！

# Insight Agent（推荐Kimi，申请地址：https://platform.moonshot.cn/）
INSIGHT_ENGINE_API_KEY = "your_api_key"
INSIGHT_ENGINE_BASE_URL = "https://api.moonshot.cn/v1"
INSIGHT_ENGINE_MODEL_NAME = "kimi-k2-0711-preview"

# Media Agent（推荐Gemini，这里我用了一个中转厂商，你也可以换成你自己的，申请地址：https://www.chataiapi.com/）
MEDIA_ENGINE_API_KEY = "your_api_key"
MEDIA_ENGINE_BASE_URL = "https://www.chataiapi.com/v1"
MEDIA_ENGINE_MODEL_NAME = "gemini-2.5-pro"

# Query Agent（推荐DeepSeek，申请地址：https://www.deepseek.com/）
QUERY_ENGINE_API_KEY = "your_api_key"
QUERY_ENGINE_BASE_URL = "https://api.deepseek.com"
QUERY_ENGINE_MODEL_NAME = "deepseek-reasoner"

# Report Agent（推荐Gemini，这里我用了一个中转厂商，你也可以换成你自己的，申请地址：https://www.chataiapi.com/）
REPORT_ENGINE_API_KEY = "your_api_key"
REPORT_ENGINE_BASE_URL = "https://www.chataiapi.com/v1"
REPORT_ENGINE_MODEL_NAME = "gemini-2.5-pro"

# Forum Host（Qwen3最新模型，这里我使用了硅基流动这个平台，申请地址：https://cloud.siliconflow.cn/）
FORUM_HOST_API_KEY = "your_api_key"
FORUM_HOST_BASE_URL = "https://api.siliconflow.cn/v1"
FORUM_HOST_MODEL_NAME = "Qwen/Qwen3-235B-A22B-Instruct-2507"

# SQL keyword Optimizer（小参数Qwen3模型，这里我使用了硅基流动这个平台，申请地址：https://cloud.siliconflow.cn/）
KEYWORD_OPTIMIZER_API_KEY = "your_api_key"
KEYWORD_OPTIMIZER_BASE_URL = "https://api.siliconflow.cn/v1"
KEYWORD_OPTIMIZER_MODEL_NAME = "Qwen/Qwen3-30B-A3B-Instruct-2507"


# ============================== 网络工具配置 ==============================
# Tavily API（申请地址：https://www.tavily.com/）
TAVILY_API_KEY = "your_api_key"

# Bocha API（申请地址：https://open.bochaai.com/）
BOCHA_WEB_SEARCH_API_KEY = "your_api_key"