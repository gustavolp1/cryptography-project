import numpy as np

# Gerando alfabeto em one hot ;

alphabet = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
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


# Transforma letras em one_hot code ;

def para_one_hot(msg:str):
    one_hot_msg = []
    for character in msg:
        character = character.lower()
        if character in alphabet:
            one_hot_msg.append(one_hot_alphabet[character])
        else:
            one_hot_msg.append(one_hot_alphabet[len(one_hot_alphabet)-1])

    return one_hot_msg


# Transforma one_hot code em letras ;

def para_string(one_hot_msg:np.array):
    msg = ""
    decode = {str(v):k for k,v in one_hot_alphabet.items()}
    for matriz in one_hot_msg:
        matriz_str = str(matriz).replace(',', '').replace('.', '').replace('\n','')
        msg += decode[matriz_str]
    return msg


# Gera uma Cifra (Matriz de Permutação) aleatorizada para apliicar ao alfabeto one_hot ;

def gera_cifra(alphabet):
    tamanho = len(alphabet)
    identidade = np.eye(tamanho)
    L = np.random.permutation(list(range(tamanho)))
    cifra = identidade[L, :]
    return cifra

# Aplica a cifra a uma mensagem : str ;

def cifrar(msg:str, cifra:np.array):
    one_hot_cifrado = []

    for character in para_one_hot(msg):
        one_hot_cifrado.append(cifra@character)

    msg_cifrada = para_string(one_hot_cifrado)
    
    return msg_cifrada

# Desfaz todas as mudanças aplicadas a mensagem com base nas cifras originais ;


def decifrar(msg_cifrada:str,cifra):
    oh_decifrado = []
    for character in para_one_hot(msg_cifrada):
        oh_decifrado.append(np.linalg.inv(cifra)@character)
    return para_string(oh_decifrado)

# Aplica uma cifra diferente para cada letra ;


def enigma (msg, cifra, cifra_auxiliar):
    encrypted_msg = []
    one_hot_msg = para_one_hot(msg)
    for i in range(len(one_hot_msg)):
        caracter = (cifra@one_hot_msg[i])
        while i > 0 :
            caracter = cifra_auxiliar@caracter
            i -= 1
        encrypted_msg.append(caracter)
    return para_string(encrypted_msg)

# Decifra o enigma gerado pela função anterior ;


def de_enigma (msg, cifra, cifra_auxiliar):
    decrypted_msg = []
    one_hot_msg = para_one_hot(msg)
    for i in range(len(one_hot_msg)):
        j = i
        caracter = one_hot_msg[i]
        while j > 0 :
            caracter = np.linalg.inv(cifra_auxiliar)@caracter
            j -= 1
        caracter = np.linalg.inv(cifra)@caracter
        decrypted_msg.append(caracter)
    return para_string(decrypted_msg)


# Test 3 :

"""
msg = 'arthur'
print(msg)
cifra = gera_cifra(alphabet)
cifra_aux = gera_cifra(alphabet)
enigma1 = enigma(msg,cifra,cifra_aux)
print(enigma1)
print(de_enigma(enigma1,cifra,cifra_aux))
cript_msg = cifrar(msg,cifra)
print(cript_msg)
print(decifrar(cript_msg,cifra))
"""
