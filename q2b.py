#def q0q1q2q3(a,i):
def transicao_aaa(a,i):
    if a[i]  == "a":
        i += 1
        if a[i]  == "a":
            i += 1
            if a[i]  == "a":
                return True
    else:
        return False
#def q0q1q4(a,i):
def transicao_bc(a,i): 
    if a[i] == "b" or a[i] == "c":
        return True
    else:
        return False
        
def check(qq):
    newqq = qq
    states = 0    
    terminal = True

    if transicao_aaa(newqq,states) == True:
        states = 3
        print("q0 --> q1, a\nq1 --> q2, a\nq2 --> q3, a")
        if(len(newqq)) == 3:
            return True
        else:
            if transicao_bc(newqq,states) == True:
                print("q3-->q4, b|c")
                while states < len(newqq)-1:
                    print("q4, b|c")
                    states += 1
                    if transicao_bc(newqq,states) == False:
                        return False
                return True
            else:
                return False           
    else:
        pass
    
    if transicao_bc(newqq,states) == True:
        print("q0 --> q5, b|c")
        states += 1
        while (newqq[states] == "b" or newqq[states] == "c") and states < len(newqq)-1:
            print("q5, b|c")
            states += 1
        if transicao_aaa(newqq,states) == True and states == len(newqq) - 3:
            print("q5 --> q6, a\nq6 --> q7, a\nq7 --> q8, a")
            return True
        else:
            return False
    else:
        return False
print("teste 1 - aaabcbcbb") 
print(check("aaabcbcbb"))
print("\n")

print("teste 2 - bcbcbbaaa") 
print(check("bcbcbbaaa"))
print("\n")

print("teste 3 - aaa")
print(check("aaa"))
print("\n")

print("teste 4 - bcbcbcbcbcb")
print(check("bcbcbcbcbcb"))
print("\n")

print("teste 5 - ddddddd")
print(check("ddddddd"))
print("\n")

print("teste 6 - aaaddddd")
print(check("aaaddddd"))
print("\n")

print("teste 7 - dddaaaaa")
print(check("dddaaaaa"))
print("\n")

print("teste 8 - aaabbdbdbd")
print(check("aaabbdbdbd"))
print("\n")

print("teste 9 - dbdbddbaaa")
print(check("dbdbddbaaa"))
print("\n")

print("teste 10 - aaaa")
print(check("aaaa"))