import ingredientes
import importlib

def test_output(capsys):
    # arrange
    importlib.reload(ingredientes)
    expected = "1 pan\n2 tomate\n3 lechuga\n4 mantequilla\n5 salsa\n"
    # act
    captured = capsys.readouterr()
    actual = captured.out
    # assert
    assert actual == expected, f"La salida esperada es: \n{expected}\n\n, pero su programa imprime: \n{actual}"