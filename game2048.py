"""4 x 4 integeMMr list이고 0은 empty를 나타냅니다"""
import random
class Board:
    """board"""
    def __init__(self):
        self.nums = [[0]*4 for _ in range(4)]

    # board를 출력했을 때의 나타날 string을 리턴해야합니다
    def __str__(self):
        line = ""
        top = "o----o----o----o----o\n"
        side = "|    |    |    |    |\n"
        for i in range(4):
            line += f"{top}{side}|"
            for j in self.nums[i]:
                if j == 0:
                    j = ' '
                line += f"{j:^4}|"
            line += f"\n{side}"
        return line + top

    def insert(self):
        """empty cell을 random하게 골라서 2 또는 4로 세팅합니다"""
        while True:
            row=random.randrange(4)
            col=random.randrange(4)
            num=self.nums[row][col]
            if num == 0:
                num=random.choice([2,4])
                self.nums[row][col]=num
                return

    # 각각의 row에 대해 실행합니다
    # empty 가 아닌 cell을 가능한 한 왼쪽으로 옮깁니다.
    # ex. 0 2 0 4 >> 2 4 0 0
    # 같은 숫자의 cell을 만나면 merge합니다
    # ex. 0 2 0 2 >> 4 0 0 0
    # 해당 push에서 merge된 cell은 해당 차수에서 다시 merge할 수 없습니다
    # ex. 0 2 2 4 >> 4 4 0 0
    # 두 cell이 merge할 때마다 새로 생긴 cell 값을 포인트로 얻습니다
    def push_left(self):
        """왼쪽으로 옮기기"""
        point=0
        for i in range(4):
            pos=0
            compare_num=0
            for j in range(4):
                if self.nums[i][j]==0:
                    continue
                if compare_num!=self.nums[i][j]:
                    compare_num=self.nums[i][j]
                    self.nums[i][j]=0
                    self.nums[i][pos]=compare_num
                    pos+=1
                elif compare_num==self.nums[i][j]:
                    self.nums[i][pos-1]=compare_num*2
                    self.nums[i][j]=0
                    compare_num=0
                    point+=compare_num*2
        return point

    def push_right(self):
        """오른쪽으로 옮기기"""
        point=0
        for i in range(4):
            pos=3
            compare_num=0
            for j in range(3,-1,-1):
                if self.nums[i][j]==0:
                    continue
                if compare_num!=self.nums[i][j]:
                    compare_num=self.nums[i][j]
                    self.nums[i][j]=0
                    self.nums[i][pos]=compare_num
                    pos-=1
                elif compare_num==self.nums[i][j]:
                    self.nums[i][pos+1]=compare_num*2
                    self.nums[i][j]=0
                    compare_num=0
                    point+=compare_num*2
        return point

    def push_up(self):
        """위쪽으로 옮기기"""
        point=0
        for i in range(4):
            pos=0
            compare_num=0
            for j in range(4):
                if self.nums[j][i]==0:
                    continue
                if compare_num!=self.nums[j][i]:
                    compare_num=self.nums[j][i]
                    self.nums[j][i]=0
                    self.nums[pos][i]=compare_num
                    pos+=1
                elif compare_num==self.nums[j][i]:
                    self.nums[pos-1][i]=compare_num*2
                    self.nums[j][i]=0
                    compare_num=0
                    point+=compare_num*2
        return point

    def push_down(self):
        """아래쪽으로 옮기기"""
        point=0
        for i in range(4):
            pos=3
            compare_num=0
            for j in range(3,-1,-1):
                if self.nums[j][i]==0:
                    continue
                if compare_num!=self.nums[j][i]:
                    compare_num=self.nums[j][i]
                    self.nums[j][i]=0
                    self.nums[pos][i]=compare_num
                    pos-=1
                elif compare_num==self.nums[j][i]:
                    self.nums[pos+1][i]=compare_num*2
                    self.nums[j][i]=0
                    compare_num=0
                    point+=compare_num*2
        return point

    def push(self, direction):
        if direction == 'l':
            return self.push_left()
        elif direction == 'r':
            return self.push_right()
        elif direction == 'u':
            return self.push_up()
        else:
            return self.push_down()

    # empty cell이 없다면 True를 리턴하고, 그 외엔 False를 리턴합니다
    def is_full(self):
        
        for i in range(4): 
            for j in range(4):
                if 0 == self.nums[i][j]:
                    return False
        return True

# >>> val b = Board()
# >>> b
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o

# >>> b.insert()
# >>> b.insert()
# >>> b
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |  2 |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |  2 |
# |    |    |    |    |
# o----o----o----o----o

def main():
    board = Board()
    board.insert()
    board.insert()

    points = 0
    
    while True:
        print(board)
        print(f"{points} points\n")
        word = input("What is your move: ").lower().strip()
        print()
        if len(word) != 1 or not word in "lrud":
            continue
        if len(word) == 1 and word in "lrud":
            points+=board.push(word)
        
            board.insert()
        if board.is_full():
            print(board)
            print("\nGame over.")
            print(f"You have {points} points.")
            return

# 1. main에서 pre 안쓰도록 변경
# 2. push_left, push_right, ... 에서 left, right 안쓰고 board.nums 의 숫자를 바로 변경
# 3. pre 변수명 바꾸기
# 4. x, y => r, c  으로 바꾸기
# [[(0,0), (0,1), (0,2)],
#      [(1,0), (1,1), (1,2)],
#    [(2,0), (2,1), (2,2)]]
# [y][x]
# (x, y)
# row, column

main()
