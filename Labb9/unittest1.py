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
                return_str = exception.message + " "
                while not q.isEmpty():
                    return_str += q.dequeue()

            return return_str

        prompts_and_answers = [
            ["Na", "Formeln är syntaktiskt korrekt"],
            ["H2O", "Formeln är syntaktiskt korrekt"],
            ["Si(C3(COOH)2)4(H2O)7", "Formeln är syntaktiskt korrekt"],
            ["Na332", "Formeln är syntaktiskt korrekt"]]

        for p_and_a in prompts_and_answers:

            self.assertEqual(start_test(p_and_a[0]), p_and_a[1])



if __name__=='__main__':
    unittest.main()