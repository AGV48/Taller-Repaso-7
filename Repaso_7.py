from dataclasses import dataclass

@dataclass
class Elemento:
    nombre: str = ''

    def __eq__(self, other) -> bool:
        return self.nombre == other.nombre
    
    def __str__(self) -> str:
        return self.nombre
        
class Conjunto:

    Contador:int = 0
    
    def __init__(self, nombre) -> None:
        self.lista_elementos: list = []
        self.nombre: str = nombre
        Conjunto.Contador += 1
        self.__id: int = Conjunto.Contador
    
    @property
    def id(self):
        return self.__id
    
    def contiene(self, obj: Elemento) -> bool:
        return any(e == elemento for e in self.elementos)
    
    def agregar_elemento(self, obj: Elemento):
        if not self.contiene(obj):
            self.lista_elementos.append(obj)

    def __add__(self, other):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {other.nombre}")
        for elemento in self.lista_elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        for elemento in other.lista_elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto
    
@classmethod
    def intersectar(cls, c1, c2):
        interseccion = [elemento for elemento in c1.lista_elementos if c2.lista_elementos.contiene(elemento)]
        conjunto_interseccion = Conjunto(f"{c1.nombre} INTERSECTADO {c2.nombre}")
        conjunto_interseccion.elementos = interseccion
        return conjunto_interseccion

    def __str__(self):
        elementos_str = ', '.join(elemento.nombre for elemento in self.lista_elementos)
        return f"({elementos_str})"