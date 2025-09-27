import os
import streamlit as st
import pywhatkit as kit
import datetime

st.set_page_config(page_title="WhatsApp Sender", page_icon="📱", layout="centered")
st.title("📱 WhatsApp Message Sender")
st.write("Schedule a WhatsApp message easily!")

# Note for user
st.info("⚠️ Only works if WhatsApp is logged in from your default browser.")

# Input fields
phone = st.text_input("Recipient Number (with country code, e.g. +91XXXXXXXXXX)")
msg = st.text_area("Message")

now = datetime.datetime.now()
hour = st.number_input("Hour (24-hour)", min_value=0, max_value=23, value=now.hour)
minute = st.number_input("Minute", min_value=0, max_value=59, value=now.minute + 1)

if st.button("Send WhatsApp Message"):
    try:
        kit.sendwhatmsg(phone, msg, hour, minute)
        st.success("✅ WhatsApp message scheduled successfully!")

        # Auto delete pywhatkit log
        log_path = os.path.join(os.path.expanduser("~"), "PyWhatKit_DB")
        log_file = os.path.join(log_path, "PyWhatKit_DB.txt")  # ya .txt file
        if os.path.exists(log_file):
            os.remove(log_file)

    except Exception as e:
        st.error(f"Error: {e}")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Made with ❤️ by Aditya Jaiswal</p>", unsafe_allow_html=True)
