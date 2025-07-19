import streamlit as st
from agent import run_agent

st.set_page_config(page_title="Budget Product Agent", page_icon="🛍️")
st.title("Budget Product Agent")
st.markdown("Ask anything like: `Best headphones under ₹2000` or `Shoes under ₹1500`")

query = st.text_input("What are you looking for?", placeholder="Type your requirement here...")

if st.button("Find Best Options"):
    if query:
        with st.spinner("Agent is working..."):
            result = run_agent(query)
        st.success("Done!")
        st.markdown("### Agent's Response")
        st.markdown(result)
    else:
        st.warning("Please enter a search query.")
