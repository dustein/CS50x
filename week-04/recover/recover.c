#include <stdio.h>
#include <stdlib.h>

//tamanho do bloco de memoria do buffer
const int BLOCK_SIZE = 512;

int main(int argc, char *argv[])
{
     // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }
    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("Couldn`t open %s", card);
        return 0;
    }
    // While there's still data left to read from the memory card
    uint8_t buffer[BLOCK_SIZE];
    while (fread(buffer, 1, BLOCK_SIZE, card) == BLOCK_SIZE)
    {
        // Create JPEGs from the data
        if (buffer[0] == 0xff & buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0))
        {

        }
    }
}
