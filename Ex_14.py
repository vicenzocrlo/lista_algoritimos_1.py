print("Vamos calcular sua conta de luz?")

Kwh = float(input("Digite a quantidade de Kwh consumidos: "))
valor = float(input("Digite o valor por Kwh: "))
conta = valor * Kwh

print(f"O valor final a ser pago pela sua conta de luz foi: {conta:.2f} reais ")

