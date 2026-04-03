import sys
 
str1 = sys.stdin.readline()
str2 = sys.stdin.readline()
 
num_deletable_symbols = 0
position_deletable_symbols = []
 
for index in range(len(str1)):
    if str1[0:index] + str1[index + 1 :] == str2:
        num_deletable_symbols += 1
        position_deletable_symbols.append(str(index + 1))
 
sys.stdout.write(f"{num_deletable_symbols}\n")
sys.stdout.write(" ".join(position_deletable_symbols))