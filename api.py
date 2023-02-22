import openai
# Use the openai library to set the API key
openai.api_key = "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"
count = 0
while count<5:
    query = input("请输入：")
    # Define the prompt for the GPT-3 model
    response = openai.Completion.create(
                    model="text-davinci-003",  # 对话模型的名称
                    prompt=query,
                    temperature=0.9,  # 值在[0,1]之间，越大表示回复越具有不确定性
                    max_tokens=1200,  # 回复最大的字符数
                    top_p=1,
                    frequency_penalty=0.0,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
                    presence_penalty=0.0,  # [-2,2]之间，该值越大则更倾向于产生不同的内容
                    stop=["\n\n\n"]
                )
    res_content = response.choices[0]['text'].strip().replace('<|endoftext|>', '')
    print("ChatGPT：{}".format(res_content))
    count+=1