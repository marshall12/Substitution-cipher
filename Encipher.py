f = open('Original_text.txt', 'r')
original_text = list(str.lower(f.read()))
#print("Original Text:\t"+''.join(original_text))
for i in range(len(original_text)):
    if original_text[i].isalpha():
        num = ((ord(original_text[i])-96)+5)%26
        if num ==0:
            num = num +26
        original_text[i] = chr(num+96)
enciphered_text = ''.join(original_text)
print("Enciphered Text:\t"+enciphered_text)
