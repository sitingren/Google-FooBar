import sys
def answer(minions):
    # your code here
# let M(1) be the first minion and M(i) be the i'th minion, 
# P(i) be the probability that the i'th minion does not speak, 
# T(i) being the time you have to wait to see if a minion speaks.
# the expected waiting time is:
#     T(1) + T(2)*P(1) + T(3)*P(1:2) + ... + T(n)*P(1:n-1)
# where P(a:b) = P(a)*P(a+1)*...*P(b). Now, since this is the optimal ordering, it should be the case that it gets worse (or equal) if I swap any two minions. 
# Somewhere in the sequence, we'll turn this:
#     ... + T(a)*P(1:a-1) + T(b)*P(1:a-1)P(a) + ...
# into this:
#     ... + T(b)*P(1:a-1) + T(a)*P(1:a-1)P(b) + ...
# The top one is smaller than or equal to the bottom one, so if I subtract one from the other we get:
#     P(1:a-1) * (T(a)-T(b) + T(b)P(a) - T(a)P(b)) <= 0
# After rearranging some terms we get:
#     T(a)/(1-P(a)) <= T(b)/(1-P(b))
    minions_expect = [(time / (numerator / float(denominator)) if numerator / float(denominator) != 0 else sys.maxint) for time, numerator, denominator in minions]
    print minions_expect
    get_expect = lambda x: minions_expect[x]
    return sorted(range(len(minions)), key = get_expect)