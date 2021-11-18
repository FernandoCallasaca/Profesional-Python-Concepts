# Creamos un metodo de duplicados con for y cosas aprendidas
def remove_duplicates(lista):
   list_duplicates = []
   for i in lista:
      if i not in list_duplicates:
         list_duplicates.append(i)
   return list_duplicates

# creamos una funcion para eliminar repetidos
func_remove_duplicates = lambda lista: list(set(lista))

def run():
   L = [1, 2, 3, 3, 5]
   print(func_remove_duplicates(L))

if __name__ == '__main__':
   run()