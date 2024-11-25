import os

# Function to validate image file
def validate_file(file):
    if file is None:
        return False
    file_extension = file.name.split('.')[-1].lower()
    if file_extension not in ['png', 'jpg', 'jpeg']:
        return False
    return True
