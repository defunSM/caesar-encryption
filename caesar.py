import sys


def encrypt(message, k):

    # contain the numerical representation of each letter in the message
    ord_list = []
    
    # find the numerical representation of each letter and place into ord_list
    for letter in message:
        numeric_rep = ord(letter)
        ord_list.append(numeric_rep)

    # shift the numerical representation of each letter by k
    encrypted_ord_list = [ num + k for num in ord_list ]

    # handle situations where the numerical rep is over due to shifting
    t_encrypted_ord_list = [ num if num <= 122 else num - 26 for num in encrypted_ord_list ]
    encrypted_message = ""

    # convert back to characters
    for encrypted_ord in t_encrypted_ord_list:
        encrypted_message += chr(encrypted_ord)

    return encrypted_message


def decrypt(message, k):

    # contain the numerical representation of each letter in the message
    ord_list = []
    
    # find the numerical representation of each letter and place into ord_list
    for letter in message:
        numeric_rep = ord(letter)
        ord_list.append(numeric_rep)

    # shift the numerical representation of each letter back by k to decrypt it
    decrypted_ord_list = [ num - k for num in ord_list ]

    # handle situations where numerical representation is under the numerical rep
    t_decrypted_ord_list = [ num if num > 96 else num + 26 for num in decrypted_ord_list ]
    decrypted_message = ""



    # convert back to characters
    for decrypted_ord in t_decrypted_ord_list:
        decrypted_message += chr(decrypted_ord)

    return decrypted_message


if __name__ == "__main__":
    # take in first arg as word
    message = sys.argv[1]
    # take in second arg as int key
    key = int(sys.argv[2])

    # make sure the key is under 26 and if its over get the remainder
    key = key % 26
    print(key)

    # encrypt your word
    encrypted = encrypt(message, key)

    # decrypt your encrypted word
    decrypted = decrypt(encrypted, key)

    print("Your encrypted word is", encrypted)
    print("Your decrypted word is", decrypted)
