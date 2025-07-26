date={
    1:{'name':'mounika','attempt_status':'false','python':0},
    2:{'name':'hema','attempt_status':'true','python':80},
    3:{'name':'bhavana','attempt_status':'true','python':70}
 }
stuid=int(input("Enter the student id:"))

if data[stuid]['attempt_status']:
    total=(data[stuid]['python'])
    if total>=80:
           print(f'congtats!!\n{data[stuid]["name"]} got "a" grade')
    elif total>=70:
        print(f'good!!\n{data[stuid]["name"]} got "b" grade')
    else:
        print(f'{data[stuid]["name"]} is not attempted the exam')


