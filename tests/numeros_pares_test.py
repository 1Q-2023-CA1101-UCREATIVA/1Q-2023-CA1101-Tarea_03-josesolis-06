import numeros_pares
import importlib

def test_output(capsys):
    # arrange
    importlib.reload(numeros_pares)
    expected = "2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n"
    # act
    captured = capsys.readouterr()
    actual = captured.out
    # assert
    assert actual == expected, f"Los números esperados son \n{expected}, pero su programa imprime: \n{actual}"
