def print_move(fr, to) :
    print ("Moving From " + str(fr) + " to " + str(to))

def Towers(n, fr, to, spare) :
    if n == 1 :
        print_move(fr, to)
    else :
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to , spare)
        Towers(n-1, spare, to, fr)
        
Towers(3, "A", "B", "C")