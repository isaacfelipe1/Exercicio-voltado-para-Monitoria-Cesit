# Definindo o tamanho máximo da pesquisa
max_respostas = 10

# Vetores para armazenar a idade e a nota dos clientes
idades = []
notas = []

# Loop para registrar a opinião dos clientes
for i in range(max_respostas):
    print(f"Cliente {i+1}:")
    idade = int(input("Informe a idade: "))
    nota = input("Informe a nota (A, B, C, D ou E): ")

    idades.append(idade)
    notas.append(nota)

# Contadores e variáveis para as informações solicitadas
quantidade_A = 0
soma_idades_D = 0
quantidade_D = 0
quantidade_E = 0
menor_idade_E = None
maior_idade_A = None
maior_idade_D = None

# Loop para gerar as informações
for i in range(max_respostas):
    if notas[i] == 'A':
        quantidade_A += 1
        if maior_idade_A is None or idades[i] > maior_idade_A:
            maior_idade_A = idades[i]
    elif notas[i] == 'D':
        soma_idades_D += idades[i]
        quantidade_D += 1
        if maior_idade_D is None or idades[i] > maior_idade_D:
            maior_idade_D = idades[i]
    elif notas[i] == 'E':
        quantidade_E += 1
        if menor_idade_E is None or idades[i] < menor_idade_E:
            menor_idade_E = idades[i]

# Cálculo da média de idade das pessoas que responderam D (ruim)
media_idades_D = soma_idades_D / quantidade_D if quantidade_D > 0 else 0

# Cálculo da porcentagem de resposta E (péssimo)
porcentagem_E = (quantidade_E / max_respostas) * 100

# Exibição das informações
print("Informações:")
print(f"Quantidade de respostas 'A' (Ótimos): {quantidade_A}")
print(f"Média de idade das pessoas que responderam 'D' (Ruim): {media_idades_D:.2f}")
print(f"Porcentagem de respostas 'E' (Péssimo): {porcentagem_E:.2f}%")
if quantidade_E > 0:
    print(f"Menor idade de quem informou a resposta 'E' (Péssimo): {menor_idade_E}")
if quantidade_A > 0:
    print(f"Maior idade de quem respondeu 'A' (Ótimo): {maior_idade_A}")
if quantidade_D > 0:
    print(f"Maior idade de quem respondeu 'D' (Ruim): {maior_idade_D}")
