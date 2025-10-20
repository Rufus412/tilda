import unittest
from main import *

class TestMoleculeMethods(unittest.TestCase):

    def test_prompts_and_answers(self):

        def start_test(input_str):

            p_stack = []

            try:

                q = LinkedQ()

                for char in input_str:
                    q.enqueue(char)

                is_molecule(q, p_stack)

                return_str = "Formeln är syntaktiskt korrekt"

            except Syntaxfel as exception:
                return_str = exception.message
                if not q.isEmpty():
                    return_str += " "
                while not q.isEmpty():
                    return_str += q.dequeue()

            return return_str

        prompts_and_answers = [
            ["C(Xx4)5", "Okänd atom vid radslutet 4)5"],
            ["C(OH4)C", "Saknad siffra vid radslutet C"],
            ["C(OH4C", "Saknad högerparentes vid radslutet"],
            ["H2O)Fe", "Felaktig gruppstart vid radslutet )Fe"],
            ["H0", "För litet tal vid radslutet"],
            ["H1C", "För litet tal vid radslutet C"],
            ["H02C", "För litet tal vid radslutet 2C"],
            ["Nacl", "Saknad stor bokstav vid radslutet cl"],
            ["a", "Saknad stor bokstav vid radslutet a"],
            ["(Cl)2)3", "Felaktig gruppstart vid radslutet )3"],
            [")", "Felaktig gruppstart vid radslutet )"],
            ["2", "Felaktig gruppstart vid radslutet 2"]
        ]

        for p_and_a in prompts_and_answers:

            self.assertEqual(start_test(p_and_a[0]), p_and_a[1])



if __name__=='__main__':
    unittest.main()