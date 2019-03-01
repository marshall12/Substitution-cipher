from Encipher import enciphered_text
import collections
# Removing blankspace from the encrypted file from Encipher.py ensuring it's not the most repeated character
enciphered_text1 = enciphered_text.replace(' ', '')

# m is the most repeated character and n is the number of m in the enciphered_text
m, n = collections.Counter(enciphered_text1).most_common(1)[0]


def decipher(char):
    deciphered_text = list(enciphered_text)
    # Finding key considering char as the most repeated character
    key = ord(m)-ord(char)
    for i in range(len(deciphered_text)):
        # Only substituting the alphabets
        if deciphered_text[i].isalpha():
            num = ((ord(deciphered_text[i])-97)-key) % 26
            deciphered_text[i] = chr(num+97)
    return ''.join(deciphered_text)
# "etaoin" is considered most repeated 6 letters in English language
# So observing the results considering them the most repeated character  for each individual
# Six results should be observed to find the valid output, or we can check the number of valid words in each output
# considering the output with most valid words the correct one.


print("Deciphered Text considering letter 'e':\t"+decipher('e')+"\n")
print("Deciphered Text considering letter 't':\t"+decipher('t')+"\n")
print("Deciphered Text considering letter 'a':\t"+decipher('a')+"\n")
print("Deciphered Text considering letter 'o':\t"+decipher('o')+"\n")
print("Deciphered Text considering letter 'i':\t"+decipher('i')+"\n")
print("Deciphered Text considering letter 'n':\t"+decipher('n'))
