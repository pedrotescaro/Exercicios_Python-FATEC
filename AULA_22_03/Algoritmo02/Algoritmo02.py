km = int(input("Digite o numero de km percorridos"));
comb = int(input("Digite a quantidade de combustível"));

txConsumo= km/comb;

print("/n O automóvel consome %1.f Km/L" % txConsumo);

if txConsumo >= 8:
    print("/n O automóvel está consumindo muito combustivel");
else:
    print("/n O consumo de combustivel do automóvel está bom");