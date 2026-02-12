
km_percoridos = float(input("Digite a quantidade de km percorridos: "))
dias_usados = int(input("Digite a quantidade de dias alugados: "))

km = km_percoridos * 0.20
dia = dias_usados * 90
valor_final = km + dia

print(f"O valor final a ser pago pelo carro alugado foi: {valor_final:.2f} reais ")

