from random import *

def RSP():
    difficulty = int(input('난이도를 입력하세요(0~60): '))
    difficulty -= 30
    defaultR = 30
    defaultS = 30
    defaultP = 30
    print(difficulty)

        # 가위 a 개 바위 b개 보 c개 로 설정 한 뒤, 리스트를 만들어서 처음 나오는 값을 cpu가 내는 값으로 하면 어떨까?

    while(True):

        user = input('가위 바위 보: ')

        if user == '바위':
            defaultR -= difficulty
            defaultS += 2* difficulty
            defaultP -= difficulty
            break
        elif user == '가위':
            defaultR -= difficulty
            defaultS += 2 * difficulty
            defaultP -= difficulty
            break
        elif user == '보':
            defaultR -= difficulty
            defaultS += 2 * difficulty
            defaultP -= difficulty
            break
        else:
            print('가위바위보를 내세요')