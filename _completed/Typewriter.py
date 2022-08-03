# Typewriter

import time

GAP = 0.1

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