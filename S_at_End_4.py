##4. Crie um programa que insere a letra s no final das palavras que
#    terminam com a letra O.##

word = input("Informe uma palavra: ").title()

if word.endswith('o'):
    print(f"{word}s")
else:
    print(f"Erro: Palavra '{word}' não é terminada em O!")