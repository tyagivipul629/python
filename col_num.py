sum1=0
def val(st):
    sum=0
    if st=='A':
        sum+=1
        return sum
    elif st=='B':
        sum+=2
        return sum
    elif st=='C':
        sum+=3
        return sum
    elif st=='D':
        sum+=4
        return sum
    elif st=='E':
        sum+=5
        return sum
    elif st=='F':
        sum+=6
        return sum
    elif st=='G':
        sum+=7
        return sum
    elif st=='H':
        sum+=8
        return sum
    elif st=='I':
        sum+=9
        return sum
    elif st=='J':
        sum+=10
        return sum
    elif st=='K':
        sum+=11
        return sum
    elif st=='L':
        sum+=12
        return sum
    elif st=='M':
        sum+=13
        return sum
    elif st=='N':
        sum+=14
        return sum
    elif st=='O':
        sum+=15
        return sum
    elif st=='P':
        sum+=16
        return sum
    elif st=='Q':
        sum+=17
        return sum
    elif st=='R':
        sum+=18
        return sum
    elif st=='S':
        sum+=19
        return sum
    elif st=='T':
        sum+=20
        return sum
    elif st=='U':
        sum+=21
        return sum
    elif st=='V':
        sum+=22
        return sum
    elif st=='W':
        sum+=23
        return sum
    elif st=='X':
        sum+=24
        return sum
    elif st=='Y':
        sum+=25
        return sum
    else:
        sum+=26
        return sum
def col_num(st):
    global sum1
    length=len(st)
    for i,j in zip(range(length-1,-1,-1),range(0,length)):
        sum1+=val(st[j])*(26**i)
    return sum1
st=input("Enter string:")
print(col_num(st))