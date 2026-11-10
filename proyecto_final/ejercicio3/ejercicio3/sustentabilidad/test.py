from django.test import SimpleTestCase
from .views import calcular_emisiones_carbono

class TestCalculoEmisiones(SimpleTestCase):
    """Pruebas unitarias automatizadas para el algoritmo de cálculo de huella de carbono."""

    def test_calculo_nominal_factor_predeterminado(self):
        """Valida la exactitud numérica con el factor de emisión por defecto (0.4)."""
        resultado = calcular_emisiones_carbono(100.0)
        self.assertEqual(resultado, 40.0)

    def test_calculo_nominal_factor_personalizado(self):
        """Valida la exactitud numérica con un factor de emisión específico."""
        resultado = calcular_emisiones_carbono(250.0, factor_emision=0.5)
        self.assertEqual(resultado, 125.0)

    def test_calculo_consumo_cero(self):
        """Valida el comportamiento en el límite con consumo cero."""
        resultado = calcular_emisiones_carbono(0.0)
        self.assertEqual(resultado, 0.0)

    def test_excepcion_consumo_negativo(self):
        """Valida que se eleve ValueError ante consumos fuera de rango (negativos)."""
        with self.assertRaises(ValueError):
            calcular_emisiones_carbono(-50.0)
