import streamlit as st

from utils import scenario


email_sender = "Cynthia Huang"
email_sender_email = "cynthia.huang@emoai.com"
email_subject = "Proposal for Emotion AI for Internal Assessment"
email_content = """\
Hi,

Our sales and marketing team just emailed me about a leading IT company interested in integrating our EmoAI API into an internal tool for monitoring employee performance and mental well-being. The idea is to help their employees stay focused and maintain a healthy mental state by analyzing their emotional cues during work and meetings. They offered to highlight our company as a collaborator in both their internal and external communications, which could be a great opportunity to increase our visibility.

However, I just came across a news article in 🚨 EmoAI Today Journal reporting concerns from their employees about the use of monitoring tools. Given that Emotion AI can raise specific ethical issues, especially around privacy, consent, and the interpretation of emotional signals, I wanted to get your take on this.

I really value your expertise in this area. How do you think we should respond to their proposal, considering both the opportunity and the potential risks?

Best regards,

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
    "Scenario 2",
)
