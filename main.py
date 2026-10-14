def ler_arquivo(nome):
    with open(nome, 'r', encoding='utf-8') as arquivo:
        texto = arquivo.read()
    return texto

def main():
    arquivoAlunos = "alunosED_2026.txt"
    textoAlunos = ler_arquivo(arquivoAlunos)    

    arquivoClaraDosAnjos = "clara-dos-anjos.txt"
    textoClaraDosAnjos = ler_arquivo(arquivoClaraDosAnjos)

main()