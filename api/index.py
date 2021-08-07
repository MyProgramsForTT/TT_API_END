from fastapi import FastAPI
from fastapi import FastAPI,Query
from fastapi import FastAPI, Form
from fastapi import Depends, FastAPI
# 导入Request上下文对象，用来在前后台之间传递参数
from starlette.requests import Request
 
# 导入jinja2模板引擎对象，用于后续使用
from starlette.templating import Jinja2Templates
 
app=FastAPI()
 

@app.post('/API/')
async def login(*,
    Author: str = Form(...)
):
    if Author == 'TT':
        return {"code":"200","Author":"TT","Web":"http://47.113.205.237/web/","Payload":"http://47.113.205.237/payload/","Playgame":"https://www.tomorrowing.cn/playgames/"}
    else:
        return {"code":"400","msg":"错误"}
 
