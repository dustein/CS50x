#include "helpers.h"

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
            pixel_red = new_color;
            pixel_green = new_color;
            pixel_blue = new_color;
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
