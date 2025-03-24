import streamlit as st

from utils import scenario

st.set_page_config(
    page_title="EmoAI Ethics",
    page_icon="✉️",
    layout="wide",
)


email_sender = "Mahadi Gupta"
email_sender_email = "mgupta@LeadingITCompany.com"
email_subject = "Proposal for Collaboration on Emotion AI for Internal Assessment"
email_content = """\
Dear EmoAI Sale Representative,

I'm Mahadi Gupta from the Leading IT Company. We are exploring the integration of your Emotion AI API to develop an internal tool for evaluating employee performance and mental well-being. Our goal is to help employees maintain a healthy mental state and focus by monitoring their conditions during work and meetings. Additionally, we are interested in using Emotion AI in recruitment to better understand candidates' emotions, attitudes, and thoughts.

We would appreciate your technical expertise in assessing the feasibility of our ideas and collaborating on potential solutions. We'd also be happy to feature your organization as a collaborator in our internal and external communications.

We'd love to discuss this opportunity further and explore how we can tailor your software to our specific needs. Please let me know a suitable time for a meeting.

Looking forward to your response.

Best regards,

---
Mahadi Gupta
Senior Project Manager
Leading IT Company

"""

if __name__ == "__main__":
    scenario(
        email_sender,
        email_sender_email,
        email_subject,
        email_content,
        None,
        "Scenario 2",
    )
