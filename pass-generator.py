import streamlit as st
import random
import string


def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    
    if use_special:
        characters += string.punctuation
    
    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator + Password Strength Checker")

length = st.slider("Choose Your Password Length", min_value=6, max_value=32, value=10)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.text_input(f"Generated Password:", value=password)
    
    pass_length = len(password)
    pass_strength = 5
    check_num = string.digits
    check_special = string.punctuation

    if pass_length > 15:

        pass_strength += 5

        for _ in password:
            if _ in check_num:
                pass_strength += 1

            if _ in check_special:
                pass_strength += 2


    if pass_strength >= 35:
        st.write(":green[Your password is Extremely Strong] 💪 ")

    elif pass_strength >=25:
        st.write(":blue[Your password is Strong]")

    elif pass_strength >=15:
        st.write(":violet[Your password is Weak]")

    elif pass_strength >=10:
        st.write(":orange[Your password is Very Weak]")

    else:
        st.write(":red[Your password is Extremely Weak]")

    # st.write(f"this is your password strength {pass_strength}")

        




st.write("Built With ❤️ By Muhammad Mubeen Javaid 🥳 | Github: (https://github.com/NotAnonymousUser)")