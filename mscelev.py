#Elevador
#Funções: selecionar andar; peso maximo; aguardando portas fecharem; subindo/descendo;você chegou ao -- andar

#Fechamento das portas
print("Leitura dos Sensores de Porta")
P1=int(input('Estado do Sensor da porta:'))
if P1==1: #1= porta desempedida, liberada para ser fechada
  print('Porta fechando')
elif P1==0: #0=Há pessoas ou objetos impedindo o fechamento da porta
  print('Porta aberta!')


#Peso maximo
if P1==1:
  peso_maximo=480
  peso=float(input('Peso do elevador:'))#o peso do elevador é calculado automaticamente
  if peso>peso_maximo:
    print('Elevador acima do limite de peso, não poderá prosseguir!')
  elif peso>0:
    print('Autorizado a prosseguir!')


#Seleção de andar
if (P1==1) and (peso<=peso_maximo) and (peso>0):
  andares=[1,2,3,4,5,6,7,8,9,10,11,12] #andares do prédio
  andar=input('Para qual andar deseja ir?')
  print('Indo para o andar', andar)


#Subindo/Descendo
if (P1==1) and (peso<=peso_maximo) and (peso>0):
  print('...prosseguindo...')

#tocar música ambiente
from playsound import playsound
playsound('musicaelevador.mp3')
  print('...tocando música...')

#Chegada
if (P1==1) and (peso<=peso_maximo) and (peso>0):
  print('Você chegou ao', andar, 'andar!')

#Elevador vazio
if (P1==1) and (peso==0): #peso=0=elevador vazio, para economizar energia, todas as funções são desligadas e só voltam a ligar ao acionar novamente o elevador
  print('Portas fechadas')
  print('Modo de economia de energia:')
  print('Luzes apagadas;')
  print('Painel desligado;')
  print('Ventilação desligada.')


