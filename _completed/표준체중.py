import time

print("\n안녕하세요? ^^")
time.sleep(2)
print("\n이 프로그램은 고객님의 키와 성별을 통해 표준 체중을 구해드립니다.")
time.sleep(4)
print("\n그리고 모든 기록은 서버에 \"영구저장\" 됨을 유의하시기 바랍니다. ^^")
time.sleep(2)

# 키
while True:
   height = input("\n고객님의 키는? ")
   time.sleep(1)
   try:
      height = float(height)
   except ValueError:
      print("\n숫자만 입력하세요. 凸ಠ益ಠ)凸")
      time.sleep(1)
   else:
      print("\n입력 완료!!")
      time.sleep(2)
      break

# 성별
while True:
   gender = input("\n남성이라면 1, 여성이라면 2, 중성이라면 3을 누르세요. ")
   time.sleep(1)
   if gender == "1" or gender == "2":
      print("\n입력 완료!!")
      time.sleep(2)
      break
   else:
      print("\nWTF")
      time.sleep(0.5)

# 표준체중 함수
def std_weight(height, gender):
   if gender == "1":
      need_to_be_this_heavy = round((height / 100) ** 2 * 22, 2)
      gender2 = "남자"
   elif gender == "2":
      need_to_be_this_heavy = round((height / 100) ** 2 * 21, 2)
      gender2 = "여자"
   print("\n키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender2, need_to_be_this_heavy))

std_weight(height, gender)
time.sleep(2)
print("\n살 좀 빼셔야겠어요. ^^")