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

I'm reaching out from the HR Company regarding a concern with the Emotion AI software we use for evaluating candidates during video interviews.

Recently, a candidate raised a complaint on social media, alleging that the AI software may be biased toward male candidates. Upon reviewing the situation, we conducted internal testing and found that female participants consistently received lower scores than their male counterparts. This raises serious concerns about the fairness and credibility of our application.

Ensuring an unbiased hiring process is critical to our integrity and reputation with clients and candidates. We would appreciate your prompt response and collaboration in addressing this issue effectively.

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
        "images/SocialMediaPost.svg",
        "Scenario 1",
    )
