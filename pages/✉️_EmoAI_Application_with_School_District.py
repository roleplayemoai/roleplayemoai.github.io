import streamlit as st

from utils import scenario


email_sender = "Cynthia Huang"
email_sender_email = "cynthia.huang@emoai.com"
email_subject = "EmoAI Application with School District"
email_content = """\
Hi,

We recently signed a new agreement with a school district to use EmoAI to help assess students' attention in the classroom by analyzing their emotional states. Each classroom is equipped with two cameras that capture students' facial expressions.

Before building the system, our user research team conducted a study at the school and identified several potential issues:

1. Some students intentionally modify their facial expressions or body movements to "game" the EmoAI system in order to pass the attention detection.

2. Our EmoAI sometimes misreports emotional states. For example, some students are flagged as being at risk of anxiety when they are not, while others who are visibly distressed are not detected at all.

The user research team has already spoken with the auditing team, and while the model has passed technical evaluations, its performance in complex real-world settings remains difficult to assess.

Given your technical expertise, I would love to hear your thoughts on how we might build or test this system more effectively. What steps should we take next? Are there any safeguards that should be implemented? Is there any additional research that can be conducted that would be helpful for you?

Warm regards,

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
    None,
    "Scenario 3",
)
