import os

def validate_file_type(file_name, allowed_types):
    return file_name.split('.')[-1].lower() in allowed_types
