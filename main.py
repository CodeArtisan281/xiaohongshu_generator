import streamlit as st
from utils import generate_xiaohongshu

# 创建一个网站的标题
st.header('爆款小红书AI写作助手 ✏️')

# 创建一个侧边栏
with st.sidebar:
    # 侧边栏中要让用户输入自己的api秘钥，并才用密码的形式展示
    api_key = st.text_input('请输入OpenAI密钥：',type='password')
    # 侧边栏中要让用户输入api接口网址
    base_url = st.text_input('请输入您的API_Key的接口网址')
    # 给用户提供一个获取OpenAI官方的API官方网址
    st.markdown('[获取OpenAI API官方密钥（需要科学上网）](https://platform.openai.com/account/api-keys)')
    # 给用户提供一个获取中转API网址，使国内用户也能够通过中转API使用到GPT
    st.markdown('[获取中转API密钥（国内可用，推荐这个）](https://api.aigc369.com/)')

# 创建一个文案主题的输入框
subject = st.text_input('主题')

# 创建一个创造性的数字参数模块
creativity = st.slider('✨ 请输入小红书文案生成的创造力（数字小说明更严谨，数字大说明更多样)',
                       max_value=1.0,
                       min_value=0.0,
                       value = 0.7,
                       step=0.1,)

# 创建一个按钮用于开始写作的按钮
submit = st.button('开始写作')

# 用户按按钮前若没输入API密钥提示用户输入API密钥才能生成脚本
if submit and not api_key:
    st.info('请输入您的OpenAI API密钥')    # 提示用户输入API秘钥
    st.stop()   # 用stop函数网页将不再运行下面的代码

# 用户按按钮前若没输入API接口网址提示用户输入API接口网址才能生成脚本
if submit and not base_url:
    st.info('请输入您的OpenAI API接口网址')  # 提示用户输入API接口网址
    st.stop()   # 用stop函数网页将不再运行下面的代码

# 用户按按钮前若没输入主题提示用户输入主题才能生成脚本
if submit and not subject:
    st.info('请输入主题')     # 提示用户输入主题
    st.stop()   # 用stop函数网页将不再运行下面的代码

# 最后当用户全都输入好按下按钮时
if submit:
    # 创建一个加载中的小提示
    with st.spinner('AI正在思考中，可以先去敲敲🫎🏄‍♂️🐠的脑瓜子🤪'):
        result = generate_xiaohongshu(subject=subject,
                                      api_key = api_key,
                                      base_url=base_url,
                                      creativity=creativity)

    # 创建一个分隔线
    st.divider()

    # 给生成的结果分两列展示
    left_column, right_column = st.columns(2)

    # 左边的一列展示标题
    with left_column:
        st.markdown('##### 小红书标题1')
        st.write(result.title[0])
        st.markdown('##### 小红书标题2')
        st.write(result.title[1])
        st.markdown('##### 小红书标题3')
        st.write(result.title[2])
        st.markdown('##### 小红书标题4')
        st.write(result.title[3])
        st.markdown('##### 小红书标题5')
        st.write(result.title[4])

    # 右边的一列展示正文内容
    with right_column:
        st.markdown('##### 小红书正文')
        st.write(result.content)
