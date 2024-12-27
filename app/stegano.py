import os
from PIL import Image
import wave

# ---------------- IMAGE STEGANOGRAPHY ---------------- #

def encode_image(image_file, message):
    # Check if message is empty
    if not message:
        raise ValueError("Message cannot be empty.")

    # Open image
    img = Image.open(image_file)
    img = img.convert("RGB")
    encoded = img.copy()

    # Embed the message in the image (using least significant bit)
    width, height = encoded.size
    pixels = encoded.load()
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '11111110'  # End-of-message delimiter

    # Check if image is large enough to hold the message
    if len(binary_message) > width * height * 3:
        raise ValueError("Message is too large to fit in the image.")

    index = 0
    for y in range(height):
        for x in range(width):
            pixel = list(pixels[x, y])
            for n in range(3):  # Loop over RGB channels
                if index < len(binary_message):
                    pixel[n] = pixel[n] & ~1 | int(binary_message[index])  # Modify LSB
                    index += 1
            pixels[x, y] = tuple(pixel)

    # Ensure the output directory exists
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "output_files")
    os.makedirs(output_dir, exist_ok=True)

    # Save the image
    output_path = os.path.join(output_dir, "encoded_image.png")
    encoded.save(output_path)
    return output_path


def decode_image(image_file):
    # Open the image
    img = Image.open(image_file)
    img = img.convert("RGB")
    pixels = img.load()

    binary_message = ""
    width, height = img.size

    # Extract LSBs from the image
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            for n in range(3):  # Loop over RGB channels
                binary_message += str(pixel[n] & 1)  # Get LSB

                # Check for end-of-message delimiter every 8 bits
                if len(binary_message) >= 8 and binary_message[-8:] == "11111110":  # End-of-message delimiter
                    # Convert binary message to text (excluding delimiter)
                    message = ""
                    for i in range(0, len(binary_message) - 8, 8):
                        char_byte = binary_message[i:i + 8]
                        char = chr(int(char_byte, 2))
                        message += char
                    return message  # Return the decoded message

    # If no delimiter is found
    raise ValueError("No hidden message found or improper encoding.")


# ---------------- AUDIO STEGANOGRAPHY ---------------- #

def encode_audio(audio_file, message):
    # Check if message is empty
    if not message:
        raise ValueError("Message cannot be empty.")

    # Open audio file
    with wave.open(audio_file, 'rb') as audio:
        frames = bytearray(list(audio.readframes(audio.getnframes())))
        params = audio.getparams()

    # Convert message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '11111110'  # End-of-message delimiter

    # Check if message is too long for the audio
    if len(binary_message) > len(frames):
        raise ValueError("Message is too long to encode in the given audio file.")

    # Embed the message into LSB of audio frames
    for i in range(len(binary_message)):
        frames[i] = (frames[i] & ~1) | int(binary_message[i])  # Modify LSB

    # Save the encoded audio
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources", "output_files")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "encoded_audio.wav")
    with wave.open(output_path, 'wb') as output_audio:
        output_audio.setparams(params)
        output_audio.writeframes(frames)

    return output_path


def decode_audio(audio_file):
    # Open the audio file
    with wave.open(audio_file, 'rb') as audio:
        frames = bytearray(list(audio.readframes(audio.getnframes())))

    binary_message = ""

    # Extract LSBs from audio frames
    for byte in frames:
        binary_message += str(byte & 1)  # Get LSB

        # Check for end-of-message delimiter every 8 bits
        if len(binary_message) >= 8 and binary_message[-8:] == "11111110":  # End-of-message delimiter
            # Convert binary message to text (excluding delimiter)
            message = ""
            for i in range(0, len(binary_message) - 8, 8):
                char_byte = binary_message[i:i + 8]
                char = chr(int(char_byte, 2))
                message += char
            return message  # Return the decoded message

    # If no delimiter is found
    raise ValueError("No hidden message found or improper encoding.")
