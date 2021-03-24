# HMM_bruteforcemethod
### What is the Hidden Markov Model (HMM) 
It is a Markov Process in which probablity of outcome depends also on a hidden state. 
It is memory-less. Future states are only affected by current states. 
###
![image](https://user-images.githubusercontent.com/81331767/112393995-53177880-8cd2-11eb-899d-6387d2ce3d57.png)
###
Figure 1: Visual representation of HMM using a fair and loaded die
### 
So for instance if we rolled, [5 2]. There would 2^2 possibilities of that sequence happening either using a fair die or loaded die. The possiblities would FF, FL, LF, LL. F being fair and L being loaded. We could figure out which possibility has the highest probablity of occuring using Markovian therom. The theorem states, 
####
P(x) = P0 * P(e0|s0) * P01 * P(e1|s1) .... 
####
Where P(x) is the probablity of the sequence happening. P0 is the initial probablity. P(e0|s0) is the probability of rolling a number given a fair or loaded die is used. P01 is the probablity of going from state 0 to state 1. 
####
In our example of [5,2] the probablity of getting that sequence using fair die twice is ... 
####
x = [5,2]
P(x) = P0 * P(e0|s0) * P01 * P(e1|s1)
     = 0.5 * (1/6) * 0.9 * (1/6) 
     = 0.125
###
Doing this for the other possibilities and comparing them would yield the highest probablity. This is sort of the gist of using the brute force method on paper, and the code follows the same logic. For more clearance on what HMM really is please check out the video below, as it really helped me understand :) 
[Hidden Markov Model : Data Science Concepts](https://www.youtube.com/watch?v=fX5bYmnHqqE&ab_channel=ritvikmath)
