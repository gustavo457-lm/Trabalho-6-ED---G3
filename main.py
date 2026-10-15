import HashTable as ht
import re
import matplotlib.pyplot as plt

def mostrarGraficos(palavras, M, idx_hash):
    letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    tabela = ht.HashTable(M)

    for palavra in palavras:
        tabela.insert(palavra, idx_hash)

    for quant in tabela.quant:
        print(quant)

    plt.bar(range(tabela.M), tabela.quant)

    plt.xlabel("Índice da tabela hash")
    plt.ylabel("Quantidade de palavras")
    plt.title("Distribuição da função hash")
    plt.axhline(tabela.N/tabela.M, 0, 100)
    if idx_hash == 1:
        plt.xticks(range(len(letras)), letras)
    plt.show()


def main():
    with open('alunosED_2026.txt', 'r', encoding="UTF-8") as arquivo_alunos:
        alunos = arquivo_alunos.readlines()

    with open('clara-dos-anjos.txt', 'r', encoding= 'UTF-8') as arquivo:
        texto = arquivo.read()
        palavras = re.split(r'[.,;:!?\d+\s/+-]', texto)
        palavras_processadas = []
        for palavra in palavras:
            repetida = 0 #booleano para saber se a palavra é repetida ou não
            if palavra.isalpha():
                for palavraIncluida in palavras_processadas: #checagem se a palavra inserida é repetida ou não 
                    if palavraIncluida == palavra.lower():
                        repetida = 1
                        break
                if repetida == 0:
                    palavras_processadas.append(palavra.lower())


    mostrarGraficos(alunos, 26, 1)

    mostrarGraficos(alunos, 26, 2)
    
    mostrarGraficos(palavras_processadas, 17, 3)
    mostrarGraficos(palavras_processadas, 43, 3)
    mostrarGraficos(palavras_processadas, 97, 3)

    mostrarGraficos(palavras_processadas, 16, 3)
    mostrarGraficos(palavras_processadas, 40, 3)
    mostrarGraficos(palavras_processadas, 100, 3)


if __name__ == "__main__":
    main()
