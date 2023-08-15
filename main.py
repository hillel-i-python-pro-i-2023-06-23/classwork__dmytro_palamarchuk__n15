# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

class Cesar:

    MAX_KEY = 1114111

    @staticmethod
    def encrypt_offset(position: int, offset: int):
        if (position + offset) > Cesar.MAX_KEY:
            return position + offset - Cesar.MAX_KEY
        return position + offset

    @staticmethod
    def decrypt_offset(position: int, offset: int):
        if (position - offset) < 0:
            return position - offset + Cesar.MAX_KEY
        return position - offset

    @staticmethod
    def encrypt(text: str, key: int) -> str:
       if not (0 < key < Cesar.MAX_KEY):
           return 'Invalid key'
       encrypted_text = ''
       for char in text:
           current_position = ord(char)
           new_position = Cesar.encrypt_offset(current_position, key)
           encrypted_text += chr(new_position)

       return encrypted_text

    @staticmethod
    def decrypt(text: str, key: int) -> str:
        if not (0 < key < Cesar.MAX_KEY):
            return 'Invalid key'
        decrypted_text = ''
        for char in text:
            current_position = ord(char)
            new_position = Cesar.decrypt_offset(current_position, key)
            decrypted_text += chr(new_position)

        return decrypted_text


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    string = 'Hello world!!!'
    # key = 0
    # key = 5
    # key = 1114111
    key = 1114109
    encrypted_message = Cesar.encrypt(string, key)
    print(encrypted_message)
    decrypted_message = Cesar.decrypt(encrypted_message, key)
    # decrypted_message = cesar_decrypt('🙒🙯🙶🙶🙹😪🚁🙹🙼🙶🙮😫😫😫', 128522)
    print(decrypted_message)

    print('================================================================')


    string = 'Привет мир!!!'
    encrypted_message = Cesar.encrypt(string, key)
    print(encrypted_message)
    decrypted_message = Cesar.decrypt(encrypted_message, key)
    print(decrypted_message)



