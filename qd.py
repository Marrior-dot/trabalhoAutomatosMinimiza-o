#def q1q3(a,i):
def transicao_a(a,i):
    if a[i]  == "a":
        return True
    else:
        return False
#def q2(a,i):
def transicao_b(a,i): 
    if a[i] == "b": 
        return True
#def q4(a,i):
def transicao_c(a,i):
    if a[i] == "c":
        return True
def check(qq):
    newqq = qq
    states = 0
    
    if transicao_a(newqq,states) == True:
        print("q0 --> q1")
        if states == len(newqq) - 1:
                return True
        if newqq[states + 1] != "a" and newqq[states + 1] != "b":
            print("q1 --> q3")
            if transicao_c(newqq,states) == True:
                print("q1 --> q3")
                while states < len(newqq) - 1:
                    print("q3")
                if newqq[states] != "c":
                    return False
                states += 1
            return True
        print("q1 --> q2")
        while newqq[states] == "a":
            if states == len(newqq) - 1:
                return True
            print("q2")
            states += 1
        if transicao_c(newqq,states) == True:
            print("q2 --> q3")
            while states < len(newqq) - 1:
                print("q3")
                if newqq[states] != "c":
                    return False
                states += 1
            return True
    
    if transicao_b(newqq, states) == True:
        if (newqq[states-1] + newqq[states-2]) == "aa":
            print("q2 --> q4")
        elif newqq[states-1] == "a":
            print("q1 --> q4")
        else:
            print("q0 --> q4")
        while newqq[states] == "b" and states < len(newqq) - 1:
            print("q4")
            states += 1
    
    if transicao_a(newqq,states) == True and states >= 0:
        print("q4 --> q5")
        if transicao_c(newqq,states) == True:
            print("q5-->q3")
            while states < len(newqq) - 1:
                print("q3")
                if newqq[states] != "c":
                    return False
        return True
    else:
        return False
#teste1
print(check("aaaaa"))
#teste2
print(check("ac"))
#teste3
print(check("aaaac"))
#teste4
print(check("aaaabbbbacccc"))
#teste5
print(check("bbbbbac"))
#teste6
print(check("bbbb"))
#teste7
print(check("abbbbb"))
#teste8
print(check("abbbbbcccccc"))