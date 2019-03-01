from Encipher import enciphered_text
import collections
print("Enciphered Text:\t"+enciphered_text)
deciphered_text = list(enciphered_text)
enciphered_text1 = enciphered_text.replace(' ', '')
m, n = collections.Counter(enciphered_text1).most_common(1)[0]
key = ord(m)-ord('e')
for i in range(len(deciphered_text)):
    if deciphered_text[i].isalpha():
        num = (ord(deciphered_text[i])-96)-5
        if num <= 0:
            num = num + 26
        deciphered_text[i] = chr(num+96)
print("Deciphered Text:\t"+''.join(deciphered_text))
