from PIL import Image

def encode_image(image_path, message, output_path):
    """
    Encode a message into an image using the Least Significant Bit (LSB) method.
    """
    image = Image.open(image_path)
    message_bin = ''.join(format(ord(i), '08b') for i in message)
    message_len = len(message_bin)
    
    data = list(image.getdata())
    pixel_index = 0

    for i in range(message_len):
        pixel = list(data[pixel_index])
        pixel[0] = pixel[0] & 0xFE | int(message_bin[i])
        data[pixel_index] = tuple(pixel)
        pixel_index += 1

    for i in range(8):
        pixel = list(data[pixel_index])
        pixel[0] = pixel[0] & 0xFE | 0  # End of message
        data[pixel_index] = tuple(pixel)
        pixel_index += 1

    image.putdata(data)
    image.save(output_path)
    print(f"Message successfully encoded into {output_path}")

def decode_image(image_path):
    """
    Decode a message from an image using the Least Significant Bit (LSB) method.
    """
    image = Image.open(image_path)
    binary_message = ''

    for pixel in image.getdata():
        binary_message += str(pixel[0] & 1)

    message = ''.join([chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8)])
    return message.strip('\x00')  # Return message without null characters

