members = ['pjh', 'duru']
for member in members:
    print('member', member)

members2 = [
    ['pjh', 'daegu', 'CEO'],
    ['cha', 'seoul', 'dba']
]
print(members2[0][2]) # 앞의수는 큰배열안에 1번째, 두번째수는 그 배열 안의 2번째라는 뜻

for member in members2:
    print(member[0], member[1])

pjh1 = ['pjh','daegu','CEO']
pjh2 = {'name':'pjh', 'city':'daegu','Job':'CEO'} #사전형
print(pjh2['city'])
for name in pjh2:
    print(pjh2[name])

members3 = [
    {'name':'pjh', 'city':'daegu','Job':'CEO'},
    {'name':'cha', 'city':'seoul','Job':'dba'}
]
for member in members3:
    print(member['name'])

#와ㅏㅏㅏㅏ어렵다 다시공부하자 으쌰