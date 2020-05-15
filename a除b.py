a,b=input().split(" ")#同行输入，以“ ”分隔
if eval(b)==0:
    print("出现了错误：除零错误")
else:
    print("得到的结果是：{:.2f}".format(eval(a)/eval(b)))
