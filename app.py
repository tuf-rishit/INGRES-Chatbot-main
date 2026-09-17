import streamlit as st
from backend.chatbot_engine import get_groundwater_dataframe, query_groundwater_text
from visualization import show_chart

# --------------------------------------------------------
#                   CUSTOM UI STYLING
# --------------------------------------------------------
st.set_page_config(page_title="AI-ChatBOT-INGRE", layout="wide")

st.markdown(
    """
    <style>
        /* Background gradient */
        .stApp {
            background: linear-gradient(135deg, #1d3b53, #3a6178, #9dbdc6);
            background-attachment: fixed;
        }

        /* Title */
        .main-title {
            font-size: 40px;
            font-weight: 900;
            text-align: center;
            color: white;
            margin-top: 10px;
            text-shadow: 2px 2px 6px rgba(0,0,0,0.4);
        }

        /* Subtitle */
        .sub-text {
            text-align: center;
            font-size: 16px;
            color: #f0f0f0cc;
            margin-top: -8px;
            margin-bottom: 5px;
        }

        /* Welcome message box */
        .welcome-box {
            background: rgba(255, 255, 255, 0.15);
            padding: 14px 20px;
            border-radius: 12px;
            backdrop-filter: blur(4px);
            -webkit-backdrop-filter: blur(4px);
            color: #ffffff;
            font-size: 17px;
            margin-top: 15px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------------
#                      HEADER
# --------------------------------------------------------
st.markdown("<div class='main-title'>💧 AI-ChatBOT-INGRE – Chat Mode</div>", unsafe_allow_html=True)

st.markdown("<div class='welcome-box'>Hello! 👋 Welcome to AI-ChatBOT-INGRE. How can I help you today?</div>", unsafe_allow_html=True)

# --------------------------------------------------------
#                      CHAT SECTION
# --------------------------------------------------------

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Language dropdown
lang = st.selectbox(
    "Select Language:",
    ["en", "hi", "mr", "gu", "ta", "te", "kn", "bn"]
)

# Display chat history (Messenger style left/right)
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])
        if "df" in msg and msg["df"] is not None:
            st.write("### 📊 Visualization")
            show_chart(msg["df"])

# Chat input field
user_text = st.chat_input("Ask something about groundwater...")

if user_text:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.write(user_text)

    # Process response
    df = get_groundwater_dataframe(user_text)
    response_text = query_groundwater_text(df, lang)

    # Store bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": response_text,
        "df": df if not df.empty else None
    })

    # Display bot message
    with st.chat_message("assistant"):
        st.write(response_text)

    if not df.empty:
        st.write("### 📊 Groundwater Data (Tabular Format)")
        st.dataframe(df)

        st.write("### 📊 Visualization")
        show_chart(df)