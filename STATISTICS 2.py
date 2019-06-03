# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 14:39:43 2019

@author: panda4
"""
from scipy import stats

#A test is conducted which is consisting of 20 MCQs (multiple choices questions) with every MCQ having its four options out of which only one is correct. Determine the probability that a person undertaking that test has answered exactly 5 questions wrong.
n = 20
p = 0.75
P(X = 5) = stats.binom.pmf(5, n, p)



#A die marked A to E is rolled 50 times. Find the probability of getting a “D” exactly 5 times.
n = 50
p = 0.2
P(X = 5) =  stats.binom.pmf(5, n, p)




# Two balls are drawn at random in succession without replacement from an urn containing 4 red balls and 6 black balls. Find the probabilities of all the possible outcomes.
P(R) = 0.4
P(B) = 0.6
If two balls are drawn at random, following are the possibilities.
RR = (4/10) * (3/9)
RB = (4/10) * (6/10)
BR = (6/10) * (4/10)
BB = (6/10) * (5/9)