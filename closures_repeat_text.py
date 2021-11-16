# Closure function
def repeat_string(x):
   
   # create the nested function
   def repeat(string):
      # we use a up scope
      assert type(string) == str, "Solo puedes utilizar cadenas"
      return string * x
   
   # return the nested function
   return repeat

def run():
   number_string = input()
   number_string = number_string.split()
   # we create the variable repeat that have a function
   repeat = repeat_string(int(number_string[1]))
   repeat(number_string[0])
   # print(repeat(1))

if __name__ == '__main__':
   run()