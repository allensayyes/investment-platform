# 投资分析数据中台（Investment Intelligence Platform）

🚀 一个模拟投后管理的数据中台服务，具备自动打分模型、REST & GraphQL 双接口、Streamlit 前端界面以及 Docker 一键部署能力。适用于展示数据工程、API设计、产品理解的综合能力。

【项目功能】
- 企业信息 + 新闻模拟抓取并入库
- 构建企业“投资吸引力评分”模型
- 提供 REST + GraphQL 接口，灵活支持查询
- 搭配 Streamlit 可视化前端（评分搜索、结果展示）
- 使用 Docker 一键打包部署，支持本地和云端运行

【技术栈】
- FastAPI：提供 REST API
- Strawberry：实现 GraphQL 查询
- SQLite：轻量级数据仓库
- Streamlit：构建前端评分搜索界面
- Docker：项目环境封装与部署

【本地运行】
git clone https://github.com/your-username/investment-platform.git
cd investment-platform
pip install -r requirements.txt
python Tencent_Data_API.py

打开浏览器访问：
- REST 接口：http://localhost:8000/companies
- GraphQL 页面：http://localhost:8000/graphql

【Docker 一键部署】
docker compose build
docker compose up

【接口示例】
GET /companies?min_score=70&keyword=ai

GraphQL 查询示例：
{
  companies(minScore: 80, keyword: "biotech") {
    companyName
    score
  }
}

【Streamlit 前端】
streamlit run streamlit_app.py
支持关键词模糊搜索 + 最低评分筛选，实时展示打分结果。

【项目结构】
Tencent/
├── Tencent_Data_API.py        → FastAPI + GraphQL 主逻辑
├── streamlit_app.py           → Streamlit 前端交互页面
├── requirements.txt           → Python 依赖项
├── docker-compose.yml         → Docker 启动配置
├── Dockerfile                 → 镜像构建配置
├── data/                      → 数据文件夹（CSV + SQLite）

【面试官可能关注的问题】
- 为什么用 REST + GraphQL 并存？
- 如何将项目扩展为生产环境（认证机制、错误日志、定时任务、CI/CD 等）
- 如何在云端部署并处理持久化存储？

【LICENSE】
MIT License. For demo, education and interview purposes.
