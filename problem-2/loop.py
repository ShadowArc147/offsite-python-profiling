import cProfile

testcode = '''
output = []
for a in (1, 3, 5, 7, 9, 11, 13):
    for b in (2, 4, 6, 8, 10, 12 , 14):
        output.append((a, b))
'''

if __name__ == "__main__":
    cProfile.run(testcode)