alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[:shift]
encryption_map = {alphabet[i]: shifted_alphabet[i] for i in range(len(alphabet))}

def encrypt_text(text):
    encrypted_text = ''
    
    for char in text:
        if char.lower() in encryption_map:
            if char.isupper():
                encrypted_text += encryption_map[char.lower()].upper()
            else:
                encrypted_text += encryption_map[char]
        else:
            encrypted_text += char
    
    return encrypted_text

def main():
    sentence = input("Please enter a sentence: ")
    encrypted_sentence = encrypt_text(sentence)
    print("The encrypted sentence is:", encrypted_sentence)

main()

