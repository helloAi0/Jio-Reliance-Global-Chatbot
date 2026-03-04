# import streamlit as st
# from langchain_jio_queryHelper import get_jio_response

# # Page Configuration
# st.set_page_config(
#     page_title="Jio Global Support", 
#     page_icon="🔵", 
#     layout="centered"
# )

# with st.sidebar:
#     st.image("https://upload.wikimedia.org/wikipedia/commons/b/bf/Reliance_Jio_Logo.svg", width=100)
#     st.title("Support Dashboard")
#     st.info("Currently searching across: \n* Jio Mobile \n* Jio Fiber \n* Jio Mart")
    
#     if st.button("Clear Conversation"):
#         st.session_state.messages = []
#         st.rerun()

# # 3. App Header
# st.title("Jio Global Assistant")
# st.markdown("""
#     Welcome! I am your unified Reliance Jio assistant.  
#     How can I help you with **Mobile, Fiber, or Mart** services today?
# """)

# st.title("Reliance Customer Support Chatbot")
# btn = st.button("Get Customer Support Info")

# if btn:
#     pass

# question = st.text_input("Ask a question about any Reliance service:")

# if question:
#     with st.spinner("Consulting Jio Global Database..."):
#         response = get_jio_response(question)
#     st.write("Answer:")
#     st.write(response['answer'])
    
    
import streamlit as st
from langchain_jio_queryHelper import get_jio_response

# 1. Page Configuration
st.set_page_config(
    page_title="Jio Global Support", 
    page_icon="🔵", 
    layout="centered"
)

# 2. Sidebar - Global Controls
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/b/bf/Reliance_Jio_Logo.svg", width=100)
    st.title("Support Dashboard")
    st.info("Currently searching across: \n* Jio Mobile \n* Jio Fiber \n* Jio Mart")
    
    if st.button("Clear Conversation"):
        st.session_state.messages = []
        st.rerun()

# 3. App Header
st.title("Jio Global Assistant")
st.markdown("""
    Welcome! I am your unified Reliance Jio assistant.  
    How can I help you with **Mobile, Fiber, or Mart** services today?
""")

# 4. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Display Chat Messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Chat Input Logic
if prompt := st.chat_input("Ex: How do I track my JioMart order?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Generate Response
    with st.chat_message("assistant"):
        with st.spinner("Consulting Jio Global Database..."):
            try:
                # Call the function from your helper file
                answer = get_jio_response(prompt)
                st.markdown(answer)
                
                # Add assistant response to history
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error: {str(e)}")
                st.info("Check if your .env file has the correct Google API Key.")

# 7. Footer
st.caption("Powered by My Own skills and Hardowrk. Built with Streamlit and LangChain.")
    