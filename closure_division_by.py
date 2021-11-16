def make_division_by(n):
   def division_by(x):
      return x / n
   return division_by

def run():
   try:
      number = [int(i) for i in input().split()]
      assert len(number) == 2, "Solo debes agregar 2 números"
      division_by = make_division_by(number[1])
      print(division_by(number[0]))
   except ValueError:
      print("Ingresa valores enteros")
   finally:
      print("Program finished")

if __name__ == '__main__':
   run()