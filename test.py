import random
from fractions import Fraction

def newz():
    f=['+','-','×','÷']
    num=random.randint(0,3)
    add1=random.randint(1,20)
    add2=random.randint(1,20)
    res=[]
    if add1<add2:
        temp=add1
        add1=add2
        add2=temp
    if num==0:
        val=str(add1+add2)
    elif num==1:
        val=str(add1-add2)
    elif num==2:
        val=str(add1*add2)
    elif num==3:
        if add1>add2 and add1%add2!=0:
            temp = add1
            add1 = add2
            add2 = temp
        val=str(Fraction(add1,add2))
    res.append(val)
    res.append(str(add1) + ' '+f[num]+' ' + str(add2))
    return res
def newf():
    f=['+','-','×','÷']
    num=random.randint(0,3)
    t1 = random.randint(1, 20)
    t2 = random.randint(t1, 20)
    a = Fraction(t1, t2)
    t1 = random.randint(1, 20)
    t2 = random.randint(t1, 20)
    b = Fraction(t1, t2)
    res=[]
    if num==0:
        val=str(a+b)
    elif num==1:
        if a<b:
            temp = a
            a = b
            b = temp
        val=str(a-b)
    elif num==2:
        val=str(a*b)
    elif num==3:
        val=str(Fraction(a,b))
    res.append(val)
    res.append(str(a) + ' ' + f[num] + ' ' + str(b))
    return res
def xianzuo():
    ok = 0
    i = 1
    r = 0
    print("小学生四则运算题目：(输入00退出做题)")
    while ok != '00':
        t = random.randint(0, 1)
        if t == 0:
            R = newz()
        else:
            R = newf()
        print("第%d：%s=" % (i, R[1]), end=" ")
        ok = input()
        if ok == '00':
            break
        elif ok == R[0]:
            print("回答正确！")
            r += 1
        else:
            print("回答错误，正确答案是%s" % R[0])
        i += 1
    print("一共做了%d题，做正确了%d题，欢迎下次使用" % (i, r))
def shengcheng():
    n=input("生成题目多少道：")
    list1=[]#保存题目
    list2=[]#保存答案
    for i in range(int(n)):
        t = random.randint(0, 1)
        if t == 0:
            R=newz()
            list1.append(R[1])
            list2.append(R[0])
        else:
            R = newf()
            list1.append(R[1])
            list2.append(R[0])
        #print(R[1]+"="+R[0])
    #print(type(list1[0]))
    for o in range(len(list1)):
        #print(type(i))
        if o%5==0:
            print("\n")
        print("%d、%s=     " % (o + 1, list1[int(o)]), end=" ")
        #print("%d."+list1[o]+"=",end=" ")
    print("\n答案如下：")
    for j in range(len(list2)):
        if j%5==0:
            print("\n")
        print("%d、%s    " %(j+1,list2[int(j)]),end=" ")

    print("\n生成完毕，一共%s道题目"%n)
print("输入1开始做题，输入2生成题目,输入00退出")
k='0'
k=input()
while k!='1' and k!='2' and k!='00':
    print("输入有误，请重新输入")
    k=input()
if k=='1':
    xianzuo()
elif k=='2':
    shengcheng()
else:
    print("欢迎下次使用")




