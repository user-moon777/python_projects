def main():
    word = input("Input: ")
    print("Output: ", end="")
    reversed_str(word)


def reversed_str(word):
    reversed_str = ""
    for char in word:
        reversed_str = char + reversed_str
    print(reversed_str)


main()