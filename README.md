# 接口自动化测试项目

## 项目简介
基于 Python + Requests + Pytest 搭建的接口自动化测试框架，
对 JSONPlaceholder 公开 API 设计并执行 8 条测试用例，
覆盖正常流程、异常场景、业务校验与响应耗时。

## 技术栈
- Python 3
- Requests（发送 HTTP 请求）
- Pytest（用例管理与执行）

## 用例清单
| 编号 | 用例 | 方法 | 预期 |
|---|---|---|---|
| 1 | 查询文章列表 | GET /posts | 200，返回100条 |
| 2 | 查询单篇文章 | GET /posts/1 | 200，字段完整 |
| 3 | 查询不存在资源 | GET /posts/999 | 404 |
| 4 | 创建文章 | POST /posts | 201，返回新id |
| 5 | 更新文章 | PUT /posts/1 | 200，title已更新 |
| 6 | 删除文章 | DELETE /posts/1 | 200/204 |
| 7 | 参数过滤校验 | GET /comments?postId=1 | 200，数据归属正确 |
| 8 | 响应耗时校验 | 任意请求 | 耗时 < 2s |

## 如何运行
pip install -r requirements.txt
pytest -v

## 项目结构
<<<<<<< HEAD
- test.py  测试用例
- requirements.txt  依赖
- README.md  说明文档
