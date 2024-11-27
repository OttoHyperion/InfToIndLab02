import lib
import pytest

class TestEratosthenes:
    # Позитивный тест с корректными данными. Возвращает последовательность простых чисел до 20
    def test_positive_eratosthenes(self):
        assert lib.eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]

    # Негативный тест с n <= 0. Если мы подаем на вход n <= 0, то программа с Решетом Эратосфена выдает ошибку
    # Вызывается исключение ValueError
    def test_negative_eratosthenes(self):
        with pytest.raises(ValueError):
            lib.eratosthenes(-1)