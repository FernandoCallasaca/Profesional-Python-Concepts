# Aquí creamos nuestro decorador para todo mayuscula
def to_upper_of(func):
   def wrapper(*args, **kwargs):
      return func(*args, **kwargs).upper()
   return wrapper

@to_upper_of
def to_upper(name = 'Fernando', lastname1 = 'Callasaca', lastname2 = 'Acuña'):
   return(f"The best people of all the world is: {name} {lastname1} {lastname2}")

# function to calculate the sum of x values
def sum_of(func):
   def wrapper(*args, **kwargs):
      suma = 0
      for i in func(*args, **kwargs):
         assert type(i) == int, 'Necesitamos un número entero para sumar'
         suma += i
      return suma
   return wrapper

@sum_of
def suma(*args):
   return args

# Llamamos a nuestra función
def run():
   # print(to_upper() + '\n')
   # print(to_upper('Angela', 'Delagado', 'Moscoso'))
   print(suma(1,2,3,4,5,6))
   # print(suma(1,2,3,4,5,'6'))

# Creamos nuestro entrypoint
if __name__ == '__main__':
   run()