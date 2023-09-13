// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string chain);

int main(int argc, string argv[])
{
    if (argc == 1 || argc != 2)
    {
        printf("Usage: ./no-vowels word\n");
        return 1;
    }
    else
    {
        printf("%s", replace(argv[1]));
        return 0;
    }
    printf("\n");
}

string replace(string s)
{
    string newWord = s;
    for (int i = 0; i < strlen(s); i++)
    {
        if (s[i] == 'a')
        {
            newWord[i] = '6';
        }
        else if (s[i] == 'e')
        {
            newWord[i] = '3';
        }
        else if (s[i] == 'i')
        {
            newWord[i] = '1';
        }
        else if (s[i] == 'o')
        {
            newWord[i] = '0';
        }
        else
        {
            newWord[i] = s[i];
        }
    }
    return newWord;
}