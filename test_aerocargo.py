import unittest
from aerocargo import validar_matrices, evaluar_balance

class TestAeroCargo(unittest.TestCase):
    
    def test_validacion_correcta(self):
        # Caso típico: matrices regulares 2x2 con valores correctos
        cargas = [[100, 200], [300, 400]]
        capacidades = [[500, 500], [500, 500]]
        self.assertTrue(validar_matrices(cargas, capacidades))
        
    def test_validacion_pesos_negativos(self):
        # Caso límite: simulamos un error de digitación con un peso negativo (-200)
        cargas = [[100, -200], [300, 400]]
        capacidades = [[500, 500], [500, 500]]
        self.assertFalse(validar_matrices(cargas, capacidades))
        
    def test_evaluar_balance_impar(self):
        # Caso límite: matriz con 3 columnas (impar). El código debe ignorar la columna central.
        cargas = [[100, 800, 100], [200, 900, 200]]
        resultado = evaluar_balance(cargas, tolerancia=50.0)
        self.assertTrue(resultado['estado_balance'])
        self.assertEqual(resultado['desbalance_lateral'], 0.0)

if __name__ == '__main__':
    unittest.main()
