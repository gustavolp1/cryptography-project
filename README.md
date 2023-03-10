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

    - Para codificação e decodificação em one-hot encoding, use as seguintes funções:
        * `para_one_hot(msg : str)`: codifica mensagens como uma matriz usando one-hot encoding. O argumento msg é uma string contendo sua mensagem, e é retornado 
        * `para_string(M : np.array)` para converter mensagens da representação one-hot encoding para uma string legível

## Modelo Matemático
    - 