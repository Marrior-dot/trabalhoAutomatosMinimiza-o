def q0(a):
    if a  == " " or a == "":
        return True
    
def q1(a):
    if a == "a":
        return True
    else:
        return False
    
def q2(a):
    if a == "b" or a == "":
        return True
def q3(a):
    if a == "c" or a == "":
        return True
    
def check(qq):
    newqq = qq
    states = 0    
    terminal = True

    if(q0(newqq) == True) :
        return terminal
    
    if q1(newqq[states]) == True:
        states += 1
        if states == len(newqq):
            return terminal
        
    else:
        terminal = False
        return terminal
    
    if q2(newqq[states]) == True:
        while newqq[states] == "b":
            states += 1
            if states == len(newqq):
                return terminal
        
    else:
        pass
    if q3(newqq[states]) == True:
        while(newqq[states] == "c"):
            states += 1
            if states == len(newqq):
                return terminal
        
    else:
        pass
    
    return terminal

print(check("dddddddddd"))