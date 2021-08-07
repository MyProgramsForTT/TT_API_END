from fastapi import FastAPI
from fastapi import FastAPI,Query
from fastapi import FastAPI, Form
from fastapi import Depends, FastAPI
# 导入Request上下文对象，用来在前后台之间传递参数
from starlette.requests import Request
 
# 导入jinja2模板引擎对象，用于后续使用
from starlette.templating import Jinja2Templates
 
app=FastAPI()
 
# 实例化一个模板引擎对象，指定模板所在路径
templates=Jinja2Templates(directory='')
 
@app.get('/')
 
# 在视图函数中传入request对象，用于在模板对象中传递上下文（同时接收路径参数info，将其传递到上下文中）
async def index(request:Request):
    # 返回一个模板对象，同时使用上下文中的数据对模板进行渲染
    return templates.TemplateResponse(name='.html',context={'request':request})
@app.post('/')
async def login(*,
    Author: str = Form(...)
):
    if Author == 'TT':
        return {"code":"200","Author":"TT","Web":"http://47.113.205.237/web/","Payload":"http://47.113.205.237/payload/","Playgame":"https://www.tomorrowing.cn/playgames/"}
    else:
        return {"code":"400","msg":"错误"}
 
