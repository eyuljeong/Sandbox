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

# Logic

class Block:
    # 배치
    def __init__(self, type:str, location:list, radius:float, deployed:list):
        self.type = type
        self.location = location
        self.radius = radius
        self.deployed = deployed # 배치된 오브젝트 리스트

    def deploy(self):
        flag = True # flag 알고리즘
        for obj in self.deployed: # 블록끼리 겹치지 않게 하기
            if abs(self.location[0] - obj[1][0]) >= obj[2] + self.radius\
                or abs(self.location[1] - obj[1][1]) >= obj[2] + self.radius\
                or abs(self.location[2] - obj[1][2]) >= obj[2] + self.radius:
                continue
            else:
                flag = False
                break

        if flag == True:
            typewrite("\nSystem : " + self.type + "이 " + str(self.location) + " 에 배치되었습니다.", GAP)
            self.deployed.append([self.type, self.location, self.radius])
            return self.deployed
        elif flag == False:
            typewrite("\nSystem : 블록을 배치하려는 공간이 다른 블록과 겹쳐져 있습니다. 위치나 크기를 재설정하십시오.", GAP)

    # 삭제
    def delete(self):
        ex_location = self.deployed.index([self.type, self.location, self.radius])
        self.deployed.pop(ex_location)
        typewrite("\nSystem : " + self.type + "이 삭제되었습니다.", GAP)
        return self.deployed


    # 재배치 = 삭제 + 배치
    def relocation(self, new_location):
        ex_location = self.deployed.index([self.type, self.location, self.radius])
        self.deployed.pop(ex_location) # 기존 블록 삭제
        self.location = new_location

        flag = True # flag 알고리즘
        for obj in self.deployed: # 블록끼리 겹치지 않게 하기
            if abs(self.location[0] - obj[1][0]) >= obj[2] + self.radius\
                or abs(self.location[1] - obj[1][1]) >= obj[2] + self.radius\
                or abs(self.location[2] - obj[1][2]) >= obj[2] + self.radius:
                continue
            else:
                flag = False
                break

        if flag == True:
            typewrite("\nSystem : " + self.type + "이 " + str(self.location) + " 로 재배치되었습니다.", GAP)
            self.deployed.append([self.type, self.location, self.radius])
            return self.deployed
        elif flag == False:
            typewrite("\nSystem : 블록을 재배치하려는 공간이 다른 블록과 겹쳐져 있습니다. 위치나 크기를 재설정하십시오.", GAP)

##################################################

# Control

deployed = []

grass_block = Block("풀 블록", [0, 0, 0], 2, deployed)
mud_block = Block("진흙 블록", [0, 0, 0], 2, deployed)
rock_block = Block("돌 블록", [0, 0, 0], 2, deployed)

deployed = grass_block.deploy()
print(deployed)
deployed = grass_block.relocation([1, 1, 1])
print(deployed)
deployed = grass_block.delete()
print(deployed)