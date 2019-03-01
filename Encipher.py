f = open('Original.txt', 'r')
original_text = list(str.lower(f.read()))
print("Original Text:\t"+''.join(original_text)+"\n")
# Enciphering the original text using Caesar Cipher with key=5
key = 4
for i in range(len(original_text)):
    # Only substituting the alphabets
    if original_text[i].isalpha():
        num = ((ord(original_text[i])-97)+key) % 26
        original_text[i] = chr(num+97)
enciphered_text = ''.join(original_text)
print("Enciphered Text:\t"+enciphered_text+"\n")
