<div align="center">

<img src="static/image/logo_compressed.png" alt="Weibo Public Opinion Analysis System Logo" width="100%">

<a href="https://trendshift.io/repositories/12461" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12461" alt="666ghj%2FWeibo_PublicOpinion_AnalysisSystem | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<a href="https://leaflow.net/" target="_blank"><img src="static/image/Leaflow_logo.png" alt="666ghj%2FWeibo_PublicOpinion_AnalysisSystem | Leaflow" style="width: 150px;" width="150"/></a>

[![GitHub Stars](https://img.shields.io/github/stars/666ghj/Weibo_PublicOpinion_AnalysisSystem?style=flat-square)](https://github.com/666ghj/Weibo_PublicOpinion_AnalysisSystem/stargazers)
[![GitHub Watchers](https://img.shields.io/github/watchers/666ghj/Weibo_PublicOpinion_AnalysisSystem?style=flat-square)](https://github.com/666ghj/Weibo_PublicOpinion_AnalysisSystem/watchers)
[![GitHub Forks](https://img.shields.io/github/forks/666ghj/Weibo_PublicOpinion_AnalysisSystem?style=flat-square)](https://github.com/666ghj/Weibo_PublicOpinion_AnalysisSystem/network)
[![GitHub Issues](https://img.shields.io/github/issues/666ghj/Weibo_PublicOpinion_AnalysisSystem?style=flat-square)](https://github.com/666ghj/Weibo_PublicOpinion_AnalysisSystem/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/666ghj/Weibo_PublicOpinion_AnalysisSystem?style=flat-square)](https://github.com/666ghj/Weibo_PublicOpinion_AnalysisSystem/pulls)

[![GitHub License](https://img.shields.io/github/license/666ghj/Weibo_PublicOpinion_AnalysisSystem?style=flat-square)](https://github.com/666ghj/Weibo_PublicOpinion_AnalysisSystem/blob/main/LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.0-green.svg?style=flat-square)](https://github.com/666ghj/Weibo_PublicOpinion_AnalysisSystem)
[![Docker](https://img.shields.io/badge/Docker-Build-2496ED?style=flat-square&logo=docker&logoColor=white)](https://hub.docker.com/)


[English](./README-EN.md) | [中文文档](./README.md)

</div>

## ⚡ Project Overview

**"BettaFish"** is an innovative multi-agent public opinion analysis system built from scratch. It helps break information cocoons, restore the original public sentiment, predict future trends, and assist decision-making. Users only need to raise analysis needs like chatting; the agents automatically analyze 30+ mainstream social platforms at home and abroad and millions of public comments.

> Betta is a small yet combative and beautiful fish, symbolizing "small but powerful, fearless of challenges".

See the system-generated research report on "Wuhan University Public Opinion": [In-depth Analysis Report on Wuhan University's Brand Reputation](./final_reports/final_report__20250827_131630.html)

Beyond just report quality, compared to similar products, we have 🚀 six major advantages:

1. **AI-Driven Comprehensive Monitoring**: AI crawler clusters operate 24/7 non-stop, comprehensively covering 10+ key domestic and international social media platforms including Weibo, Xiaohongshu, TikTok, Kuaishou, etc. Not only capturing trending content in real-time, but also drilling down to massive user comments, letting you hear the most authentic and widespread public voice.

2. **Composite Analysis Engine Beyond LLM**: We not only rely on 5 types of professionally designed Agents, but also integrate middleware such as fine-tuned models and statistical models. Through multi-model collaborative work, we ensure the depth, accuracy, and multi-dimensional perspective of analysis results.

3. **Powerful Multimodal Capabilities**: Breaking through text and image limitations, capable of deep analysis of short video content from TikTok, Kuaishou, etc., and precisely extracting structured multimodal information cards such as weather, calendar, stocks from modern search engines, giving you comprehensive control over public opinion dynamics.

4. **Agent "Forum" Collaboration Mechanism**: Endowing different Agents with unique toolsets and thinking patterns, introducing a debate moderator model, conducting chain-of-thought collision and debate through the "forum" mechanism. This not only avoids the thinking limitations of single models and homogenization caused by communication, but also catalyzes higher-quality collective intelligence and decision support.

5. **Seamless Integration of Public and Private Domain Data**: The platform not only analyzes public opinion, but also provides high-security interfaces supporting seamless integration of your internal business databases with public opinion data. Breaking through data barriers, providing powerful analysis capabilities of "external trends + internal insights" for vertical businesses.

6. **Lightweight and Highly Extensible Framework**: Based on pure Python modular design, achieving lightweight, one-click deployment. Clear code structure allows developers to easily integrate custom models and business logic, enabling rapid platform expansion and deep customization.

**Starting with public opinion, but not limited to public opinion**. The goal of "WeiYu" is to become a simple and universal data analysis engine that drives all business scenarios.

> For example, you only need to simply modify the API parameters and prompts of the Agent toolset to transform it into a financial market analysis system.

<div align="center">
<img src="static/image/system_schematic.png" alt="banner" width="800">

Say goodbye to traditional data dashboards. In "WeiYu", everything starts with a simple question - you just need to ask your analysis needs like a conversation
</div>

## 🏗️ System Architecture

### Overall Architecture Diagram

**Insight Agent** Private Database Mining: AI agent for in-depth analysis of private public opinion databases

**Media Agent** Multimodal Content Analysis: AI agent with powerful multimodal capabilities

**Query Agent** Precise Information Search: AI agent with domestic and international web search capabilities

**Report Agent** Intelligent Report Generation: Multi-round report generation AI agent with built-in templates

<div align="center">
<img src="static/image/framework.png" alt="banner" width="800">
</div>

### A Complete Analysis Workflow

| Step | Phase Name | Main Operations | Participating Components | Cycle Nature |
|------|------------|-----------------|-------------------------|--------------|
| 1 | User Query | Flask main application receives the query | Flask Main Application | - |
| 2 | Parallel Launch | Three Agents start working simultaneously | Query Agent, Media Agent, Insight Agent | - |
| 3 | Preliminary Analysis | Each Agent uses dedicated tools for overview search | Each Agent + Dedicated Toolsets | - |
| 4 | Strategy Formulation | Develop segmented research strategies based on preliminary results | Internal Decision Modules of Each Agent | - |
| 5-N | **Iterative Phase** | **Forum Collaboration + In-depth Research** | **ForumEngine + All Agents** | **Multi-round cycles** |
| 5.1 | In-depth Research | Each Agent conducts specialized search guided by forum host | Each Agent + Reflection Mechanisms + Forum Guidance | Each cycle |
| 5.2 | Forum Collaboration | ForumEngine monitors Agent communications and generates host summaries | ForumEngine + LLM Host | Each cycle |
| 5.3 | Communication Integration | Each Agent adjusts research directions based on discussions | Each Agent + forum_reader tool | Each cycle |
| N+1 | Result Integration | Report Agent collects all analysis results and forum content | Report Agent | - |
| N+2 | Report Generation | Dynamically select templates and styles, generate final reports through multiple rounds | Report Agent + Template Engine | - |

### Project Code Structure Tree

```
Weibo_PublicOpinion_AnalysisSystem/
├── QueryEngine/                   # Domestic and international news breadth search Agent
│   ├── agent.py                   # Agent main logic
│   ├── llms/                      # LLM interface wrapper
│   ├── nodes/                     # Processing nodes
│   ├── tools/                     # Search tools
│   ├── utils/                     # Utility functions
│   └── ...                        # Other modules
├── MediaEngine/                   # Powerful multimodal understanding Agent
│   ├── agent.py                   # Agent main logic
│   ├── nodes/                     # Processing nodes
│   ├── llms/                      # LLM interfaces
│   ├── tools/                     # Search tools
│   ├── utils/                     # Utility functions
│   └── ...                        # Other modules
├── InsightEngine/                 # Private database mining Agent
│   ├── agent.py                   # Agent main logic
│   ├── llms/                      # LLM interface wrapper
│   │   └── base.py                # Unified OpenAI-compatible client
│   ├── nodes/                     # Processing nodes
│   │   ├── base_node.py           # Base node class
│   │   ├── formatting_node.py     # Formatting node
│   │   ├── report_structure_node.py # Report structure node
│   │   ├── search_node.py         # Search node
│   │   └── summary_node.py        # Summary node
│   ├── tools/                     # Database query and analysis tools
│   │   ├── keyword_optimizer.py   # Qwen keyword optimization middleware
│   │   ├── search.py              # Database operation toolkit
│   │   └── sentiment_analyzer.py  # Sentiment analysis integration tool
│   ├── state/                     # State management
│   │   ├── __init__.py
│   │   └── state.py               # Agent state definition
│   ├── prompts/                   # Prompt templates
│   │   ├── __init__.py
│   │   └── prompts.py             # Various prompts
│   └── utils/                     # Utility functions
│       ├── __init__.py
│       ├── config.py              # Configuration management
│       └── text_processing.py     # Text processing tools
├── ReportEngine/                  # Multi-round report generation Agent
│   ├── agent.py                   # Agent main logic
│   ├── llms/                      # LLM interfaces
│   ├── nodes/                     # Report generation nodes
│   │   ├── template_selection.py  # Template selection node
│   │   └── html_generation.py     # HTML generation node
│   ├── report_template/           # Report template library
│   │   ├── 社会公共热点事件分析.md
│   │   ├── 商业品牌舆情监测.md
│   │   └── ...                    # More templates
│   └── flask_interface.py         # Flask API interface
├── ForumEngine/                   # Forum engine simple implementation
│   ├── monitor.py                 # Log monitoring and forum management
│   └── llm_host.py                # Forum host LLM module
├── MindSpider/                    # Weibo crawler system
│   ├── main.py                    # Crawler main program
│   ├── config.py                  # Crawler configuration file
│   ├── BroadTopicExtraction/      # Topic extraction module
│   │   ├── database_manager.py    # Database manager
│   │   ├── get_today_news.py      # Today's news fetching
│   │   ├── main.py                # Topic extraction main program
│   │   └── topic_extractor.py     # Topic extractor
│   ├── DeepSentimentCrawling/     # Deep sentiment crawling
│   │   ├── keyword_manager.py     # Keyword manager
│   │   ├── main.py                # Deep crawling main program
│   │   ├── MediaCrawler/          # Media crawler core
│   │   └── platform_crawler.py    # Platform crawler management
│   └── schema/                    # Database schema
│       ├── db_manager.py          # Database manager
│       ├── init_database.py       # Database initialization
│       └── mindspider_tables.sql  # Database table structure
├── SentimentAnalysisModel/        # Sentiment analysis model collection
│   ├── WeiboSentiment_Finetuned/  # Fine-tuned BERT/GPT-2 models
│   ├── WeiboMultilingualSentiment/# Multilingual sentiment analysis (recommended)
│   ├── WeiboSentiment_SmallQwen/  # Small parameter Qwen3 fine-tuning
│   └── WeiboSentiment_MachineLearning/ # Traditional machine learning methods
├── SingleEngineApp/               # Individual Agent Streamlit applications
│   ├── query_engine_streamlit_app.py
│   ├── media_engine_streamlit_app.py
│   └── insight_engine_streamlit_app.py
├── templates/                     # Flask templates
│   └── index.html                 # Main interface frontend
├── static/                        # Static resources
├── logs/                          # Runtime log directory
├── final_reports/                 # Final generated HTML report files
├── utils/                         # Common utility functions
│   ├── forum_reader.py            # Agent forum communication
│   └── retry_helper.py            # Network request retry mechanism tool
├── app.py                         # Flask main application entry
├── config.py                      # Global configuration file
└── requirements.txt               # Python dependency list
```

## 🚀 Quick Start

> If you are new to building Agent systems, you can start with a very simple demo: [Deep Search Agent Demo](https://github.com/666ghj/DeepSearchAgent-Demo)

### System Requirements

- **Operating System**: Windows, Linux, MacOS
- **Python Version**: 3.9+
- **Conda**: Anaconda or Miniconda
- **Database**: MySQL (optional, you can choose our cloud database service)
- **Memory**: 2GB+ recommended

### 1. Create Conda Environment

```bash
# Create conda environment
conda create -n your_conda_name python=3.11
conda activate your_conda_name
```

### 2. Install Dependencies

```bash
# Basic dependency installation
pip install -r requirements.txt

#========Below are optional========
# If you need local sentiment analysis functionality, install PyTorch
# CPU version
pip install torch torchvision torchaudio

# CUDA 11.8 version (if you have GPU)
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install transformers and other AI-related dependencies
pip install transformers scikit-learn xgboost
```

### 3. Install Playwright Browser Drivers

```bash
# Install browser drivers (for crawler functionality)
playwright install chromium
```

### 4. System Configuration

#### 4.1 Configure API Keys

Edit the `config.py` file and fill in your API keys (you can also choose your own models and search proxies; see the config file for details):

```python
# MySQL Database Configuration
DB_HOST = "localhost"
DB_PORT = 3306
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_NAME = "your_db_name"
DB_CHARSET = "utf8mb4"

# LLM configuration
# You can switch each Engine's LLM provider as long as it follows the OpenAI-compatible request format

# Insight Agent
INSIGHT_ENGINE_API_KEY = "your_api_key"
INSIGHT_ENGINE_BASE_URL = "https://api.moonshot.cn/v1"
INSIGHT_ENGINE_MODEL_NAME = "kimi-k2-0711-preview"
# Media Agent
...
```

#### 4.2 Database Initialization

**Option 1: Use Local Database**
```bash
# Local MySQL database initialization
cd MindSpider
python schema/init_database.py
```

**Option 2: Use Cloud Database Service (Recommended)**

We provide convenient cloud database service with 100,000+ daily real public opinion data, currently **free application**!

- Real public opinion data, updated in real-time
- Multi-dimensional tag classification
- High-availability cloud service
- Professional technical support

**Contact us to apply for free cloud database access: 📧 670939375@qq.com**

> To conduct a data compliance review and service upgrade, we are suspending new applications for the cloud database, effective October 1, 2025.

### 5. Launch System

#### 5.1 Complete System Launch (Recommended)

```bash
# In project root directory, activate conda environment
conda activate your_conda_name

# Start main application
python app.py
```

> Note 1: After a run is terminated, the Streamlit app might not shut down correctly and may still be occupying the port. If this occurs, find the process that is holding the port and kill it.

> Note 2: Data scraping needs to be performed as a separate operation. Please refer to the instructions in section 5.3.

Visit http://localhost:5000 to use the complete system

#### 5.2 Launch Individual Agents

```bash
# Start QueryEngine
streamlit run SingleEngineApp/query_engine_streamlit_app.py --server.port 8503

# Start MediaEngine  
streamlit run SingleEngineApp/media_engine_streamlit_app.py --server.port 8502

# Start InsightEngine
streamlit run SingleEngineApp/insight_engine_streamlit_app.py --server.port 8501
```

#### 5.3 Crawler System Standalone Use

This section has detailed configuration documentation: [MindSpider Usage Guide](./MindSpider/README.md)

```bash
# Enter crawler directory
cd MindSpider

# Project initialization
python main.py --setup

# Run complete crawler workflow
python main.py --complete --date 2024-01-20

# Run topic extraction only
python main.py --broad-topic --date 2024-01-20

# Run deep crawling only
python main.py --deep-sentiment --platforms xhs dy wb
```

## ⚙️ Advanced Configuration

### Modify Key Parameters

#### Agent Configuration Parameters

Each agent has dedicated configuration files that can be adjusted according to needs:

```python
# QueryEngine/utils/config.py
class Config:
    max_reflections = 2           # Reflection rounds
    max_search_results = 15       # Maximum search results
    max_content_length = 8000     # Maximum content length
    
# MediaEngine/utils/config.py  
class Config:
    comprehensive_search_limit = 10  # Comprehensive search limit
    web_search_limit = 15           # Web search limit
    
# InsightEngine/utils/config.py
class Config:
    default_search_topic_globally_limit = 200    # Global search limit
    default_get_comments_limit = 500             # Comment retrieval limit
    max_search_results_for_llm = 50              # Max results for LLM
```

#### Sentiment Analysis Model Configuration

```python
# InsightEngine/tools/sentiment_analyzer.py
SENTIMENT_CONFIG = {
    'model_type': 'multilingual',     # Options: 'bert', 'multilingual', 'qwen'
    'confidence_threshold': 0.8,      # Confidence threshold
    'batch_size': 32,                 # Batch size
    'max_sequence_length': 512,       # Max sequence length
}
```

### Integrate Different LLM Models

The system supports any LLM provider that follows the OpenAI request format. You only need to fill in KEY, BASE_URL, and MODEL_NAME in `config.py`.

> What is the OpenAI request format? Here's a simple example:
>```python
>from openai import OpenAI
>
>client = OpenAI(api_key="your_api_key",
>                base_url="https://api.siliconflow.cn/v1")
>
>response = client.chat.completions.create(
>    model="Qwen/Qwen2.5-72B-Instruct",
>    messages=[
>        {
>            'role': 'user',
>            'content': "What new opportunities will reasoning models bring to the market?"
>        }
>    ],
>)
>
>complete_response = response.choices[0].message.content
>print(complete_response)
>```

### Change Sentiment Analysis Models

The system integrates multiple sentiment analysis methods, selectable based on needs:

#### 1. Multilingual Sentiment Analysis

```bash
cd SentimentAnalysisModel/WeiboMultilingualSentiment
python predict.py --text "This product is amazing!" --lang "en"
```

#### 2. Small Parameter Qwen3 Fine-tuning

```bash
cd SentimentAnalysisModel/WeiboSentiment_SmallQwen
python predict_universal.py --text "This event was very successful"
```

#### 3. BERT-based Fine-tuned Model

```bash
# Use BERT Chinese model
cd SentimentAnalysisModel/WeiboSentiment_Finetuned/BertChinese-Lora
python predict.py --text "This product is really great"
```

#### 4. GPT-2 LoRA Fine-tuned Model

```bash
cd SentimentAnalysisModel/WeiboSentiment_Finetuned/GPT2-Lora
python predict.py --text "I'm not feeling great today"
```

#### 5. Traditional Machine Learning Methods

```bash
cd SentimentAnalysisModel/WeiboSentiment_MachineLearning
python predict.py --model_type "svm" --text "Service attitude needs improvement"
```

### Integrate Custom Business Database

#### 1. Modify Database Connection Configuration

```python
# Add your business database configuration in config.py
BUSINESS_DB_HOST = "your_business_db_host"
BUSINESS_DB_PORT = 3306
BUSINESS_DB_USER = "your_business_user"
BUSINESS_DB_PASSWORD = "your_business_password"
BUSINESS_DB_NAME = "your_business_database"
```

#### 2. Create Custom Data Access Tools

```python
# InsightEngine/tools/custom_db_tool.py
class CustomBusinessDBTool:
    """Custom business database query tool"""
    
    def __init__(self):
        self.connection_config = {
            'host': config.BUSINESS_DB_HOST,
            'port': config.BUSINESS_DB_PORT,
            'user': config.BUSINESS_DB_USER,
            'password': config.BUSINESS_DB_PASSWORD,
            'database': config.BUSINESS_DB_NAME,
        }
    
    def search_business_data(self, query: str, table: str):
        """Query business data"""
        # Implement your business logic
        pass
    
    def get_customer_feedback(self, product_id: str):
        """Get customer feedback data"""
        # Implement customer feedback query logic
        pass
```

#### 3. Integrate into InsightEngine

```python
# Integrate custom tools in InsightEngine/agent.py
from .tools.custom_db_tool import CustomBusinessDBTool

class DeepSearchAgent:
    def __init__(self, config=None):
        # ... other initialization code
        self.custom_db_tool = CustomBusinessDBTool()
    
    def execute_custom_search(self, query: str):
        """Execute custom business data search"""
        return self.custom_db_tool.search_business_data(query, "your_table")
```

### Custom Report Templates

#### 1. Upload in Web Interface

The system supports uploading custom template files (.md or .txt format), selectable when generating reports.

#### 2. Create Template Files

Create new templates in the `ReportEngine/report_template/` directory, and our Agent will automatically select the most appropriate template.

## 🤝 Contributing Guide

We welcome all forms of contributions!

### How to Contribute

1. **Fork the project** to your GitHub account
2. **Create Feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to branch**: `git push origin feature/AmazingFeature`
5. **Open Pull Request**

### Development Standards

- Code follows PEP8 standards
- Commit messages use clear Chinese/English descriptions
- New features need corresponding test cases
- Update related documentation

## 🦖 Next Development Plan

The system has currently completed only the first two steps of the "three-step approach": requirement input -> detailed analysis. The missing step is prediction, and directly handing this over to LLM lacks persuasiveness.

<div align="center">
<img src="static/image/banner_compressed.png" alt="banner" width="800">
</div>

Currently, after a long period of crawling and collection, we have accumulated massive data on topic popularity trends over time, trending events, and other change patterns across the entire network. We now have the conditions to develop prediction models. Our team will apply our technical reserves in time series models, graph neural networks, multimodal fusion, and other prediction model technologies to achieve truly data-driven public opinion prediction functionality.

## ⚠️ Disclaimer

**Important Notice: This project is for educational, academic research, and learning purposes only**

1. **Compliance Statement**:
   - All code, tools, and functionalities in this project are intended solely for educational, academic research, and learning purposes
   - Commercial use or profit-making activities are strictly prohibited
   - Any illegal, non-compliant, or rights-infringing activities are strictly prohibited

2. **Web Scraping Disclaimer**:
   - The web scraping functionality in this project is intended only for technical learning and research purposes
   - Users must comply with the target websites' robots.txt protocols and terms of use
   - Users must comply with relevant laws and regulations and must not engage in malicious scraping or data abuse
   - Users are solely responsible for any legal consequences arising from the use of web scraping functionality

3. **Data Usage Disclaimer**:
   - The data analysis functionality in this project is intended only for academic research purposes
   - Using analysis results for commercial decision-making or profit-making purposes is strictly prohibited
   - Users should ensure the legality and compliance of the data being analyzed

4. **Technical Disclaimer**:
   - This project is provided "as is" without any express or implied warranties
   - The authors are not responsible for any direct or indirect losses caused by the use of this project
   - Users should evaluate the applicability and risks of this project independently

5. **Liability Limitation**:
   - Users should fully understand relevant laws and regulations before using this project
   - Users should ensure their usage complies with local legal and regulatory requirements
   - Users are solely responsible for any consequences arising from the illegal use of this project

**Please carefully read and understand the above disclaimer before using this project. Using this project indicates that you have agreed to and accepted all the above terms.**

## 📄 License

This project is licensed under the [GPL-2.0 License](LICENSE). Please see the LICENSE file for details.

## 🎉 Support & Contact

### Get Help

- **Project Homepage**: [GitHub Repository](https://github.com/666ghj/Weibo_PublicOpinion_AnalysisSystem)
- **Issue Reporting**: [Issues Page](https://github.com/666ghj/Weibo_PublicOpinion_AnalysisSystem/issues)
- **Feature Requests**: [Discussions Page](https://github.com/666ghj/Weibo_PublicOpinion_AnalysisSystem/discussions)

### Contact Information

- 📧 **Email**: 670939375@qq.com

### Business Cooperation

- **Enterprise Custom Development**
- **Big Data Services**
- **Academic Collaboration**
- **Technical Training**

## 👥 Contributors

Thanks to these excellent contributors:

[![Contributors](https://contrib.rocks/image?repo=666ghj/Weibo_PublicOpinion_AnalysisSystem)](https://github.com/666ghj/Weibo_PublicOpinion_AnalysisSystem/graphs/contributors)
