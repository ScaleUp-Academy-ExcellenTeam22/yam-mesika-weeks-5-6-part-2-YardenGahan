"""
This is the generator version to interleave.
"""


def interleave(*iter_param):
    for tup in zip(*iter_param):
        yield list(tup)


for x in interleave('abc', [1, 2, 3], ('!', '@', '#')):
    print(x)
