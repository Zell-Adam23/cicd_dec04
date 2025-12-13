import sys
import math
from pathlib import Path

root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))

from app import add, subtract, multiply, division, log, square, sin, cos, sqroot, percent

def test_add():
    assert add(5,6) == 11

def test_add2():
    assert add(5,6) != 10

def test_sub():
    assert subtract(10, 5) == 5

def test_sub2():
    assert subtract(11, 4) != 8

def test_mult():
    assert multiply(3,4) == 12

def test_mult2():
    assert multiply(2,7) == 14

def test_div():
    assert division(12,4) == 3

def test_div2():
    assert division(16, 4) != 7

def test_log():
    assert log(100) == 10

def test_log2():
    assert log(8, 2) != 2

def test_square():
    assert square(9) == 81

def test_cos():
    assert cos(math.pi) == -1.0

def test_sin():
    assert sin(math.pi) == 1.0

def test_sqroot():
    assert sqroot(16) == 4.0

def test_percent():
    assert percent(23,100) == 23.0