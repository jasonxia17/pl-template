from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCase
from code_feedback import Feedback

from language_definition import isInLanguage

NUM_ELEMENTS_TO_CHECK = 20

class Test(PLTestCase):
    @points(1)
    @name("Elements of set are distinct")
    def test_0(self):
        num_distinct_elements = len({Feedback.call_user(self.st.getFoolingSetElement, i)
                                    for i in range(1, NUM_ELEMENTS_TO_CHECK + 1)})
        
        if num_distinct_elements == NUM_ELEMENTS_TO_CHECK:
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)
    
    @points(9)
    @name("All pairs of distinct elements can be distinguished")
    def test_1(self):
        for i in range(1, NUM_ELEMENTS_TO_CHECK + 1):
            for j in range(i + 1, NUM_ELEMENTS_TO_CHECK + 1):
                x = Feedback.call_user(self.st.getFoolingSetElement, i)
                y = Feedback.call_user(self.st.getFoolingSetElement, j)
                z = Feedback.call_user(self.st.getDistinguishingSuffix, i, j)

                if not (isInLanguage(x + z) ^ isInLanguage(y + z)):
                    Feedback.add_feedback(
                        f"When i = {i} and j = {j}, the suffix\n\n"
                        f"z = '{z}'\n\n"
                        f"fails to distinguish the two fooling set elements\n\n"
                        f"x = '{x}'\n"
                        f"y = '{y}'"
                    )
                    Feedback.set_score(0)
                    return
        
        Feedback.set_score(1)
