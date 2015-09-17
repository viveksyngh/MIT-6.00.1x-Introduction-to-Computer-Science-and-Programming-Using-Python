def sharp(x) :
    if x == 2 :
        return 2
    else :
        return sharp(x-1)**x

def num_digits(x) :
    return len(str(x))

print(num_digits(sharp(7)) + 2 * num_digits(sharp(6)) + num_digits(sharp(5)) + num_digits(sharp(4)))