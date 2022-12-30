from time import sleep
from pynput.mouse import *

print ('----------- AUTO CLICK --------------')
print ('\n[ 1 ] CLICK COM LADO ESQUERDO')
print ('[ 2 ] CLICK COM LADO DIREITO')
opção = int(input('\n[ + ] Escolha uma opção: '))

def autoclick():
  qtclicks = int(input("[ + ] Quantidade de cliks: "))
  segundos = 5
  mous = Controller()
  while segundos>0:
      segundos = segundos-1
      sleep(1)
  while qtclicks > 0:
      qtclicks = qtclicks-1
      botao = Button.left
      if opção == 2:
         botao = Button.right
      mous.press(botao) # Qual botão vai ser apertado
      mous.release(botao) # Qual botão vai ser apertado (left ou right)
      sleep(0.1)

if opção != 3:
  autoclick()
  print('\n -------- Done!! --------')
else:
  print('ERROR!!! número invalido.')
