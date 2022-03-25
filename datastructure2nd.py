from re import X


class myList():
    def __init__(self):
        self.capacity = 2	  # myList의 용량 (저장할 수 있는 원소 개수)
        self.n = 0          # 실제 저장된 값의 개수
        self.A = [None] * self.capacity  # 실제 저장 자료구조 (python의 리스트 사용)

    def __len__(self):
        return self.n

    def __str__(self):
        return f'  ({self.n}/{self.capacity}): ' + '[' + ', '.join([str(self.A[i]) for i in range(self.n)]) + ']'

    def __getitem__(self, k):  # k번째 칸에 저장된 값 리턴
        # k가 음수일 수도 있음
        if k < 0:
            k += self.n
        # k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
        if len(self.A) == 0 or k >= self.n:
            raise IndexError
        return self.A[k]

    def __setitem__(self, k, x):  # k번째 칸에 값 x 저장
        # k가 음수일 수도 있음
        if k < 0:
            k += self.n
        # k가 올바른 인덱스 범위를 벗어나면 IndexError 발생시킴
        if len(self.A) == 0 or k >= self.n:
            raise IndexError
        self.A[k] = x

    def change_size(self, new_capacity):
        # 이 첫 문장은 수정하지 말 것
        print(f'  * changing capacity: {self.capacity} --> {new_capacity}')
        # 1. new_capacity의 크기의 리스트 B를 만듬
        B = [None] * new_capacity
        # 2. self.A의 값을 B로 옮김
        for i in range(self.n):  # 헷갈려
            B[i] = self.A[i]
        # B = [[self.A[i]]*new_capacity for i in range(self.n) ]
        del self.A
        self.A = B
        self.capacity = new_capacity

    def append(self, x):
        if self.n == self.capacity:
            self.change_size(self.capacity*2)
        self.A[self.n] = x
        self.n += 1

    def pop(self, k=None):
        if k is not None and self.n == 0 or k >= self.n:  # 빈 리스트이거나 올바른 인덱스 범위를 벗어나면: ##헷갈려
            raise IndexError
        if self.capacity >= 4 and self.n <= self.capacity//4:
            self.change_size(self.capacity//2)
        # 1. k 값이 주어진 경우와 주어지지 않은 경우 구별해야 함
        if k is None:
            x = self.A[self.n-1]
        elif k < 0:
            if k < 0:  # 이부분 while로 쓰면 모든 음수에 대해 양수로 만들어줌..
                k += self.n
            x = self.A[k]
            for i in range(k, self.n-1):
                self.A[i] = self.A[i+1]
        self.A[self.n-1] = None
        self.n -= 1
        return X

        # k is 1
        # k == 1
        # 무슨 차이?
        '''
        A = [1,2,3]
        B = A
        print(A==B)
        print(A is B)


        print(A.pop(-1))
        print(A.pop(-4))-> 오류. 

        '''

        if k == -1 or k == self.n-1:
            x = self.A[k]
            self.A[-1] = 0
        else:
            x = self.A[k]
            for i in range(k, self.n-1):
                self.A[i] = self.A[i+1]
        self.n -= 1
        return x

    def insert(self, k, x):
        # 주의: k 값이 음수값일 수도 있음
        if k < 0:
            k += self.n
        # k 값이 올바른 인덱스 범위를 벗어나면, raise IndexError
        # 1. k의 범위가 올바르지 않으면 IndexError 발생시킴
        if k < 0 or k >= self.n:
            raise IndexError
        # 2. self.n == self.capacity이면 self.change_size(self.capacity*2) 호출해 doubling
        if self.n == self.capacity:
            self.change_size(self.capacity*2)
        # 3. A[k]와 오른쪽 값을 한 칸씩 오른쪽으로 이동
        for i in range(self.n, k-1, -1):
            self.A[i] = self.A[i-1]
        self.A[k] = x
        self.n += 1

        def size(self):
            return self.capacity


L = myList()
while True:
    cmd = input().strip().split()
    if cmd[0] == 'append':
        L.append(int(cmd[1]))
        print(f"  + {cmd[1]} is appended.")
    elif cmd[0] == 'pop':
        if len(cmd) == 1:
            idx = -1
        else:
            idx = int(cmd[1])
        try:
            x = L.pop(idx)
            print(f"  - {x} at {idx} is popped.")
        except IndexError:
            if len(L) == 0:
                print("  ! list is empty.")
            else:
                print(f"  ! {idx} is an invalid index.")
    elif cmd[0] == 'insert':
        try:
            L.insert(int(cmd[1]), int(cmd[2]))
            print(f"  + {cmd[2]} is inserted at index {cmd[1]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'get':  # getitem A[k]
        try:
            L[int(cmd[1])]
            print(f"  @ L[{cmd[1]}] --> {L[int(cmd[1])]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'set':  # setitem A[k] = x
        try:
            L[(int(cmd[1]))] = int(cmd[2])
            print(f"  ^ L[{cmd[1]}] <-- {cmd[2]}.")
        except IndexError:
            print(f"  ! {cmd[1]} is an invalid index.")
    elif cmd[0] == 'size':
        print("  ? capacity =", L.size())
    elif cmd[0] == 'print':
        print(L)
    elif cmd[0] == 'exit':
        print('bye~')
        break
    else:
        print(" ? invalid command! Try again.")
