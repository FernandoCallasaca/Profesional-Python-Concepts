# Create the decorator
def decorator(function):
   # wrapper = envoltura
   def wrapper(text):
      return function(text).upper()
   return wrapper

@decorator
def message(text):
   return f'{text}, recibiste un mensaje'

def run():
   print(message('fernando'))


if __name__ == '__main__':
   run()