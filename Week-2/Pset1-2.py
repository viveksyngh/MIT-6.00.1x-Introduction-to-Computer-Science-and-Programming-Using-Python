s = 'azcbobobegghakl'
sub_string = 'bob'
sub_len = len(sub_string)
count = 0
for i in range(0, len(s) - sub_len + 1) :
    print i
    print s[i : i + sub_len]
    if s[i : i + sub_len] == sub_string :
        count = count + 1
print("Number of times bob occurs is: " + str(count))

    