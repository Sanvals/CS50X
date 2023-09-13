#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // asks for the user's name
    string name = get_string("What's your name? ");

    // outputs the user name
    printf("hello %s\n", name);
}