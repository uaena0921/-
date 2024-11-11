from BinaryTree import *
from BinSrchTree import *

def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

# 코드 9.13: 노드의 균형인수 계산 함수
def calc_height_diff(n) :
    if n==None :
       return 0
    return calc_height(n.left) - calc_height(n.right)


'''
# 코드 9.14: AVL 트리의 LL회전    수정 
def rotateLL(A) :
    B = A.left
    if calc_height_diff( B.left ) > 0 :
        A.left = B.right
        B.right = A
    else:
        A.left = B.left
        B.left = A
    return B
            

# 코드 9.15: AVL 트리의 RR회전    수정 
def rotateRR(A) :
    B = A.right
    if(calc_height(B.left) < calc_height(B.right)):
        A.right = B.left
        B.left = A
    else:
     	A.right = B.right
     	B.right = A   
    return B
'''
def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B


def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

# 코드 9.16: AVL 트리의 RL회전
def rotateRL(A) :
	B = A.right
	A.right = rotateLL(B)
	return rotateRR(A)

# 코드 9.17: AVL 트리의 LR회전
def rotateLR(A) :
	B = A.left
	A.left = rotateRR(B)
	return rotateLL(A)

# 코드 9.18: AVL 트리의 재균형 함수
def reBalance (parent) :
	hDiff = calc_height_diff(parent)

	if hDiff > 1 :
		if calc_height_diff( parent.left ) > 0 :
			parent = rotateLL( parent )
		else :
			parent = rotateLR( parent )
	elif hDiff < -1 :
		if calc_height_diff( parent.right ) < 0 :
			parent = rotateRR( parent )
		else :
			parent = rotateRL( parent )
	return parent

# 코드 9.19: AVL 트리의 삽입 연산
def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None :
            parent.left = insert_avl(parent.left, node)
        else :
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None :
            parent.right = insert_avl(parent.right, node)
        else :
            parent.right = node
        return reBalance(parent);
    else :
        print("중복된 키 에러")


        
#과제: 삭제 연산 (무조건 최소값)

def delete_min_avl(root):
    if root is None:
        return None, None  # 트리가 비어 있을 경우
    
    # 최소값 삭제: 왼쪽 서브트리가 None인 경우
    if root.left is None:
        deleted_key = root.key  # 삭제된 최소값 저장
        return root.right, deleted_key 
    
    # 왼쪽 자식을 탐색하여 최소값을 찾고 삭제
    root.left, deleted_key = delete_min_avl(root.left)
    
    return reBalance(root), deleted_key




#예제
from CircularQueue import CircularQueue

def levelorder(root) :
    queue = CircularQueue(100)
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.key, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)




# 코드 9.20: AVL 트리 테스트 프로그램
if __name__ == "__main__":
    node = [7,8,9,2,1,5,3,6,4]
    #node = [3, 4, 5, 1, 2, 1, 7, 9]

    root = None
    for i in node :
        n = BSTNode(i)
        if root == None :
            root = n
        else :
           root = insert_avl(root, n)

        print("AVL(%d): "%i, end='')
        levelorder(root)
        print()

    print(" 노드의 개수 =", count_node(root))
    print(" 단말의 개수 =", count_leaf(root))
    print(" 트리의 높이 =", calc_height(root))
    print("삭제 시작")

    #delete 위해 추가
    for _ in range(len(node)):
        root, deleted_key = delete_min_avl(root) 
        if deleted_key is not None:
            print(f"삭제된 값: {deleted_key}")
        print("AVL (삭제 후):", end=' ')
        if root:  
            levelorder(root)
        else:
            print("트리가 비어 있습니다.")
        print()
