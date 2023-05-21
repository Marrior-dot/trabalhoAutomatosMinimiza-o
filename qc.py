def q0q1q2(a,i):
    if a[i]  == "a":
        return True
def q0q1q2q3(a,i): 
    if a[i] == "b": 
        return True
    
def check(qq):
    newqq = qq
    states = 0
    
    if q0q1q2(newqq,states) == True:
        states += 1
        if len(newqq) == 1:
            return True
        elif q0q1q2(newqq,states) == True:
            while newqq[states] == "a" and states < len(newqq)-1:
                states += 1
            if q0q1q2q3(newqq,states) == True:
                return True
            else:
                return False
        elif q0q1q2q3(newqq,states) == True:
            while states < len(newqq):
                if newqq[states] != "b":
                    return False
                states += 1
            return True
        else:
            return False    
                
    elif q0q1q2q3(newqq,states) == True and len(newqq) == 1:
        return True
    else:
        return False    

print(check("aaaa"))
#print(check("aaaaaaab"))