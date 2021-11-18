# Crear 2 sets
set_A = set()
set_B = set()

# agregar elementos a los conjuntos
set_A.add(1)
set_A.add(2)
set_A.add(3)
set_A.add(4)
set_A.update([True, False, 10])

set_B.add(2)
set_B.add(15)
set_B.update([1, 8, 8], {10, 11})

# eliminamos el elemento 15 del conjunto 1
set_A.discard(15)
# eliminamos el elemento 8 del conjunto 2
set_B.remove(8)

# Realizamos operaciones

# union
set_union = set_A | set_B
# interseccion
set_interseccion = set_A & set_B
# diferencia A
set_diferencia_A = set_A - set_B
# diferencia B
set_diferencia_B = set_B - set_A
# diferencia simetrica
set_diferencia_simetrica = set_A ^ set_B


if __name__ == '__main__':
   # imprimimos todo
   # tipos
   print("Tipo de set_A: {0}".format(type(set_A)))
   print("Tipo de set_A: {0}".format(type(set_B)))
   print("Conjunto 1: ", set_A)
   print("Conjunto 1: ", set_B)
   print("Union: {0}".format(set_union))
   print("Interseccion: {0}".format(set_interseccion))
   print("Diferencia A: {0}".format(set_diferencia_A))
   print("Diferencia B: {0}".format(set_diferencia_B))
   print("Diferencia Simetrica: {0}".format(set_diferencia_simetrica))