s = 'zsgckcqptaqr'
#max_length = 0
longest_substr = ""
prev_char = 0 
#count = 0
substr = ""
for char in s :
    if ord(char) >= prev_char :
        #count += 1
        substr += char
    else :
        if len(substr) > len(longest_substr) :
            #max_length = count
            longest_substr = substr
        substr = "" + char
        #count = 1
    prev_char = ord(char)
if len(substr) == len(s) :
    longest_substr = s
elif len(substr) > len(longest_substr) :
    longest_substr = substr
print "Longest substring in alphabetical order is: " + longest_substr
     