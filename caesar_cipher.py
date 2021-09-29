def encode_caesar_cipher(message: str, k: int = 3, ignore_spaces: bool = False):
    """
    Encodes a message using the caesar cipher
    :precondition: Message may only contain letters and spaces
    :param message: The message to encode
    :param k: The amount each character should be shifted
    :param ignore_spaces: Indicates whether spaces should be ignored
    :return:
    """
    if not all(char.isalpha() or char.isspace() for char in message):
        raise ValueError("Message may only contain letters and spaces")
    message = message.lower()

    cipher_text = ""
    for char in message:
        if char.isspace():
            cipher_text += " "*(not ignore_spaces) # Only add a space if spaces are not ignored
        else:
            cipher_text += chr((ord(char)+k-ord('a')) % 26 + ord('a'))

    return cipher_text


def decode_caesar_cipher(message: str, k: int = 3):
    return encode_caesar_cipher(message, -k)
