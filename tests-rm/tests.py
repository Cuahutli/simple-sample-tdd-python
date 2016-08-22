import unittest

from unittest.mock import Mock #python3
from borrarFicheros import BorraFicheros

class Test(unittest.TestCase):
    def test_cuando_hayDosFicherosConElMismoTamanyo_entonces_borrarUnFichero(self):
        fichero_repetido = Mock()
        fichero_repetido.nombre = "fichero_repetido"
        fichero_repetido.tamanyo = 100

        directorio = Mock()
        directorio.ruta = "./directorio_de_prueba"
        directorio.ficheros = [fichero_repetido, fichero_repetido]

        borrado = BorraFicheros()
        borrado.borra_ficheros_en(directorio)

        directorio.borraFichero.assert_called_with(fichero_repetido)
