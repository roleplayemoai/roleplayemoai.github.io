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
    st.markdown(
    """
    <div style="background-color: #1E1E1E; color: #FFFFFF; padding: 20px; border-radius: 10px;">
        <div class='welcome' style="color: #FFFFFF;">👋 Welcome to EmoAI Inc.</div>
        <p>We are a B2B company that provides Emotion AI software to help businesses analyze facial expressions, voice tone, and body language to detect human emotions. 
        Our AI solutions are designed to engage with humans and enable any industry to benefit from the insights of human emotions.</p>
    </div>
    """,
    unsafe_allow_html=True,
    )

    st.divider()
    st.subheader("Our Products")

    col1_1, mid, col2_1 = st.columns([5,0.5,4])
    with col1_1:
        st.markdown(
        """
        <div class='section'>Video EmoAI</div>
        <p>
            Our Video EmoAI allows businesses to identify emotional reactions real-time, evaluate the engagement level, and monitor the attention of the participants.
        </p>
        """,
        unsafe_allow_html=True,
        )
    
    with col2_1:
        st.image('images/VideoEmoAI.png')

    col1_2, mid, col2_2 = st.columns([5,0.5,4])
    with col1_2:
        st.markdown(
        """
        <div class='section'>Audio EmoAI</div>
        <p>
            Our Audio EmoAI helps identify the emotional cues and understand the emotional content from speech.
        </p>
        """,
        unsafe_allow_html=True,
        ) 
        
    with col2_2:
        st.image('images/AudioEmoAI.png')

    col1_3, mid, col2_3 = st.columns([5,0.5,4])
    with col1_3:
        st.markdown(
        """
        <div class='section'>Text EmoAI</div>
        <p>
            Our Text EmoAI leverages state-of-the-art natural language processing to detect and analyze a wide range of emotions in written text.
        </p>
        """,
        unsafe_allow_html=True,
        ) 
        
    with col2_3:
        st.image('images/TextEmoAI.png')

    st.markdown(
        """
        <div class='section'>Our Customers</div>
        <p>
            We are trusted by customers across various industries, including Healthcare, Human Resources, IT Services, and more.
        </p>
        """,
        unsafe_allow_html=True,
    )
    col1_, col2_, col3_, col4_ = st.columns([2,2,2,5])
    with col1_:
        st.image('images/Logo-1.svg',width=200)
    with col2_:
        st.image('images/Logo-2.svg',width=200)
    with col3_:
        st.image('images/Logo-3.svg',width=200)
    st.markdown(
        """
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
