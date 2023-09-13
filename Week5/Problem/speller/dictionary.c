// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 17576;

// Hash table
node *table[N];

// Word counter
int counter = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // Hash the word
    int hashV = hash(word);

    // Access the linked list on a given index
    node *n = table[hashV];

    // Go through the linked list checking against strcasecomp
    while (n != NULL)
    {
        if (strcasecmp(word, n->word) == 0)
        {
            return true;
        }
        n = n->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    long sum = 0;
    for (int i = 0; i < strlen(word); i++)
    {
        sum += tolower(word[i]);
    }
    return sum % N;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    // Open dictionary fily
    FILE *dictFile = fopen(dictionary, "r");

    // Check if it returns null
    if (dictFile == NULL)
    {
        return false;
    }

    // Load the word array
    char nextWord[LENGTH + 1];

    // Read the strings one at a time
    while (fscanf(dictFile, "%s", nextWord) != EOF)
    {
        // Create nodes for each word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }

        // Copy word into node using strcpy
        strcpy(n->word, nextWord);

        // Hash word
        int hashN = hash(nextWord);

        // Insert node into hash table at that location
        n->next = table[hashN];
        table[hashN] = n;
        counter++;
    }

    // Close the file
    fclose(dictFile);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    // Iterate over the hash table
    for (int i = 0; i < N; i ++)
    {
        // Get cursor
        node *n = table[i];

        // Loop through linked list
        while (n != NULL)
        {
            // Apply swap function
            node *tmp = n;
            n = n->next;
            free(tmp);
        }

        if (n == NULL && i == N - 1)
        {
            return true;
        }
    }
    return false;
}