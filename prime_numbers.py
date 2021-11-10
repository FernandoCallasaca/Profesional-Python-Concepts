def is_prime(number: int) -> int:
   if number <= 1:
      return True
   midle: int = number // 2
   is_prime: bool = True
   for i in range(2, midle +1):
      if (number % i == 0):
         is_prime = False
         break
   return is_prime

def run():
   # here we have an error before run the python module with module mypy
   number: int = (input("Enter a number: "))
   print(is_prime(number))

if __name__ == '__main__':
   run()