#include <stdint.h>
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
        //printf("Couldn`t open %s", card);
        printf("Could Not Open Card");
        return 0;
    }
    // While there's still data left to read from the memory card
    uint8_t buffer[512];
    int file_num = 0;
    while (fread(&buffer, sizeof(BLOCK_SIZE), 1, card) == BLOCK_SIZE)
    {
        //if tiver esses bytes no bloco de 512KB, é o início de um jpg
        if (buffer[0] == 0xff & buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0))
        {
            // Create JPEGs from the data
            FILE* imagem = fopen(imagem, "w");
            fprintf(imagem, "%03i.jpg", file_num);
            fwrite(&buffer, sizeof(BLOCK_SIZE), 1, imagem);
            fclose(imagem);
            file_num++;

        }
    }
    fclose(card);
}
