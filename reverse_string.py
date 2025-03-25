def main():
    word = input("Input: ")
    print("Output: ", end="")
    reversed_str(word)


def reversed_str(word):
    for i in range(len(word) - 1, -1, -1):
        print(word[i], end="")
    print()


main()