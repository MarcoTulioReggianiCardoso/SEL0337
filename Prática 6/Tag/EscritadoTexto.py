#para gravação de texto na Tag

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

#desabilita os avisos
GPIO.setwarnings(False)

#cria o objeto "leitor" para a instância "SimpleMRFC522" da biblioteca
leitor = SimpleMFRC522()

#criado da variavel que armazena o texto que será gravado na tag
texto = "12547531" #altere para o texto que deseja gravar

#escreve a tag assim que ela for aproximada do leitor, e informa a conclusão
print("Aproxime a tag do leitor para gravar.")
leitor.write(texto)#função que realiza a gravação do texto configurado
print("Concluido!")
