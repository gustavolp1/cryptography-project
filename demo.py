from criptography import *

# Test 3 :




print("Esta é a demo da biblioteca criptography, que tem como objetivo permitir a rapida geração de criptografias e cifras em python com base em one hot encoding")
print("----------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Para realizar esta demo faremos uma breve apresentação das capacidades desta biblioteca :\n")
print("     Antes de começarmos a usar as funções de criptografia, precisamos definir e armazenar dois alfabetos : Um alfabeto de strings, no formato str 'A B C D E ...'\ne um alfabeto de one hot encoding, gerado a partir deste bloco de código :\n\n alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z' \n gera_oh_alfabeto(alphabet)\n")
alphabet = "A B C"
one_hot_alphabet = gera_oh_alfabeto(alphabet)
print(f"Resultado : {one_hot_alphabet}\n")
print("(Não se preocupe com o espaço,ele é adicionado automaticamente.)\n")
msg = "Alglin é demais !"
print(f"    Agora, suponha que temos a mensagem '{msg}', que por algum motivo queremos garantir que ninguem além do destinatário será capaz de entender.")
print(f"para isso, será necessário primeiro gerar uma cifra de permutação, que nesta biblioteca é feito a partir da função 'gera_cifra'\n\n cifra = gera_cifra(alphabet)\n\n    Esta cifra será aplicada ao one hot encoding para aleatorizar os caracteres da mensagem, com a função 'cifrar' da seguinte forma:\n\n msg_cifrada = cifrar(msg,cifra,one_hot_alphabet)")
cifra =  gera_cifra(alphabet)
msg_cifrada = cifrar(msg,cifra,one_hot_alphabet,alphabet)
print(f"Resultado : {one_hot_alphabet}\n")