while True:
    height = input("고객님의 키는? ")
    try: # 아래 명령문을 일단 실행
        height = float(height)
    except ValueError: # ValueError 가 뜰 때
        print("숫자만 입력하세요. 凸ಠ益ಠ)凸")
    else: # 정상적으로 실행될 때
        print("입력 완료!!")
        break

# 예시
food = ["chicken", "Red Bull", "biscuit"]
medi_kit = ["surgery kit", "board", "adrenalin"]
gun = ["Desert Eagle", "Mp5", "Vector"]
sec_code = [12, 356, 907]

food.extend(medi_kit) # 리스트를 합치고
food.extend(gun)
food.extend(sec_code)
print(food)

obj_list = []
code_list = []
for obj in food:
    try:
        int(obj)
    except ValueError:
        obj_list.append(obj)
    else:
        code_list.append(obj)

print(obj_list) # 나눔
print(code_list)

print("I have only {0} codes.. They are ".format(len(code_list)), end = "")
for n in code_list:
    print("{0}".format(n), end = ", ")
print("\b\b.")