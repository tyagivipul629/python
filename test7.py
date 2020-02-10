# Enter your code here. Read input from STDIN. Print output to STDOUT
l1,r1=input().split(" ")
l2,r2=input().split(" ")
l1,r1,l2,r2=int(l1),int(r1),int(l2),int(r2)
sumA,sumB=0,0
for i in range(l1,r1+1):
    for j in range(1,i+1):
        if i%j==0:
            sumA+=j
for i in range(l2,r2+1):
    for j in range(1,i+1):
        if i%j==0:
            sumB+=j
if sumA>sumB:
    print("A")
elif sumB>sumA:
    print("B")
else:
    print("Draw")
