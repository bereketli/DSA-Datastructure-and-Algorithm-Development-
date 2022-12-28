def traffic(seq, start):
    n = len(seq)
    seq += seq
    index = -1
    soln =0
    for i in range(n):
        if index == -1 and seq[i] == start:
            index = i
        if index != -1 and seq[i] == "g":
            soln = max(soln, i - index)
            index = -1
    while index != -1:
        if index != -1 and seq[n] == "g":
            soln = max(soln, n - index)
            index = -1
        n +=1
    print(soln)
traffic("yrrgy","y")
        



        