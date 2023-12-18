#Pratica 6 - Controle de acesso via Tag RFID
#Marco Túlio Reggiani Cardoso - 12547531
#João Marcelo dos Santos Vieira - 12547527


# Para descobrir qual a codificação da Tag com texto gravado anteriormente
from mfrc522 import SimpleMFRC522
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)      #Utiliza os números BCM dos pinos
GPIO.setup(17, GPIO.OUT)    #Determina PIN 17 (conectado ao led verde na protoboard) como saída
GPIO.setup(18, GPIO.OUT)    #Determina PIN 17 (conectado ao led vermelho na protoboard) como saída

#desabilitar os avisos
GPIO.setwarnings(False)

#cria o objeto "leitor" para a instância "SimpleMFRC522" da biblioteca
leitor = SimpleMFRC522()

print("Aproxime a tag do leitor para cadastro.")

idtag,textotag = leitor.read()
print("ID: {}\nTexto: {}".format(idtag, textotag)) #exibe as informações coletadas

print("\nCadastro realizado")

while True: #loop
#cria as variáveis "id" e "texto", e as atribui as leituras da id e do texto coletado da tag pelo leitor, respectivamente
    id,texto = leitor.read()
    print("ID: {}\nTexto: {}".format(id, texto)) #exibe as informações coletadas

	if id == idtag
		print("acesso liberado")
		GPIO.output(17, True) #Aciona o Led Verde
	else:
		print("acesso negado")
		GPIO.output(18, True)  #Aciona o Led Vermelho

    sleep(3) #aguarda 3 segundos para nova leitura
	
    GPIO.output(17, False) #Desliga o Led Verde
	GPIO.output(18, False) #Desliga o Led Vermelho


except KeyboardInterrupt:   #exceção que é disparada quando o usuário interrompe a execução de um programa pressionando a combinação de teclas Ctrl+C no teclado.
	GPIO.cleanup()          #função da biblioteca Rpi.GPIO que Limpa os pinos GPIO antes de encerrar o programa
