verify_1= float(input("Digite o valor do raio do circulo (caso tenha apenas a circunferência digite 1): "))
area = verify_1 **2
area_1 = area * 3.14

if verify_1 == 1:
    circun =float(input("Digite o valor da circunfência:"))
    area_2 = circun /2
    area_3 = area_2 **2
    area_4 = area_3 * 3.14

    print(f"O valor da área do seu círculo é {area_4:.2f} ")

else:
    print(f"O valor da área do seu círculo é: {area_1:.2f}")








