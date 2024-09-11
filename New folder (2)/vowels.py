def vowcount():
    line=input("enter the string: ")
    list=line.split()
    count=0
    for i in list:
        if i[0] in 'aeiou' or i[0] in 'AEIOU':
            count+=1
            print(i)
    print("vowelwords:",count)
vowcount()
            