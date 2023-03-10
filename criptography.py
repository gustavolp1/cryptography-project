import numpy as np

# Gerando alfabeto em one hot ;

def gera_oh_alfabeto(alphabet):
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
    return one_hot_alphabet
    
# Transforma letras em one_hot code ;

def para_one_hot(msg:str,one_hot_alphabet,alphabet):
    one_hot_msg = []
    alphabet = alphabet.lower().split(" ")
    for character in msg:
        character = character.lower()
        if character in alphabet:
            one_hot_msg.append(one_hot_alphabet[character])
        else:
            one_hot_msg.append(one_hot_alphabet[" "])

    return one_hot_msg


# Transforma one_hot code em letras ;

def para_string(one_hot_msg:np.array,one_hot_alphabet):
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

def cifrar(msg:str, cifra:np.array,one_hot_alphabet,alphabet):
    one_hot_cifrado = []
    oh_msg = para_one_hot(msg,one_hot_alphabet,alphabet)
    for character in oh_msg:
        one_hot_cifrado.append(cifra@character)

    msg_cifrada = para_string(one_hot_cifrado,one_hot_alphabet)
    
    return msg_cifrada

# Desfaz todas as mudanças aplicadas a mensagem com base nas cifras originais ;


def de_cifrar(msg_cifrada:str,cifra,one_hot_alphabet,alphabet):
    oh_decifrado = []
    for character in para_one_hot(msg_cifrada,one_hot_alphabet,alphabet):
        oh_decifrado.append(np.linalg.inv(cifra)@character)
    return para_string(oh_decifrado,one_hot_alphabet)

# Aplica uma cifra diferente para cada letra ;


def enigma (msg, cifra, cifra_auxiliar,one_hot_alphabet):
    encrypted_msg = []
    one_hot_msg = para_one_hot(msg,one_hot_alphabet)
    for i in range(len(one_hot_msg)):
        caracter = (cifra@one_hot_msg[i])
        while i > 0 :
            caracter = cifra_auxiliar@caracter
            i -= 1
        encrypted_msg.append(caracter)
    return para_string(encrypted_msg,one_hot_alphabet)

# Decifra o enigma gerado pela função anterior ;


def de_enigma (msg, cifra, cifra_auxiliar,one_hot_alphabet):
    decrypted_msg = []
    one_hot_msg = para_one_hot(msg,one_hot_alphabet)
    for i in range(len(one_hot_msg)):
        j = i
        caracter = one_hot_msg[i]
        while j > 0 :
            caracter = np.linalg.inv(cifra_auxiliar)@caracter
            j -= 1
        caracter = np.linalg.inv(cifra)@caracter
        decrypted_msg.append(caracter)
    return para_string(decrypted_msg,one_hot_alphabet)
