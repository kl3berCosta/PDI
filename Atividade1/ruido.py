import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

try:
    original_image_pil = Image.open('galaxia.jpg').convert('L')
    # Converte a imagem para um array NumPy e para o tipo float para cálculos
    original_image = np.array(original_image_pil, dtype=np.float32)

except FileNotFoundError:
    print("Erro: Arquivo de imagem original não encontrado.")
    original_image = np.zeros((512, 512), dtype=np.float32)

# Gerar um Conjunto de Imagens Ruidosas
# Define a quantidade máxima de imagens ruidosas a serem geradas
num_images_to_generate = 100

# Define os parâmetros do ruído gaussiano
mean = 0
std_dev = 25 

# Lista para armazenar todas as imagens com ruído
noisy_images_stack = []

print(f"Gerando {num_images_to_generate} imagens com ruído...")
for _ in range(num_images_to_generate):
    # Gera uma nova matriz de ruído aleatório para cada imagem
    gaussian_noise = np.random.normal(mean, std_dev, original_image.shape)
    # Adiciona o ruído à imagem original
    noisy_image = original_image + gaussian_noise
    noisy_images_stack.append(noisy_image)

# Converte a lista de imagens em um único array 3D do NumPy para cálculos eficientes
# O formato será (100, altura, largura)
noisy_images_stack = np.array(noisy_images_stack)
print("Geração concluída.")

# Calcular a Média de Conjuntos de Imagens
# Definindo os números de imagens que vamos usar para cada média
averaging_counts = [5, 10, 20, 50, 100]
averaged_images = []
print("Calculando as médias...")

for count in averaging_counts:
    # Seleciona as primeiras 'count' imagens da nossa pilha
    images_to_average = noisy_images_stack[:count]   
    # Calcula a média ao longo do eixo 0 (o eixo que empilha as imagens)
    average_result = np.mean(images_to_average, axis=0)
    # "Corta" os valores para o intervalo [0, 255] e converte para o tipo de imagem (uint8)
    average_result_clipped = np.clip(average_result, 0, 255).astype(np.uint8)
    averaged_images.append(average_result_clipped)
print("Cálculos concluídos.")


fig, axes = plt.subplots(2, 3, figsize=(18, 12))
ax = axes.ravel() 
img_a = np.clip(noisy_images_stack[0], 0, 255).astype(np.uint8)
ax[0].imshow(img_a, cmap='gray', vmin=0, vmax=255)
ax[0].set_title("(a) Imagem com Ruído Gaussiano")
titles = [
    f"(b) Média de {averaging_counts[0]} imagens",
    f"(c) Média de {averaging_counts[1]} imagens",
    f"(d) Média de {averaging_counts[2]} imagens",
    f"(e) Média de {averaging_counts[3]} imagens",
    f"(f) Média de {averaging_counts[4]} imagens",
]

for i, (img, title) in enumerate(zip(averaged_images, titles)):
    ax[i+1].imshow(img, cmap='gray', vmin=0, vmax=255)
    ax[i+1].set_title(title)

for axis in ax:
    axis.axis('off')

plt.tight_layout()
plt.savefig("galaxy_apos_ruido.png")
plt.show()
