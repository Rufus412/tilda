import unittest
from main import *

class TestMoleculeMethods(unittest.TestCase):

    def test_is_num(self):
        self.assertTrue(is_num("12"))

        with self.assertRaises(Syntaxfel):
            is_num("1")

    def test_is_lower(self):
        self.assertTrue(is_lowercase_letter("a"))
        self.assertFalse(is_lowercase_letter("A"))
    
    def test_is_upper(self):
        self.assertTrue(is_uppercase_letter("A"))
        self.assertFalse(is_uppercase_letter("a"))
    
    def test_is_atom(self):

        correct_atom = LinkedQ()
        false_atom = LinkedQ()


        for char in "Ab":
            correct_atom.enqueue(char)

        for char in "AB":
            false_atom.enqueue(char)


        self.assertTrue(is_atom(correct_atom))

        with self.assertRaises(Syntaxfel):
            is_atom(false_atom)
    
    def test_is_molecule(self):

        correct_molecule = "Ab123"
        false_molecule = "Ab012"

        self.assertTrue(is_molecule(correct_molecule))
        self.assertFalse(is_molecule(false_molecule))


if __name__=='__main__':
    unittest.main()