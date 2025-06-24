# 🧠 投资分析数据中台（Investment Intelligence Platform）

一个基于 FastAPI + SQLite + GraphQL + Streamlit 构建的模拟投后数据平台，自动计算公司投资吸引力评分，支持 REST & GraphQL 双接口查询，并提供可视化搜索前端，支持 Docker 一键部署。

---

## 🚀 项目亮点

- 模拟企业基本面 + 新闻数据抓取并清洗入库
- 构建“公司评分”模型，模拟投后风控/投资偏好
- 提供 REST + GraphQL 查询接口（字段可选、条件过滤）
- 可视化前端：Streamlit 页面支持评分筛选与搜索
- 支持 Docker Compose 一键打包部署

---

## 🛠 技术栈

- **Backend**：FastAPI + SQLite + Strawberry GraphQL
- **Frontend**：Streamlit
- **Infra**：Docker + docker-compose

---

## ⚡ 快速开始

### 🧪 本地运行

```bash
git clone https://github.com/your-username/investment-platform.git
cd investment-platform
pip install -r requirements.txt
python Tencent_Data_API.py```

访问接口：

REST: http://localhost:8000/companies

GraphQL: http://localhost:8000/graphql

🐳 Docker 部署
bash
Copy
Edit
docker compose build
docker compose up
📬 接口示例
✅ REST 查询公司评分：
http
Copy
Edit
GET /companies?min_score=70&keyword=ai
✅ GraphQL 查询公司列表：
graphql
Copy
Edit
{
  companies(minScore: 80, keyword: "biotech") {
    companyName
    score
  }
}

📊 Streamlit 前端页面
bash
Copy
Edit
streamlit run streamlit_app.py
分数滑动选择器 + 公司名模糊搜索

结果表格实时刷新

📁 目录结构
kotlin
Copy
Edit
investment-platform/
├── Tencent_Data_API.py        ← FastAPI + GraphQL 主逻辑
├── streamlit_app.py           ← Streamlit 可视化界面
├── requirements.txt           ← Python 依赖项
├── Dockerfile                 ← Docker 镜像配置
├── docker-compose.yml         ← 容器编排启动
├── .gitignore / .dockerignore← 项目清洁工具
├── data/                      ← SQLite 数据库 & CSV 数据
└── README.md                  ← 项目说明文档（你正在看）
