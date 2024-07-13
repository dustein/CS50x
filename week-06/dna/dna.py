import csv
import sys


def main():

    database = []
    individuo = []

    # TODO: Check for command-line usage
    if (len(sys.argv) != 3):
        print("You must inform TWO parameter (csv file)")
        sys.exit()

    # TODO: Read database file into a variable
    #
    with open(sys.argv[1]) as arquivo_csv:
        dados = csv.DictReader(arquivo_csv)
        for linha in dados:
            database.append(linha)
        # print(database)

    # TODO: Read DNA sequence file into a variable
    #
    with open(sys.argv[2], encoding="utf-8") as sequencia:
        sequencia_pessoa = sequencia.read()

    # TODO: Find longest match of each STR in DNA sequence
    #
    lista_str = dados.fieldnames
    lista_str.remove('name')

    pessoa_dna = {}
    for tipo in lista_str:
        pessoa_dna[tipo] = longest_match(sequencia_pessoa, tipo)
    # print(pessoa_dna)

    # TODO: Check database for matching profiles
    #
    for pessoa in database:
        correspondencia = True
        for tipo in lista_str:
            if (int(pessoa[tipo]) != pessoa_dna[tipo]):
                correspondencia = False
                break

        if correspondencia == True:
            print(pessoa['name'])
            sys.exit()

    print('No match')

    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
