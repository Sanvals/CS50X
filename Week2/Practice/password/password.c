// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library

#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    string s = password;
    bool upperCase = false;
    bool lowerCase = false;
    bool number = false;
    bool symbol = false;
    for (int i = 0; i < strlen(s); i++)
    {
        if (isupper(s[i]))
        {
            upperCase = true;
        }
        else if (islower(s[i]))
        {
            lowerCase = true;
        }
        else if (isdigit(s[i]))
        {
            number = true;
        }
        else if (isgraph(s[i]))
        {
            symbol = true;
        }
    }
    if (upperCase && lowerCase && number && symbol)
    {
        return true;
    }
    else
    {
        return false;
    }
}
