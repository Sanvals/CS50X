#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // Change all black pixels to a color of your choosing
    for (int row = 0; row < width; row++)
    {
        for (int column = 0; column < height; column++)
        {
            int r = image[column][row].rgbtRed;
            int g = image[column][row].rgbtGreen;
            int b = image[column][row].rgbtBlue;

            if (r == 0 && g == 0 && b == 0)
            {
                image[column][row].rgbtRed = 5;
                image[column][row].rgbtGreen = 160;
                image[column][row].rgbtBlue = 56;
            }
        }
    }
}
