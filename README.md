# Agent Email

基于 LangGraph 的智能客服邮件 Agent。

## 功能

- 解析邮件意图
- 检索知识库
- 生成回复草稿
- 人工审核断点
- 检索为空时自动重试

## 技术栈

- Python 3.11
- LangGraph
- FastAPI
- Pydantic
- Chroma / BM25 / Rerank

## 项目结构

app/
  agents/     # LangGraph 图与节点
  tools/      # 工具注册
  schemas/    # Pydantic 模型
  core/       # 配置与日志
  main.py     # FastAPI 入口
tests/        # pytest 测试

## 启动

pip install -r requirements.txt
uvicorn app.main:app --reload

## 状态

Day 1：项目初始化完成。
