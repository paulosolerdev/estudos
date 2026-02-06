# def average(values):
#     """Calcula a média aritmética de uma lista de números.

#     >>> print(average([20, 30, 70]))
#     40.0
#     """

#     return sum(values) / len(values)


# import doctest
# doctest.testmod()


#==============================================================#


import unittest

def average(values):
    return sum(values) / len(values)

class TestStatisticaFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)

if __name__ == '__main__':
    unittest.main()
