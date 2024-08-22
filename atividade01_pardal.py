# Caminho absoluto para o arquivo, não consegui executar com o caminho sireto da pasta
nome_do_arquivo = '/Users/labsfiap/downloads/darkweb2017-top100.txt'

# Tenta abrir e ler o arquivo alvo
try:
    with open(nome_do_arquivo, 'r') as a:
        # Lê somente as 10 primeiras linhas
        for i, linha in enumerate(a):
            if i < 10:
                print(linha, end='')
            else:
                break
except FileNotFoundError:
    print(f"O arquivo '{nome_do_arquivo}' não foi encontrado.")
except IOError:
    print(f"Ocorreu um erro ao tentar ler o arquivo '{nome_do_arquivo}'.")
