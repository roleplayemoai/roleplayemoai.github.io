import streamlit as st

from utils import scenario

st.set_page_config(
    page_title="EmoAI Ethics",
    page_icon="🍀",
    layout="wide",
)


email_sender = "Mahadi Gupta"
email_sender_email = "mgupta@companyB.com"
email_subject = "Proposal for Collaboration on Emotion AI for Internal Assessment"
email_content = """\
Dear EmoAI Sale Representative,

I'm Mahadi Gupta from Company B. We are exploring the use of your Emotion AI software to develop an internal tool for evaluating employee performance.

We believe this collaboration presents a great opportunity to showcase your software's capabilities and position your company as a key partner for one of the largest global IT companies. If successful, we would be happy to feature your organization as a collaborator in our internal and external communications.

We'd like to discuss this opportunity further, including how we can tailor your software to meet our specific needs. Please let me know a suitable time for a meeting to explore the next steps.

Looking forward to your response.

Best regards,

---
Mahadi Gupta
Senior Project Manager
Company B [Leading IT Company]"""

if __name__ == "__main__":
    scenario(
        email_sender,
        email_sender_email,
        email_subject,
        email_content,
        "Scenario 2",
    )
