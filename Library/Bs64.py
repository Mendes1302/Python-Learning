import base64

class bs64:
    """
        Simplify the use of the base64 library:
    """

    def __init__(self, text):
        """
            Parameters: 
                text (str): Text for encode or decode.
        """

        self.text = text


    def encode(self):
        """
            Returns:
                str: Encoded text
        """

        message_bytes = self.text.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        message = base64_bytes.decode('ascii')

        return message


    def decode(self, txt):
        """
            Returns:
                str: Decoded text
        """

        base64_bytes = txt.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        message = message_bytes.decode('ascii')

        return message

