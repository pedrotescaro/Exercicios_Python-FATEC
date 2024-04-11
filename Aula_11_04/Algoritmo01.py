try:
    numero_j01 = int(input("Digite um número de 1 a 10: "))
    if 1 <= numero_j01 <= 10:
        numero_secreto = numero_j01
        tentativas = 0
    else:
        print("Erro: Por favor, escolha um número entre 1 e 10.")
except ValueError:
    print("Erro: Por favor, insira um número válido.")

while True:
    tentativa = int(input("J02, tente adivinhar o número: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(f"Parabéns! J02 acertou o número {numero_secreto} em {tentativas} tentativas!")
        break
    elif tentativa < numero_secreto:
        print("Tente novamente: Tente um número maior.")
    else:
        print("Tente novamente: Tente um número menor.")
