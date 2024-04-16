idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("O nadador está na categoria infantil A");
elif idade >= 8 and idade <= 10:
    print("O nadador está na categoria infantil B")
elif idade >= 11 and idade <= 13:
    print("O nadador está na categoria juvenil A")
elif idade >= 13 and idade <= 17:
    print("O nadador está na categoria juvenil B")
elif idade >= 18:
    print("O nadador está na categoria adulto")
else:
    ("Idade inválida para categorização")