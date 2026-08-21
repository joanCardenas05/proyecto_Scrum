from src.app import sumar, saludar


def test_sumar():
    assert sumar(2, 3) == 5


def test_saludar():
    assert saludar("Stefy") == "Hola, Stefy!"
