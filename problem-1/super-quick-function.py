import re
import time
from tqdm import tqdm

num_total_matches = 0
pattern1 = r"[0-9]{1}help"
pattern2 = r"[0-9]{1}me"
start = time.time()
    
print("Finding File")

with open('random.txt', 'rt') as f:
    print("Opened File")
    print("Searching For Patterns")
    for line in tqdm(f, total=1_000_000):
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
end = time.time()
print("Time taken = " + str(end-start) + "s")
            
