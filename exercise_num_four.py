"""#4 Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
    - Palíndromos
    - Anagramas
    - Isogramas
"""
def is_palindromes (word:str)->bool:
    return word == word[::-1]

def are_anagrams(word_one:str,word_two:str)->bool:
    return sorted(word_one) == sorted(word_two)

def is_isogram(word:str)->bool:
    return len(set(word)) == len(word)

def get_word(label:str)->str:
    while True:
        word = input(label).strip()
        if not word:
            print("Please enter a word")
        elif not word.isalpha():
            print("Only letters are allowed (no numbers or spaces).")
        else:
            return word.lower()


print("""Let's analyze two different words and see if they are:
      - Palindromes
      - Anagrams
      - Isograms
      """)
word_one = get_word("Insert the first word: ")
word_two = get_word("Insert the second word: ")
        
print("\nYour words are palindromes?")
print(f"Your word {word_one} is a palindrome" if is_palindromes(word_one) else f"Your word {word_one} is not a palindrome")
print(f"Your word {word_two} is a palindrome" if is_palindromes(word_two) else f"Your word {word_two} is not a palindrome")

print("\nYour words are anagrams?")
print("Your words are anagrams" if are_anagrams(word_one,word_two) else "Your words are not anagrams")

print("\nYour words are Isograms?")
print(f"Your word {word_one} is an isogram" if is_isogram(word_one) else f"Your word {word_one} is not an isogram")
print(f"Your word {word_two} is an isogram" if is_isogram(word_two) else f"Your word {word_two} is not an isogram")
