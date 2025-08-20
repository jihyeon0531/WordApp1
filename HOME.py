import streamlit as st

st.markdown("### Welcome to Ms.Choi's English Classroo")
st.caption("Since Aug 20, 2025")

# Image links
main_image_url = "https://github.com/jihyeon0531/WordApp/raw/main/images/welcome3.png"
qr_image_url = "https://github.com/jihyeon0531/WordApp/raw/main/images/wordapp1.png"

# Use columns to center images
col1, col2, col3 = st.columns([1, 2, 1])  # middle column bigger

with col1:
    st.image(main_image_url, width=500, caption="Welcome Image")  # Expand button appears
with col3:
    st.image(qr_image_url, width=50, caption="QR")  # Expand button appears
