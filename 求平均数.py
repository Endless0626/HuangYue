n=eval(input("数字的个数："))#数字的个数
sum=0
for i in range(n):
    x=eval(input())
    sum=sum+x
    i=i+1
print("{}".format(sum/n))
