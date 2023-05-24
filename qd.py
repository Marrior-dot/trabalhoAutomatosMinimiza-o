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
        print("q0 --> q1, a")
        if states == len(newqq) - 1:
                return True
        if newqq[states + 1] != "a" and newqq[states + 1] != "b":
            states += 1
            print("q1 --> q3, c")
            if transicao_c(newqq,states) == True:
                #print("q1 --> q3, c")
                while states < len(newqq) - 1:
                    print("q3, c")
                if newqq[states] != "c":
                    return False
                states += 1
            return True
        states += 1
        print("q1 --> q2, a")
        states += 1
        while newqq[states] == "a":
            states += 1
            if states == len(newqq):
                return True
            print("q2, a")
        if transicao_c(newqq,states) == True:
            print("q2 --> q3, c")
            #states += 1
            while states < len(newqq) - 1:
                states += 1
                if newqq[states] != "c":
                    return False
                print("q3, c")
            return True
    
    if transicao_b(newqq, states) == True:
        if (newqq[states-1] + newqq[states-2]) == "aa":
            print("q2 --> q4, b")
            states += 1
        elif newqq[states-1] == "a":
            print("q1 --> q4, b")
            states += 1
        else:
            print("q0 --> q4, b")
            states += 1
        while newqq[states] == "b" and states < len(newqq) - 1:
            print("q4, b")
            states += 1
    
    if transicao_a(newqq,states) == True and states >= 0:
        print("q4 --> q5, a")
        states += 1
        if transicao_c(newqq,states) == True:
            print("q5-->q3, c")
            while states < len(newqq) - 1:
                print("q3, c")
                if newqq[states] != "c":
                    return False
                states += 1
                
        return True
    else:
        return False
    
print("teste 1 - aaaaa")
print(check("aaaaa"))
print("\n")

print("teste 2 - ac")
print(check("ac"))
print("\n")

print("teste 3 - aaaac")
print(check("aaaac"))
print("\n")

print("teste 4 - aaaabbbbacccc")
print(check("aaaabbbbacccc"))
print("\n")

print("teste 5 - bbbbbac")
print(check("bbbbbac"))
print("\n")

print("teste 6 - bbbb")
print(check("bbbb"))
print("\n")

print("teste 7 - abbbbb")
print(check("abbbbb"))
print("\n")

print("teste 8 - abbbbbcccccc")
print(check("abbbbbcccccc"))