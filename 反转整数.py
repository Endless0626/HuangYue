x=input()
n=len(x)
if (x[0] is "-" and x[1:].isdigit()):
    m=1
    print("-",end='')
    for m in range(n-1):
        print(x[n-m-1],end='')
        m=m+1
elif x.isdigit():
    m=0
    for m in range(n):
        print(x[n-m-1],end='')
        m=m+1
else:
    print("输入有误！")
