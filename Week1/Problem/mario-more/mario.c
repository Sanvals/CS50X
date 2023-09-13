#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // ask the user for the pyramid's height
    int height;
    do
    {
        height = get_int("Height: ");
    }
    while (height <= 0 || height >= 9);

    // start the loop for the pyramid
    for (int level = 1; level <= height; level++)
    {
        int spaces = height - level;

        // Print spaces
        for (int i = 0; i < spaces; i++)
        {
            printf(" ");
        }

        // Print left hashes
        for (int i = 0; i < level; i++)
        {
            printf("#");
        }

        // Print gap
        printf("  ");

        // Print right hashes
        for (int i = 0; i < level; i++)
        {
            printf("#");
        }

        printf("\n");
    }
}