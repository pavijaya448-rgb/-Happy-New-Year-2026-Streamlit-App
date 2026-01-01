import streamlit as st

# App title
st.set_page_config(page_title="Happy New Year 2026 🎉", layout="centered")

st.title("🎆 Happy New Year 2026 🎆")

# Name input
name = st.text_input("Enter your name:")

# Button action
if st.button("🎉 Send Wishes"):
    if name:
        st.success(f"✨ Happy New Year 2026, {name}! ✨")

        # Message shown AFTER wish
        st.write("🌟 May this New Year bring you happiness, success, and new opportunities.")
        st.write("🎊 May all your dreams come true in 2026!")
        st.write("💫 Wishing you health, peace, and prosperity.")

        st.balloons()
    else:
        st.warning("Please enter your name 😊")

