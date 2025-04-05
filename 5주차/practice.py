import random

def lotto():
    print("** 로또 추첨을 시작합니다. **")
    
    list=[]
    
    while len(list)<6:
        num=random.randrange(1,46)
        
        if num not in list:
            list.append(num)
            
    print("추첨된 로또 번호 ==> ", end=" ")
    i=0
    list=sorted(list)
    for i in range(0,6,1):
        print("%d " % list[i],end=" ")
        
lotto()
