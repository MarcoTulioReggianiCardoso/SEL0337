# Prática 6 - Introdução às interfaces de visão computacional, controle de acesso, versionamento e repositório de códigos
## SEL0337 - Projetos em Sistemas Embarcados
### Marco Túlio Reggiani Cardoso - 12547531
### João Marcelo dos Santos Vieira - 12547527

Esta prática envolve a incorporação de periféricos na Raspberry Pi, utilizando o módulo de câmera, tags RFID e técnicas de aprendizado de máquina. Ele abrange aplicações práticas, como sistemas de controle de acesso baseados em tags e reconhecimento facial em bancos de dados e servidores.

## Controle de acesso via Tag RFID
Neste projeto, foi elaborado um código em Python que se dedica à integração de uma tag RFID. O programa realiza a leitura do ID associado a essa tag e, por meio de um sistema de verificação, compara seu valor com o ID esperado. Para interação com o usuário, um LED verde é aceso se o ID for coincidente (acesso liberado), e um LED vermelho é aceso caso os IDs sejam distintos (acesso negado).

Para viabilizar essa operação, o código faz uso do módulo ```SimpleMFRC522```, importado da biblioteca ```mfrc522```, que permite a interação com o ID de uma tag. Os pinos GPIO são configurados, utilizando o canal BCM da Broadcom (pinos GPIO), e os warnings são desativados para evitar mensagens indesejadas.

O programa define variáveis para os pinos dos LEDs verde e vermelho, configurando-os como saídas inicialmente apagadas. Em seguida, é criado um objeto leitor da classe ```SimpleMFRC522()``` para possibilitar a interação com o leitor RFID.

Inicialmente, pede-se para aproximar uma tag do leitor para cadastramento da ID que será salva e usada para dar o acesso ou não.

O loop principal é responsável por exibir a mensagem "Aproxime a tag do leitor" no terminal, chamar a função ```leitor.read()```, utilizada para obter o ID e o texto da tag, para assim verificar a compatibilidade do ID identificado com o cartão cadastrado anteriormente e realizar o controle dos LEDs. Os dados da tag, incluindo ID e texto, são impressos no terminal. Há um atraso de 3 segundos antes da próxima leitura, proporcionando um intervalo entre as operações.

![Circuito RFID](https://github.com/MarcoTulioReggianiCardoso/SEL0337/blob/main/Pr%C3%A1tica%206/Tag/circuitotag.jpg?raw=true)

![Circuito RFID](https://github.com/MarcoTulioReggianiCardoso/SEL0337/blob/main/Pr%C3%A1tica%206/Tag/acessoliberadotag.jpg?raw=true)

![Circuito RFID](https://github.com/MarcoTulioReggianiCardoso/SEL0337/blob/main/Pr%C3%A1tica%206/Tag/acessonegadotag.jpg?raw=true)

## Reconhecimento Facial

Nesta fase, foi desenvolvido um sistema de reconhecimento facial utilizando a câmera da Raspberry Pi e o algoritmo ```Haar Cascade```, um classificador em cascata pré-treinado para a detecção facial. Durante o processamento da imagem, um LED vermelho é ativado para interação com o usuário. Os rostos detectados pelo classificador são armazenados no diretório "detected_faces".

No início do código, bibliotecas essenciais são importadas, como ```cv2``` para visão computacional, ```os``` para interação com o sistema operacional, ```RPi.GPIO``` para controle dos pinos GPIO, ```time``` para manipulação de tempo e ```picamera2``` para controle da câmera da Raspberry Pi.

A configuração dos pinos GPIO é realizada, associando o LED ao pino 12 (GPIO 18). Esse pinos é inicializado como saída, com o LED é inicialmente desligado.

A câmera da Raspberry Pi é inicializada e configurada para criar uma visualização com resolução de 640x480 pixels. O diretório "detected_faces" é definido para armazenar as imagens dos rostos detectados e é criado caso ainda não exista.

A função ```photo()``` é definida para lidar com a detecção facial. Um quadro é capturado pela câmera, convertido para escala de cinza e o classificador em cascata é aplicado para detectar rostos na imagem. As faces detectadas são destacadas na imagem original com retângulos verdes, e as porções contendo os rostos são salvas como arquivos JPEG no diretório definido anteriormente. Além disso, a imagem com os retângulos desenhados é exibida em uma janela com o título "Camera". O LED é ligado durante a detecção facial e desligado após a conclusão.

![Circuito RFID](https://github.com/MarcoTulioReggianiCardoso/SEL0337/blob/main/Pr%C3%A1tica%206/Camera/circuitocamera.jpg?raw=true)
![Circuito RFID](https://github.com/MarcoTulioReggianiCardoso/SEL0337/blob/main/Pr%C3%A1tica%206/Camera/camerafuncionando.png?raw=true)
