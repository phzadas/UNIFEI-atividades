capital = int(input("Digite seu capital inicial: "))
taxa = float(input("Digite uma taxa de sua escolha: "))

n = int(input("Digite o tempo do investimento em anos: "))

for ano in range(1, n + 1):
    montante = capital * ((1 + taxa) ** ano)
    print(f"Ano {ano}: R$ ou U$ {montante:.2f}")

