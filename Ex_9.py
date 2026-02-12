print("Vamos calcular o seu indice de Massa Corporal?")

peso = float(input("Qual o seu peso?: "))
altura = float(input("Qual a sua altura: "))

imc = (altura ** 2) / peso

print(f"O seu IMC é {imc:.2f}")
