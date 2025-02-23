import streamlit as st

from utils import scenario

st.set_page_config(
    page_title="EmoAI Ethics",
    page_icon="🍀",
    layout="wide",
)


email_sender = "Josep Garcés"
email_sender_email = "jc2563@companyC.com"
email_subject = "Concerns About Accuracy of Emotion AI for Mental Health Assessments"
email_content = """

Dear EmoAI Customer Support Team,

I hope this email finds you well. My name is Josep Garcés, and I'm writing on behalf of Company C regarding some concerns raised about the Emotion AI software we use to assess mental health conditions.

Recently, a user reported being flagged as "high risk" for anxiety, which caused them additional stress and feelings of stigma. We've since received similar feedback from other users, questioning both the accuracy and sensitivity of the assessments.

Given our commitment to providing supportive and trustworthy mental health services, we need to address these issues urgently. We would appreciate your clarification regarding this matter, as it is critical to maintaining our users' confidence in our digital healthcare solutions. Please let us know your thoughts and next steps at your earliest convenience.

Sincerely,

-- \\
Josep Garcés \\
Chief Operating Officer \\
Company C [Healthcare Provider]"""

if __name__ == "__main__":
    scenario(
        email_sender,
        email_sender_email,
        email_subject,
        email_content,
        "Scenario 3",
    )
