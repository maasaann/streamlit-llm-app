# from dotenv import load_dotenv
# load_dotenv()

import streamlit as st
from langchain_openai import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

st.title("21-6 【提出課題】LLM機能を搭載したWebアプリを開発しよう")
st.write("")
st.write("##### LLMタイプ①: 旅行プランを考えてほしい")
st.write("##### LLMタイプ②: 観光名所を教えてほしい")
st.write("")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["旅行プランを考えてほしい", "観光名所を教えてほしい"]
)
st.write("")
input_message = st.text_input(label="旅行したい目的の都市名を入力してください。")

if st.button("質問する"):

    st.divider()

    if selected_item == "旅行プランを考えてほしい":

        messages = [
        SystemMessage(content="あなたは旅行プランを考えるプロです。100文字程度で回答してください。"),
        HumanMessage(content=input_message),
        ]

        result = llm(messages)

        st.write(result.content)

    else:

        messages = [
            SystemMessage(content="あなたは観光名所を教えるプロです。100文字程度で回答してください。"),
            HumanMessage(content=input_message),
        ]

        result = llm(messages)

        st.write(result.content)