import streamlit as st
import sqlite3
import pandas as pd

st.title("📊 投资公司评分搜索引擎")

# 连接数据库
conn = sqlite3.connect("data/investment.db")
df = pd.read_sql("SELECT * FROM companies", conn)
conn.close()

# 筛选栏
min_score = st.slider("最低评分", 0, 100, 60)
keyword = st.text_input("公司关键词")

# 过滤数据
filtered = df[df['score'] >= min_score]
if keyword:
    filtered = filtered[filtered['company_name'].str.lower().str.contains(keyword.lower())]

st.markdown(f"共筛选出 {len(filtered)} 家公司：")

# 展示结果
st.dataframe(filtered.sort_values(by="score", ascending=False), use_container_width=True)
