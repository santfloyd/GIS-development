"""
mostrar los algoritmos disponibles
"""

for alg in QgsApplication.processingRegistry().algorithms():
    print(alg.id(), '->', alg.displayName()) #identificador y nombre