from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase
from code_feedback import Feedback

from language_definition import isInLanguage, alphabet

import re
import itertools

MAX_LENGTH_TO_CHECK = 16

class Test(PLTestCase):
    @points(1)
    @name("Check that regular expression is correct")
    def test_0(self):
        allowed_chars = {'(', ')', '+', '*', 'e', ' '}.union(alphabet)
        for char in self.st.reg_exp:
            if char not in allowed_chars:
                Feedback.add_feedback(f"Your regular expression contains the character '{char}', "
                                      "which is not permitted.")
                return
        
        processed_re = self.st.reg_exp.replace('e', '').replace('+', '|'). replace(' ', '')
        try:
            compiled_re = re.compile(processed_re)
        except re.error:
            Feedback.add_feedback("Your regular expression failed to compile.")
            return


        for str_length in range(0, MAX_LENGTH_TO_CHECK + 1):
            for char_list in itertools.product(alphabet, repeat=str_length):
                x = "".join(char_list)
                
                in_language = isInLanguage(x)
                match = compiled_re.fullmatch(x)
                
                if in_language and not match:
                    Feedback.add_feedback(f"Your regular expression did not match the string '{x}', "
                                          "which is in the language.")
                    return
                elif not in_language and match:
                    Feedback.add_feedback(f"Your regular expression matched the string '{x}', "
                                          "which is not in the language.")
                    return
        
        Feedback.set_score(1)
