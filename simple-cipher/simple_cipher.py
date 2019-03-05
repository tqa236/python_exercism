class Cipher(object):
    def __init__(self, key=None):
        # self.key = key if key else 0
        self.key = 0

    def encode(self, text):
        return "".join([chr((ord(char) + self.key - 97) % 26 + 97)
                        for char in text])

    def decode(self, text):
        return "".join([chr((ord(char) + self.key - 97) % 26 + 97)
                        for char in text])
