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
    FILE *cartao_memoria = fopen(argv[1], "r");
    if (cartao_memoria == NULL)
    {
        //printf("Couldn`t open %s", card);
        printf("Could Not Open Card");
        return 0;
    }
    // While there's still data left to read from the memory card
    //aloca memoria de 512KB pro buffer
    uint8_t buffer[BLOCK_SIZE];
    //aloca memoria pra os filenames
    char filename[8];
    //imagem sera o novo arquivo no qual vamos escrever
    FILE* imagem_pointer =  NULL;
    int file_num = 0;
    //vamos ler o card, usando tamanho BLOCK_SIZE, 1 por vez,
    while (fread(&buffer, BLOCK_SIZE, 1, cartao_memoria) == 1)
    {
        //if tiver esses bytes no bloco de 512KB, é o início de um jpg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && ((buffer[3] & 0xf0) == 0xe0))
        {
            if (file_num != 0)
            {
                fclose(imagem_pointer);
            }
            //iniciar arquivo
            fprintf(filename, "%03i.jpg", file_num);
            imagem_pointer = fopen(filename, "w");
            file_num++;
        }
        // se encontrou jpg comecar a escrever no arquivo
        if (file_num != 0)
        {
            fwrite(&buffer, BLOCK_SIZE, 1, imagem_pointer);
            }
    fclose(cartao_memoria);
    fclose(imagem_pointer);
}
