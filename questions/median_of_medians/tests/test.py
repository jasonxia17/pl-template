from pl_helpers import name, points, not_repeated
from pl_unit_test import PLTestCaseWithPlot, PLTestCase
from code_feedback import Feedback
from functools import wraps


class Test(PLTestCaseWithPlot):
    @points(1)
    @name("groups")
    def test_0(self):
        if Feedback.check_numpy_array_allclose('groups', self.ref.groups, self.st.groups):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name("medians")
    def test_1(self):
        if Feedback.check_numpy_array_allclose('medians', self.ref.medians, self.st.medians):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name("pivot")
    def test_2(self):
        if Feedback.check_scalar('pivot', self.ref.pivot, self.st.pivot):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name("left_side")
    def test_3(self):
        if Feedback.check_numpy_array_allclose('left_side', self.ref.left_side, self.st.left_side):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name("right_side")
    def test_4(self):
        if Feedback.check_numpy_array_allclose('right_side', self.ref.right_side, self.st.right_side):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name("next_arr")
    def test_5(self):
        if Feedback.check_numpy_array_allclose('next_arr', self.ref.next_arr, self.st.next_arr):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

    @points(1)
    @name("next_k")
    def test_6(self):
        if Feedback.check_scalar('next_k', self.ref.next_k, self.st.next_k):
            Feedback.set_score(1)
        else:
            Feedback.set_score(0)

Test.total_iters = 10
