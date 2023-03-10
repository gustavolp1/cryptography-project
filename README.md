# cryptography-project

- Pedro Antônio Silva e Gustavo Lindenberg Pacheco

https://github.com/gustavolp1/cryptography-project

## Como instalar e executar

    - Instale o Python (https://www.python.org/) em sua máquina. O jogo foi desenvolvido especificamente para Windows, portanto não há garantia de que funcionará em outros sistemas operacionais.

    - Instale algum editor de texto/código, como o Visual Studio Code (https://code.visualstudio.com/).

    - Abra o Visual Studio Code, procure pela opção Clonar Repositório, e selecione Clonar da Internet. No campo, cole o seguinte link: https://github.com/gustavolp1/cryptography-project

    - Escolha uma localização em sua máquina para salvar o repositório clonado.

    - Abra o terminal e digite o comando a seguir:
        pip install -r "requirements.txt"

    - No Visual Studio, abra o arquivo "demo.py" dentro do repositório clonado. Você poderá usá-lo para testar o código.

    - Se deseja usar as funções em outros arquivos, salve "cryptography.py" no diretório no qual está trabalhando, e adicione a seguinte linha de código no começo de cada arquivo que as usa:
        import cryptography


## Como usar a biblioteca

    - Defina um alfabeto desejado como uma string no seguinte formato: "A B C D E F G", onde cada caractere do alfabeto é separado por espaços. Tal string deve ser carregada numa variável chamada "alphabet". Note que o alfabeto em si automaticamente terá o caractere " " (barra de espaço) adicionado.

    - Para codificação e decodificação em one-hot encoding, use as seguintes funções:
        * `para_one_hot(msg : str)`: codifica mensagens como uma matriz usando one-hot encoding. O argumento `msg` é uma string contendo sua mensagem, e é retornado um np.array de matrizes que correspondem à mensagem codificada.
        * `para_string(M : np.array)`: converte mensagens da representação one-hot encoding para uma string legível. O argumento `M` é um np.array de matrizes que representam uma mensagem codificada, e é retornada uma string com a mensagem decodificada.

    - Para criar e trabalhar com cifras por cima do one-hot:
        * `gera_cifra(alphabet)`: gera uma cifra (matriz de permutação) aleatorizada para aplicar ao alfabeto one-hot selecionado. O argumento `alphabet` é seu alfabeto, e é retornada a matriz de permutação num np.array.
        * `cifrar(msg : str, P : np.array)`: aplica uma cifra simples em uma mensagem recebida como entrada e retorna a mensagem cifrada. O argumento `msg` é uma string contendo sua mensagem, `P` é a matriz de permutação np.array que realiza a cifra, e é retornada uma string com a mensagem cifrada.
        * `de_cifrar(msg : str, P : np.array)`: recupera uma mensagem cifrada, recebida como entrada, e retorna a mensagem original. O argumento `msg` é uma string contendo sua mensagem, `P` é a matriz de permutação np.array que realiza a cifra, e é retornada uma string com a mensagem original.

    - Para usar cifras-enigma por um cifrador auxiliar:
        * `enigma(msg : str, P : np.array, E : np.array)`: faz a cifra enigma na mensagem de entrada usando um cifrador comum e um cifrador auxiliar. O argumento `msg` é uma string contendo sua mensagem, `P` é o cifrador comum np.array, `E` é o cifrador auxiliar np.array, e é retornada uma string com a mensagem cifrada.
        * `de_enigma(msg : str, P : np.array, E : np.array)`: recupera uma mensagem cifrada como enigma, assumindo que ela foi cifrada com um cifrador comum e um auxiliar. O argumento `msg` é uma string contendo sua mensagem, `P` é o cifrador comum np.array, `E` é o cifrador auxiliar np.array, e é retornada uma string com a mensagem decifrada.

## Modelo Matemático
    - 