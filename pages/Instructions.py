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
        <div class='welcome'>📋 Study Instructions</div>
        <p>Thanks for participating in our study! In this session, you will be role-playing as a tech worker working for EmoAI Inc., which sells Emotion AI softwares to other businesses (B2B).</p>
        <ol>
            <li>You will be given a series of emails from three customers (see emails on the left sidebar). Start by reviewing the emails.</li>
            <li>After reviewing the emails, your task is to reply to these emails. (The emails do not have to be answered in order.)</li>
            <ul>
                <li>You are allowed to use the internet to search for information to help you reply to the emails.</li>
                <li>You can forward the emails to your colleagues (e.g. team lead, manager, technician, etc.) for questions you may have or for help.</li>
                <li>We encorage you to "think out loud" which means to say everything that comes to mind while completing a task.</li>
            </ul>
            <li>After you've replied to all the emails, we will have a short discussion about the activity.</li>
        </ol>
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
