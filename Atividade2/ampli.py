import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo():
    """Abre uma caixa de diálogo para o usuário selecionar um arquivo de imagem."""
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal do tkinter
    
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo de imagem",
        filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.bmp;*.gif"), ("Todos os arquivos", "*.*")]
    )
    return caminho_arquivo

def ampliar_imagem(caminho_imagem, fator_ampliacao, caminho_saida):
    """
    Amplia uma imagem por replicação de pixels.
    """
    try:
        imagem_original = Image.open(caminho_imagem)
        largura_original, altura_original = imagem_original.size
        pixels_originais = imagem_original.load()

        nova_largura = largura_original * fator_ampliacao
        nova_altura = altura_original * fator_ampliacao
        imagem_ampliada = Image.new(imagem_original.mode, (nova_largura, nova_altura))
        pixels_ampliados = imagem_ampliada.load()

        for y in range(nova_altura):
            for x in range(nova_largura):
                pixel_x_original = x // fator_ampliacao
                pixel_y_original = y // fator_ampliacao
                pixels_ampliados[x, y] = pixels_originais[pixel_x_original, pixel_y_original]

        imagem_ampliada.save(caminho_saida)
        print(f"Imagem ampliada com sucesso e salva em: {caminho_saida}")

    except Exception as e:
        print(f"Ocorreu um erro ao ampliar a imagem: {e}")

def reduzir_imagem(caminho_imagem, fator_reducao, caminho_saida):
    """
    Reduz uma imagem por replicação de pixels.
    """
    try:
        imagem_original = Image.open(caminho_imagem)
        largura_original, altura_original = imagem_original.size
        pixels_originais = imagem_original.load()

        nova_largura = largura_original // fator_reducao
        nova_altura = altura_original // fator_reducao
        imagem_reduzida = Image.new(imagem_original.mode, (nova_largura, nova_altura))
        pixels_reduzidos = imagem_reduzida.load()

        for y in range(nova_altura):
            for x in range(nova_largura):
                pixel_x_original = x * fator_reducao
                pixel_y_original = y * fator_reducao
                pixels_reduzidos[x, y] = pixels_originais[pixel_x_original, pixel_y_original]

        imagem_reduzida.save(caminho_saida)
        print(f"Imagem reduzida com sucesso e salva em: {caminho_saida}")

    except Exception as e:
        print(f"Ocorreu um erro ao reduzir a imagem: {e}")

if __name__ == "__main__":
    print("Iniciando o programa de redimensionamento de imagem...")
    
    # Passo 1: O usuário seleciona a imagem que deseja processar
    caminho_da_imagem_original = selecionar_arquivo()
    
    # Verifica se o usuário selecionou um arquivo ou fechou a janela
    if not caminho_da_imagem_original:
        print("Nenhum arquivo selecionado. Encerrando o programa.")
    else:
        print(f"Arquivo selecionado: {caminho_da_imagem_original}")

        # Extrai o nome base do arquivo e sua extensão
        nome_base, extensao = os.path.splitext(os.path.basename(caminho_da_imagem_original))
        
        # --- Processo de Ampliação ---
        try:
            fator_de_ampliacao = int(input("Digite o fator de AMPLIAÇÃO (número inteiro, ex: 2): "))
            if fator_de_ampliacao > 0:
                # Gera o nome do arquivo de saída automaticamente
                caminho_da_imagem_ampliada = f"{nome_base}_ampliada{extensao}"
                ampliar_imagem(caminho_da_imagem_original, fator_de_ampliacao, caminho_da_imagem_ampliada)
            else:
                print("Fator de ampliação inválido. Deve ser um inteiro maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

        print("-" * 30)

        # --- Processo de Redução ---
        try:
            fator_de_reducao = int(input("Digite o fator de REDUÇÃO (número inteiro, ex: 3): "))
            if fator_de_reducao > 0:
                # Gera o nome do arquivo de saída automaticamente
                caminho_da_imagem_reduzida = f"{nome_base}_reduzida{extensao}"
                reduzir_imagem(caminho_da_imagem_original, fator_de_reducao, caminho_da_imagem_reduzida)
            else:
                print("Fator de redução inválido. Deve ser um inteiro maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

    print("\nPrograma finalizado.")
