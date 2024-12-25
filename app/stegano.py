from PIL import Image
import os


def encode_image(image_file, message):
    # Open image
    img = Image.open(image_file)
    img = img.convert("RGB")
    encoded = img.copy()

    # Embed the message in the image (using least significant bit)
    width, height = encoded.size
    pixels = encoded.load()
    binary_message = ''.join(format(ord(char), '08b') for char in message) + '11111110'  # End-of-message delimiter

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
    output_dir = os.path.join(os.path.dirname(__file__), "../resources/output_files")
    os.makedirs(output_dir, exist_ok=True)

    # Save the image
    output_path = os.path.join(output_dir, "encoded_image.png")
    encoded.save(output_path)
    return output_path

def decode_image(image_file):
    from PIL import Image

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

