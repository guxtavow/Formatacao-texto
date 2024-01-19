from unidecode import unidecode #importação do codigo

def remover_acentos(texto): #def para retornar o unicode
    return unidecode(texto)

caminho_entrada = "Desktop/Ativos.txt"  #caminho do repositorio de entrada
caminho_saida = "Desktop/AtivosAlterados.txt" #caminho do repositorio de saída após a conclusão


with open(caminho_entrada, 'r', encoding='ISO-8859-1') as arquivo_entrada: #le todo o arquivo de entrada (necessário enconding)
    conteudo = arquivo_entrada.read()


conteudo_processado = remover_acentos(conteudo) # Remove todos os caracteres especiais


with open(caminho_saida, 'w', encoding='ISO-8859-1') as arquivo_saida: # Após retir todos os caracteres, reescreve em outro arquivo
    arquivo_saida.write(conteudo_processado)

print("Processamento concluído. Resultado salvo em", caminho_saida) #assim que concluido printa o caminho
