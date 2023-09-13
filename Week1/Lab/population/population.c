#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // TODO: Prompt for start size
    int start;

    do
    {
        start = get_int("Start size: ");
    }
    while (start < 9);
    // TODO: Prompt for end size

    int end;

    do
    {
        end = get_int("End size: ");
    }
    while (end < start);
    // TODO: Calculate number of years until we reach threshold

    int yearRun = 0;
    int populationRun = start;

    if (start != end)
    {
        do
        {
            populationRun = populationRun + populationRun / 3 - populationRun / 4;
            yearRun ++;
        }
        while (populationRun < end);
    }
    else
    {
        yearRun = 0;
    }
    // TODO: Print number of years
    printf("Years: %i", yearRun);

}