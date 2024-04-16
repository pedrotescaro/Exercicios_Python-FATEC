# Inicializando as quantidades de produtos e o total do dia
total_do_dia = 0
total_clientes = 0

while True:
    quantidade_produto_1 = 0
    quantidade_produto_2 = 0
    quantidade_produto_3 = 0
    quantidade_produto_4 = 0
    quantidade_produto_5 = 0
    quantidade_produto_6 = 0
    total = 0

    print(
        "Especificação     Código  Preço"
        "\n-------------------------------"
        "\nCachorro Quente   1       R$ 8.10"
        "\nBauru Simples     2       R$ 11.30"
        "\nBauru com ovo     3       R$ 15.50"
        "\nHambúrguer        4       R$ 13.10"
        "\nCheeseburguer     5       R$ 14.30"
        "\nRefrigerante      6       R$ 5.00\n"
    )

    while True:
        codigo = int(input("Digite o código do produto (ou 0 para encerrar este pedido): "))
        if codigo == 0:
            break
        if codigo < 1 or codigo > 6:
            print("Código inválido!")
            continue

        quantidade = int(input("Digite a quantidade desse produto: "))
        if codigo == 1:
            quantidade_produto_1 += quantidade
        elif codigo == 2:
            quantidade_produto_2 += quantidade
        elif codigo == 3:
            quantidade_produto_3 += quantidade
        elif codigo == 4:
            quantidade_produto_4 += quantidade
        elif codigo == 5:
            quantidade_produto_5 += quantidade
        else:
            quantidade_produto_6 += quantidade

    print(
        "\nFechamento do pedido"
        "\nCódigo  -  Quantidade  -  Preço unidade  -  Preço total"
    )
    if quantidade_produto_1 > 0:
        print(
            f"1\t  -\t  {quantidade_produto_1}\t-  R$ 8.10\t-"
            f"\tR$ {quantidade_produto_1 * 8.10:.2f}"
        )
        total += quantidade_produto_1 * 8.10
    if quantidade_produto_2 > 0:
        print(
            f"2\t  -\t  {quantidade_produto_2}\t-  R$ 11.30\t-"
            f"\tR$ {quantidade_produto_2 * 11.30:.2f}"
        )
        total += quantidade_produto_2 * 11.30
    if quantidade_produto_3 > 0:
        print(
            f"3\t  -\t  {quantidade_produto_3}\t-  R$ 15.50\t-"
            f"\tR$ {quantidade_produto_3 * 15.50:.2f}"
        )
        total += quantidade_produto_3 * 15.50
    if quantidade_produto_4 > 0:
        print(
            f"4\t  -\t  {quantidade_produto_4}\t-  R$ 13.10\t-"
            f"\tR$ {quantidade_produto_4 * 13.10:.2f}"
        )
        total += quantidade_produto_4 * 13.10
    if quantidade_produto_5 > 0:
        print(
            f"5\t  -\t  {quantidade_produto_5}\t-  R$ 14.30\t-"
            f"\tR$ {quantidade_produto_5 * 14.30:.2f}"
        )
        total += quantidade_produto_5 * 14.30
    if quantidade_produto_6 > 0:
        print(
            f"6\t  -\t  {quantidade_produto_6}\t-  R$ 5.00\t-"
            f"\tR$ {quantidade_produto_6 * 5.00:.2f}"
        )
        total += quantidade_produto_6 * 5.00

    print(f"Total do pedido: R$ {total:.2f}\n")
    total_do_dia += total
    total_clientes += 1

    continuar = input("Deseja continuar (s/n)? ")
    if continuar.lower() != 's':
        break

print(f"Total de clientes atendidos hoje: {total_clientes}")
print(f"Total arrecadado hoje: R$ {total_do_dia:.2f}")
