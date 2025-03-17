import streamlit as st
import requests

st.title("GitHub Code Review Automation")

repo_url = st.text_input("Enter GitHub Repository URL")
access_token = st.text_input("Enter GitHub Access Token", type="password")

if st.button("Set Up Webhook"):
    if repo_url and access_token:
        response = requests.post(
            "http://localhost:8000/setup-webhook/",
            json={"repo_url": repo_url, "access_token": access_token}
        )
        if response.status_code == 200:
            st.success("Webhook set up successfully!")
        else:
            st.error(f"Failed to set up webhook: {response.json().get('detail', 'Unknown error')}")
    else:
        st.error("Please provide both repository URL and access token.")
