print("Vamos calcular o seu indice de Massa Corporal?")

peso = float(input("Qual o seu peso?: "))
altura = float(input("Qual a sua altura: "))

imc = peso / (altura ** 2)
print(f"O seu IMC é {imc:.2f}")
