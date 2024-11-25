import streamlit as st
from stegano import encode_image, decode_image
from utils import validate_file

def main():
    st.title("Covert Data Embedding Project")
    
    st.subheader("Image Steganography")
    
    # Upload Image and Message
    uploaded_image = st.file_uploader("Choose an image to embed data", type=["png", "jpg", "jpeg"])
    message = st.text_area("Enter the message to hide in the image")
    
    if uploaded_image and message:
        if st.button("Embed Message in Image"):
            if validate_file(uploaded_image):
                encoded_image = encode_image(uploaded_image, message)
                st.image(encoded_image, caption="Image with hidden message", use_column_width=True)
                st.success("Message successfully embedded!")
    
    # Decode Hidden Message
    st.subheader("Decode Message from Image")
    uploaded_image_to_decode = st.file_uploader("Choose an image to decode message", type=["png", "jpg", "jpeg"])
    
    if uploaded_image_to_decode:
        if st.button("Extract Message from Image"):
            decoded_message = decode_image(uploaded_image_to_decode)
            if decoded_message:
                st.text_area("Hidden Message", decoded_message)
            else:
                st.warning("No hidden message found!")

if __name__ == "__main__":
    main()
