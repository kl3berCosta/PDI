#include <opencv2/opencv.hpp>
#include <iostream>
#include <string>
#include <vector>

int main() {
    cv::Mat img_dollar = cv::imread("Fig0314(a)(100-dollars).tif", cv::IMREAD_GRAYSCALE);

    if (img_dollar.empty()) {
        std::cerr << "Erro: Nao foi possivel carregar a imagem 'Fig0314(a)(100-dollars).tif'" << std::endl;
        return -1;
    }

    cv::Mat bit_planes[8];
    for (int k = 0; k < 8; ++k) {
        bit_planes[k] = cv::Mat::zeros(img_dollar.size(), CV_8U);
        for (int i = 0; i < img_dollar.rows; ++i) {
            for (int j = 0; j < img_dollar.cols; ++j) {
                uchar pixel_value = img_dollar.at<uchar>(i, j);
                bool bit_is_set = (pixel_value >> k) & 1;
                if (bit_is_set) {
                    bit_planes[k].at<uchar>(i, j) = 255;
                }
            }
        }
    }
    std::cout << "Planos de bits calculados." << std::endl;

    int rows = img_dollar.rows;
    int cols = img_dollar.cols;
    int canvas_rows = rows * 3;
    int canvas_cols = cols * 3;

    cv::Mat canvas = cv::Mat::zeros(canvas_rows, canvas_cols, CV_8U);

    std::vector<cv::Rect> rois;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            rois.push_back(cv::Rect(j * cols, i * rows, cols, rows));
        }
    }

    img_dollar.copyTo(canvas(rois[0]));

    for (int k = 0; k < 8; ++k) {
        bit_planes[k].copyTo(canvas(rois[k + 1]));
    }

    std::string output_filename = "figura_3_14_combinada.png";
    if (cv::imwrite(output_filename, canvas)) {
        std::cout << "Imagem combinada salva como '" << output_filename << "'" << std::endl;
    } else {
        std::cerr << "Erro ao salvar a imagem combinada." << std::endl;
        return -1;
    }

    return 0;
}
