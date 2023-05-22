def q1q3(a,i):
    if a[i]  == "a":
        return True
    else:
        return False
def q2(a,i): 
    if a[i] == "b": 
        return True
def q4(a,i):
    if a[i] == "c":
        return True
def check(qq):
    newqq = qq
    states = 0
    
    if q1q3(newqq,states) == True:
        print("q0 --> q1")
        while newqq[states] == "a":
            print("q1")
            if states == len(newqq) - 1:
                return True
            states += 1
        if q4(newqq,states) == True:
            print("q1 --> q4")
            while states < len(newqq) - 1:
                print("q4")
                if newqq[states] != "c":
                    return False
                states += 1
            return True
    
    if q2(newqq, states) == True:
        print("q1 --> q2")
        while newqq[states] == "b" and states < len(newqq) - 1:
            print("q2")
            states += 1
    
    if q1q3(newqq,states) == True and states >= 0:
        print("q2-->q3")
        if q4(newqq,states) == True:
            while states < len(newqq) - 1:
                if newqq[states] != "c":
                    return False
        return True
    else:
        return False
   
print(check("ddddaaabaacccc"))