import re

#determine a pattern and search through the text file for any instances of that patter appearing

num_total_matches = 0
pattern1 = r"[0-9]{1}help"
pattern2 = r"[0-9]{1}me"
    
print("finding file")
with open('random.txt', 'rt') as f:
    print("Opened File")
    print("searching for patterns")
    for line in f:
        line = line.lower()  # make sure our text is all lowercase 
        for pattern in [pattern1, pattern2]:
            # Find all occurrences of the pattern in the string
            matches = re.findall(pattern, line)

                # Count the number of matches
            num_matches = len(matches)
            num_total_matches += num_matches
                
    if num_total_matches == 0:
        print ("No Matches")
    else:
        print ("Pattern Matches =" + ' ' + str(num_total_matches))
            
