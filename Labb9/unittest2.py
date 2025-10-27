import unittest
from main import *

class TestMoleculeMethods(unittest.TestCase):

    def test_prompts_and_answers(self):

        def start_test(input_str):

            try:

                q = LinkedQ()

                for char in input_str:
                    q.enqueue(char)

                is_molecule(q)

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
            ["2", "Felaktig gruppstart vid radslutet 2"],
            ["Na", "Formeln är syntaktiskt korrekt"],                   # single atom
            ["H2O", "Formeln är syntaktiskt korrekt"],                  # simple molecule
            ["Si(C3(COOH)2)4(H2O)7", "Formeln är syntaktiskt korrekt"], # complex nested
            ["(H)2", "Formeln är syntaktiskt korrekt"],                 # minimal parentheses with number
            ["(H)", "Saknad siffra vid radslutet"],                     # missing number after parenthesis
            ["(H2(O2)3)4", "Formeln är syntaktiskt korrekt"],           # nested parentheses
            ["()", "Felaktig gruppstart vid radslutet )"],                           # empty parentheses
            ["H2(O2", "Saknad högerparentes vid radslutet"],             # missing closing parenthesis
            ["(H2)1", "För litet tal vid radslutet"],                   # number 1 not allowed
            ["Na332", "Formeln är syntaktiskt korrekt"],                # large number
            ["C12H22O11", "Formeln är syntaktiskt korrekt"],            # multi-digit numbers
            ["C(H2O)2(OH)3", "Formeln är syntaktiskt korrekt"],         # multiple groups with parentheses
            ["(Na(Cl)2)3", "Formeln är syntaktiskt korrekt"],           # nested parentheses with numbers
            ["H2O2", "Formeln är syntaktiskt korrekt"],                 # peroxide molecule
            ["H2O2O", "Formeln är syntaktiskt korrekt"],                # molecule ending with atom
            ["(H2O)2Fe3", "Formeln är syntaktiskt korrekt"],            # multiple groups
            ["C(H)2(O)2N", "Formeln är syntaktiskt korrekt"],           # mixed single atoms and groups
            ["(H2(O)2)2", "Formeln är syntaktiskt korrekt"],            # nested with multiple digits
            ["(Xx)2", "Okänd atom vid radslutet )2"],                   # unknown atom in parentheses

        ]

        for p_and_a in prompts_and_answers:

            self.assertEqual(start_test(p_and_a[0]), p_and_a[1])



if __name__=='__main__':
    unittest.main()