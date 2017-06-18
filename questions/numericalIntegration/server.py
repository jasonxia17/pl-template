#!/usr/bin/env python

# Do this so that division of one integer by another integer will - if the
# result is not an int - produce a float.

# Division in Python 2 and Python 3 is different:
# https://docs.python.org/3/howto/pyporting.html#division
#
# In particular:
#   5 / 2 == 2.5 in Python 3
#   5 / 2 == 2 in Python 2
#
# The following line makes it so you get Python 3 behavior even if you are
# still using Python 2. More information is here:
# https://www.python.org/dev/peps/pep-0238/
#
from __future__ import division

# Import python modules
import sys, json, random, math
import numpy as np
from scipy.integrate import quad

# This function returns the value of the integrand at the specified time.
def integrand(t,a,b):
    return a*np.exp(-b*t)

# This function generates the data for a question.
def getData(vid, options, questionDir):
    # Initialize random number generator by creating a local instance of
    # np.random.RandomState. The reason to create a local instance instead of
    # using the global instance is that the global instance is shared (maybe,
    # on some systems, for some calls...) and so would completely break
    # reproducibility.
    #
    # Use vid as the seed so that getData is a deterministic function of vid,
    # as is a PrairieLearn best practice for reproducibility. To use vid as the
    # seed, it needs to be converted to a 32-bit unsigned int. We do NOT do
    # this with "hash" because "hash" is often non-deterministic, depending on
    # your version of python.
    #
    # Common uses are:
    #   mynprandom.random_sample([size])
    #   mynprandom.random_integers(low[, high, size])
    #
    # More information:
    #   https://docs.scipy.org/doc/numpy/reference/routines.random.html
    #
    global mynprandom
    mynprandom = np.random.RandomState(int(vid,36))

    # Parameters
    #
    # Often we want floating-point numbers from a given interval. One way to
    # generate them would be to sample them uniformly at random:
    #
    # a = (1.0-0.1)*mynprandom.random_sample()+0.1;
    # b = (0.5-0.1)*mynprandom.random_sample()+0.1;
    # c = (15.0-5.0)*mynprandom.random_sample()+5.0;
    #
    # This is often a bad idea, however, because to give these parameters to
    # students you will have to print them to the screen with some number of
    # significant digits. If you are not careful, students will end up using
    # a parameter value that is different from what your code uses.
    #
    # For this reason, it is often better to sample with a specific number of
    # digits after the decimal place:
    #
    # Sample a number between 0.1 (i.e., 10/100) and 1.0 (i.e., 100/100) with
    # at most two digits after the decimal:
    a = mynprandom.random_integers(10,100)/100.0;
    # Sample a number between 0.1 and 0.5 with at most two digits after the
    # decimal:
    b = mynprandom.random_integers(10,50)/100.0;
    # Sample a number between 5 and 15 with at most one digit after the
    # decimal:
    c = mynprandom.random_integers(50,150)/10.0;

    # Answer
    theIntegral,theError = quad(integrand,0,c,args=(a,b))

    # Create params (you MUST be sure that the number of digits in the
    # string matches the number of digits to which you rounded params,
    # otherwise students will get a different set of params)
    params = {
        "a": str(a),
        "b": str(b),
        "c": str(c)
    }

    # Create trueAnswer
    trueAnswer = {
        # The actual answer
        "theIntegral": theIntegral,
        # The answer as a string with four digits after the decimal place, so
        # it can be displayed
        "theIntegralForDisplay": '{:.{indigits}{iwtype}}'.format(theIntegral,indigits=4,iwtype='f')
    }

    questionData = {
        "params": params,
        "trueAnswer": trueAnswer,
        "options": {},
    }

    return questionData

# This function grades a submitted answer.
def gradeAnswer(vid, params, trueAnswer, submittedAnswer, options):
    msg = ''

    # Get the true answer
    tru = trueAnswer['theIntegral']

    # Get the submitted answer
    sub = submittedAnswer.get('theIntegral')

    # Compare the true answer to the submitted answer. The reason to use
    # "try/except" is that the submitted answer may not be in the correct
    # format (or may not even exist). If the submitted answer can be
    # compared to the true answer using np.allclose, then it's either right
    # or wrong. If the submitted answer cannot even be compared ("except"),
    # then it's in the wrong format. It is VERY IMPORTANT to use try/except
    # when evaluating submitted answers.
    try:
        # Cast submitted answer as a floating-point number
        sub = float(sub)
        # Compare the true answer to the submitted answer
        if np.allclose(tru,sub,rtol=1e-03,atol=1e-03):
            # It is the same
            score = 1.0
        else:
            # It is not the same
            score = 0.0
            msg += 'The submitted answer is incorrect. '
    except:
        # Either the call to "float" or the call to "np.allclose" threw an
        # error, which means that the submitted answer has the wrong format.
        score = 0.0
        msg += 'The submitted answer is in the wrong format. '

    feedback = {
        'msg': msg
    }

    grading = {
        'score': score,
        'feedback': feedback,
    }

    return grading


########################
# The interface between PrairieLearn and your code. You can ignore
# this and, indeed, should not change it
#
def main():
    if len(sys.argv) != 2:
        raise Exception('Expected 2 argments, got %d' % len(sys.argv))
    json_inp = sys.stdin.read()
    inp = json.loads(json_inp)
    if sys.argv[1] == 'getData':
        outp = getData(inp['vid'], inp['options'], inp['questionDir'])
    elif sys.argv[1] == 'gradeAnswer':
        outp = gradeAnswer(inp['vid'], inp['params'], inp['trueAnswer'], inp['submittedAnswer'], inp['options'])
    else:
        raise Exception('Unknown command: %s' % sys.argv[1])
    json_outp = json.dumps(outp)
    sys.stdout.write(json_outp)

if __name__ == '__main__':
    main()

#
#
########################
