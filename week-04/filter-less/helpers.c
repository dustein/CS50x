#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int pixel_red;
    int pixel_green;
    int pixel_blue;

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int actual_pixel = RGBTRIPLE image[i][j];
            pixel_red = actual_pixel.rgbtRed;
            pixel_gree = actual_pixel.rgbtGreen;
            pixel_blue = actual_pixel.rgbtBlue;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
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
