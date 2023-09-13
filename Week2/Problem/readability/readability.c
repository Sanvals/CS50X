#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    printf("%s\n", text);

    // Initialize the variables for the formula
    float L = (count_letters(text) / (float) count_words(text)) * 100;
    float S = (count_sentences(text) / (float) count_words(text)) * 100;

    // Calculate the index
    int index = (int) round(0.0588 * L - 0.296 * S - 15.8);

    // Check against range values
    if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 0)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}

// Checking the amount of letters on the string
// By iterating through each character
// And checking if it's alpha
int count_letters(string text)
{
    int counter = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            counter++;
        }
    }
    return counter;
}

// Checking the amount of words on the string
// By iterating through each character
// And checking the spaces, then we add 1
int count_words(string text)
{
    int counter = 1;

    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == ' ')
        {
            counter++;
        }
    }
    return counter;
}

// Checking the amount of sentences on the string
// By iterating through each character
// And checking the special characters to account for sentences
int count_sentences(string text)
{
    int counter = 0;

    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i + 1] == '.' || text[i + 1] == '!' || text[i + 1] == '?')
        {
            counter++;
        }
    }
    return counter;
}