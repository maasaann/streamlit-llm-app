# from dotenv import load_dotenv
# load_dotenv()
import streamlit as st
# from langchain_openai import ChatOpenAI
# from langchain.schema import SystemMessage, HumanMessage, AIMessage

# llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# messages = [
#     SystemMessage(content="You are a helpful assistant."),
#     HumanMessage(content="私の名前は田中です"),
#     AIMessage(content="こんにちは、田中さん"),
#     HumanMessage(content="私の名前が分かりますか？"),
# ]

# result = llm(messages)
# st.write(result.content)



st.title("Lesson 21 Streamlitを活用したWebアプリ開発")
st.title("Chapter 6 【提出課題】LLM機能を搭載したWebアプリを開発しよう")

st.write("##### LLMタイプ①: あああ")
st.write("##### LLMタイプ②: いいい")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["文字数カウント", "BMI値の計算"]
)

# st.divider()

# if selected_item == "文字数カウント":
#     input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")
#     text_count = len(input_message)

# else:
#     height = st.text_input(label="身長（cm）を入力してください。")
#     weight = st.text_input(label="体重（kg）を入力してください。")

# if st.button("実行"):
#     st.divider()

#     if selected_item == "文字数カウント":
#         if input_message:
#             st.write(f"文字数: **{text_count}**")

#         else:
#             st.error("カウント対象となるテキストを入力してから「実行」ボタンを押してください。")

#     else:
#         if height and weight:
#             try:
#                 bmi = round(int(weight) / ((int(height)/100) ** 2), 1)
#                 st.write(f"BMI値: {bmi}")

#             except ValueError as e:
#                 st.error("身長と体重は数値で入力してください。")

#         else:
#             st.error("身長と体重をどちらも入力してください。")