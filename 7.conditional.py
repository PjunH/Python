print(1)
if True:
    print(2)
    print(3)  #들여쓰기 해서 if안에 종속됨
print(4) #들여쓰기 안해서 if바깥으로 벗어남

print(1)
if False:
    print(2)
    print(3)  #흐릿한거는 이런 잉여행동?왜하냐고 흐릿한거 개똑똑ㅋ
print(4)


print(1)
if True:
    print(2.1)
    print(3.1)
else:
    print(2.2)  #출력안된다는거임
    print(3.3)
print(4)

print(1)
if False:
    print(2.1) #이것도 안된다는거임
    print(3.1)
else:
    print(2.2)
    print(3.3)
print(4)