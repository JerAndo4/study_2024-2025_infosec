import random
import string
from random import seed

def xor_text_f(text, key):
    if len(key) != len(text): print("ERORR!!!!")
    xor_text =''
    for i in range(len(text)):
        xor_text_sym = ord(text[i]) ^ ord(key[i])
        xor_text += chr(xor_text_sym)
    return xor_text

text1 = "С Новым Годом, друзья!"
key = ''
seed(22)
for i in range(len(text)):
    key += random.choice(string.ascii_letters + string.digits)

xor_text_it = xor_text_f(text, key)
key_f = xor_text_f(text, xor_text_it)
textt = xor_text_f(xor_text_it, key_f)


print("Ключ шифрования: " + key_f)
print("Зашифрованный текст: " + xor_text_it)
print("Рашифрованный текст с помощью ключа: " + textt)
