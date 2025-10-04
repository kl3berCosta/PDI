import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog

def selecionar_arquivo():
    root = tk.Tk()
    root.withdraw()
    
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione um arquivo de imagem",
        filetypes=[("Arquivos de Imagem", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tif"), ("Todos os arquivos", "*.*")]
    )
    return caminho_arquivo

def reduzir_imagem(caminho_imagem, fator_reducao, caminho_saida):
    try:
        imagem_original = Image.open(caminho_imagem)
        largura_original, altura_original = imagem_original.size
        
        nova_largura = largura_original // fator_reducao
        nova_altura = altura_original // fator_reducao
        
        imagem_reduzida = imagem_original.resize((nova_largura, nova_altura), Image.Resampling.NEAREST)
        
        imagem_reduzida.save(caminho_saida)
        print(f"1. Imagem reduzida com sucesso e salva em: {caminho_saida}")
        return imagem_reduzida

    except Exception as e:
        print(f"Ocorreu um erro ao reduzir a imagem: {e}")
        return None

def ampliar_imagem(imagem_obj, fator_ampliacao, caminho_saida):
    try:
        largura_original, altura_original = imagem_obj.size
        
        nova_largura = largura_original * fator_ampliacao
        nova_altura = altura_original * fator_ampliacao
        
        imagem_ampliada = imagem_obj.resize((nova_largura, nova_altura), Image.Resampling.NEAREST)
        
        imagem_ampliada.save(caminho_saida)
        print(f"2. Imagem re-ampliada com sucesso e salva em: {caminho_saida}")

    except Exception as e:
        print(f"Ocorreu um erro ao ampliar a imagem: {e}")

if __name__ == "__main__":
    print("Iniciando o programa para o projeto de Processamento de Imagens...")
    
    caminho_da_imagem_original = selecionar_arquivo()
    
    if not caminho_da_imagem_original:
        print("Nenhum arquivo selecionado. Encerrando o programa.")
    else:
        print(f"Arquivo selecionado: {caminho_da_imagem_original}")

        fator = 10
        print(f"Usando fator de redução/ampliação fixo: {fator}")

        nome_base, _ = os.path.splitext(os.path.basename(caminho_da_imagem_original))
        extensao_saida = ".png"
        
        caminho_da_imagem_reduzida = f"{nome_base}_reduzida_x{fator}{extensao_saida}"
        caminho_da_imagem_reampliada = f"{nome_base}_reampliada_x{fator}{extensao_saida}"
        
        print("\n--- Etapa de Redução ---")
        imagem_reduzida_obj = reduzir_imagem(caminho_da_imagem_original, fator, caminho_da_imagem_reduzida)
        
        if imagem_reduzida_obj:
            print("\n--- Etapa de Re-ampliação ---")
            ampliar_imagem(imagem_reduzida_obj, fator, caminho_da_imagem_reampliada)

    print("\nPrograma finalizado.")


