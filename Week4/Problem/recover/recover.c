#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdint.h>
#include <cs50.h>

// Create the variable type
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // TODO
    // Check for two arguments
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE");
        return 1;
    }
    // Open the image
    FILE *inpointer = fopen(argv[1], "r");

    // Check if it can be opened
    if (!inpointer)
    {
        printf("Error: Cannot open file\n");
        return 1;
    }

    // We use unsigned as we only want to store positive int
    unsigned char buffer[512];
    // And initialize the variable to go through
    int counter = 0;
    // Initialize output pointer in NULL as we start without pictures
    FILE *outpointer = NULL;
    // Prepare the memory to receive the picture
    char *filename = malloc(8 * sizeof(char));

    // Look for the JPEG
    while (fread(buffer, sizeof(char), 512, inpointer))
    {
        // Look for the start of the image
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // Close the output file for memory
            if (counter > 0)
            {
                fclose(outpointer);
            }

            // Write the filenames
            sprintf(filename, "%03i.jpg", counter);

            // Open the outpointer to write
            outpointer = fopen(filename, "w");

            // Incremedebnt the counter
            counter++;
        }

        // Check if there's a valid input
        if (outpointer != NULL)
        {
            fwrite(buffer, sizeof(char), 512, outpointer);
        }
    }
    free(filename);
    fclose(outpointer);
    fclose(inpointer);
}