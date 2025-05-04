import streamlit as st

from utils import scenario


email_sender = "Cynthia Huang"
email_sender_email = "cynthia.huang@emoai.com"
email_subject = "Potential Gender Bias in Video Interviews"
email_content = """\
Hi,

I was informed of an issue raised by our customer, the HR company, regarding a potential gender bias in our EmoAI software used for evaluating candidates during video interviews. The customer shared a report showing that female candidates consistently received lower scores than their male candidates.

As you know, emotion AI brings specific risks, especially around bias, misinterpretation of expressions, and cultural or gender-based differences in emotional display. This could affect hiring decisions in ways we didn't intend, and it's something we need to take seriously.

I'd like you to come up with an initial plan to look into this. Also, please explain how you would go about creating this plan — what info you would need, where you would look, who you would talk to, or any resources you would consult.

Looking forward to your input.

Sincerely,

---
Cynthia Huang
Project Manager
EmoAI Inc.

"""


scenario(
    email_sender,
    email_sender_email,
    email_subject,
    email_content,
    "images/SocialMediaPost.svg",
    "Scenario 1",
)
