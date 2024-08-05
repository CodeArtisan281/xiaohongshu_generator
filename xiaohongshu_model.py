from langchain_core.pydantic_v1 import Field,BaseModel
from typing import List

# 创建一个继承BaseModel数据模块的类，使用Field函数为标题和正文提供额外信息
class Xiaohongshu(BaseModel):
    title:List[str] = Field(description='小红书的5个标题',max_items=5,min_items=5)
    content:str = Field(description='小红书的正文内容')