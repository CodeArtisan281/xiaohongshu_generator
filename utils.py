from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.output_parsers import PydanticOutputParser
from prompt_template import system_template_text,user_template_text
from xiaohongshu_model import Xiaohongshu

def generate_xiaohongshu(subject,api_key,base_url,creativity):
    # 用ChatPromptTemplate的from_messages函数创建一个提示模板
    prompt = ChatPromptTemplate.from_messages(
        [
            ('system', system_template_text),
            ('user', user_template_text),
        ]
    )

    # 使用'gpt-3.5-turbo'模型并设置好参数
    model = ChatOpenAI(
        model = 'gpt-3.5-turbo',
        api_key = api_key,
        base_url = base_url,
        temperature = creativity,
        frequency_penalty = 1.1
    )

    # 创建一个PydanticOutputParser的实例，其中为pydantic_object放入Xiaohongshu这个类，让PydanticOutputParser给我们解析
    output_parser = PydanticOutputParser(pydantic_object=Xiaohongshu)

    # 使用管道操作用invoke方法用AI进行生成
    chain = prompt | model | output_parser

    result = chain.invoke(
        {
            'parser_instructions':output_parser.get_format_instructions(),
            'subject':subject
        }
    )

    return result

# # 进行一个简单的小测试
# print(generate_xiaohongshu(subject = '大模型',
#                            api_key = '请输入自己的Open AI的API密钥',
#                            base_url = '请输入自己的API密钥的接口网址',
#                            creativity = 0.7,))