from datetime import datetime

import streamlit as st
from pymongo import MongoClient
from streamlit_extras.stylable_container import stylable_container


def set_styles(st_function):
    def load_styles():
        with open("styles.css") as f:
            return f.read()

    def wrapper(*args, **kwargs):
        styles = load_styles()
        with stylable_container(
            key=f"{st_function.__name__}-container",
            css_styles=styles,
        ):
            return st_function(*args, **kwargs)

    return wrapper


our_email_sender = "You"
our_email_sender_email = "you@emoai.com"

signature = """\n\n
---
You
you@emoai.com
EmoAI Inc."""


client = MongoClient(st.secrets["MONGO_URI"])
db = client["emoai"]


def save_response(participant_id, scenario_name, response=None):
    collection = db["responses"]

    if response is None:
        if not st.session_state.get(
            f"reply_text_area_{participant_id}_{scenario_name}", None
        ):
            return
        response = st.session_state[f"reply_text_area_{participant_id}_{scenario_name}"]

    collection.update_one(
        {"participant_id": participant_id, "scenario_name": scenario_name},
        {"$set": {"response": response}},
        upsert=True,
    )


def get_saved_response(participant_id, scenario_name):
    collection = db["responses"]
    result = collection.find_one(
        {"participant_id": participant_id, "scenario_name": scenario_name}
    )
    return result["response"] if result else None


def send_response(participant_id, scenario_name):
    collection = db["sent_responses"]
    response = get_saved_response(participant_id, scenario_name)
    collection.update_one(
        {
            "participant_id": participant_id,
            "scenario_name": scenario_name,
        },
        {
            "$set": {
                "response": response,
                "sent_at": datetime.now(),
            }
        },
        upsert=True,
    )


def get_sent_response(participant_id, scenario_name):
    collection = db["sent_responses"]
    result = collection.find_one(
        {"participant_id": participant_id, "scenario_name": scenario_name}
    )
    return result["response"] if result else None


@set_styles
def scenario(
    email_sender,
    email_sender_email,
    email_subject,
    email_content,
    scenario_name,
):
    participant_id = st.session_state.participant_id

    st.markdown(
        f"""
        <div class='email-subject'>Subject: {email_subject}</div>
        """,
        unsafe_allow_html=True,
    )

    icon, content = st.columns([1, 14])
    icon.image("images/icon.png")
    content.markdown(
        f"<div class='email-sender'>{email_sender} <span class='email-sender-email' style='margin-left: 2px;'>{email_sender_email}</span></div>",
        unsafe_allow_html=True,
    )
    content.markdown(
        f"<div class='email-content'>{email_content}</div>",
        unsafe_allow_html=True,
    )
    if (sent_response := get_sent_response(participant_id, scenario_name)) is not None:
        icon, content = st.columns([1, 14])
        icon.image("images/icon.png")
        content.markdown(
            "<div class='email-sender'>You <span class='email-sender-email' style='margin-left: 2px;'>you@emoai.com</span></div>",
            unsafe_allow_html=True,
        )
        content.markdown(
            f"<div class='email-content'>{sent_response}</div>",
            unsafe_allow_html=True,
        )
    elif get_saved_response(participant_id, scenario_name) is not None:
        icon, content = st.columns([1, 14])
        icon.image("images/icon.png")

        response = get_saved_response(participant_id, scenario_name)
        content.text_area(
            "Reply",
            height=250,
            value=response,
            label_visibility="hidden",
            key=f"reply_text_area_{participant_id}_{scenario_name}",
            on_change=save_response(participant_id, scenario_name),
        )
        if content.button(
            "Send",
            key="send_button",
        ):
            send_response(participant_id, scenario_name)
            st.rerun()
    else:
        if content.button(
            "Reply",
            key="reply_button",
        ):
            save_response(participant_id, scenario_name, signature)
            st.rerun()
