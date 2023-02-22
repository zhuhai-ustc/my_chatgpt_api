import streamlit as st

# 定义主函数
def main():
    # 添加页面标题
    st.title("Your Title Here")
    
    # 添加页面副标题
    st.header("Your Subtitle Here")
    
    # 添加页面文本
    st.write("Your Text Here")

    # 添加表单输入框
    user_input = st.text_input("Enter your input here:")
    #content = st.text_area("输入新闻正文", max_chars=512)
    #if st.button("一键生成摘要"):
    #    start_message = st.empty()
    #    start_message.write("正在抽取，请等待...")
    #    for i, title in enumerate(titles):
    #        st.text_input("第{}个结果".format(i + 1), title)
    # 添加按钮
    output_container = st.empty()
    output = []
    if st.button("Submit"):
        # 在点击按钮后执行代码
        output.append(user_input)
        output_container.text(user_input)
    else:
        st.stop()
    print(output)
    for i in output:
        st.write(i)

# 调用主函数
if __name__ == "__main__":
    main()