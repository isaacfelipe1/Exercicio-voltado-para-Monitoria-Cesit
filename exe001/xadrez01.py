# Criando um tabuleiro vazio
tabuleiro = [['-' for _ in range(8)] for _ in range(8)]
# Solicitando a posição da Torre
linha = int(input("Digite o número da linha da Torre (entre 1 e 8): "))
coluna = int(input("Digite o número da coluna da Torre (entre 1 e 8): "))
# Convertendo as posições para índices da matriz
linha -= 1
coluna -= 1
# Marcando os possíveis movimentos da Torre
for i in range(8):
    tabuleiro[linha][i] = 'x'
    tabuleiro[i][coluna] = 'x'
# Imprimindo o tabuleiro com os movimentos e números das colunas
print("  1 2 3 4 5 6 7 8 ")
print("  ----------------")
i = 0
while i < 8:
    print(f"{i+1}" , end='')
    print("|", end='')
    j = 0
    while j < 8:
        print(tabuleiro[i][j], end=' ')
        j += 1
    print()
    i += 1
    

 