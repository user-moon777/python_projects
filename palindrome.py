def main():
  word = input("Input: ").strip().lower()
  reverse_word = word[::-1]

  if word == reverse_word:
    print("Palindrome")
  else:
    print("Not Palindrome")


main()
