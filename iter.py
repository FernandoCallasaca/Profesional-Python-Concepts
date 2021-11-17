def iter_func():
   lista = [1, 2, 3]
   # convert to a iter object
   l = iter(lista)
   # recorrer cada elemento del iter
   while True:
      try:
         element = next(l)
         print(element)
      except StopIteration:
         break

def run():
   iter_func()

if __name__ == '__main__':
   run()