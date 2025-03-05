import streamlit as st

from utils import set_styles

st.set_page_config(
    page_title="EmoAI Ethics",
    page_icon="🤖",
    layout="wide",
)

DEBUG = False


@set_styles
def main():
    col1, mid, col2 = st.columns([5,0.5,4])
    with col1:
        st.markdown(
        """
        <div class='welcome'>👋 Welcome to EmoAI Inc.</div>
        <p>We are a B2B company that provides Emotion AI software to <span style="background-color: #fff1ab;">help businesses analyze facial expressions, voice tone, and body language to detect human emotions</span>.</p>
        <p>Our AI solutions are designed to engage with humans and enable any industry to benefit from the insights of human emotions.</p>
        """,
        unsafe_allow_html=True,
        ) 
    with col2:
        st.image('images/EmoAI.png')

    st.markdown(
        """
        <div class='section'>Mission & Principles</div>
        <p>Our mission is to empower businesses to harness the power of human emotions to drive innovation and growth.</p>
        <p>
            Our employees are action-driven professionals who excel at seeking information and resources to deliver innovative solutions. 
            We prioritize rapid iteration and continuous learning while maintaining high ethical standards in our development of emotion AI technology.
        </p>
        <div class='section'>Our Customers</div>
        <p>
            We are trusted by customers across various industries, including Healthcare, HR, IT Services, and more.
        </p>
        """,
        unsafe_allow_html=True,
    )
    col1_, col2_, col3_, col4_ = st.columns([2,2,2,5])
    with col1_:
        st.image('images/Logo-1.png')
    with col2_:
        st.image('images/Logo-2.png')
    with col3_:
        st.image('images/Logo-3.png')
    st.markdown(
        """
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
