nome = "Henrique"
idade = 21
peso = 54
altura = 1.76

# Forma 1
print("1. O meu nome é", nome, "tenho", idade, "anos e ", peso, "Quilos", "e minha altura é ", altura)

# Forma 2
print("2. O meu nome é {} tenho {} anos e {} Quilos e minha altura é {}".format(nome, idade, peso, altura))
print("2. O meu nome é {0} tenho {1} anos e {2:.1f} Quilos e minha altura é {3:.2f}".format(nome, idade, peso, altura))
print("2. O meu nome é {n} tenho {i} anos e {p:.1f} Quilos e minha altura é {a:.2f}".format(n=nome,i=idade,p=peso, a=altura))

# Forma 3
print(f"3. O meu nome é {nome} tenho {idade} anos e {peso:.1f} Quilos e minha altura é {altura:.2f}")