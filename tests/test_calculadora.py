import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "Calculadora de notas.py"


def run_calculator(inputs):
    result = subprocess.run(
        [sys.executable, str(SCRIPT)],
        input="\n".join(map(str, inputs)) + "\n",
        text=True,
        capture_output=True,
        check=False,
    )
    return result


def test_two_grades_calculates_average_and_extremes():
    result = run_calculator([2, 15, 10])

    assert result.returncode == 0
    assert "Esta es tu mejor nota 15.0" in result.stdout
    assert "Esta es tu peor nota 10.0" in result.stdout
    assert "Este es tu promedio 12.5" in result.stdout


def test_ten_grades_calculates_average_and_extremes():
    result = run_calculator([10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 19])

    assert result.returncode == 0
    assert "Esta es tu mejor nota 19.0" in result.stdout
    assert "Esta es tu peor nota 1.0" in result.stdout
    assert "Este es tu promedio 6.4" in result.stdout


def test_invalid_number_of_grades_is_reported():
    result = run_calculator([1])

    assert result.returncode == 0
    assert "cantidad de notas inválida" in result.stdout
