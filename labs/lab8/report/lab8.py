import random
import string

def generate_key_hex(text):
    key = ''
    for i in range(len(text)):
        key += random.choice(string.ascii_letters + string.digits) #генерация цифры для каждого символа в тексте
    return key

#для шифрования и дешифрования
def en_de_crypt(text, key):
    new_text = ''
    for i in range(len(text)): #проход по каждому символу в тексте
        new_text += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return new_text

t1 = "С Новым Годом, друзья!"
key = generate_key_hex(t1)
en_t1 = en_de_crypt(t1, key)
de_t1 = en_de_crypt(en_t1, key)

t2 = "У Слона домов, огого!"
en_t2 = en_de_crypt(t2, key)
de_t2 = en_de_crypt(en_t2, key)

print("--------")
print(f"Открытй текст: {t1} \nКлюч: {key} \nШифротекст: {en_t1} \n Исходный текст: {de_t1} ")
print("--------")
print(f"Открытй текст: {t2} \nКлюч: {key} \nШифротекст: {en_t2} \n Исходный текст: {de_t2} ")
print("--------")

r = en_de_crypt(en_t2, en_t1)
print(f"Расшифровать второй текст, зная первый: {en_de_crypt(t1, r)}")
print(f"Расшифровать первый текст, зная второй: {en_de_crypt(t2, r)}")