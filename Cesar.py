class Cesar:

    @staticmethod
    def encryption(message):
        new_phrase = ""
        new_assci = 0
        for i in range(len(message)):
            new_assci = ord(message[i])+3
            new_phrase += chr(new_assci)
        return new_phrase

    @staticmethod
    def decryption(message):
        new_phrase = ""
        new_assci = 0
        for i in range(len(message)):
            new_assci = ord(message[i])-3
            new_phrase += chr(new_assci)
        return new_phrase


