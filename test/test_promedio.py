import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from promedio import promedio
from promedio import promedio

# Caso correcto
def test_promedio_correcto():
    assert promedio([10, 20, 30]) == 50

# Caso límite
def test_promedio_un_elemento():
    assert promedio([5]) == 5

# Caso error - lista vacía
def test_promedio_lista_vacia():
    with pytest.raises(ValueError):
        promedio([])

# Caso error - tipo incorrecto
def test_promedio_tipo_incorrecto():
    with pytest.raises(TypeError):
        promedio("no es lista")
