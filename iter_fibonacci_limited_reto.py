import time

class Fibonacci_limited():

   def __init__(self, max):
      self.max = max

   def __iter__(self):
      self.n1 = 0
      self.n2 = 1
      self.counter = 0
      return self

   def __next__(self):
      if self.counter == 0:
         self.counter += 1
         return self.n1
      elif self.counter == 1:
         self.counter += 1
         return self.n2
      else:
         if self.counter < self.max:
            self.aux = self.n1 + self.n2
            self.n1, self.n2 = self.n2, self.aux
            self.counter += 1
            return self.aux
         else:
            raise StopIteration

if __name__ == '__main__':
   fibonnaci = Fibonacci_limited(10)
   for element in fibonnaci:
      print(element)
      time.sleep(0.5)