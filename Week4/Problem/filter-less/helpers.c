#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate through the height
    for (int column = 0; column < height; column++)
    {
        // Iterate thgough the width
        for (int row = 0; row < width; row++)
        {
            // Store the values for easy formulation
            int r = image[column][row].rgbtRed;
            int b = image[column][row].rgbtBlue;
            int g = image[column][row].rgbtGreen;

            int gray = round((r + b + g) / 3.0);

            // Turn the values into the calculated integer
            image[column][row].rgbtRed = gray;
            image[column][row].rgbtGreen = gray;
            image[column][row].rgbtBlue = gray;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    // Create the empty integers to operate
    int beforeRed, beforeGreen, beforeBlue;
    int afterRed, afterGreen, afterBlue;

    // Iterate through the height
    for (int column = 0; column < height; column++)
    {
        // Iterate through the width
        for (int row = 0; row < width; row++)
        {
            // Store the value of the position
            beforeRed = image[column][row].rgbtRed;
            beforeGreen = image[column][row].rgbtGreen;
            beforeBlue = image[column][row].rgbtBlue;

            // Calculate
            int sepiaRed = round(0.393 * beforeRed + 0.769 * beforeGreen + 0.189 * beforeBlue);
            int sepiaGreen = round(0.349 * beforeRed + 0.686 * beforeGreen + 0.168 * beforeBlue);
            int sepiaBlue = round(0.272 * beforeRed + 0.534 * beforeGreen + 0.131 * beforeBlue);

            // Check for limits
            // Red
            if (sepiaRed > 255)
            {
                image[column][row].rgbtRed = 255;
            }
            else
            {
                image[column][row].rgbtRed = sepiaRed;
            }

            // Green
            if (sepiaGreen > 255)
            {
                image[column][row].rgbtGreen = 255;
            }
            else
            {
                image[column][row].rgbtGreen = sepiaGreen;
            }

            // Blue
            if (sepiaBlue > 255)
            {
                image[column][row].rgbtBlue = 255;
            }
            else
            {
                image[column][row].rgbtBlue = sepiaBlue;
            }

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    // Iterate through the height
    for (int column = 0; column < height; column++)
    {
        // Iterate through half the image width
        for (int row = 0; row < width / 2; row++)
        {
            // Using a swap method
            // For red
            int tempRed = image[column][row].rgbtRed;
            image[column][row].rgbtRed = image[column][width - row - 1].rgbtRed;
            image[column][width - row - 1].rgbtRed = tempRed;

            // For Green
            int tempGreen = image[column][row].rgbtGreen;
            image[column][row].rgbtGreen = image[column][width - row - 1].rgbtGreen;
            image[column][width - row - 1].rgbtGreen = tempGreen;

            // For Blue
            int tempBlue = image[column][row].rgbtBlue;
            image[column][row].rgbtBlue = image[column][width - row - 1].rgbtBlue;
            image[column][width - row - 1].rgbtBlue = tempBlue;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // We first create a temporary image
    RGBTRIPLE temp[height][width];

    for (int column = 0; column < height; column++)
    {
        for (int row = 0; row < width; row++)
        {
            // Setting the initial value
            int tRed, tGreen, tBlue;
            tRed = tGreen = tBlue = 0;
            float counter = 0.00;

            // Get closeby pixels
            for (int x = -1; x < 2; x++)
            {
                for (int y = -1; y < 2; y++)
                {
                    int currentX = column + x;
                    int currentY = row + y;

                    // Check if it's valid
                    if (currentX < 0 || currentX > (height - 1) || currentY < 0 || currentY > (width - 1))
                    {
                        continue;
                    }

                    // Set the image
                    tRed += image[currentX][currentY].rgbtRed;
                    tGreen += image[currentX][currentY].rgbtGreen;
                    tBlue += image[currentX][currentY].rgbtBlue;

                    counter ++;
                }

                // Average the results
                temp[column][row].rgbtRed = round(tRed / counter);
                temp[column][row].rgbtGreen = round(tGreen / counter);
                temp[column][row].rgbtBlue = round(tBlue / counter);
            }
        }
    }

    // Copy the temporary image on the destination

    for (int column = 0; column < height; column++)
    {
        for (int row = 0; row < width; row++)
        {
            image[column][row].rgbtRed = temp[column][row].rgbtRed;
            image[column][row].rgbtGreen = temp[column][row].rgbtGreen;
            image[column][row].rgbtBlue = temp[column][row].rgbtBlue;
        }
    }
    return;
}
