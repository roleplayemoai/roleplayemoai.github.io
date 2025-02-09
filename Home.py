import streamlit as st

from utils import set_styles

st.set_page_config(
    page_title="EmoAI Ethics",
    page_icon="🍀",
    layout="wide",
)


@set_styles
def main():
    st.markdown(
        "<div style='font-size: 20px;'>Hello, world!</div>", unsafe_allow_html=True
    )
    if "participant_id" not in st.session_state:
        st.session_state.participant_id = st.query_params["participant"]


if __name__ == "__main__":
    main()
