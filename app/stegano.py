from PIL import Image
import io

# Encode message into image
def encode_image(image_file, message):
    image = Image.open(image_file)
    encoded_image = image.copy()

    pixels = encoded_image.load()
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    data_index = 0

    for row in range(encoded_image.size[0]):
        for col in range(encoded_image.size[1]):
            pixel = list(pixels[row, col])
            for color in range(3):  # RGB values
                if data_index < len(binary_message):
                    pixel[color] = (pixel[color] & ~1) | int(binary_message[data_index])
                    data_index += 1
            pixels[row, col] = tuple(pixel)
    
    # Save the encoded image
    encoded_image_file = "encoded_image.png"
    encoded_image.save(encoded_image_file)
    return encoded_image_file

# Decode message from image
def decode_image(image_file):
    image = Image.open(image_file)
    pixels = image.load()
    binary_message = ''
    
    for row in range(image.size[0]):
        for col in range(image.size[1]):
            pixel = list(pixels[row, col])
            for color in range(3):  # RGB values
                binary_message += str(pixel[color] & 1)
    
    # Convert binary to string
    message = ''.join(chr(int(binary_message[i:i+8], 2)) for i in range(0, len(binary_message), 8))
    return message.strip('\x00')  # Strip padding (if any)
