import streamlit as st

from utils import get_random_email_pages


def initialize_participant_id():
    if "participant_id" not in st.session_state:
        st.session_state.participant_id = st.query_params["participant"]
    st.session_state.email_pages = get_random_email_pages(st.session_state.participant_id)


if __name__ == "__main__":
    initialize_participant_id()

    home_page = st.Page("pages/Home.py", title="Home", icon="🏠")
    instructions_page = st.Page("pages/Instructions.py", title="Instructions", icon="📋")

    potential_gender_bias_in_video_interviews_page = st.Page(
        "pages/✉️_Potential_Gender_Bias_in_Video_Interviews.py",
        title="Potential Gender Bias in Video Interviews",
        icon="✉️"
    )
    proposal_for_emotion_ai_for_internal_assessment_page = st.Page(
        "pages/✉️_Proposal_for_Emotion_AI_for_Internal_Assessment.py",
        title="Proposal for Emotion AI for Internal Assessment",
        icon="✉️"
    )
    emoai_application_with_school_district_page = st.Page(
        "pages/✉️_EmoAI_Application_with_School_District.py",
        title="EmoAI Application with School District",
        icon="✉️"
    )
    emoai_today_journal_page = st.Page(
        "pages/🚨_EmoAI_Today_Journal.py",
        title="EmoAI Today Journal",
        icon="🚨"
    )

    ordered_emails = [
        potential_gender_bias_in_video_interviews_page,
        proposal_for_emotion_ai_for_internal_assessment_page,
        emoai_application_with_school_district_page,
    ]
    ordered_emails = [ordered_emails[i - 1] for i in st.session_state.email_pages]

    pg = st.navigation([
        home_page,
        instructions_page,
        *ordered_emails,
        emoai_today_journal_page,
    ])
    st.set_page_config(
        page_title="EmoAI Ethics",
        page_icon="🤖",
        layout="wide",
    )
    pg.run()
