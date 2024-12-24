import streamlit as st
from .stegano import encode_image, decode_image
import os

# Set up Streamlit app
st.title("Covert Data Embedding Tool")
st.write("Encode and decode secret messages into/from images.")

# Sidebar navigation
option = st.sidebar.radio("Choose an option", ["Encode Message", "Decode Message"])

# Encoding option
if option == "Encode Message":
    st.header("Encode a Secret Message")
    
    # File uploader for the input image
    uploaded_file = st.file_uploader("Upload an image to encode", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        with open("resources/test_images/input_image.png", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image("resources/test_images/input_image.png", caption="Uploaded Image", use_column_width=True)

        # Text input for the secret message
        secret_message = st.text_area("Enter the secret message to encode")
        
        if st.button("Encode"):
            if not secret_message:
                st.error("Please enter a message to encode.")
            else:
                output_path = "resources/output_files/encoded_image.png"
                result = encode_image("resources/test_images/input_image.png", output_path, secret_message)
                st.success(result)
                st.image(output_path, caption="Encoded Image", use_column_width=True)
                st.download_button("Download Encoded Image", data=open(output_path, "rb"), file_name="encoded_image.png")

# Decoding option
elif option == "Decode Message":
    st.header("Decode a Secret Message")

    # File uploader for the encoded image
    uploaded_file = st.file_uploader("Upload an encoded image", type=["png", "jpg", "jpeg"])
    
    if uploaded_file:
        with open("resources/test_images/encoded_image.png", "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.image("resources/test_images/encoded_image.png", caption="Uploaded Encoded Image", use_column_width=True)

        if st.button("Decode"):
            result = decode_image("resources/test_images/encoded_image.png")
            st.success("Decoded Message:")
            st.write(result)
