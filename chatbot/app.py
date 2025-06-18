import streamlit as st
from openai import OpenAI

# Initialize OpenAI client with OpenRouter config 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
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)

st.title("OpenRouter Chatbot")

# Create a text input for user messages
user_input = st.text_input("You:", "")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if user_input:
    # Add user message to chat history
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    # Call OpenRouter API with chat history
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1-0528:free",
        messages=st.session_state.chat_history,
        extra_headers={
            "HTTP-Referer": "https://your-site-url.com",  # optional, replace if you want
            "X-Title": "MyChatbot",  # optional, replace if you want
        },
    )

    # Extract assistant reply
    assistant_reply = completion.choices[0].message.content

    # Add assistant reply to chat history
    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_reply}
    )

# Display chat history
for chat in st.session_state.chat_history:
    if chat["role"] == "user":
        st.markdown(f"**You:** {chat['content']}")
    else:
        st.markdown(f"**Bot:** {chat['content']}")
