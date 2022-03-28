def desafio001():
 print("Olá, mundo!")

def desafio002():
  Nome = input('Digite seu nome:')
  print('Olá',Nome, '! ', 'Prazer em te conhcer!')

def desafio003():
  n1 = int(input('Digite um numero:'))
  n2 = int(input('Digite outro numero para realizar a soma:'))
  s = n1 + n2 
  print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
def desafio004():
  a = input('Digite a sua nota de Algoritimos no primeiro modulo:')
  print('O tipo primitivo desse valor é:', type(a))
  print('Só tem espaços?', a.isspace())
  print('É um número?', a.isnumeric())
  print('É alfabético?', a.isalpha())
  print('É alfanumérico?', a.isalnum())
  print('Está em maiúsculas?', a.isupper())
  print('Está em minúsculas?', a.islower())
  print('Está capitalizada?', a.istitle())

  b = input('Digite alguma coisa:')
  print('O tipo primitivo desse valor é:', type(b))
  print('Só tem espaços?', b.isspace())
  print('É um número?', b.isnumeric())
  print('É alfabético?', b.isalpha())
  print('É alfanumérico?', b.isalnum())
  print('Está em maiúsculas?', b.isupper())
  print('Está em minúsculas?', b.islower())
  print('Está capitalizada?', b.istitle())
def desafio005():
  n = int(input('Digite um número:  '))
  a = n - 1
  s = n + 1
  print('Analizando o número{}, seu antecessor é {} e o sucessor é {}'.format( n, a, s))
def desafio006():
  n = int(input('Digite um número:'))
  print('O dobro de {} vale {}.'.format(n, n * 2))
  print('O triplo de {} vale {}'.format(n, n * 3))
  print('A raiz quadrada de {} é {:.2f}'.format(n, n ** (1/2)))

def desafio007():
  n1 = float(input('Digite sua primeira nota em ALgorítimos: '))
  n2 = float(input('Digite sua segunda nota em Algorítimos: '))
  média = (n1 + n2) /2
  print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(n1, n2, média))
def desafio008():
  medida = float(input('Digite uma distância em metros:'))
  cm = medida * 100
  mm = medida * 1000
  print('A medida de {}m corresponde a {}cm e {}mm.'.format(medida, cm, mm))

def desafio009():
  num = int(input('Digite um número para ver sua tabuada:'))
  print('_' * 12)
  print('{} x {:2} = {}'.format(num, 1, num * 1))
  print('{} x {:2} = {}'.format(num, 2, num * 2))
  print('{} x {:2} = {}'.format(num, 3, num * 3))
  print('{} x {:2} = {}'.format(num, 4, num * 4))
  print('{} x {:2} = {}'.format(num, 5, num * 5))
  print('{} x {:2} = {}'.format(num, 6, num * 6))
  print('{} x {:2} = {}'.format(num, 7, num * 7))
  print('{} x {:2} = {}'.format(num, 8, num * 8))
  print('{} x {:2} = {}'.format(num, 9, num * 9))
  print('{} x {:2} = {}'.format(num, 10, num * 10))
  print('_' * 12)
def desafio010():
  real = float(input('Quanto dinheiro você tem na carteira? R$:'))
  dolar = real /4.74
  print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
def desafio011():
  larg = float(input('Largura da parede:'))
  alt = float(input('Altura da parede:'))
  área = larg* alt
  print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(larg, alt, área))
  tinta = área / 2
  print('Você precisará de {} litros de tinta para conseguir pintar a parede.'.format(tinta))
def desafio012():
  preço = float(input('Qual o preço do produto?'))
  desconto = preço - (preço* 5 / 100)
  print(' O produto custa R${}, e com o cupom de 5% de desconto custará R${}.'.format(preço, desconto))
def desafio013():
  salário = float(input('Digite seu salário: R$'))
  novo = salário + (salário * 15 / 100)
  print('Parabéns! Pela sua dedicação e competência na empresa, você terá um aumento de 15% no seu salário, seu salário que era R${:.2f} agora é R${:.2f}.'.format(salário, novo))
def desafio014():
  temperatura = float(input("Digite uma temperatura:"))
  fahrenheit = (temperatura *9/5)+32
  print('A temperatuda de {}ºC corresponde a {}ºF.'.format(temperatura, fahrenheit))
def desafio015():
  dias = int(input('Quantos dias alugados?'))
  km = float(input('Quantos km rodados?'))
  pago = (dias * 60) + (km * 0.15)
  print('O total a pagar vai ser de R${:.2f}.'.format(pago))
def desafio016():
  from math import trunc
  num = float(input('Digite um valor: '))
  print('O valor digitado foi {} e sua porção inteira é {}'.format(num, trunc(num))) 
def desafio017():
  from math import hypot
  co = float(input('Comprimento do cateto oposto:'))
  ca = float(input('Comprimento do cateto adjacente:'))
  hi = hypot(co, ca)
  print('A hipotenusa vai medir {:.2f}'.format(hi))
def desafio018():
  from math import radians, sin, cos, tan
  ângulo = float(input('Digite o ângulo que você quer:'))
  seno = sin(radians(ângulo))
  print('O ângulo de {} tem o SENO de {:.2f}'.format(ângulo, seno))
  cosseno = cos(radians(ângulo))
  print('O ângulo de {} tem o Cosseno de {:.2f}'.format(ângulo, cosseno))
  tangente = tan(radians(ângulo))
  print('O ângulo de {} tem o Tangente de {:.2f}'.format(ângulo, tangente))
def desafio019():
  import random
  n1 = str(input('Primeiro aluno:'))
  n2 = str(input('Segundo aluno:'))
  n3 = str(input('Terceiro aluno:'))
  n4 = str(input('Quarto aluno:'))
  lista = [n1, n2, n3, n4]
  escolhido = random.choice(lista)
  print('O aluno(a) escolhido para apagar o quadro foi {}.'.format(escolhido))
def desafio020():
  import random
  n1 = str(input('Primeiro aluno:'))
  n2 = str(input('Segundo aluno:'))
  n3 = str(input('Terceiro aluno:'))
  n4 = str(input('Quarto aluno:'))
  lista = [n1, n2, n3, n4]
  random.shuffle(lista)
  print('A ordem de apresentação será:')
  print(lista)

def desafio021():
  '''#import pygame
  #pygame.init()
  #pygame.mixer.music.load("ex021.mp3")
  #pygame.mixer.music.play()
  #pygame.event.wait()'''


def desafio022():
  nome = str(input('Digite seu nome completo: ')).strip()
  print('Analisando seu nome...')
  print('Seu nome em maiúsculas é {}'.format(nome.upper()))
  print('Seu nome em minúsculas é {}'.format(nome.lower()))
  print('Seu nome tem ao todo {} letras'.format(len(nome) - 
  nome.count(' ')))
  print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
def desafio023():
  n = int(input('Digite um número: '))
  u = n // 1 % 10
  d = n // 10 % 10
  c = n // 100 % 10
  m = n // 1000 % 10
  print('Analizando o número {}'.format(n))
  print('Unidade: {}'.format(u))
  print('Dezena: {}'.format(d))
  print('Centena: {}'.format(c))
  print('Milhar: {}'.format(m))
def desafio024():
  cid = str(input('Em que cidade você nasceu? ')).strip()
  print(cid[:5].upper() == 'SANTO')
def desafio025():
  nome = str(input('Qual seu nome completo? ')).strip()
  print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
def desafio026():
  frase = str(input('Digite uma frase: ')).upper().strip()
  print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
  print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
  print('A última letra A aparecu na posição {}'.format(frase.rfind('A')+1))
def desafio027():
  n = str(input('Digite seu nome completo: ')).strip()
  nome = n.split()
  print('Muito prazer em te conhecer!')
  print('Seu primeiro nome é: {}.'.format(nome[0]))
  print('Seu último nome é:{}.'.format(nome[len(nome)-1]))
def desafio028():
  from random import randint 
  from time import sleep
  computador = randint(0, 5)
  print('-=-' * 20)
  print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
  print('-=-' * 20)
  jogador = int(input('Em que número eu pensei? '))
  print('Processando...')
  sleep(3)
  if jogador == computador:
   print('Parabéns! Você conseguiu me vencer!')
  else:
   print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))
def desafio029():
  velocidade = float(input('Qual é a velocidade atual do carro? '))
  if velocidade > 80:
   print('Multado! Você excedeu o limite permitido que é de 80km/h')
  multa = (velocidade-80) * 7
  print('Você tem que pagar uma multa de R${:.2f}!'.format(multa))
  print('Tenha um bom dia! Dirija com segurança! <3')
def desafio030():
  n = int(input('Me diga um número qualquer: '))
  resultado = n % 2
  if resultado == 0:
   print('O número {} é Par.'.format(n))
  else:
   print('O número {} é Ímpar.'.format(n))
def desafio031():
  distância = float(input('Qual é a distância da sua viagem? '))
  print('Você está prestes a começar uma viagem de {}Km.'.format(distância))
  preço = distância * 0.50 if distância <= 200 else distância * 0.45
  print('E o preço da sua passagem será de RS{:.2f}'.format(preço))
def desafio032():
  from datetime import date
  ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
  if ano == 0:
   ano = date.today().year
  if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
   print('O ano {} é Bissexto!'.format(ano))
  else:
   print('O ano {} Não é Bissexto!'.format(ano))
def desafio033():
  a = int(input('Primeiro valor: '))
  b = int(input('Segundo valor: '))
  c = int(input('Terceiro valor: '))

  menor = a
  if b < a and b < c:
   menor = b
  if c < a and c < b:
   menor = c

  maior = a 
  if b > a and b > c:
   maior = b
  if c > a and c > b:
   maior = c
  print('O menor valor digitado foi {}.'.format(menor))
  print('O maior valor digitado foi {}.'.format(maior))
def desafio034():
  salário = float(input('Qual é o salário do funcionário? R$'))
  if salário <= 1250:
   novo = salário + (salário * 15 / 100)
  else:
   novo = salário + (salário * 10 / 100)
  print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
def desafio035():
  print('-='*20)
  print('Analizador de triângulos')
  print('-='*20)
  r1 = float(input('Primeiro segmento: '))
  r2 = float(input('Segundo segmento: '))
  r3 = float(input('Terceiro segmento: '))
  if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
   print('Os segmentos acima Podem formar triângulo!')
  else:
   print('Os segmentos acima Não podem formar triângulo')


