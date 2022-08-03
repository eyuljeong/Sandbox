# Typewriter

import time

GAP = 0.05

# print
def typewrite(text, GAP):
    length = len(text)
    for i in range(0, length):
        print(text[i], end = "")
        time.sleep(GAP)
    print("")
    
# input
def question(text, GAP):
    length = len(text)
    for i in range(0, length - 1):
        print(text[i], end = "")
        time.sleep(GAP)
    answer = input(text[-1])
    return answer

##################################################

# Control

typewrite("Block", 0.1)

deployed = []
while True:
    time.sleep(1)
    menu_answer = question("\n1.배치    2.삭제    3.재배치    4.종료 ", GAP)
    print("")
    # 배치
    if menu_answer == "1":
        name = question("블록의 이름 : ", GAP)
        x = int(question("블록의 x 좌표(정수) : ", GAP))
        y = int(question("블록의 y 좌표(정수) : ", GAP))
        z = int(question("블록의 z 좌표(정수) : ", GAP))
        location = [x, y, z]
        radius = int(question("블록 한 변의 길이(정수) : ", GAP)) / 2

        flag = True # flag 알고리즘
        for obj in deployed: # 블록끼리 겹치지 않게 하기
            if abs(location[0] - obj[1][0]) >= obj[2] + radius\
                or abs(location[1] - obj[1][1]) >= obj[2] + radius\
                or abs(location[2] - obj[1][2]) >= obj[2] + radius:
                continue
            else:
                flag = False
                break

        if flag == True:
            typewrite("\nSystem : " + name + "이 " + str(location) + " 에 배치되었습니다.", GAP)
            deployed.append([name, location, radius])
            print("[이름, [x, y, z], 반지름] : {0}".format(deployed))
        elif flag == False:
            typewrite("\nSystem : 블록을 배치하려는 공간이 다른 블록과 겹쳐져 있습니다. 위치나 크기를 재설정하십시오.", GAP)
            print("[이름, [x, y, z], 반지름] : {0}".format(deployed))

    # 삭제
    elif menu_answer == "2":
        typewrite("몇 번째 블록을 지우시겠습니까?", GAP)
        will_be_deleted = int(input("[이름, [x, y, z], 반지름] : {0} ".format(deployed))) - 1
        deployed.pop(will_be_deleted)
        typewrite("\nSystem : " + name + "이 삭제되었습니다.", GAP)
        print("[이름, [x, y, z], 반지름] : {0}".format(deployed))

    # 재배치
    elif menu_answer == "3":
        typewrite("몇 번째 블록을 재배치하시겠습니까?", GAP)
        will_be_relocated = int(input("[이름, [x, y, z], 반지름] : {0} ".format(deployed))) - 1
        name = deployed[will_be_relocated][0]
        x = int(question("재배치될 x 좌표(정수) : ", GAP))
        y = int(question("재배치될 y 좌표(정수) : ", GAP))
        z = int(question("재배치될 z 좌표(정수) : ", GAP))
        location = [x, y, z]
        radius = deployed[will_be_relocated][2]
        deployed.pop(will_be_relocated)

        flag = True # flag 알고리즘
        for obj in deployed: # 블록끼리 겹치지 않게 하기
            if abs(location[0] - obj[1][0]) >= obj[2] + radius\
                or abs(location[1] - obj[1][1]) >= obj[2] + radius\
                or abs(location[2] - obj[1][2]) >= obj[2] + radius:
                continue
            else:
                flag = False
                break

        if flag == True:
            typewrite("\nSystem : " + name + "이 " + str(location) + " 로 재배치되었습니다.", GAP)
            deployed.append([name, location, radius])
            print("[이름, [x, y, z], 반지름] : {0}".format(deployed))
        elif flag == False:
            typewrite("\nSystem : 블록을 재배치하려는 공간이 다른 블록과 겹쳐져 있습니다. 위치나 크기를 재설정하십시오.", GAP)

    # 종료
    elif menu_answer == "4":
        typewrite("System : Block2 을 이용해주셔서 감사합니다.", GAP)
        time.sleep(1)
        break