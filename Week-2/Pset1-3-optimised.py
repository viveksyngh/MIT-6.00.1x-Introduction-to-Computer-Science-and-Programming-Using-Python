s = 'zsgckcqptaqr'
longest_substr = substr = ""
prev_char = 0 
for char in s :
    if ord(char) >= prev_char : # ord() returns ASCII Value of 'char'
        substr += char
    else :
        if len(substr) > len(longest_substr) :
            longest_substr = substr
        substr = "" + char
    prev_char = ord(char)
if len(substr) == len(s) : # when 's' itself is in increasing order
    longest_substr = s
elif len(substr) > len(longest_substr) : # To capture the end of the string
    longest_substr = substr
print "Longest substring in alphabetical order is: " + longest_substr
     