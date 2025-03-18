import streamlit as st

from utils import scenario

st.set_page_config(
    page_title="EmoAI Ethics",
    page_icon="✉️",
    layout="wide",
)


email_sender = "Josep Garcés"
email_sender_email = "jc2563@HealthcareProvider.com"
email_subject = "Concerns About Accuracy of Emotion AI for Mental Health Assessments"
email_content = """\
Dear EmoAI Customer Support Team,

I'm writing on behalf of Healthcare Provider regarding some concerns raised about the Emotion AI software we use to assess mental health conditions.

Recently, some of our users have reported that Emotion AI sometimes incorrectly identifies their emotions—for example, falsely reporting anxiety when they are not. We've since received similar feedback from other users, questioning both the accuracy and the sensitivity of the assessments.

Given our commitment to providing supportive and trustworthy mental health services, we need to address these issues urgently. We would appreciate your clarification regarding this matter, as it is critical to maintaining our users' confidence in our digital healthcare solutions.

Sincerely,

---
Josep Garcés
Chief Operating Officer
Healthcare Provider

"""

if __name__ == "__main__":
    scenario(
        email_sender,
        email_sender_email,
        email_subject,
        email_content,
        None,
        "Scenario 3",
    )
