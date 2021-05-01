import unittest
from fast import *

# После начало тестирования стало понятно, что fastq фильтратор надо переписать
# К сожалению мне не удалось сделать нормальные тесты для fastq фильтратора.
# Получилось это сделать только для нескольких функций из него.

class Test_filtration_for_length(unittest.TestCase):

    def test_filtration_for_length_true(self):
        result = filtration_for_length("ACACACACACAC", 5)
        self.assertTrue(result, True)

    def test_filtration_for_length_false(self):
        result = filtration_for_length("ACACACACACAC", 15)
        self.assertFalse(result, False)

class Test_gc_counter_filter(unittest.TestCase):

    def test_filtration_for_length_true(self):
        gc_result = gc_counter_filter("ACACACACACAC", 49, 51, False)
        self.assertTrue(gc_result)

    def test_filtration_for_length_true_max_flag(self):
        gc_result = gc_counter_filter("ACACACACACAC", 49, 53, True)
        self.assertTrue(gc_result, True)

    def test_filtration_for_length_false(self):
        gc_result = gc_counter_filter("ACACACACACAC", 51, 53, False)
        self.assertFalse(gc_result, False)

    def test_filtration_for_length_false_max_flag(self):
        gc_result = gc_counter_filter("ACACACACACAC", 51, 53, True)
        self.assertFalse(gc_result, False)


if __name__ == '__main__':
    unittest.main()