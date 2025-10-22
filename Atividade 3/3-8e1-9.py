import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('Agg') 

try:
    img_spine = cv2.imread('Fig0308(a)(fractured_spine) (1).tif', cv2.IMREAD_GRAYSCALE)
    if img_spine is None:
        print("Erro: Nao foi possivel carregar 'Fig0308(a)(fractured_spine) (1).tif'")
    else:
        img_norm_spine = img_spine / 255.0
        
        c = 1
        gammas_spine = [0.6, 0.4, 0.3]
        results_spine = []
        
        for gamma in gammas_spine:
            corrected = c * (img_norm_spine ** gamma)
            corrected = np.clip(corrected * 255, 0, 255).astype(np.uint8)
            results_spine.append(corrected)
            
        fig, axs = plt.subplots(2, 2, figsize=(10, 10))
        axs[0, 0].imshow(img_spine, cmap='gray', vmin=0, vmax=255)
        axs[0, 0].set_title('(a) Original')
        axs[0, 0].axis('off')
        
        axs[0, 1].imshow(results_spine[0], cmap='gray', vmin=0, vmax=255)
        axs[0, 1].set_title(f'(b) $\gamma = {gammas_spine[0]}$')
        axs[0, 1].axis('off')
        
        axs[1, 0].imshow(results_spine[1], cmap='gray', vmin=0, vmax=255)
        axs[1, 0].set_title(f'(c) $\gamma = {gammas_spine[1]}$')
        axs[1, 0].axis('off')
        
        axs[1, 1].imshow(results_spine[2], cmap='gray', vmin=0, vmax=255)
        axs[1, 1].set_title(f'(d) $\gamma = {gammas_spine[2]}$')
        axs[1, 1].axis('off')
        
        plt.tight_layout()
        plt.savefig('fig_3_8_reproduction.png')
        print("Figura 3.8 reproduzida e salva como 'fig_3_8_reproduction.png'")

except Exception as e:
    print(f"Erro ao processar Figura 3.8: {e}")

try:
    img_aerial = cv2.imread('Fig0309(a)(washed_out_aerial_image).tif', cv2.IMREAD_GRAYSCALE)
    if img_aerial is None:
        print("Erro: Nao foi possivel carregar 'Fig0309(a)(washed_out_aerial_image).tif'")
    else:
        img_norm_aerial = img_aerial / 255.0
        
        c = 1
        gammas_aerial = [3.0, 4.0, 5.0]
        results_aerial = []
        
        for gamma in gammas_aerial:
            corrected = c * (img_norm_aerial ** gamma)
            corrected = np.clip(corrected * 255, 0, 255).astype(np.uint8)
            results_aerial.append(corrected)
            
        fig, axs = plt.subplots(2, 2, figsize=(10, 10))
        axs[0, 0].imshow(img_aerial, cmap='gray', vmin=0, vmax=255)
        axs[0, 0].set_title('(a) Original')
        axs[0, 0].axis('off')
        
        axs[0, 1].imshow(results_aerial[0], cmap='gray', vmin=0, vmax=255)
        axs[0, 1].set_title(f'(b) $\gamma = {gammas_aerial[0]}$')
        axs[0, 1].axis('off')
        
        axs[1, 0].imshow(results_aerial[1], cmap='gray', vmin=0, vmax=255)
        axs[1, 0].set_title(f'(c) $\gamma = {gammas_aerial[1]}$')
        axs[1, 0].axis('off')
        
        axs[1, 1].imshow(results_aerial[2], cmap='gray', vmin=0, vmax=255)
        axs[1, 1].set_title(f'(d) $\gamma = {gammas_aerial[2]}$')
        axs[1, 1].axis('off')
        
        plt.tight_layout()
        plt.savefig('fig_3_9_reproduction.png')
        print("Figura 3.9 reproduzida e salva como 'fig_3_9_reproduction.png'")

except Exception as e:
    print(f"Erro ao processar Figura 3.9: {e}")
