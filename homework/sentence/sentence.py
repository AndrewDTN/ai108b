import random
people = ["Andy","Allen","Andrew","Auther","Ada","Adele"]
lastname = ["Chen","Chang","Wang","Hsu"]
habbit = ["play game","pllay basebll","read","play basketball"]
introduce = ["大家好","各位好"]
introduce2 =["各位面試官好","在座的面試官好"]
end = ["跟大家成為好朋友","和各位成為志同道合的朋友"]
end2 = ["夠勝任這份工作","成為這家公司的一份子"]

def People():
    return random.choice(people)

def LastName():
    return random.choice(lastname)

def Habbit():
    return random.choice(habbit)

def Introduce():
    return random.choice(introduce)

def Introduce2():
    return random.choice(introduce2)

def End():
    return random.choice(end)

def End2():
    return random.choice(end2)

def Name():
    return People()+" "+LastName()


i=int(1)
while i==1:
    a=int(input('請選擇你需要的:(1:普通自我介紹;2:職場自我介紹;3:結束)'))
    if a == 1:
        print(Introduce()+ " " + Name() + "我的興趣是" + Habbit() + "希望能" + End())
        
    elif a == 2:
        print(Introduce2()+ " " + Name() + "我的興趣是" + Habbit() + "希望能" + End2())

    elif a == 3:
        break
    
    else:
        print("請輸入1,2或3")



