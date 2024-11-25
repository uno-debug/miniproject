import streamlit as st
from stegano import encode_image, decode_image
import os

# Streamlit user interface
def main():
    st.title("Steganography with LSB Encoding")

    # Upload an image for encoding
    uploaded_image = st.file_uploader("Choose an image to encode message", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_image is not None:
        # Show the uploaded image
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        # Get the message to encode
        message = st.text_area("Enter message to encode")

        if st.button("Encode Message"):
            if message:
                image_path = os.path.join('resources', 'test_images', uploaded_image.name)
                with open(image_path, "wb") as f:
                    f.write(uploaded_image.getbuffer())

                output_path = os.path.join('resources', 'output_files', f"encoded_{uploaded_image.name}")
                encode_image(image_path, message, output_path)
                st.success(f"Message successfully encoded! Check the encoded image here:")
                st.image(output_path, caption="Encoded Image", use_column_width=True)

    # Decoding Section
    uploaded_encoded_image = st.file_uploader("Choose an encoded image to decode message", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_encoded_image is not None:
        st.image(uploaded_encoded_image, caption="Uploaded Encoded Image", use_column_width=True)
        
        if st.button("Decode Message"):
            image_path = os.path.join('resources', 'output_files', uploaded_encoded_image.name)
            with open(image_path, "wb") as f:
                f.write(uploaded_encoded_image.getbuffer())

            decoded_message = decode_image(image_path)
            if decoded_message:
                st.success(f"Decoded Message: {decoded_message}")
            else:
                st.warning("No message found in this image!")

if __name__ == "__main__":
    main()
