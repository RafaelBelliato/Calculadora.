# -*- coding: utf-8 -*-
"""
Calculadora 
Autor: Rafael Belliato 
Primeiro Projeto Back. 
"""

print("----- Calucladora Versão 2.0 ------")
print("--- Seja muito bem vindo! ---")

sair=False
while sair == False:

	num1=input("Digite o 1º número: ")
	num1=int(num1)
	operador=input("Digite o operador:")
	num2=input("Digite o 2º número: ")
	num2=int(num2)

	if operador == "+":
		operacao = num1 + num2
	if operador == "-":
		operacao=num1 - num2
	if operador == "/":
		operacao=num1 / num2
	if operador == "*":
		operacao=num1 * num2

	print("Resultado:")
	print(operacao)
	print("Muito Obrigado por usar!!")

	teste = input("Deseja sair? (n/s): ")
	if teste=="s":
		sair= True
		if teste == "s":
			print("Até logo!")