import unittest

# Função Mutada (ordena de forma decrescente)
def ordenar_crescente(lista):
    n= len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return (lista)

# Função Mutada (ordena de forma decrescente)
def ordenar_decrescente(lista):
    n= len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1]: # Alteração na lógica para ordenação decrescente
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return (lista)

# Testes para a função ordenar_crescente
class TestOrdenarCrescente(unittest.TestCase):
    def test_ordenacao_crescente(self):
        lista = [5,3,8,1,2]
        self.assertEqual(ordenar_crescente(lista), [1,2,3,5,8])

    def test_ordenacao_vazia(self):
        lista = []
        self.assertEqual(ordenar_crescente(lista), [])

# Testes para a função ordenar_decrescente
class TestOrdenarDecrescente(unittest.TestCase):
    def test_ordenacao_decrescente(self):
        lista = [5,3,8,1,2]
        self.assertEqual(ordenar_decrescente(lista), [8,5,3,2,1])

    def test_ordenacao_vazia(self):
        lista = []
        self.assertEqual(ordenar_decrescente(lista), [])

if __name__ == '__main__':
    unittest.main()