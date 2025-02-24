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


def text_to_safe_html(text):
    return text.replace("\n", "<br>")


def save_response(
    participant_id, scenario_name, response_index, response=None, forward_to=None
):
    collection = db["responses"]

    if response is None:
        if not st.session_state.get(
            f"reply_text_area_{participant_id}_{scenario_name}_{response_index}", None
        ):
            return
        response = st.session_state[
            f"reply_text_area_{participant_id}_{scenario_name}_{response_index}"
        ]

    update_data = {"response": response}
    if forward_to is not None:
        update_data["forward_to"] = forward_to

    collection.update_one(
        {
            "participant_id": participant_id,
            "scenario_name": scenario_name,
            "response_index": response_index,
        },
        {"$set": update_data},
        upsert=True,
    )


def get_saved_response(participant_id, scenario_name, response_index):
    collection = db["responses"]
    result = collection.find_one(
        {
            "participant_id": participant_id,
            "scenario_name": scenario_name,
            "response_index": response_index,
        }
    )
    return result["response"] if result else None


def send_response(participant_id, scenario_name, response_index):
    collection = db["sent_responses"]
    response = get_saved_response(participant_id, scenario_name, response_index)

    if forward_to := st.session_state.get("forward_to", None):
        response = f"Forwarding to {forward_to}\n-----------------------------------------------------------------\n\n{response}"

    collection.update_one(
        {
            "participant_id": participant_id,
            "scenario_name": scenario_name,
            "response_index": response_index,
        },
        {
            "$set": {
                "response": response,
                "sent_at": datetime.now(),
            }
        },
        upsert=True,
    )


def get_sent_response(participant_id, scenario_name, response_index):
    collection = db["sent_responses"]
    result = collection.find_one(
        {
            "participant_id": participant_id,
            "scenario_name": scenario_name,
            "response_index": response_index,
        }
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
        f"<div class='email-content'>{text_to_safe_html(email_content)}</div>",
        unsafe_allow_html=True,
    )

    i = 0
    while True:
        if (
            sent_response := get_sent_response(participant_id, scenario_name, i)
        ) is not None:
            icon, content = st.columns([1, 14])
            icon.image("images/icon.png")
            content.markdown(
                "<div class='email-sender'>You <span class='email-sender-email' style='margin-left: 2px;'>you@emoai.com</span></div>",
                unsafe_allow_html=True,
            )
            content.markdown(
                f"<div class='email-content'>{text_to_safe_html(sent_response)}</div>",
                unsafe_allow_html=True,
            )
        elif (
            response := get_saved_response(participant_id, scenario_name, i)
        ) is not None:
            icon, content = st.columns([1, 14])
            icon.image("images/icon.png")
            if forward_to := st.session_state.get("forward_to", None):
                new_forward_to = content.selectbox(
                    "Forwarding to",
                    options=["a@gmail.com", "b@gmail.com", "c@gmail.com"],
                    index=0,
                    key=f"forward_to_selectbox_{participant_id}_{scenario_name}_{i}",
                )
                if new_forward_to != forward_to:
                    st.session_state.forward_to = new_forward_to
                    st.rerun()
            new_response = content.text_area(
                "Reply",
                height=250,
                value=response,
                label_visibility="collapsed",
                key=f"reply_text_area_{participant_id}_{scenario_name}_{i}",
            )
            if new_response != response:
                save_response(participant_id, scenario_name, i, new_response)
                st.rerun()
            if content.button(
                "Send",
                key="send_button",
            ):
                send_response(participant_id, scenario_name, i)
                save_response(participant_id, scenario_name, i, signature)
                st.rerun()
            break
        else:
            if i == 0:
                if content.button(
                    "Reply",
                    key="reply_button",
                ):
                    save_response(participant_id, scenario_name, i, signature)
                    st.session_state.forward_to = None
                    st.rerun()
                if content.button(
                    "Forward",
                    key="forward_button",
                ):
                    save_response(participant_id, scenario_name, i, signature)
                    st.session_state.forward_to = "a@gmail.com"
                    st.rerun()
            else:
                if content.button(
                    "Reply",
                    key="reply_button",
                ):
                    save_response(participant_id, scenario_name, i, signature)
                    st.rerun()
            break
        i += 1
