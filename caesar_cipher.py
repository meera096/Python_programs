#encryption and decryption
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direct = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def caesar(plain_text, shift_amount,direction):
  cipher_text = ""
  for letter in plain_text:
    position = alphabet.index(letter)
    if direct == "encrypt":
      new_position = position + shift_amount 
    else:
      new_position = position - shift_amount
    cipher_text += alphabet[new_position]
  print(f"The {direct} text is {cipher_text}")

caesar(plain_text=text, shift_amount=shift,direction=direct)
