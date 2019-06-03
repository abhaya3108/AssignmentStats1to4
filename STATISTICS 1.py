# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#You survey households in your area to find the average rent they are paying. Find the standard deviation from the following data:
import statistics as st
rent = [1550,1700,900,850,1000,950]
st.stdev(rent)

#Find the variance for the following set of data representing trees in California (heights in feet):
heightOfTrees = [3, 21, 98, 203, 17, 9]
st.variance(heightOfTrees)

#In a class on 100 students, 80 students passed in all subjects, 10 failed in one subject, 7 failed in two subjects and 3 failed in three subjects. Find the probability distribution of the variable for number of subjects a student from the given class has failed in.
For a random student, 

The probability of failing in 0 subjects, P(X = 0) = 0.8

The probability of failing in 1 subjects, P(X = 1) = 0.1

The probability of failing in 2 subjects, P(X = 2) = 0.07

The probability of failing in 3 subjects, P(X = 3) = 0.03

The probability distribution can be shown as:

   X	 0	  1	       2	   3
 P(X)	0.8	 0.1	 0.07	 0.03
