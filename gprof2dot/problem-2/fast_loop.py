for x in range(3000000):
    [(a, b) for a in (1, 3, 5, 7, 9, 11) for b in (2, 4, 6, 8, 10, 12)]
    
# It spent less than a second in string, and never called list’s append method.
# Based on the profile, the list comprehension got more work done inside built-in code and didn’t rely on list or string to get the work done. 
