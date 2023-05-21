def q0q1q2q3(a,i):
    if a[i]  == "a":
        i += 1
        if a[i]  == "a":
            i += 1
            if a[i]  == "a":
                return True
    else:
        return False
def q0q1q4(a,i): 
    if(a[i] == "b" or a[i] == "c"):
        return True    
   
       
def check(qq):
    newqq = qq
    while type(newqq) != str:
        newqq = str(input("Escolha uma string"))
    
    states = 0    
    terminal = True

    if q0q1q2q3(newqq,states) == True:
        if q0q1q4(newqq,states) == True:
            while newqq[states] == "b" or newqq[states] == "c":
                states += 1
            if newqq[states] != "b" or newqq[states] != "c" or newqq[states] !="a":
                    return False
            return terminal
    else:
        pass
    
    if q0q1q4(newqq,states) == True:
        while newqq[states] == "b" or newqq[states] == "c":
            states += 1
        if q0q1q2q3(newqq,states) == True:
            return terminal
        else:
            return False
    else:
        pass
    
    #if q0q1q2q3(newqq,states) == False:
    #    return False
        
    '''else:
        terminal = False
        print(terminal)
        return terminal
    
    if q0q1q4(newqq,states) == True:
        while(newqq[states] == "b" or newqq[states] == "c"):
            states += 1 '''

print(check("bccccccbcbcaaa"))