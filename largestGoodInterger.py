def largestGoodInteger(num: str):
    p1 = 0
    p2 = 1
    p3 = 2
    store = []
    single_digit_store = []
    for i in range(len(num)):
        if i+2 < len(num):
            if (num[p1] == num[p2] and num[p1] == num[p3]): #can be optimized by checking the max while inserting
                store.append(num[p1] + num[p2] + num[p3])
                single_digit_store.append(int(num[p1]))
                p1+=1
                p2+=1
                p3+=1
            else:
                p1+=1
                p2+=1
                p3+=1
    
    
    if len(single_digit_store) == 0:
        return ''
    else:
        return store[single_digit_store.index(max(single_digit_store))]
print(largestGoodInteger('42352338'))