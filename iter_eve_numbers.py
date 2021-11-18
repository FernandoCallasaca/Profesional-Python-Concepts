# creamos un iterador de numeros pares
class even_iterator:
   def __init__(self, max = None):
      self.max = None

   def __iter__(self):
      self.num = 0
      return self

   def __next__(self):
      if not self.max or self.num <= self.max:
         value = self.num
         self.num += 2
         return value
      else:
         raise StopIteration

def run():
   iter_object = even_iterator(10)
   iter_object.__iter__()
   for _ in range(10):
      print(iter_object.__next__())
      

if __name__ == '__main__':
   run()