#include <cs50.h>
#include <stdio.h>

int checklength(int number);
int getlength(long number);
int checksum(long number, int digits);
void companyname(long number, int digits);

int main(void)
{
    long number = get_long("Number: ");

    // Get the numeric length
    int nlength = getlength(number);

    // Check length, checksum
    if (checklength(nlength) + checksum(number, nlength) == 2)
    {
        // Retrieve the company name
        companyname(number, nlength);
    }
    else
    {
        printf("INVALID\n");
    }
}

int getlength(long number)
{
    // Extract the number of digits
    int i = 0;
    long check = number;
    while (check > 0)
    {
        check = check / 10;
        i++;
    }
    return i;
}

int checklength(int number)
{
    // Test that the length matches certain values
    if (number == 13 || number == 15 || number == 16)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int checksum(long number, int digits)
{
    // Store the variables
    long n = number;
    int d = digits;

    // Split the sum operations into two
    int sumA = 0;
    int sumB = 0;

    // Skip odd numbers
    for (int i = 0; i < d; i = i + 2)
    {
        // First add the last digit
        int modB = n % 10;
        sumB = sumB + modB;

        // Jump to the next digit
        n = n / 10;
        int modA = (n % 10) * 2;

        // if the digit * 2 is > 10, mod again
        if (modA >= 10)
        {
            modA = 1 + (modA % 10);
        }

        // Jump to the second position
        n = n / 10;
        sumA = sumA + modA;
    }

    // Check the congruency to 0
    if ((sumA + sumB) % 10 != 0)
    {
        return 0;
    }
    else
    {
        return 1;
    }
}

void companyname(long number, int digits)
{
    // Create a variable to store the number
    long n = number;
    int d = digits;

    for (int i = 0; i < (d - 2); i++)
    {
        n = n / 10;
    }

    if (n == 34 || n == 37)
    {
        printf("AMEX\n");
    }
    else if (n >= 51 && n <= 55)
    {
        printf("MASTERCARD\n");
    }
    else if (n / 10 == 4)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
