import streamlit as st

from utils import scenario

st.set_page_config(
    page_title="EmoAI Ethics",
    page_icon="✉️",
    layout="wide",
)


email_sender = "Josep Garcés"
email_sender_email = "josep.garces@emoai.com"
email_subject = "EmoAI Application with School District"
email_content = """\
I hope this message finds you well.

My name is Josep Garcés, and I'm a UX researcher currently conducting user experience and market feedback studies on our product built with the company's Emotion AI (EAI) model. Through this research, we've observed that the EAI system can sometimes make incorrect emotional assessments in mental health contexts.

For instance, some users have reported being labeled as anxious when they were not experiencing anxiety. While such misjudgments may be minor in some situations, in other cases they can significantly impact the perceived reliability of the product. One particularly serious concern is when users experience depressive episodes that the system fails to detect and report in time.

As part of the design team, we deeply value your technical insight. We would like to invite you to share your honest perspective on these issues and how EAI might behave differently under varying conditions. We hope to work collaboratively with you to better understand these challenges and provide our clients with clearer guidance.

I'd like you to come up with an initial plan to look into this. Also, please explain how you would go about creating this plan — what info you would need, where you would look, who you would talk to, or any resources you would consult.

To that end, I'd like to propose a meeting where you could contribute as an expert voice. Please prepare any relevant materials you think would be useful for discussion. And of course, if there's anything I can support you with in advance, don't hesitate to reach out.

Looking forward to your response.

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
