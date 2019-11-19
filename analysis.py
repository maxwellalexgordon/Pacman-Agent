# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    #Explination: this modification reduces the chances of mis-stepping and travelling into a -10- area.
    # Garenteed moving forward will return a positive reward, greater than to the left
    answerDiscount = 0.9
    answerNoise = 0.01
    return answerDiscount, answerNoise

def question3a():
    #Reduce chance of mis-stepping.
    #less can go wrong when moving by -10

    answerDiscount = 0.1
    answerNoise = 0
    answerLivingReward = 0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3b():
    #increasing the noice increases the chance of a mistake.
    #negative living reward so player tries to achieve points fast.
    answerDiscount = 0.0001
    answerNoise = 0.3
    answerLivingReward = -0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3c():
    #longer path results in score being lower. due to living reward and discount
    #+1 very small compared to +10 with a high discount
    #low chance to mistakes while moving
    answerDiscount = 0.9
    answerNoise = 0.000001
    answerLivingReward = -0.5
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3d():
    #high discount so +10 is much greater reward(due to high living reward  and discount) making +1 a bad choice
    #high answer noice prevents taking risky path
    answerDiscount = 0.8
    answerNoise = 0.4
    answerLivingReward = 0.5
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question3e():
    #make being alive better than any possible reward
    #high discount rate prevents +1 and +10 from being very valuable
    answerDiscount = 0.99
    answerNoise = 0.1
    answerLivingReward = +10
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'

def question8():
    answerEpsilon = None
    answerLearningRate = None
    return answerEpsilon, answerLearningRate
    # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
