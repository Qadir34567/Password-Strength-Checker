import streamlit as st
import re

st.title(" Ultimate Password Strength Checker")

st.markdown("""
    Welcome to the **Ultimate Password Strength Checker!**
    Ensure your password is secure by checking:
    - ✅ Length
    - ✅ Upper & Lowercase letters
    - ✅ Numbers
    - ✅ Special characters
    Improve your online privacy by creating strong passwords!""")

password = st.text_input("Enter your password:", type="password")

def check_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Include both uppercase and lowercase letters.")

    # Check for numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number (0-9).")

    # Check for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (!@#$%^&*).")

    return score, feedback

# Button to Check Password
if st.button("Check Password Strength"):
    if password:
        score, feedback = check_password_strength(password)

        st.subheader("Password Strength Result:")

        if score == 4:
            st.success("Strong Password! Your password is secure.")
        elif score == 3:
            st.warning("Moderate Password - Consider adding more security features.")
        else:
            st.error("Weak Password - Improve it using the suggestions below.")
        
        if feedback:
            st.info("Suggestions to improve your password:")
            for tip in feedback:
                st.write(tip)
    else:
        st.error("Please enter a password to check.")

st.markdown(""" 
    Made with by ❤ Abdul Qadir
""")
