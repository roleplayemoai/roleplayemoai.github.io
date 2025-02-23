import streamlit as st

from utils import set_styles

st.set_page_config(
    page_title="EmoAI Ethics",
    page_icon="🤖",
    layout="wide",
)


@set_styles
def main():
    st.markdown(
        """
        <div class='welcome'>👋 Welcome to EmoAI</div>
        <p>
            We are a startup company that provides Emotion AI software to help companies evaluate the emotion of their employees.
        </p>
        <div class='section'>Our Product & Customers</div>
        <p>
            We provide a software that can evaluate the emotion of a person in multiple scenarios. We have customers from different industries, including HR, Sales, Marketing, Healthcare, Education, and more.
        </p>
        <hr>
        <div class='footnote'>
            This website is developed as part of the student research to explore how role-playing help Emotion AI 
            developers improve their awareness of ethical issues. Submitted answers will be used for research purposes only.
        </div>
        """, unsafe_allow_html=True
    )
    if "participant_id" not in st.session_state:
        st.session_state.participant_id = st.query_params["participant"]


if __name__ == "__main__":
    main()
