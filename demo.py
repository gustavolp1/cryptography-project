from criptography import *

# Test 3 :




print("Esta é a demo da biblioteca criptography, que tem como objetivo permitir a rapida geração de criptografias e cifras em python com base em one hot encoding")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Para realizar esta demo faremos uma breve apresentação das capacidades desta biblioteca :\n")
print("     Antes de começarmos a usar as funções de criptografia, precisamos definir e armazenar dois alfabetos : Um alfabeto de strings, no formato str 'A B C D E ...'\ne um alfabeto de one hot encoding, gerado a partir deste bloco de código :\n\n alphabet = 'A g l i n e d m s !' \n gera_oh_alfabeto(alphabet)\n")
alphabet = "A g l i n e d m s !"
one_hot_alphabet = gera_oh_alfabeto(alphabet)
print(f"Resultado : {one_hot_alphabet}\n")
print("(Não se preocupe com o espaço,ele é adicionado automaticamente.)\n")
msg = "Alglin e demais !"
print(f"    Agora, suponha que temos a mensagem '{msg}', que por algum motivo queremos garantir que ninguem além do destinatário será capaz de entender.")
print(f"para isso, será necessário primeiro gerar uma cifra de permutação, que nesta biblioteca é feito a partir da função 'gera_cifra'\n\n cifra = gera_cifra(alphabet)\n\n    Esta cifra será aplicada ao one hot encoding para aleatorizar os caracteres da mensagem, com a função 'cifrar' da seguinte forma:\n\n msg_cifrada = cifrar(msg,cifra,one_hot_alphabet)\n")
cifra =  gera_cifra(one_hot_alphabet)
msg_cifrada = cifrar(msg,cifra,one_hot_alphabet,alphabet)
print(f"Resultado : {msg_cifrada}\n")
print(f"    Após cifrar, a recuperação da mensagem pode ser feita a partir da cifra original e dos alfabetos usados,\n  *lembrando que a função não irá recuperar letras fora deste alfabeto.\n" )
msg_decifrada = de_cifrar(msg_cifrada,cifra,one_hot_alphabet,alphabet)
print(" msg_decifrada = de_cifrar(msg_cifrada,cifra,one_hot_alphabet,alphabet)")
print(f"Resultado : '{msg_decifrada}'\n")
print("     Por fim, existem as funções enigma e de_enigma, com a enigma aplicando uma cifra primária e uma cifra auxiliar para aprimorar a criptografia e de_enigma desfazendo este processo\n - Vide readme para mais detalhes.\n")
cifra = gera_cifra(one_hot_alphabet)
cifra_aux = gera_cifra(one_hot_alphabet)
msg_enigma = enigma(msg,cifra,cifra_aux,one_hot_alphabet,alphabet)
print(f" cifra = gera_cifra(one_hot_alphabet)\n cifra_aux = gera_cifra(one_hot_alphabet)\n msg_enigma = enigma(msg,cifra,cifra_aux,one_hot_alphabet)\n")
print(f"Resultado : {msg_enigma}\n")
print("Decifrando :")
msgE_decifrada = de_enigma(msg_enigma,cifra,cifra_aux,one_hot_alphabet,alphabet)
print(" msgE_decifrada = de_enigma(msg_enigma,cifra,cifra_aux,one_hot_alphabet,alphabet)")
print(f"Resultado : {msgE_decifrada}")