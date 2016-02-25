def answer(meetings):
    # your code here
    # sort meetings according to start times
    meetings = sorted(meetings, key = lambda x: x[0])
    
    # Dynamic Programming
    # f[i] is the maximum number of non-overlapping 
    # meetings between meetings[0] and meetings[i].
    # f[i] = max_{0<=j<i}{f[j]+d[i,j]}
    # d[i,j] = 1 if not overlap, otherwise 0
    f = [1] * len(meetings)
    for i in range(1, len(meetings)):
        for j in range(0, i):
            if overlap(meetings[j], meetings[i]):
                f[i] = max(f[i], f[j])
            else:
                f[i] = max(f[i], f[j] + 1)
                
    return f[len(meetings) - 1]
    
    
def overlap(interval1, interval2):
    # Input: interval1[0] <= interval2[0]
    if interval1[1] > interval2[0]:
        return True
    return False