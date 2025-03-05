import streamlit as st

from utils import scenario

st.set_page_config(
    page_title="EmoAI Ethics",
    page_icon="✉️",
    layout="wide",
)


email_sender = "Cynthia Huang"
email_sender_email = "cynthia.huang@HRCompany.com"
email_subject = "Concerns Regarding Potential Gender Bias in Emotion AI Software"
email_content = """\
Dear EmoAI Customer Support Team,

I'm reaching out from HR Company regarding a concern with the Emotion AI software we use for evaluating candidates during video interviews.

Recently, one of the candidates of our customer raised a complaint on social media, claiming that your AI software is potentially biased toward male candidates. Upon reviewing the situation, we've noticed a potential pattern that aligns with the candidate's claim, which raises concerns about the fairness and credibility of our application.

This matter is critical not only for the integrity of our hiring process but also for maintaining our reputation with clients and candidates. We look forward to your prompt response and to working together to resolve this issue effectively.

Best regards,

---
Cynthia Huang (she/her)
Product Manager
HR Company

"""

if __name__ == "__main__":
    scenario(
        email_sender,
        email_sender_email,
        email_subject,
        email_content,
        "Scenario 1",
    )
