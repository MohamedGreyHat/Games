def substract(L):
    print "> "
    for i in L:
        print "> ", i 
    t = []
    for i in range(len(L)) :
        for j in range(i+1, len(L)) :
            if  [L[i],L[j]] not in t :
                t.append([L[i], L[j]])
    for v in t : 
        print "> ", 
        for i in v :
            print  i, 
        print 

substract([1, 2, 3, 5])

            
