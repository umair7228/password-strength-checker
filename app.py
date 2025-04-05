import streamlit as st
import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

def strength_label(score):
    if score == 4:
        return "✅ Strong Password!", "green"
    elif score == 3:
        return "⚠️ Moderate Password - Consider improving.", "orange"
    else:
        return "❌ Weak Password - Improve it using suggestions below.", "red"

# Streamlit App UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password", type="password")

if password:
    score, feedback = check_password_strength(password)
    msg, color = strength_label(score)
    st.markdown(f"### <span style='color:{color}'>{msg}</span>", unsafe_allow_html=True)
    
    if feedback:
        st.subheader("Suggestions:")
        for item in feedback:
            st.write(item)