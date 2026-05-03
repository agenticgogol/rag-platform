# frontend/streamlit_app.py

import streamlit as st
import requests

#BACKEND_URL = "http://localhost:8000"
import os
BACKEND_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
)

st.set_page_config(
    page_title="RAG Platform",
    layout="wide"
)

st.title("📘 RAG Knowledge Assistant")

# -----------------------------------
# Session State
# -----------------------------------
if "answer" not in st.session_state:
    st.session_state.answer = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# -----------------------------------
# Tabs
# -----------------------------------
tab1, tab2, tab3 = st.tabs(
    ["Upload PDFs", "Add URLs", "Upload Images"]
)

# -----------------------------------
# Upload PDFs
# -----------------------------------
with tab1:

    files = st.file_uploader(
        "Upload PDFs",
        type=["pdf"],
        accept_multiple_files=True,
        key="pdf_uploader"
    )

    if st.button("Process PDFs"):

        if not files:
            st.warning("Please upload PDFs.")

        else:

            data = []

            for f in files:
                data.append(
                    (
                        "files",
                        (
                            f.name,
                            f.getvalue(),
                            "application/pdf"
                        )
                    )
                )

            try:
                with st.spinner("Processing PDFs..."):

                    res = requests.post(
                        f"{BACKEND_URL}/upload-pdf",
                        files=data
                    )

                if res.status_code == 200:
                    st.success(res.json()["message"])
                else:
                    st.error(res.text)

            except Exception as e:
                st.error(str(e))

# -----------------------------------
# URL Upload
# -----------------------------------
with tab2:

    urls = st.text_area(
        "Enter one URL per line"
    )

    if st.button("Process URLs"):

        url_list = [
            u.strip()
            for u in urls.split("\n")
            if u.strip()
        ]

        if not url_list:
            st.warning("Please enter URLs.")

        else:

            try:
                with st.spinner("Processing URLs..."):

                    res = requests.post(
                        f"{BACKEND_URL}/upload-url",
                        json={"urls": url_list}
                    )

                if res.status_code == 200:
                    st.success(res.json()["message"])
                else:
                    st.error(res.text)

            except Exception as e:
                st.error(str(e))

# -----------------------------------
# Image Upload
# -----------------------------------
with tab3:

    image_files = st.file_uploader(
        "Upload Images",
        type=["png", "jpg", "jpeg"],
        accept_multiple_files=True,
        key="image_uploader"
    )

    if st.button("Process Images"):

        if not image_files:
            st.warning("Please upload images.")

        else:

            data = []

            for f in image_files:
                data.append(
                    (
                        "files",
                        (
                            f.name,
                            f.getvalue(),
                            f.type
                        )
                    )
                )

            try:
                with st.spinner("Processing Images..."):

                    res = requests.post(
                        f"{BACKEND_URL}/upload-image",
                        files=data
                    )

                if res.status_code == 200:
                    st.success(res.json()["message"])
                else:
                    st.error(res.text)

            except Exception as e:
                st.error(str(e))

# -----------------------------------
# Ask Question
# -----------------------------------
st.divider()

question = st.text_input(
    "Ask Question",
    placeholder="Ask from PDFs / URLs / Images..."
)

if st.button("Submit"):

    if not question.strip():

        st.warning("Please enter question.")

    else:

        try:
            with st.spinner("Thinking..."):

                res = requests.post(
                    f"{BACKEND_URL}/ask",
                    json={"question": question}
                )

            if res.status_code == 200:

                answer = res.json()["answer"]

                st.session_state.answer = answer

                st.session_state.chat_history.append(
                    {
                        "question": question,
                        "answer": answer
                    }
                )

            else:
                st.error(res.text)

        except Exception as e:
            st.error(str(e))

# -----------------------------------
# Current Answer
# -----------------------------------
if st.session_state.answer:

    st.subheader("Answer")

    st.info(st.session_state.answer)

# -----------------------------------
# Chat History
# -----------------------------------
if st.session_state.chat_history:

    st.divider()

    st.subheader("Conversation History")

    for item in reversed(
        st.session_state.chat_history
    ):

        st.markdown(
            f"**Q:** {item['question']}"
        )

        st.markdown(
            f"**A:** {item['answer']}"
        )

        st.markdown("---")