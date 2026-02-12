custo_fabrica = float(input("Digite o valor de custo do carro na fábrica: "))
distribuidor =  custo_fabrica * 0.28
imposto = custo_fabrica * 0.45

custo_final = custo_fabrica + distribuidor + imposto

print(f"O custo final do seu carro foi de: {custo_final:.2f} reais")