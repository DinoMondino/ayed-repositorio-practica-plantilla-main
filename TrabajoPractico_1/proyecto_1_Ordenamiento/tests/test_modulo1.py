# Archivo de test para realizar pruebas unitarias del modulo1
import random
import time 
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from proyecto_1_Ordenamiento.modules.modulo1 import ord_burbuja, ord_quicksort, radix_sort


class SortingTest:
    def __init__(self):
        self.cant=range(1,1001,100)
        self.tiempo_burbuja=[]
        self.tiempo_quicksort=[]
        self.tiempo_radixsort=[]
        self.tiempos_ordenados=[]


    def medir_tiempo(self,funcion_ordenar, lista):
       tiempo_inicial=time.time()
       funcion_ordenar(lista.copy())
       return time.time()-tiempo_inicial

    def generar_lista_random(self,cant_elementos):
       return [random.randint(10000,99999) for i in range(cant_elementos)]

    def test_algoritmos(self):
       cant=range(1,1001,100)
       for i in cant:
          lista_random=self.generar_lista_random(i)
          self.tiempo_burbuja.append(self.medir_tiempo(ord_burbuja,lista_random))
          self.tiempo_quicksort.append(self.medir_tiempo(ord_quicksort,lista_random))
          self.tiempo_radixsort.append(self.medir_tiempo(radix_sort,lista_random))
          self.tiempos_ordenados.append(self.medir_tiempo(sorted,lista_random))



if __name__=="__main__":
    test=SortingTest()
    test.test_algoritmos()

def test_algoritmos(self):
    cant = range(1, 1001, 100)
    for i in cant:
        lista_random = self.generar_lista_random(i)
        self.tiempo_burbuja.append(self.medir_tiempo(ord_burbuja, lista_random))
        self.tiempo_quicksort.append(self.medir_tiempo(ord_quicksort, lista_random))
        self.tiempo_radixsort.append(self.medir_tiempo(radix_sort, lista_random))
        self.tiempos_ordenados.append(self.medir_tiempo(sorted, lista_random))

    # Imprimir los resultados después de la prueba
    print("Tiempos de ejecución para el algoritmo de Burbuja:")
    print(self.tiempo_burbuja)

    print("\nTiempos de ejecución para el algoritmo de Quicksort:")
    print(self.tiempo_quicksort)

    print("\nTiempos de ejecución para el algoritmo de Radix Sort:")
    print(self.tiempo_radixsort)

    print("\nTiempos de ejecución para el método sorted de Python:")
    print(self.tiempos_ordenados)