# verify if it is a palindrome word
def is_palindrom(word: str) -> bool:
   # first replace 
   word = word.replace(" ", '').lower()
   return(word == word[::-1])

def run():
   # enter a word
   word = input('Enter a word to veryfy if its palindrome: ')
   print(is_palindrom(100))

if __name__ == '__main__':
   run()
