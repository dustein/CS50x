// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // TODO: Copy header from input file to output file
    // fread(void *ptr, size_t size, size_t count, FILE *stream)
    // copiando o header que vai se repetir no arquivo de output
    // reserva espaco memoria pro header de 44 bytes
    uint8_t header[HEADER_SIZE];
    fread(header, HEADER_SIZE, 1, input);
    fwrite(header, HEADER_SIZE, 1, output);

    // TODO: Read samples from input file and write updated data to output file
    // criar um buffer para colocar os sample bits temporariamente
    int16_t buffer;
    // usar um while para ler sample por sample ate que nao haja mais, ate seja 0
    while (fread(&buffer, sizeof(int16_t), 1, input) != 0)
    {
        // multiplica pelo fator que altera o volume
        buffer = buffer * factor;
        // gravar o pedacinho modificado no novo arquivo
        fwrite(&buffer, sizeof(int16_t), 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}
