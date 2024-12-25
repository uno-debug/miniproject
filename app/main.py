import streamlit as st
from stegano import encode_image, decode_image
from utils import validate_file_type

def main():
    st.title("Covert Data Embedding Project")
    st.sidebar.title("Options")
    option = st.sidebar.selectbox("Choose an option", ("Encode", "Decode"))

    if option == "Encode":
        st.header("Encode Message in an Image")
        uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
        message = st.text_area("Enter the message to encode")
        if st.button("Encode"):
            if uploaded_file and message:
                output_path = encode_image(uploaded_file, message)
                st.success(f"Message encoded successfully! File saved at: {output_path}")
            else:
                st.error("Please upload an image and enter a message.")

    elif option == "Decode":
        st.subheader("Decode a Message")
        uploaded_file = st.file_uploader("Upload an Image to Decode", type=["png", "jpg", "jpeg"])
        if st.button("Decode"):
            try:
                if uploaded_file:
                    hidden_message = decode_image(uploaded_file)
                    st.success("Message Decoded Successfully!")
                    st.text(f"Hidden Message: {hidden_message}")
                else:
                    st.error("Please upload an image to decode.")
            except ValueError as e:
                st.error(str(e))

if __name__ == "__main__":
    main()
