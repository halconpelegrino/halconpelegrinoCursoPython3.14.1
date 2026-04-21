from main import saludo


def test_saludo():
    assert saludo("Ana") == "Hola, Ana desde VS Code"
