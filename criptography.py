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
        matriz_str = str(matriz).replace(',', '').replace('.', '').replace('\n',"")
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
        one_hot_cifrado.append(character@cifra)

    msg_cifrada = para_string(one_hot_cifrado)
    
    return msg_cifrada

# Desfaz todas as mudanças aplicadas a mensagem com base nas cifras originais ;


def decifrar(msg_cifrada:str,cifras:list):
    oh_cifrado = para_one_hot(msg_cifrada)
    n = len(cifras)
    if n > 1:
        for i in range(1,n):
            oh_cifrado = oh_cifrado@np.linalg.inv(cifras[-i])
    oh_decifrado = oh_cifrado@np.linalg.inv(cifras[0])

    return oh_decifrado
