# Caminho absoluto para o arquivo, não consegui executar com o caminho sireto da pasta
caminho_absoluto = '/Users/labsfiap/downloads/darkweb2017-top100.txt'

# Tenta abrir e ler o arquivo alvo
try:
    with open(caminho_absoluto, 'r') as a:
        # Lê somente as 10 primeiras linhas
        for i, linha in enumerate(a):
            if i < 10:
                print(linha, end='')
            else:
                break
except FileNotFoundError:
    print(f"O arquivo '{caminho_absoluto}' não foi encontrado.")
except IOError:
    print(f"Ocorreu um erro ao tentar ler o arquivo '{caminho_absoluto}'.")
