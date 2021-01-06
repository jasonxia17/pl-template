from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase
from code_feedback import Feedback

from language_definition import generateLanguage

from nltk.parse.generate import generate

MAX_LENGTH_TO_CHECK = 16

class Test(PLTestCase):
    @points(1)
    @name("Check that regular expression is correct")
    def test_0(self):
        studentL = {"".join(s) for s in generate(self.st.cfg, depth=MAX_LENGTH_TO_CHECK + 5)}
        # The "+ 5" is for wiggle room, since not every rule will add a new terminal symbol to the output

        studentL = {s for s in studentL if len(s) <= MAX_LENGTH_TO_CHECK}
        correctL = generateLanguage(MAX_LENGTH_TO_CHECK)

        falsePositives = studentL.difference(correctL)
        if falsePositives:
            Feedback.add_feedback("Your CFG generated the string "
                                  f"'{min(falsePositives, key=lambda s: len(s))}', "
                                  "which is not in the language.")
            return
        
        falseNegatives = correctL.difference(studentL)
        if falseNegatives:
            Feedback.add_feedback("Your CFG did not generate the string "
                                  f"'{min(falseNegatives, key=lambda s: len(s))}', "
                                  "which is in the language.")
            return
        
        Feedback.set_score(1)
