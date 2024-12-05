
num_data = 0
num_com = 0
swap = 0


def dataReset():
    global num_data
    global num_com    
    global swap
    num_data = 0
    num_com = 0
    swap = 0

def print_result(data_list):
    global num_data
    global num_com
    global swap
    print('Sorted : ', data_list)
    print('Number of comparisions :', num_com)
    print('Number of data movements :', num_data)
    print('Number of swap :', swap)

# Shell sort
def sortGapInsertion(A, first, last, gap) :
    global num_data
    global num_com
    for i in range(first+gap, last+1, gap) :
        key = A[i]
        j = i - gap
        while j >= first and key<A[j] :
            A[j + gap] = A[j]
            j = j - gap
            num_com += 1
        A[j + gap] = key
        num_data += 1

def shell_sort(A) :
    n = len(A)
    gap = n//2
    
    global num_data 
    global num_com
    
    while gap > 0 :
        if (gap % 2) == 0 : gap += 1	
        for i in range(gap) :
            sortGapInsertion(A, i, n - 1, gap);
            
        if(gap == 1):
            print('Sorted : ',A)
            print('Number of comparisions :', num_com)
            print('Number of data movements :', num_data)
        gap = gap//2



#SEL
def selection_sort(A) :
    global num_data
    global num_com
    
    n = len(A)
    for i in range(n-1) :
        least = i;
        for j in range(i+1, n) :
            num_com += 1            #if 들어가든말든 비교니까             
            if (A[j]<A[least]) :
                least = j
        A[i], A[least] = A[least], A[i]
        num_data += 1               
    print('Sorted : ',A)
    print('Number of comparisions :', num_com)
    print('Number of data movements :', num_data)



# INS

def insertion_sort(A):
    global num_data
    global num_com
    
    n = len(A)
    print("정렬과정")
    for i in range(1, n):
        key = A[i]
        j = i - 1
        
        while j >= 0 and A[j] > key:
                num_com += 1  # 비교 발생
                A[j + 1] = A[j]
                num_data += 1  # 데이터 이동 발생
                j -= 1
                print( A)
            
        if j >= 0:  # 루프 탈출 후에도 비교는 한 번 더 발생
            num_com += 1
        A[j + 1] = key
        num_data += 1  # key를 삽입하는 것도 데이터 이동으로 간주
    print('Sorted : ',A)
    print('Number of comparisions :', num_com)
    print('Number of data movements :', num_data)





# BUB

def bubble_sort(A) :
    global num_com
    global swap
    print("정렬과정")
    n = len(A)
    for i in range(n-1, 0, -1) :
        bChanged = False
        
        for j in range (i) :

            num_com += 1
            if (A[j]>A[j+1]) :
                swap += 1 
                A[j], A[j+1] = A[j+1], A[j] 
                bChanged = True
                print(A)

        if not bChanged:
            print()
            print('Sorted : ',A)
            print('Number of comparisions :', num_com)
            print('Number of swap :', swap)
            break;			




# HEAP

def heapify(arr, n, i):
    global swap
    global num_com
    
    largest = i         # Initialize largest as root 
    l = 2 * i + 1       # left = 2*i + 1 
    r = 2 * i + 2       # right = 2*i + 2 
  
    if l < n and arr[i] < arr[l]: largest = l
    num_com += 1
    if r < n and arr[largest] < arr[r]:  largest = r 
    num_com += 1
    
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
        swap += 1
        heapify(arr, n, largest) 
  
# 코드 12.5: 제자리 정렬로 구현된 힙 정렬
def heapSort(arr):
    global swap
    global num_com
    n = len(arr) 
  
    print("i=", 0, arr)
    for i in range(n//2, -1, -1): 
        heapify(arr, n, i) 
        print("i=", i, arr)
  
    print()
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap
        swap += 1
        heapify(arr, i, 0) 
        print("i=", i, arr)
    print()





#merge

sorted = [0]*100
def merge_sort(A, left, right):
    global num_com

    num_com += 1  # left < right 비교 발생
    if left < right:
        mid = (left + right) // 2  # 중간점 계산
        merge_sort(A, left, mid)       # 왼쪽 부분 리스트 정렬
        merge_sort(A, mid + 1, right)  # 오른쪽 부분 리스트 정렬
        merge(A, left, mid, right)     # 병합 과정 수행

# 병합 함수
def merge(A, left, mid, right):
    
    global sorted
    global num_data
    global num_com

    k = left
    i = left
    j = mid + 1

    # 두 부분 리스트를 병합
    while i <= mid and j <= right:
        num_com += 1  # A[i]와 A[j] 비교
        if A[i] <= A[j]:
            sorted[k] = A[i]
            num_data += 1  # 데이터 이동
            i += 1
        else:
            sorted[k] = A[j]
            num_data += 1  # 데이터 이동
            j += 1
        k += 1

    # 남은 왼쪽 리스트 복사
    while i <= mid:
        num_com += 1  # 비교는 한 번 더 발생
        sorted[k] = A[i]
        num_data += 1  # 데이터 이동
        i += 1
        k += 1

    # 남은 오른쪽 리스트 복사
    while j <= right:
        num_com += 1  # 비교는 한 번 더 발생
        sorted[k] = A[j]
        num_data += 1  # 데이터 이동
        j += 1
        k += 1

    # sorted[]의 내용을 다시 A[]로 복사
    A[left:right+1] = sorted[left:right+1]
    num_data += (right - left + 1)  # 데이터 이동
    




# quick
def quick_sort(A, left, right):
    global num_data
    global num_com

    if left < right:                                # 정렬 범위가 2개 이상인 경우
        num_com += 1                          # left < right 비교
        q = partition(A, left, right)       # 좌우로 분할
        quick_sort(A, left, q - 1)          # 왼쪽 부분 리스트 정렬
        quick_sort(A, q + 1, right)         # 오른쪽 부분 리스트 정렬
    else:
        num_com += 1  # left >= right 비교

# 퀵 정렬을 위한 분할 함수
def partition(A, left, right):
    global num_data
    global num_com
    global swap
    
    low = left + 1
    high = right
    pivot = A[left]  # 피벗 설정

    while low <= high:  # low와 high가 역전되지 않는 한 반복
        # 피벗보다 작은 값을 찾는 과정
        while low <= right and A[low] < pivot:
            num_com += 1  # 비교 발생
            low += 1

        # 피벗보다 큰 값을 찾는 과정
        while high >= left and A[high] > pivot:
            num_com += 1  # 비교 발생
            high -= 1

        # low와 high가 엇갈리지 않았을 때 교환
        if low < high:
            A[low], A[high] = A[high], A[low]
            swap += 1  # 교환 발생

    # 피벗과 high를 교환
    A[left], A[high] = A[high], A[left]
    swap += 1  # 교환 발생

    return high



#radix

from queue import Queue
from collections import deque

BUCKETS = 10
DIGITS  = 4


# Radix Sort with tracking
def radix_sort(A):
    global num_data
    global num_com
    DIGITS  = int(input("리스트의 최대 자리수 ="))

    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())

    n = len(A)
    factor = 1

    for d in range(DIGITS):
        # 각 자릿수에 따라 큐에 삽입
        for i in range(n):
            bucket_index = (A[i] // factor) % BUCKETS
            queues[bucket_index].put(A[i])
            num_data += 1  # 데이터 이동: A[i] -> 큐

        i = 0
        # 각 큐에서 데이터를 꺼내 배열로 합친다
        
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[i] = queues[b].get()
                num_data += 1  # 데이터 이동: 큐 -> A[i]
                i += 1

        factor *= 10  # 다음 자릿수로 이동		



while True :
    
    print("[메뉴선택] 1-입력, 2-매크로, 0-종료")
    command = input("[정렬선택]s-SEL, i-INS, b-BUB, S- SHELL, h-HEAP, m-MERGE, q-QUI, r-RAD => ")

    if command == '0' : exit()

    elif command == '2' :
        print("입력한 값: [5, 8, 1, 3, 4]")
        data_list = [5, 8, 1, 3, 4]

    elif command == '1' :
        data_list = [*map(int, input("데이터 리스트를 입력하세요:").split(', '))]


    elif command == 'S' :
        shell_sort(data_list)
    
    elif command == 's' :
        selection_sort(data_list)
        
    elif command == 'i' :
        insertion_sort(data_list)
        
    elif command == 'b' :
        bubble_sort(data_list)
        
    elif command == 'h' :
        heapSort(data_list)
        print_result(data_list)
        
    elif command == 'm' :
        merge_sort(data_list, 0, len(data_list)-1)
        print_result(data_list)

    elif command == 'q' :
        quick_sort(data_list, 0, len(data_list)-1)
        print_result(data_list)

    elif command == 'r' :
        radix_sort(data_list)
        print_result(data_list)

    else :
        print("없는 커맨드입니다")
    print()
    
    print("==========================================")
    dataReset()

    
