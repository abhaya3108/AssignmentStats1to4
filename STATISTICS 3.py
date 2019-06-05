# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 20:16:23 2019

@author: panda4
"""
from scipy import stats

#Blood glucose levels for obese patients have a mean of 100 with a standard deviation of 15. A researcher thinks that a diet high in raw cornstarch will have a positive effect on blood glucose levels. A sample of 36 patients who have tried the raw cornstarch diet have a mean glucose level of 108. Test the hypothesis that the raw cornstarch had an effect or not.

H0: μ = 100
H1: μ > 100

Set up the significance level as 5% (0.05).

For this set of data: Zo(derived) = (108-100) / (15/√36)=3.20

For significance level(alpha) as 0.05, 
    Zo = stats.norm.ppf(0.95) = 1.65
    
Since Zo(derived) > Zo, so we will reject the Null hypothesis i.e. there is raw cornstarch effect. 

#In one state, 52% of the voters are Republicans, and 48% are Democrats. In a second state, 47% of the voters are Republicans, and 53% are Democrats. Suppose a simple random sample of 100 voters are surveyed from each state. What is the probability that the survey will show a greater percentage of Republican voters in the second state than in the first state?

 let P1 = the proportion of Republican voters in the first state, 
 P2 = the proportion of Republican voters in the second state,
 p1 = the proportion of Republican voters in the sample from the first state, 
 and p2 = the proportion of Republican voters in the sample from the second state. 
 The number of voters sampled from the first state (n1) = 100, 
 and the number of voters sampled from the second state (n2) = 100
 
 n1P1 = 100 * 0.52 = 52, n1(1 - P1) = 100 * 0.48 = 48, n2P2 = 100 * 0.47 = 47, and n2(1 - P2) = 100 * 0.53 = 53 
 are each greater than 10, the sample size is large enough.
 
 E(p1 - p2) = P1 - P2 = 0.52 - 0.47 = 0.05
 
 σd = sqrt{ [ P1(1 - P1) / n1 ] + [ P2(1 - P2) / n2 ] } 
σd = sqrt{ [ (0.52)(0.48) / 100 ] + [ (0.47)(0.53) / 100 ] } 
σd = sqrt (0.002496 + 0.002491) = sqrt(0.004987) = 0.0706

We need to find if the probability p1 - p2 is less than zero.
To find this probability, we need to transform the random variable (p1 - p2) into a z-score.

zp1 - p2 = (x - μp1 - p2) / σd = = (0 - 0.05)/0.0706 = -0.7082

p - value for zp1 - p2 = stats.norm.cdf(-0.7082) = 0.24

Therefore, the probability that the survey will show a greater percentage 
of Republican voters in the second state than in the first state is 0.24.

#You take the SAT and score 1100. The mean score for the SAT is 1026 and the standard deviation is 209. How well did you score on the test compared to the average test taker?

We need to find the z score in this case

Z = Xbar - mu / sigma = (1100 - 1026)/209 = 0.354

p - value = stats.norm.cdf(0.354) = 0.6383 or 63.83%

So, I scored 63.83% more than the average test taker






 