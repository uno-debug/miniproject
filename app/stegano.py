from PIL import Image
import numpy as np

def encode_image(input_image_path, output_image_path, secret_message):
    """
    Encodes a secret message into an image using LSB steganography.
    """
    try:
        # Open the input image
        img = Image.open(input_image_path)
        img_array = np.array(img)

        # Convert the secret message into binary
        binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
        binary_message += '1111111111111110'  # Delimiter to mark the end of the message

        # Check if the message can fit in the image
        total_pixels = img_array.size
        if len(binary_message) > total_pixels:
            raise ValueError("Message is too large to fit in the image!")

        # Flatten the image array to manipulate pixel values
        flat_array = img_array.flatten()

        # Modify the LSB of each pixel to encode the message
        for i in range(len(binary_message)):
            flat_array[i] = (flat_array[i] & ~1) | int(binary_message[i])

        # Reshape the modified array back to the original shape and save it
        encoded_array = flat_array.reshape(img_array.shape)
        encoded_image = Image.fromarray(encoded_array.astype('uint8'))
        encoded_image.save(output_image_path)

        return "Message successfully encoded into the image!"
    except Exception as e:
        return f"Error: {e}"


def decode_image(encoded_image_path):
    """
    Decodes and extracts the secret message from an image.
    """
    try:
        # Open the encoded image
        img = Image.open(encoded_image_path)
        img_array = np.array(img).flatten()

        # Extract the LSBs to reconstruct the binary message
        binary_message = ''.join(str(pixel & 1) for pixel in img_array)

        # Split the binary message into chunks of 8 bits and convert to characters
        chars = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
        secret_message = ''.join(chr(int(char, 2)) for char in chars)

        # Stop decoding when the delimiter is reached
        delimiter_index = secret_message.find(chr(255) + chr(255))
        if delimiter_index != -1:
            secret_message = secret_message[:delimiter_index]

        return secret_message
    except Exception as e:
        return f"Error: {e}"
