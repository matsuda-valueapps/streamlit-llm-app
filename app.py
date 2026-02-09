import streamlit as st
from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# .env読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# LLM関数（課題条件）
def ask_llm(prompt, role):
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.7,
        api_key=api_key
    )

    system_prompt = ""
    if role == "法律の専門家":
        system_prompt = "あなたは法律の専門家です。初心者にも分かりやすく説明してください。"
    elif role == "飲食店ビジネスの専門家":
        system_prompt = "あなたは飲食店ビジネスの専門家です。実用的なアドバイスをしてください。"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=prompt)
    ]

    response = llm.invoke(messages)
    return response.content


# ------------------------------
# Streamlit UI
# ------------------------------
st.title("🧠 LLMアプリ")
st.write("入力した質問に対して、専門家としてLLMが回答します。")

role = st.radio(
    "🧑‍🏫 専門家を選択してください",
    ["法律の専門家", "飲食店ビジネスの専門家"]
)

user_input = st.text_input("質問を入力してください")

if st.button("送信"):
    if user_input:
        result = ask_llm(user_input, role)
        st.write("### 回答")
        st.write(result)
    else:
        st.warning("質問を入力してください")