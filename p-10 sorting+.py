
num_data = 0
num_com = 0
swap = 0



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



# INS
def selection_sort(A) :
    global num_data
    global num_com
    
    n = len(A)
    for i in range(n-1) :
        least = i;
        for j in range(i+1, n) :
            num_com += 1
            if (A[j]<A[least]) :
                least = j
        A[i], A[least] = A[least], A[i]
        swap += 1
        num_data += 3
    print('Sorted : ',A)
    print('Number of comparisions :', num_com)
    print('Number of data movements :', num_data)



# sort

def insertion_sort(A) :
    
    global num_data
    global num_com
    n = len(A)
    for i in range(1, n) :
        key = A[i]
        j = i-1
        while j>=0 and A[j] > key :
            num_com += 1
            A[j + 1] = A[j]
            num_data += 1
            j -= 1
        A[j + 1] = key
        num_data += 1
    print('Sorted : ',A)
    print('Number of comparisions :', num_com)
    print('Number of data movements :', num_data)



# 코드 7.3: 버블 정렬 알고리즘        참고 파일: ch07/basic_sort.py
def bubble_sort(A) :
    n = len(A)
    for i in range(n-1, 0, -1) :
        bChanged = False
        for j in range (i) :
            if (A[j]>A[j+1]) :
                A[j], A[j+1] = A[j+1], A[j] 
                bChanged = True

        if not bChanged: break;			# 교환이 없으면 종료




# 최대힙

def heapify(arr, n, i): 
    largest = i         # Initialize largest as root 
    l = 2 * i + 1       # left = 2*i + 1 
    r = 2 * i + 2       # right = 2*i + 2 
  
    if l < n and arr[i] < arr[l]: largest = l 
    if r < n and arr[largest] < arr[r]:  largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        heapify(arr, n, largest) 
  
# 코드 12.5: 제자리 정렬로 구현된 힙 정렬
def heapSort(arr): 
    n = len(arr) 
  
    print("i=", 0, arr)
    for i in range(n//2, -1, -1): 
        heapify(arr, n, i) 
        print("i=", i, arr)
  
    print()
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 
        print("i=", i, arr)


#merge

sorted = [0]*100

def merge_sort(A, left, right) :
	if left<right :
		mid = (left + right) // 2		# 리스트의 균등 분할
		merge_sort(A, left, mid)		# 부분 리스트 정렬
		merge_sort(A, mid + 1, right)	# 부분 리스트 정렬
		merge(A, left, mid, right)	    # 병합


# 코드 12.7: 병합 정렬을 위한 merge() 함수
def merge(A, left, mid, right) :
    global sorted
    k = left			# k는 정렬될 리스트에 대한 인덱스
    i = left
    j = mid + 1
    while i<=mid and j<=right :
        if A[i] <= A[j] :
            sorted[k] = A[i]
            i, k = i+1, k+1
            #i += 1
            #k += 1
        else:
            sorted[k] = A[j]
            j, k = j+1, k+1
            #j += 1
            #k += 1
	# 한쪽에 남아 있는 레코드의 일괄 복사
    if i > mid :
        sorted[k:k+right-j+1] = A[j:right+1]
    else :
        sorted[k:k+mid-i+1] = A[i:mid+1]
	# 배열 sorted[]의 리스트를 배열 list[]로 다시 복사
    A[left:right+1] = sorted[left:right+1]





# 퀵 정렬 알고리즘을 이용해 배열의 left ~ right 항목들을 오름차순으로 정렬하는 함수
def quick_sort(A, left, right) :
	if left<right :						    # 정렬 범위가 2개 이상인 경우
		q = partition(A, left, right)	    # 좌우로 분할 
		quick_sort(A, left, q - 1)		    # 왼쪽 부분리스트를 퀵 정렬
		quick_sort(A, q + 1, right)	    # 오른쪽 부분리스트를 퀵 정렬


# 코드 12.9: 퀵 정렬을 위한 partition() 함수
def partition(A, left, right) :
	low = left + 1
	high = right
	pivot = A[left] 		# 피벗 설정 
	while (low < high) :	# low와 high가 역전되지 않는 한 반복 
	    while low <= right and A[low] < pivot : low += 1
	    while high >= left and A[high]> pivot : high-= 1

	    if low < high :	# 선택된 두 레코드 교환 
	        A[low], A[high] = A[high], A[low]

	A[left], A[high] = A[high], A[left]	    # high와 피벗 항목 교환 
	return high




from queue import Queue
from collections import deque

def printStep(arr, val) :
    print("step%2d " % val, end='')
    print(arr)


# 코드 12.12: 기수 정렬
def radix_sort(A) :
    queues = []
    for i in range(BUCKETS) :
        queues.append(Queue())

    n = len(A)
    factor = 1
    for d in range(DIGITS) :
        for i in range(n) : 	            # 자릿수에 따라 큐에 삽입
            queues[(A[i]//factor) % BUCKETS].put(A[i])

        i = 0
        for b in range(BUCKETS) :		    # 버킷에서 꺼내어 list로 합친다.
            while not queues[b].empty() :
                A[i] = queues[b].get()
                i += 1
        factor *= 10					    # 그 다음 자리수로 간다.
        printStep(A, d + 1)			        # 중간 과정 출력용 문장




'''
ex)  5, 8, 1, 3, 4
sorted : 1,3,4,5,8
number of comparisions : 8
Number of data movements : 26
'''


while True :
    num_data = 0
    num_com = 0
    swap = 0
    
    command = input("[메뉴선택]M-매크로,i-입력 s-SEL, I -INS, b-BUB, S- SHELL, h-HEAP, m-MERGE, q-QUI, r-RAD, Q-QUIT => ")

    if command == 'Q' : exit()

    elif command == 'M' :
        data_list = [5, 8, 1, 3, 4]

    elif command == 'i' :
        data_list = input("데이터 리스트를 입력하세요:").split(', ')

    elif command == 'S' :
        shell_sort(data_list)
    
    elif command == 's' :
        selection_sort(data_list)
        
    elif command == 'I' :
        insertion_sort(data_list)
        
    elif command == 'b' :
        bubble_sort(data_list)
        
    elif command == 'h' :
        heapSort(data_list)
        
    elif command == 'm' :
        merge_sort(data_list, 0, len(data_list)-1)

    elif command == 'q' :
        quick_sort(data_list, 0, len(data_list)-1)

    elif command == 'r' :
        radix_sort(data_list)

    else :
        print("없는 커맨드입니다")
    print()
    print("==========================================")

    
