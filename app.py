from Repaso_7 import Elemento, Conjunto

nombre1 = Elemento(nombre="A")
nombre2 = Elemento(nombre="B")
nombre3 = Elemento(nombre="C")
nombre4 = Elemento(nombre="D")
nombre5 = Elemento(nombre="D")

comparar = nombre1 == nombre2
print(comparar)

conjunto = Conjunto(nombre="Conjunto AA")
print(conjunto.Contador, conjunto.nombre)
print(conjunto.id)

conjunto2 = Conjunto(nombre="Conjunto BB")
print(conjunto2.Contador, conjunto2.nombre)
print(conjunto2.id)


print(conjunto.lista_elementos)
conjunto.agregar_elemento(nombre1)
print(conjunto.lista_elementos)
conjunto.agregar_elemento(nombre3)
print(conjunto.lista_elementos)

print(conjunto2.lista_elementos)
conjunto2.agregar_elemento(nombre2)
print(conjunto2.lista_elementos)
conjunto2.agregar_elemento(nombre4)
print(conjunto2.lista_elementos)
conjunto2.agregar_elemento(nombre5)
print(conjunto2.lista_elementos)

lista = conjunto + conjunto2
print(lista)


