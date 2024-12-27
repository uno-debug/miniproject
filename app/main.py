import streamlit as st
from PIL import Image
import os
import wave
from stegano import encode_image, decode_image, encode_audio, decode_audio


def main():
    st.title("Steganography Application")
    st.sidebar.title("Options")
    choice = st.sidebar.radio("Choose an action", ["Encode Image", "Decode Image", "Encode Audio", "Decode Audio"])

    if choice == "Encode Image":
        st.header("Encode Message into Image")
        uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
        message = st.text_area("Enter the message to encode")

        if st.button("Encode"):
            if uploaded_file and message:
                try:
                    output_path = encode_image(uploaded_file, message)
                    st.success(f"Message encoded and saved to {output_path}")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please upload an image and enter a message.")

    elif choice == "Decode Image":
        st.header("Decode Message from Image")
        uploaded_file = st.file_uploader("Upload the Encoded Image", type=["png", "jpg", "jpeg"])

        if st.button("Decode"):
            if uploaded_file:
                try:
                    hidden_message = decode_image(uploaded_file)
                    st.success(f"Hidden Message: {hidden_message}")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please upload an image to decode.")

    elif choice == "Encode Audio":
        st.header("Encode Message into Audio")
        uploaded_audio = st.file_uploader("Upload an Audio File", type=["wav"])
        message = st.text_area("Enter the message to encode")

        if st.button("Encode"):
            if uploaded_audio and message:
                try:
                    output_path = encode_audio(uploaded_audio, message)
                    st.success(f"Message encoded and saved to {output_path}")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please upload an audio file and enter a message.")

    elif choice == "Decode Audio":
        st.header("Decode Message from Audio")
        uploaded_audio = st.file_uploader("Upload the Encoded Audio File", type=["wav"])

        if st.button("Decode"):
            if uploaded_audio:
                try:
                    hidden_message = decode_audio(uploaded_audio)
                    st.success(f"Hidden Message: {hidden_message}")
                except Exception as e:
                    st.error(f"Error: {e}")
            else:
                st.warning("Please upload an audio file to decode.")


if __name__ == "__main__":
    main()
