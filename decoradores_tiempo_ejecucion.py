from datetime import datetime

def execution_time(func):
   # *args no importa la cantidad de argumentos posicionales
   # **kwargs no importa la cantidad de argunentos nombrados
   def wrapper(*args, **kwargs):
      initial_time = datetime.now()
      func(*args, **kwargs)
      final_time = datetime.now()
      time_elapsed =  final_time - initial_time
      print(f"Pasaron {time_elapsed.total_seconds()} segundos")

   return wrapper

@execution_time
def random_func():
   for _ in range(1, 100000000):
      pass

@execution_time
def suma(a: int, b: int) -> int:
   return a + b

@execution_time
def saludo(nombre = 'Fernando'):
   print(f"Hola {nombre}")

def run():
   random_func()
   print()
   suma(5, 5)
   print()
   saludo()

if __name__ == '__main__':
   run()