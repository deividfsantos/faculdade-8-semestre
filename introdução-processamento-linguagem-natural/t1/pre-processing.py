import os
import csv

def ler_palavras_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='UTF-16 LE') as arquivo:
        conteudo = arquivo.read()
        return conteudo.split(), conteudo.split(".")

def main():
    pasta = "DADOS_FOLHADESAOPAULO"
    arquivos = os.listdir(pasta)

    total_palavras = 0
    total_turismo = 0
    total_esporte = 0
    total_tokens = set()
    total_sentencas = set()

    for nome_arquivo in arquivos:
        if nome_arquivo.startswith("TURISMO"):
            total_turismo += 1
        if nome_arquivo.startswith("ESPORTE"):
            total_esporte += 1

        caminho_arquivo = os.path.join(pasta, nome_arquivo)
        palavras, sentencas = ler_palavras_arquivo(caminho_arquivo)
        num_palavras = len(palavras)
        total_palavras += num_palavras
        total_tokens.update(set(palavras))
        total_sentencas.update(set(sentencas))
        
        # print(f"O arquivo '{nome_arquivo}' contém {num_palavras} palavras e {len(num_tokens)} tokens.")

    print(f"Total de arquivos: {len(arquivos)}")
    print(f"Total de arquivos sobre esportes: {total_esporte}")
    print(f"Total de arquivos sobre turismo: {total_turismo}")
    print(f"Tamanho medio dos arquivos: {total_palavras/len(arquivos)}")
    print(f"Total de palavras em todos os arquivos: {total_palavras}")
    print(f"Total de tokens em todos os arquivos: {len(total_tokens)}")
    print(f"Total de sentenças em todos os arquivos: {len(total_sentencas)}")
    
    with open("tokens_e_sentencas.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Tipo", "Texto"])
        for token in total_tokens:
            writer.writerow(["Token", token])
        for sentenca in total_sentencas:
            writer.writerow(["Sentenca", sentenca])

if __name__ == "__main__":
    main()