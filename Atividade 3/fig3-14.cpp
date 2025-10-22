#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>

int main() {
    // Carrega a imagem original em escala de cinza
    cv::Mat img_dollar = cv::imread("Fig0314(a)(100-dollars).tif", cv::IMREAD_GRAYSCALE);

    if (img_dollar.empty()) {
        std::cerr << "Erro: Nao foi possivel carregar a imagem 'Fig0314(a)(100-dollars).tif'" << std::endl;
        return -1;
    }

    // Array para armazenar os 8 planos de bits
    cv::Mat bit_planes[8];

    // Itera por cada bit, de 0 (LSB) a 7 (MSB)
    for (int k = 0; k < 8; ++k) {
        // Cria uma imagem vazia para o plano de bit
        bit_planes[k] = cv::Mat::zeros(img_dollar.size(), CV_8U);

        // Itera por cada pixel da imagem
        for (int i = 0; i < img_dollar.rows; ++i) {
            for (int j = 0; j < img_dollar.cols; ++j) {

                // 1. Pega o valor do pixel
                uchar pixel_value = img_dollar.at<uchar>(i, j);

                // 2. Isola o k-ésimo bit ( (pixel >> k) & 1 )
                //    Se o bit for 1, o resultado é 1. Se for 0, o resultado é 0.
                bool bit_is_set = (pixel_value >> k) & 1;

                // 3. Define o pixel do plano de bit como 255 (branco) se o bit estiver 
                //    definido, ou 0 (preto) caso contrário.
                if (bit_is_set) {
                    bit_planes[k].at<uchar>(i, j) = 255;
                }
                // (Nao e necessario um 'else', pois a imagem ja foi inicializada com zeros)
            }
        }

        // Salva a imagem do plano de bit
        std::string filename = "bit_plane_" + std::to_string(k + 1) + ".png";
        cv::imwrite(filename, bit_planes[k]);
    }

    std::cout << "Planos de bits de 1 a 8 salvos como 'bit_plane_1.png' a 'bit_plane_8.png'" << std::endl;

    // Opcional: Mostrar as imagens em uma grade (requer mais código de UI)
    // Para simplificar, este exemplo apenas salva os arquivos.

    return 0;
}
