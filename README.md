# 🧠 投资分析数据中台（Investment Intelligence Platform）

一个基于 FastAPI + SQLite + GraphQL + Streamlit 构建的模拟投后数据平台，自动计算公司投资吸引力评分，支持 REST & GraphQL 双接口查询，并提供可视化搜索前端，支持 Docker 一键部署。

## 🚀 项目亮点
- 模拟企业基本面 + 新闻数据抓取并清洗入库
- 构建“公司评分”模型，模拟投后风控/投资偏好
- 提供 REST + GraphQL 查询接口（字段可选、条件过滤）
- 可视化前端：Streamlit 页面支持评分筛选与搜索
- 支持 Docker Compose 一键打包部署

## 🛠 技术栈
- Backend：FastAPI + SQLite + Strawberry GraphQL
- Frontend：Streamlit
- Infra：Docker + docker-compose

## ⚡ 快速开始（命令 + 接口 + 示例 + Docker）

```bash
# 克隆项目并安装依赖
git clone https://github.com/your-username/investment-platform.git
cd investment-platform
pip install -r requirements.txt

# 运行主服务（FastAPI + SQLite + REST + GraphQL）
python Tencent_Data_API.py

# 访问接口：
# REST:     http://localhost:8000/companies
# GraphQL:  http://localhost:8000/graphql

# REST 查询示例：
# http://localhost:8000/companies?min_score=70&keyword=ai

# GraphQL 查询示例：
# {
#   companies(minScore: 80, keyword: "biotech") {
#     companyName
#     score
#   }
# }

# 启动前端界面（Streamlit 可视化）
streamlit run streamlit_app.py

# 启动 Docker 服务（可选）
docker compose build
docker compose up
```
## 📁 项目结构
├── Tencent_Data_API.py          ← FastAPI + GraphQL 主逻辑
├── streamlit_app.py             ← Streamlit 可视化界面
├── requirements.txt             ← Python 依赖项
├── Dockerfile                   ← Docker 镜像配置
├── docker-compose.yml           ← 容器编排启动
├── .gitignore / .dockerignore   ← 项目清洁工具
├── data/                        ← SQLite 数据库 & CSV 数据
└── README.md                    ← 项目说明文档（你正在看）

## 📝 License
MIT License. For education, demo and interview purposes only.
