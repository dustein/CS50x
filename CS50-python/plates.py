def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if (len(s) < 2 or len(s) > 6):
        return False

    if not s[0:2].isalpha():
        return False

    if check_alfanum(s):
        return False

    if final_num(s):
        return False

    else:
        return True


# testar se a partr do primeior numero so haja numero e o prmero nao e zero
def final_num(word):
    # for i in range(len(word)):
    #     if word[i].isnumeric():
    #         numeros = word[i:]
    #         for numero in numeros:
    #             if numero == "0" or numero.isalpha():
    #                 return True
    found_a_number = False
    for letter in word:
        if letter.isnumeric():
            if not found_a_number and letter == "0":
                return True
            found_a_number = True
        elif found_a_number and letter.isalpha():
            return True

def check_alfanum(word):
    for letter in word:
        if letter.isalnum() == False:
            return True

# def two_letter(word):
#     if word[0:2].isalpha():
#         return True

# def min_len(word):
#     if 2 <= len(word) <= 6:
#         return True

main()
