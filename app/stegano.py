from PIL import Image

def encode_image(image_file, message):
    img = Image.open(image_file)
    encoded = img.copy()
    width, height = img.size
    message += '<<END>>'  # End marker for decoding

    binary_message = ''.join(format(ord(char), '08b') for char in message)
    data_index = 0

    for x in range(width):
        for y in range(height):
            if data_index < len(binary_message):
                pixel = list(img.getpixel((x, y)))
                pixel[0] = pixel[0] & ~1 | int(binary_message[data_index])  # Modify the LSB
                encoded.putpixel((x, y), tuple(pixel))
                data_index += 1

    output_path = "resources/output_files/encoded_image.png"
    encoded.save(output_path)
    return output_path

def decode_image(image_file):
    img = Image.open(image_file)
    binary_message = ""
    for pixel in img.getdata():
        binary_message += str(pixel[0] & 1)

    byte_chunks = [binary_message[i:i+8] for i in range(0, len(binary_message), 8)]
    decoded_message = "".join([chr(int(byte, 2)) for byte in byte_chunks])
    end_marker = decoded_message.find("<<END>>")
    return decoded_message[:end_marker] if end_marker != -1 else "No hidden message found"
