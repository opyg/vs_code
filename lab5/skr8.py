def xor_letters(text: str, key: str) -> str:
    coded_text = ""
    for i in range(len(text)):
        xor_result = ord(text[i]) ^ ord(key[i])
        coded_text += chr(xor_result)
    return coded_text

text = "algorytm"
key = "kodykody"

coded_text = xor_letters(text, key)
print(f"Niejawny tekst: {coded_text}")

decoded_text = xor_letters(coded_text, key)
print(f"Jawny tekst po dekodowaniu: {decoded_text}")
