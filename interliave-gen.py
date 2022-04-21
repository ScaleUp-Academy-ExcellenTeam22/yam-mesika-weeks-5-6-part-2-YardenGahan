"""
This is the generator version to interleave.
"""


def interleave(*iter_param):
    # Returns interleave list of 3 given objects.
    # Arguments: iter_param - undefined number of objects. can be tuple,list,string.
    for tup in zip(*iter_param):
        yield list(tup)


for x in interleave('abc', [1, 2, 3], ('!', '@', '#')):
    print(x)
