#include "helpers.h"
#include <math.h>

int sepia_round(float pixel);
void swap(RGBTRIPLE *p, RGBTRIPLE *q);

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int pixel_red;
    int pixel_green;
    int pixel_blue;
    int new_color;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            pixel_red = image[i][j].rgbtRed;
            pixel_green = image[i][j].rgbtGreen;
            pixel_blue = image[i][j].rgbtBlue;
            new_color = round((pixel_red + pixel_green + pixel_blue) / 3.0);
            image[i][j].rgbtRed = new_color;
            image[i][j].rgbtGreen = new_color;
            image[i][j].rgbtBlue = new_color;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    int pixel_red;
    int pixel_green;
    int pixel_blue;
    float sepiaRed;
    float sepiaGreen;
    float sepiaBlue;
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            pixel_red = image[i][j].rgbtRed;
            pixel_green = image[i][j].rgbtGreen;
            pixel_blue = image[i][j].rgbtBlue;
            // make sepia
            sepiaRed = .393 * pixel_red + .769 * pixel_green + .189 * pixel_blue;
            sepiaGreen = .349 * pixel_red + .686 * pixel_green + .168 * pixel_blue;
            sepiaBlue = .272 * pixel_red + .534 * pixel_green + .131 * pixel_blue;

            image[i][j].rgbtRed = sepia_round(sepiaRed);
            image[i][j].rgbtGreen = sepia_round(sepiaGreen);
            image[i][j].rgbtBlue = sepia_round(sepiaBlue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width / 2; j++)
        {
            swap(&image[i][j], &image[i][width - 1 - j]);
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    float contador;
    int pixel_red, pixel_green, pixel_blue;
    // Create a copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            contador = 1;
            pixel_red = image[i][j].rgbtRed;
            pixel_green = image[i][j].rgbtGreen;
            pixel_blue = image[i][j].rgbtBlue;
            if (i - 1 >= 0 && j - 1 >= 0)
            {
                // pixel top esquerda
                pixel_red += image[i - 1][j - 1].rgbtRed;
                pixel_green += image[i - 1][j - 1].rgbtGreen;
                pixel_blue += image[i - 1][j - 1].rgbtBlue;
                contador++;
            }
            if (i - 1 >= 0)
            {
                // pixel top centro
                pixel_red += image[i - 1][j].rgbtRed;
                pixel_green += image[i - 1][j].rgbtGreen;
                pixel_blue += image[i - 1][j].rgbtBlue;
                contador++;
            }
            if (i - 1 >= 0 && j + 1 < width)
            {
                // pixel top direita
                pixel_red += image[i - 1][j + 1].rgbtRed;
                pixel_green += image[i - 1][j + 1].rgbtGreen;
                pixel_blue += image[i - 1][j + 1].rgbtBlue;
                contador++;
            }
            if (j - 1 >= 0)
            {
                // pixel esquerda
                pixel_red += image[i][j - 1].rgbtRed;
                pixel_green += image[i][j - 1].rgbtGreen;
                pixel_blue += image[i][j - 1].rgbtBlue;
                contador++;
            }
            if (j + 1 < width)
            {
                // pixel direita
                pixel_red += image[i][j + 1].rgbtRed;
                pixel_green += image[i][j + 1].rgbtGreen;
                pixel_blue += image[i][j + 1].rgbtBlue;
                contador++;
            }
            if (i + 1 < height && j - 1 >= 0)
            {
                // pixel down esquerda
                pixel_red += image[i + 1][j - 1].rgbtRed;
                pixel_green += image[i + 1][j - 1].rgbtGreen;
                pixel_blue += image[i + 1][j - 1].rgbtBlue;
                contador++;
            }
            if (i + 1 < height)
            {
                // pixel down centro
                pixel_red += image[i + 1][j].rgbtRed;
                pixel_green += image[i + 1][j].rgbtGreen;
                pixel_blue += image[i + 1][j].rgbtBlue;
                contador++;
            }
            if (i + 1 < height && j + 1 < width)
            {
                // pixel down direita
                pixel_red += image[i + 1][j + 1].rgbtRed;
                pixel_green += image[i + 1][j + 1].rgbtGreen;
                pixel_blue += image[i + 1][j + 1].rgbtBlue;
                contador++;
            }

            pixel_red = (int) round(pixel_red / contador);
            pixel_green = (int) round(pixel_green / contador);
            pixel_blue = (int) round(pixel_blue / contador);
            copy[i][j].rgbtRed = pixel_red;
            copy[i][j].rgbtGreen = pixel_green;
            copy[i][j].rgbtBlue = pixel_blue;
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            image[i][j] = copy[i][j];
        }
    }
    // image[i][j].rgbtRed = copy[i][j].rgbtRed;
    // image[i][j].rgbtGreen = copy[i][j].rgbtGreen;
    // image[i][j].rgbtBlue = copy[i][j].rgbtBlue;
    return;
}

// funcao sepia round e maximo 255
int sepia_round(float pixel)
{
    int good = round(pixel);
    if (good > 255)
    {
        return 255;
    }
    else
    {
        return good;
    }
}

// funcao swap
void swap(RGBTRIPLE *p, RGBTRIPLE *q)
{
    RGBTRIPLE temp = *p;
    *p = *q;
    *q = temp;
}
