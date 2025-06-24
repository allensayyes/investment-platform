# 项目名称：投资分析数据中台 + API 服务

"""
项目目标：模拟一个为投后管理提供支持的数据中台系统，实现数据采集、ETL处理、存储与API服务能力，适配腾讯JD中提到的多源数据建模、API设计、数据自动化处理。
"""

# === 第一阶段：数据采集模块（使用 Mock 数据替代网页抓取） ===
import pandas as pd
import os
import sqlite3
import random
from fastapi import FastAPI
from typing import Optional
import uvicorn

# === 第五阶段：GraphQL 接口支持 ===
import strawberry
from strawberry.fastapi import GraphQLRouter

app = FastAPI()

# === GraphQL 类型定义 ===
@strawberry.type
class Company:
    company_name: str
    score: int

@strawberry.type
class Query:
    @strawberry.field
    def companies(self, min_score: Optional[int] = 0, keyword: Optional[str] = None) -> list[Company]:
        conn = sqlite3.connect("data/investment.db")
        df = pd.read_sql("SELECT * FROM companies", conn)
        conn.close()

        if min_score:
            df = df[df['score'] >= min_score]
        if keyword:
            df = df[df['company_name'].str.lower().str.contains(keyword.lower())]

        return [Company(company_name=row['company_name'], score=row['score']) for _, row in df.iterrows()]

schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")


# === 原始 REST 接口 ===
@app.get("/companies")
def get_companies(min_score: Optional[int] = 0, keyword: Optional[str] = None):
    conn = sqlite3.connect("data/investment.db")
    query = "SELECT * FROM companies"
    df = pd.read_sql(query, conn)
    conn.close()

    if min_score:
        df = df[df['score'] >= min_score]
    if keyword:
        df = df[df['company_name'].str.lower().str.contains(keyword.lower())]

    return df.to_dict(orient="records")


# === 数据生成部分 ===
def fetch_company_info():
    mock_data = [
        "ByteLeap Technologies",
        "Orion Biotech",
        "Harmonia AI",
        "GreenShift Renewables",
        "Nebula Robotics"
    ]
    return pd.DataFrame({'company_name': mock_data})

def fetch_news_headlines():
    mock_news = [
        "AI startup Harmonia raises $100M Series B to expand Asia ops",
        "GreenShift secures solar panel deal with European energy group",
        "ByteLeap's new data platform targets cross-border investors",
        "Nebula Robotics to partner with automotive giants on warehouse automation",
        "Orion Biotech reports promising Phase II trial results"
    ]
    return pd.DataFrame({'headline': mock_news})


def clean_company_data(df):
    df = df.drop_duplicates()
    df['company_name'] = df['company_name'].astype(str).str.title().str.strip()
    df = df[df['company_name'].str.len() > 2]
    return df

def clean_news_data(df):
    df = df.drop_duplicates()
    df['headline'] = df['headline'].astype(str).str.strip()
    df = df[df['headline'].str.len() > 10]
    return df

def store_to_sqlite(df, table_name, conn):
    df.to_sql(table_name, conn, if_exists='replace', index=False)

def score_companies(df_companies, df_news):
    scores = []
    for company in df_companies['company_name']:
        base_score = random.randint(50, 70)
        keyword = company.split()[0].lower()
        related_news = df_news['headline'].str.lower().str.contains(keyword).sum()
        score = base_score + related_news * 5
        scores.append(min(score, 100))
    df_companies['score'] = scores
    return df_companies


if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)

    df_companies = fetch_company_info()
    df_news = fetch_news_headlines()

    df_companies = clean_company_data(df_companies)
    df_news = clean_news_data(df_news)

    df_companies = score_companies(df_companies, df_news)

    df_companies.to_csv("data/companies.csv", index=False)
    df_news.to_csv("data/news.csv", index=False)

    conn = sqlite3.connect("data/investment.db")
    store_to_sqlite(df_companies, "companies", conn)
    store_to_sqlite(df_news, "news", conn)
    conn.close()

    print("数据抓取、清洗、打分和入库完成")
    uvicorn.run(app, host="127.0.0.1", port=8000)
