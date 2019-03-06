class Cipher(object):
    def __init__(self, key=None):
        self.key = key

    def encode(self, text):
        if not self.key:
            return text
        # return "".join([chr((ord(char) + self.key - 97) % 26 + 97)
        #                 for char in text])

    def decode(self, text):
        if not self.key:
            return text
        # return "".join([chr((ord(char) + self.key - 97) % 26 + 97)
        #                 for char in text])
