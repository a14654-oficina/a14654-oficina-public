print ("Hello World")
valorA = input ("insira um numero inteiro entre 0 e 10: ")
valorB = input ("insira um numero inteiro entre 0 e 10: ")
soma = valorA+valorB
media = (soma/2) 
if media >=10
if media <=10

#EX0.1
"""Declara uma variável chamada "idade" e atribuiu a tua idade.
Declara uma variável chamada "nome" e atribuiu o teu nome.
Imprima no ecrã a frase "O meu nome é [nome] e tenho [idade] anos."
"""
idade =input("Insira a sua idade:")
nome =input("Insira o seu nome:")
print (f"O meu nome é {nome} e tenho {idade} anos").

#EX0.2 

"""EX0.2: 

Escreve um programa que imprima "Olá, mundo!" no ecrã.
Cria uma variável chamada "fruta" e atribuiu o nome de uma fruta.
Imprime no ecrã a frase "Eu gosto de [fruta]."
"""
print ("Olá,mundo!")
fruta = "banana"
print (f"Eu gosto de {fruta}")

#EX0.3: Input

"""
Solicita ao utilizador para digitar o nome.
Imprime no ecrã uma saudação personalizada utilizando o nome fornecido.
Pede ao utilizador para digitar um número inteiro.
Imprime o dobro desse número."""

nome = input ("Insira o seu nome:")
print (f"Boas rei, {nome}, tem um grande dia de trabalho!")
valor = int(input ("Insira um numero: "))
dobro = valor * 2
print (f"O dobro de {valor} é:{dobro}") 

#EX1.1
"""Elabora um programa que imprima a mensagem “Bem-vindos ao Python!”, precedida por uma linha em branco"""
N="\nBem-vindos ao Python!"
print(N)

#EX1.2
"""Elabora um programa que imprima a mensagem “José, bem-vindo ao Python!”, precedida por uma linha em branco"""
N="\nJosé, bem-vindo ao Python!"
print(N)

#EX1.3
"""Elabora um programa que atribua a mensagem a uma variável e, em seguida, imprima o valor da variável"""
carro=("audi r8")
print(F"\n O meu carro é {carro}.")


#EX1.4
"""Elabora um programa que atribua o nome, a idade e a localidade de residência do aluno a três variáveis e imprima os valores dessas variáveis."""
nome = input ("Como te chamas?")
idade = input ("Quantos anos tens?")
localidade = input ("Onde vives?")
print (f"Olá chamo-me {nome} tenho {idade} anos e vivo na {localidade}")

#EX1.5
"""Elabora um programa que intercale a designação da linguagem de programação e o nome do aluno na mensagem."""
linguagem = "Phyton"
nome = "Bernardo"
print (f"O {nome} sabe programar em {linguagem}")

#EX1.6
"""Elabora um programa que alinhe à direita, à esquerda e ao centro a mensagem “Bem-vindo ao Python!” num campo de edição com 50 carateres."""
print(f"{'Bem vindo ao Python':<20}")
print(f"{'Bem vindo ao Python':>40}")
print(f"{'Bem vindo ao Python':^250}")


#EX1.7
"""Elabora um programa que desenvolva o algoritmo de um programa que permita calcular o perímetro e área de uma circunferência a partir do valor do raio.""" 
raio = float(input ("Insira um raio: "))
perimetro = 2 * 3,14 * raio
area = 3,14 * raio * 2
print(f"O perimetro é: {perimetro}")
print(f"A area é: {area}")

#EX1.8
"""Elabora um programa que imprima a data e horas correntes nos seguintes formatos:
02-10-2024
02-10-2024 16:11:20
10-02-2024 16:11:20
02/10/24
16:11:20"""
import datetime
x= data = datetime.datetime.now()
dia = x.strftime("%d")
mes = x.strftime("%m")
ano = x.strftime("%y")
hora = x.strftime("%H")
minutos = x.strftime("%M")
segundos = x.strftime("%S")
print (f"{dia}-{mes}-{ano}")
print (f"{dia}-{mes}-{ano} {hora}:{minutos}:{segundos}")
print (f"{mes}-{dia}-{ano} {hora}:{minutos}:{segundos}")
print (f"{mes}/{dia}/{ano}") 
print (f"{hora}:{minutos}:{segundos}")


#EX1.9
"""Elabora um programa que leia o número mecanográfico de um atleta, assim como a sua pontuação. O número é inteiro e a pontuação final é real.
Digite o número do atleta: 12304
Digite a pontuação final: 7.89
O atleta número 12304 obteve 7.89 pontos."""
numero = int(input("Insira o seu numero:"))
pontuação = int(input("Insira a sua pontuação:"))
print (f"O atlena numero {numero} teve {pontuação} pontos.")


#X1.10
"""Elabora um programa que leia a data de nascimento de uma pessoa e imprima a sua idade à data atual."""
import datetime
birthdate = input("Insira a dua date de nascimento: ")
day,month,year = map(int, birthdate.split("-"))
today = datetime.date.today()
age = today.year - year - ((today.month, today.day) < (month, day))
print("A tua idade é",age,"anos.")

#EX1.11
"""Elabora um programa que desenvolva o algoritmo de um programa que permita converter libras em euros, considerando a taxa de conversão de 1,19 ( ou seja, 1 GBP = 1,19 EURO)."""
libras = float(input(f"Insira o valor em libras: "))
euro = libras * 1.19
print (f"O valor em euros é: {euro}")



idade = int(input("Digite sua idade: "))

if idade < 12:
    print("Você é uma criança.")
elif idade < 18:
    print("Você é um adolescente.")
elif idade < 60:
    print("Você é um adulto.")
else:
    print("Você é idoso.")


#A.28
  import random
  segredo = print(random.randint(0, 5))
  print (f"O numero secreto é: {segredo}")

  numeroescolhido = int(input("Insira um numero entre 0 e 5: "))

  if numeroescolhido > segredo:
        print ("O numero inserido é maior que o numero secreto")
  elif numeroescolhido < segredo:
        print ("O numero inserido é menor que o numero secreto")
  else:  
       print ("Acretaste!")

#A.29
"""Escreva um programa que leia a velocidade de um carro+
Se ele ultrapassar 80 km/h,mostre um mensagem dizendo que ele foi multado."""


km = float(input("Insira a velocidade em km/h:") )
multa = (velocidade) - 80
valor = (multa) * 7

if km > 100:
   print("Você foi multado!")
else:
   print("Você não foi multado!")
  print (f"A multa foi de {valor} euros")

#Exercício FP1: Verificar se um número é positivo, negativo ou zero.
"""Escreve um programa em Python que peça ao utilizador para introduzir um número e verifica se ele é positivo, negativo ou igual a zero.
Dica: Usa as estruturas condicionais if, elif e else."""

numero = int(input("Insira um numero: "))

if numero > 0:
    print("O número é positivo.") 
elif numero < 0: 
    print("O número é negativo.")
else: 
    print ("O número é zero.")


#Exercício FP2: Verificar se um número é par ou ímpar.
"""Escreve um programa que peça ao utilizador um número inteiro e verifica se ele é par ou ímpar.
Dica: Para verificar se um número é par, utilize a operação de módulo %."""

numero = int(input("Insira um número: "))
if numero % 2 == 0:
    print (f"o numero {numero} é par")
elif numero % 2 != 0:
    print (f"o numero {numero} é impar") 

#Exercício FP3: Calcular a nota final de um aluno.
"""Elabora um programa que pergunte ao utilizador a nota final de um aluno e verifica a classificação de acordo com a seguinte tabela:"""

Nota inferior a 10: "Reprovado"
Nota entre 10 e 14: "Suficiente"
Nota entre 15 e 17: "Bom"
Nota superior a 17: "Muito Bom"""

nota = int(input("Insira sua nota final: "))

if nota < 10:
    print ("Reprovado")
elif nota >= 10 and nota <= 14:
    print ("Suficiente")
elif nota  >=14 and nota <=17:
    print ("Bom")
elif nota > 17:
    print ("Muito Bom")

#Exercício FP4: Conversor de temperaturas.
"""Cria um programa que pergunte ao utilizador uma temperatura em graus Celsius e a converta para Fahrenheit, Kelvin ou ambas. O utilizador deve escolher a unidade de destino (Fahrenheit ou Kelvin), e o programa deve exibir o valor convertido.

Fórmulas:

Fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15"""



Celsius = int(input("Insira a temperatura em graus Celsius: "))
fahrenheit = Celsius * 9/5 + 32
Kelvin = Celsius + 273.15
print (f"Os graus em Kelvin são: {Kelvin} e em fahrenheit são: {fahrenheit}  ")


#Exercício FP5: Cálculo de impostos
"""Crie um programa que peça ao utilizador o seu salário mensal e calcule o imposto de acordo com a seguinte tabela:


Salário até 1000: isento de impostos
Salário entre 1001 e 2000: 10% de imposto
Salário superior a 2000: 20% de imposto
O programa deve exibir o salário após a dedução do imposto."""

salario = int(input("Insira o seu salário mensal: ")) 
if salario <= 1000: 
    print("Isento de impostos")
elif salario > 1000 and salario <= 2000: 
    imposto = salario * 0.1 
    print(f"O seu salário mensal com 10% de imposto é de {imposto} €")
elif salario > 2000: 
    imposto = salario * 0.2 
    print(f"O seu salário mensal com 20% de imposto é de {imposto} €")

#Exercício FP6: Imprimir números de 1 a 10.
"""screve um programa em Python que use um ciclo for para imprimir todos os números de 1 a 10.
[consola]
1
2
3
...
10"""
for i in range(1, 11):
     print(i)

#Exercício FP7: 
""" Soma de números de 1 a 100.
Escreve um programa que use um ciclo while para calcular a soma de todos os números de 1 a 100.

[consola]
A soma de 1 a 100 é: 5050"""

soma = 0
i = 1
while i <= 100:
  soma += i
  i += 1
print(f"A soma de 1 a 100 é: {soma}")

#Exercício FP8: Contagem de vogais numa string.
"""Contagem de vogais numa string.
Escreve um programa que peça ao utilizador para introduzir uma frase e utilize um ciclo for para contar quantas vogais (a, e, i, o, u) existem na frase.

[consola]
Introduza uma frase: Programação em Python
Número de vogais: 7"""

frase = nput("Insira uma frase: ")
vogais = "aeiouAEIOU"
contador = 0
for letra in frase:
  if letra in vogais:
    contador += 1
print(f"Número de vogais: {contador}"

 #Exercício FP9: Listar múltiplos de 5
"""Listar múltiplos de 5.
Escreve um programa que utilize um ciclo for para listar todos os múltiplos de 5 entre 1 e 50.

      [consola]
      5
      10
      15
      ...
      50"""

      for i in range(5,51,5):
        print(i)

n(lista)
print(f"A média é: {media}")

#Exercício FP10: Verificar se um número é primo.
"""Escreve um programa que peça ao utilizador um número inteiro e verifique se ele é primo. Um número primo é divisível apenas por 1 e por ele mesmo. O programa deve utilizar um ciclo for para testar se o número é divisível por algum outro número.
[consola]
Introduza um número: 13
13 é um número primo."""

numero = int(input("Insira um numero: "))
if numero % 2 == 0:
  print(f"{numero} é um número primo.")
else:
  print(f"{numero} não é um número primo.")

#Exercício FP11: Média de uma lista de números..
"""Escreve um programa que crie uma lista de 5 números inteiros, pede ao utilizador para introduzir cada número e, em seguida, calcula e exibe a média desses números.

[consola]
Introduza o número 1: 10
Introduza o número 2: 20
Introduza o número 3: 30
Introduza o número 4: 40
Introduza o número 5: 50
A média é: 30.0"""

lista = []
for i in range(5):
  numero = int(input(f"Insira o número {i+1}: "))
  lista.append(numero)
media = sum(lista) / len(lista)
print(f"A média é: {media}")

#Exercício FP12: Gerar uma lista de números pares.
"""Gerar uma lista de números pares.
Cria um programa que utilize a função range() e um ciclo for para gerar uma lista com todos os números pares entre 1 e 20 e imprima a lista.

[consola]
Lista de números pares: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
"""
lista = []
for i in range(1,21):
  if i % 2 == 0:
    lista.append(i)
print(f"Lista de números pares: {lista}")

#Exercício FP13: Inverter uma string.
"""Escreve um programa que peça ao utilizador para introduzir uma palavra ou frase e utilize um ciclo para imprimir a string invertida.
[consola]
Introduza uma palavra: Python
A palavra invertida é: nohtyP"""

texto = str(input("Insira um texto: "))
textoinv = texto[::-1]
print (textoinv)


#Exercício FP14: Tabuada de multiplicação
"""
Escreve um programa que gere a tabuada de multiplicação de um número introduzido pelo utilizador. O programa deve utilizar um ciclo for para calcular e exibir a tabuada até 10.

[consola]
Introduza um número: 6
Tabuada de 6:
6 x 1 = 6
6 x 2 = 12
...
6 x 10 = 60"""


num = int(input("Insira um numero: "))
for i in range (1,11):
  mult = num * i
  print (f"{num} x {i} = {mult}")



