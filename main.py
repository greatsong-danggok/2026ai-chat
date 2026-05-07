import streamlit as st
import anthropic

st.set_page_config(page_title="AI 도우미", page_icon="🤖")
client = anthropic.Anthropic(
    api_key=st.secrets["ANTHROPIC_API_KEY"]
)

model = st.selectbox("AI 모델", [
    "claude-sonnet-4-6",  # 빠르고 저렴
    "claude-opus-4-6"     # 더 똑똑
])

question = st.text_area("질문을 입력하세요")
if st.button("🚀 질문하기") and question:
    with st.spinner("AI가 생각하는 중..."):
        msg = client.messages.create(
            model=model,
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": question
            }]
        )
        st.markdown(msg.content[0].text)
        st.caption(
            f"입력: {msg.usage.input_tokens}토큰 / 출력: {msg.usage.output_tokens}토큰"
        )
