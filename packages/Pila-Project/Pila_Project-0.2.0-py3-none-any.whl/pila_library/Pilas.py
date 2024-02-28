import nodo from Nodo
import random
class Pila:
    def __init__(self):
        self.top = None

    def apilar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.top is None:
            self.top = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.top
            self.top = nuevo_nodo
    
    def llenar_pila(self, n):
        self.n = n
        for _ in range(n):
            nuevo_nodo = Nodo(random.randint(-100,100))
            if self.top is None:
                self.top = nuevo_nodo
            else:
                nuevo_nodo.siguiente = self.top
                self.top = nuevo_nodo

    def desapilar(self):
        if self.top is None:
            print("La pila está vacía")
        else:
            valor = self.top.dato
            self.top = self.top.siguiente
            print(f"Elemento desapilado: {valor}")
        return valor

    def imprimir(self):
        actual = self.top
        pila = []
        while actual:
            pila.append(actual.dato)
            actual = actual.siguiente
        print(pila)

    def maximo(self):
        if self.top is None:
            print("La pila está vacía")
        else:
            max_valor = self.top.dato
            actual = self.top.siguiente
            while actual:
                if actual.dato > max_valor:
                    max_valor = actual.dato
                actual = actual.siguiente
            print(f"Número máximo en la pila: {max_valor}")
    
    def minimo(self):
        if self.top is None:
            print("La pila está vacía")
        else:
            min_valor = self.top.dato
            actual = self.top.siguiente
            while actual:
                if actual.dato < min_valor:
                    min_valor = actual.dato
                actual = actual.siguiente
            print(f"Número mínimo en la pila: {min_valor}")