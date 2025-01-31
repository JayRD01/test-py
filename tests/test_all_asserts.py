import unittest

class AllAssertsTests(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(10,10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("No soy un numero")

    def test_assert_in(self):
        self.assertIn(10, [1,2,3,4,5,6,7,8,9,10])
        self.assertNotIn(2, [1,3,4,5,6,7,8,9,10])

    def test_assert_dicts(self):
        dict1 = {
            "Nombre":"Trump",
            "Edad":68
        }
        dict2 = {
            "Nombre":"Trump",
            "Edad":68
        }
        self.assertDictEqual(dict1, dict2)

    def test_assert_sets(self):
        set1 = {1,2,3}
        set2 = {1,2,3}

        self.assertSetEqual(set1,set2)

