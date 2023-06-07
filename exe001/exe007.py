capacidade = 3
pessoas_entraram = 0
pessoas_sairam = 0
lugares_ocupados = 0
while True:
    print("Menu:")
    print("0 – FIM")
    print("1 – ENTRA UMA PESSOA")
    print("2 – SAI UMA PESSOA")
    print("3 – MOSTRAR QUANTOS LUGARES ESTÃO DISPONÍVEIS")
    print("4 – MOSTRAR O TOTAL DE PESSOAS QUE ENTRARAM")
    print("5 – MOSTRAR O TOTAL DE PESSOAS QUE SAÍRAM")
    codigo = int(input("Digite o código: "))
    if codigo == 0:
        print("Encerrando o programa...")
        break
    elif codigo == 1:
        if lugares_ocupados < capacidade:
            pessoas_entraram += 1
            lugares_ocupados += 1
            print("Entrou")
        else:
            print("Não há mais vagas disponíveis.")
    elif codigo == 2:
        if pessoas_sairam < pessoas_entraram:
            pessoas_sairam += 1
            lugares_ocupados -= 1
            print("Saiu")
        else:
            print("Não há pessoas suficientes para sair.")
    elif codigo == 3:
        lugares_disponiveis = capacidade - lugares_ocupados
        if lugares_disponiveis < 0:
            lugares_disponiveis = 0
        print(f"Lugares disponíveis: {lugares_disponiveis}")
    elif codigo == 4:
        pessoas_atuais = pessoas_entraram - pessoas_sairam
        if pessoas_atuais < 0:
            pessoas_atuais = 0
        print(f"Total de pessoas que entraram: {pessoas_atuais}")
    elif codigo == 5:
        print(f"Total de pessoas que saíram: {pessoas_sairam}")
    else:
        print("Código inválido")
