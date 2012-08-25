#!/usr/bin/env python
"""
Search for the substring in a string, and if exists return the index of the first match

Can be implemented using the Rabin-Karp algorithm using Hashes
"""
def substring(pattern, string):
    """
    replicate the .find() String function

    O(n)
    """
    pattern_length = len(pattern)

    if pattern_length > len(string):
        return -1

    # loop through string, add one to the range because we need to start at the first position
    # if the pattern and string are the same, we would get range(0)
    for i in range(len(string) - pattern_length + 1):
        for j in range(pattern_length):
            if pattern[j] != string[i+j]:
                break
            elif pattern_length == j + 1: # add one to the zero-based substring index
                return i

    # we did not find a match
    return -1

if __name__ == '__main__':
    print 'find(): %s' % 'hello'.find('lo')
    print 'substring(): %s' % substring('lo', 'hello')

    print 'find(): %s' % 'hello'.find('ello')
    print 'substring(): %s' % substring('ello', 'hello')

    print 'find(): %s' % 'hello'.find('hello')
    print 'substring(): %s' % substring('hello', 'hello')

    print 'find(): %s' % 'hello'.find('helloo')
    print 'substring(): %s' % substring('helloo', 'hello')
