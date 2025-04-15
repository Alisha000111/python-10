import streamlit as st
from cryptography.fernet import Fernet
st.title("Secure Data Encryption System😊")
st.write("Encrypt/decrypt your sensitive data securely❤️")
key = Fernet.generate_key()
cipher = Fernet(key)
data = st.text_input("Enter your secret message:😊")
if st.button("Encrypt❤️"):
    encrypted = cipher.encrypt(data.encode())
    st.text("Encrypted Message:😊")
    st.code(encrypted.decode())
if st.button("Decrypt❤️"):
    try:
        decrypted = cipher.decrypt(data.encode()).decode()
        st.text("Original Message:😊")
        st.success(decrypted)
    except:
        st.error("Invalid input. Please enter encrypted data❤️")