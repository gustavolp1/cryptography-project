# cryptography-project

- Pedro Antônio Silva e Gustavo Lindenberg Pacheco

https://github.com/gustavolp1/cryptography-project

## Como instalar e executar

- Instale o Python (https://www.python.org/) em sua máquina. O jogo foi desenvolvido especificamente para Windows, portanto não há garantia de que funcionará em outros sistemas operacionais.

- Instale algum editor de texto/código, como o Visual Studio Code (https://code.visualstudio.com/).

- Abra o Visual Studio Code, procure pela opção Clonar Repositório, e selecione Clonar da Internet. No campo, cole o seguinte link: https://github.com/gustavolp1/cryptography-project

- Escolha uma localização em sua máquina para salvar o repositório clonado.

- Abra o terminal e digite o comando a seguir:

> pip install -r "requirements.txt"

- No Visual Studio, abra o arquivo "demo.py" dentro do repositório clonado. Você poderá usá-lo para testar o código.

- Se deseja usar as funções em outros arquivos, salve "cryptography.py" no diretório no qual está trabalhando, e adicione a seguinte linha de código no começo de cada arquivo que as usa:

> import cryptography

  
## Como usar a biblioteca

Defina um alfabeto desejado como uma string no seguinte formato: "A B C D E F G", onde cada caractere do alfabeto é separado por espaços. Tal string deve ser carregada numa variável chamada "alphabet". Note que o alfabeto em si automaticamente terá o caractere " " (barra de espaço) adicionado.

Para codificação e decodificação em one-hot encoding, use as seguintes funções:

* `para_one_hot(msg : str, alphabet : str)`: codifica mensagens como uma matriz usando one-hot encoding. O argumento `msg` é uma string contendo sua mensagem, `alphabet` é uma string contendo seu alfabeto, e é retornado um np.array de matrizes que correspondem à mensagem codificada.

* `para_string(M : np.array, alphabet : str)`: converte mensagens da representação one-hot encoding para uma string legível. O argumento `M` é um np.array de matrizes que representam uma mensagem codificada, `alphabet` é uma string contendo seu alfabeto, e é retornada uma string com a mensagem decodificada.

Para criar e trabalhar com cifras por cima do one-hot:

* `gera_cifra(alphabet)`: gera uma cifra (matriz de permutação) aleatorizada para aplicar ao alfabeto one-hot selecionado. O argumento `alphabet` é seu alfabeto, e é retornada a matriz de permutação num np.array.

* `cifrar(msg : str, P : np.array, alphabet : str)`: aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. O argumento `msg` é uma string contendo sua mensagem, `P` é a matriz de permutação np.array que realiza a cifra, `alphabet` é uma string contendo seu alfabeto, e é retornada uma string com a mensagem cifrada.

* `de_cifrar(msg : str, P : np.array, alphabet : str)`: recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. O argumento `msg` é uma string contendo sua mensagem, `P` é a matriz de permutação np.array que realiza a cifra, `alphabet` é uma string contendo seu alfabeto, e é retornada uma string com a mensagem original.

Para usar cifras-enigma por um cifrador auxiliar:

* `enigma(msg : str, P : np.array, E : np.array, alphabet : str)`: faz a cifra enigma na mensagem de entrada usando um cifrador comum e um cifrador auxiliar. O argumento `msg` é uma string contendo sua mensagem, `P` é o cifrador np.array, `E` é o cifrador auxiliar np.array, `alphabet` é uma string contendo seu alfabeto, e é retornada uma string com a mensagem cifrada.

* `de_enigma(msg : str, P : np.array, E : np.array, alphabet : str)`: recupera uma mensagem cifrada como enigma, assumindo que ela foi cifrada com um cifrador comum e um auxiliar. O argumento `msg` é uma string contendo sua mensagem, `P` é o cifrador np.array, `E` é o cifrador auxiliar np.array, `alphabet` é uma string contendo seu alfabeto, e é retornada uma string com a mensagem decifrada.

  

## Modelo Matemático

- A codificação de mensagens em one-hot é feita por meio da representação de cada caractere como uma matriz de uma coluna e tantas linhas quanto a quantidade de caracteres no alfabeto. Por exemplo, um alfabeto de três letras pode ser representado como:

  

$$

A =

\begin{bmatrix}

1 \\

0 \\

0

\end{bmatrix}

\hspace{0.5in}

  

B =

\begin{bmatrix}

0 \\

1 \\

0

\end{bmatrix}

\hspace{0.5in}

C =

\begin{bmatrix}

0 \\

0 \\

1

\end{bmatrix}

$$

Portanto, uma mensagem inteira é representada por uma matriz onde cada coluna equivale a uma matriz de caractere diferente. A mensagem "BACA", por exemplo, seria representada como:
  

$$

M =

\begin{bmatrix}

0 & 1 & 0 & 1 \\

1 & 0 & 0 & 0 \\

0 & 0 & 1 & 0

\end{bmatrix}

$$

  

Dessa forma, ao multiplicar a matriz da caracter por uma matriz identidade permutada, podemos permutar cada coluna, e, consequentemente, substituir um caractere por outro linearmente, para cada caracter da mensagem.

  

$$

\begin{bmatrix}

0 & 0 & 1 \\

1 & 0 & 0 \\

0 & 1 & 0

\end{bmatrix}

\begin{bmatrix}

0 \\

1 \\

0

\end{bmatrix}

=

\begin{bmatrix}

0 \\

0 \\

1 

\end{bmatrix}

$$

  

- O reverso desse processo pode ser aplicado para decodificar a mensagem e quanto maior o alfabeto maiores as dimensões em one-hot.

(OBS : Como este alfabeto não é padronizado, ele também é necessário para se codificar e decifrar a mensagem mais para frente, com sua ordem e quantidade de caracteres mudando a relação letra - one hot encoding. Ou seja, armazene o dicicionário de one-hots para uso nas demais funções.)

No que se trata das matrizes de permutação, para que a cifra possa funcionar, é realizada uma multiplicação matricial de uma cifra por cada caractere de uma mensagem codificada em one-hot encoding.

$$
 Cc = P*C
$$

- Cc : caracter cifrado;
- C(n) ou C : caracter de numero n (ordem alfabética) ou caracter em questão;
- P : cifra base de permutação;

\
Finalmente, para a aplicação do ciframento enigma, usamos multiplicações matriciais como no processo do ciframento anterior, porém com o uso de uma cifra auxiliar. Este processo se dá através do seguinte método :

$$
Cc = E^n * P * C(n)
$$

- $E^n$ : cifra auxiliar aplicada n vezes;

Esse padrão adiciona uma camada de ciframento a mais para cada caracter da mensagem, sendo uma forma simples de gerar uma mensagem difícil de se decifrar para quem não possui as cifras e no nosso caso, o alfabeto origem também. 