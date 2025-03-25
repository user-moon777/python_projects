def main():
    word = input("Input: ")
    print("Output: ", end="")
    reversed_str(word)


def reversed_str(word):
    for i in range(1, len(word) + 1):
        print(word[-i], end="")
    print()


main()