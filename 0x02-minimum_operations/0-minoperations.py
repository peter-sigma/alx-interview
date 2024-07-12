#!/usr/bin/python3
'''
   Minimum operations coding challenge.
'''


def minOperations(n):
    '''
       Computes the fewest number of operations needed to give 
       result in n H characters.
    '''
    if not isinstance(n, int):
        return 0
    opperationsCount = 0
    clipboard = 0
    done = 1
    
    while done < n:
        if clipboard == 0:
            clipboard = done
            done += clipboard
            opperationsCount += 2
        elif n - done > 0 and (n - done) % done == 0:
            clipboard = done
            done += clipboard
            opperationsCount += 2
        elif clipboard > 0:
            done += clipboard
            opperationsCount += 1
    return opperationsCount
