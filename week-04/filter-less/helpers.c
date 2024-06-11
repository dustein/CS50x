#include "helpers.h"
#include <math.h>

int sepia_round(float pixel);

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
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

//funcao sepia round e maximo 255
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
