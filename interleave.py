def interleave(*iter_param):
    # Returns interleave list of 3 given objects.
    # Arguments: iter_param - undefined number of objects. can be tuple,list,string.

    return [val for obj in zip(*iter_param) for val in obj]


print(interleave('abc', [1, 2, 3], ('!', '@', '#')))
