import streamlit as st

from utils import set_styles

st.set_page_config(
    page_title="EmoAI Today Journal | Role Playing Emotion AI Research",
    page_icon="🚨",
    layout="centered",
)

DEBUG = False


@set_styles
def main():
    st.markdown(
        """
        <p><b>🚨 EmoAI Today Journal</b></p>
        <h2>Leading IT Company Employees Protest Emotion-Scanning AI in Workplace</h2>
        <p><i>By Rosie Anderson</i></p>
        """,
        unsafe_allow_html=True,
    )
    st.image("images/News.jpg", width=650)
    st.markdown(
        """
        <p><b>Tech workers voice concerns over invasive monitoring system that scans facial expressions and emotions during work hours and meetings.</b></p>
        <p>Employees at Leading IT Company have expressed serious privacy and ethical concerns after internal documents revealed plans to implement an emotion-scanning AI system to monitor workers during their daily activities and meetings.</p>
        <p>The controversial technology, which would analyze facial expressions, voice patterns, and other biometric data to evaluate "mental well-being" and job performance, was detailed in communications between the company and EmoAI, a provider of emotion recognition software.</p>
        <p>"This crosses a fundamental line between professional oversight and invasive surveillance," said one senior developer who requested anonymity. "Many of us feel this technology could create a hostile work environment where we're constantly anxious about being judged not just on our work output, but on our facial expressions during meetings."</p>
        <p>Company leadership has yet to respond to the growing employee concerns, which include questions about data security, algorithmic bias, and the scientific validity of emotion recognition technology itself.</p>
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
