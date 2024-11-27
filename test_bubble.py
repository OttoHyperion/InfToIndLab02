import lib
import pytest

class TestBubbleSort:

    # Позитивный тест с корректными данными. Возвращает отсортированный массив
    def test_positive_bubble_sort(self):
        assert lib.bubble_sort([1, 8, 4, 2]) == [1, 2, 4, 8]

    # Негативный тест с пустым массивом. Вызывается исключение ValueErrorм
    def test_negative_bubble_sort(self):
        with pytest.raises(ValueError):
            lib.bubble_sort([])
