def main():
    word = input("Input: ")
    print("Output: ", "".join(reversed(word)))


main()

# "".join - Joins each character from the iterator into single string
# reversed(word) - iterator that goes through word backwards, without creating a new string immediately