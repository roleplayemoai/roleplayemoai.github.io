import streamlit as st

from utils import scenario

st.set_page_config(
    page_title="EmoAI Ethics",
    page_icon="✉️",
    layout="wide",
)


email_sender = "Josep Garcés"
email_sender_email = "josep.garces@emoai.com"
email_subject = "EmoAI Application for Mental Health Assessment"
email_content = """\
We recently signed a new agreement with a health care provider to use EmoAI to help assess patients' mental health by analyzing their emotional states. Before building the system, our user research team conducted a study and observed that the Emotion AI system can sometimes make incorrect emotional assessments in mental health contexts.

For instance, some users have reported being labeled as anxious when they were not experiencing anxiety. While such misjudgments may be minor in some situations, in other cases they can significantly impact the perceived reliability of the product. One particularly serious concern is when users experience depressive episodes that the system fails to detect and report in time.

Given your technical expertise, we would love to hear your thoughts on how we might build or test this system more effectively. What steps should we take next? Are there any safeguards that should be implemented? Is there any additional research we can conduct that would be helpful for you?

To that end, I'd like to propose a meeting where you could contribute as an expert voice. Please prepare any relevant materials you think would be useful for discussion. And of course, if there's anything I can support you with in advance, don't hesitate to reach out.

Warm regards,

---
Josep Garcés
UX Researcher
EmoAI Inc.

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
