a,b=input().split(";")#同行输入，以“；”分隔
if eval(b)==0:
    print("除零错误")
else:
    print("{:.2f}".format(eval(a)/eval(b)))
