from django.test import TestCase
from indexapp.models import Cableoperadores, Proyectos

class ProyectosModelTest(TestCase):

    def setUp(self):
        self.cableoperador = Cableoperadores.objects.create(
            nombre="Proyecto Test",
            nombre_largo="Descripción del proyecto de prueba"
        )

    def test_proyecto_creation(self):
        self.assertEqual(self.cableoperador.nombre, "Proyecto Test")
        self.assertEqual(self.cableoperador.nombre_largo, int)
