A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))

if A % B == 0 or B % A == 0:
    print("Seus números são múltiplos")
else:
    print("Seus números não são múltiplos")