import numpy as np
import random

# Gerando alfabeto em one hot.

#alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
alphabet = "A B C"
alphabet = alphabet.lower().split(" ") + [" "]
t_alfa = len(alphabet)
one_hot_alphabet = {}

for i in range(t_alfa):
    matriz_letra = []
    for j in range(t_alfa):
        if j == i:
            matriz_letra.append(1)
        else: 
            matriz_letra.append(0)
        
    matriz_letra = np.array(matriz_letra)
    one_hot_alphabet[alphabet[i]] = matriz_letra



# Transforma letras em one_hot code.

def para_one_hot(msg:str):
    one_hot_msg = []
    for character in msg:
        character = character.lower()
        if character in alphabet:
            one_hot_msg.append(one_hot_alphabet[character])
        else:
            one_hot_msg.append(one_hot_alphabet[len(one_hot_alphabet)-1])

    return one_hot_msg

print(para_one_hot("abc"))



# Transforma one_hot code em letras

def para_string(one_hot_msg:np.array):
    msg = ""
    decode = {str(v):k for k,v in one_hot_alphabet.items()}
    print(decode)
    for matriz in one_hot_msg:
        matriz_str = str(matriz).replace(',', '')
        print(matriz_str)
        msg += decode[matriz_str]
    return msg

print(para_string([
    [1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
    [1,0,0,0],
]))

# Testing:

msg = "hello world"
print(msg)
msg = para_one_hot(msg)
msg = para_string(msg)
print(msg)



# Gera cifra e cifrar

def gera_cifra(alphabet):
    tamanho = len(alphabet)
    identidade = np.eye(tamanho)
    L = np.random.permutation(list(range(tamanho)))
    cifra = identidade[L, :]
    print(cifra)
    return cifra


def cifrar(msg:str, cifra:np.array):
    one_hot_cifrado = []

    for character in para_one_hot(msg):
        one_hot_cifrado.append(character@cifra)
    print(one_hot_cifrado)
    msg_cifrada = para_string(one_hot_cifrado)
    
    return msg_cifrada



# teste 2 ; tem algo errado

gera_cifra(alphabet)

#cifrar("abcd",gera_cifra(alphabet))

#msg = "abcd e"
#cifra = gera_cifra(alphabet)
#oh_msg = para_one_hot(msg)
#one_hot_cifrado = []
#for character in para_one_hot(msg):
#    one_hot_cifrado.append(cifra@character)

#for character in one_hot_cifrado:
#    print(character)