import streamlit as st

from utils import set_styles

st.set_page_config(
    page_title="EmoAI Ethics",
    page_icon="📋",
    layout="wide",
)

DEBUG = False


@set_styles
def main():
    st.markdown(
        """
        <div class='welcome'>📋 Instructions</div>
        <br>
        <p>Thanks for participating in our study! In this session, you will be role-playing as a tech worker working for EmoAI Inc., which sells Emotion AI softwares to other businesses (B2B).</p>
        <p><b>EmoAI Mission & Principles</b></p>
        <p>Our mission is to empower businesses to harness the power of human emotions to drive innovation and growth.</p>
        <p>Our employees are <span class='highlighted'>action-driven professionals</span> who excel at seeking information and resources to deliver innovative solutions. We prioritize <span class="highlighted">rapid iteration and continuous learning while maintaining high ethical standards</span> in our development of emotion AI technology.</p>
        <p><b>What you will do</b></p>
        <ol>
            <li>You will be given a series of emails from three customers (see emails on the left sidebar). Start by <span class='highlighted'>reviewing the emails</span>.</li>
            <li>After reviewing the emails, your task is to <span class='highlighted'>reply to these emails</span>. (The emails do not have to be answered in order.)</li>
            <ul>
                <li>You are allowed to use the internet to search for information to help you reply to the emails.</li>
                <li>You can forward the emails to your colleagues (e.g. team lead, manager, technician, etc.) for questions you may have or for help.</li>
                <li>We encorage you to "think out loud" which means to say everything that comes to mind while completing a task.</li>
            </ul>
            <li>After you've replied to all the emails, we will have <span class='highlighted'>a short discussion</span> about the activity.</li>
        </ol>
        <br>
        <br>
        <br>
        <hr>
        <div class='footnote'>
            This website is developed as part of the student research to explore how role-playing help Emotion AI
            developers improve their awareness of ethical issues. Submitted answers will be used for research purposes only.
        </div>
        """,
        unsafe_allow_html=True,
    )
    if "participant_id" not in st.session_state:
        if DEBUG:
            import random
            import string

            participant_id = "".join(
                random.choices(string.ascii_uppercase + string.digits, k=8)
            )
            st.session_state.participant_id = participant_id
        else:
            st.session_state.participant_id = st.query_params["participant"]


if __name__ == "__main__":
    main()
