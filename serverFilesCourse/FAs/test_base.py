from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase
from code_feedback import Feedback

from language_definition import isInLanguage, alphabet

import re
import itertools

MAX_LENGTH_TO_CHECK = 16

class Test(PLTestCase):
    @points(1)
    @name("Check that DFA/NFA is correct")
    def test_0(self):
        # Check type

        for str_length in range(0, MAX_LENGTH_TO_CHECK + 1):
            for char_list in itertools.product(alphabet, repeat=str_length):
                x = "".join(char_list)
                
                in_language = isInLanguage(x)
                accepted = self.st.fa.accepts_input(x)
                
                if in_language and not accepted:
                    Feedback.add_feedback(f"Your DFA/NFA did not accept the string '{x}', "
                                          "which is in the language.")
                    return
                elif not in_language and accepted:
                    Feedback.add_feedback(f"Your DFA/NFA accepted the string '{x}', "
                                          "which is not in the language.")
                    return
        
        Feedback.set_score(1)
