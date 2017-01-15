from DS.Stack.ArrayStack import ArrayStack
def transfer(S,T):
    while not S.is_empty():
        T.push(S.pop())

def empty(S):
    if not S.is_empty():
        S.pop()
        empty(S)

def reverse(S,L):
    for e in L:
        S.push(e)
    i = 0
    while not S.is_empty():
        L[i] = S.pop()
        i+=1

if __name__ == "__main__":
    L = [1,2,3,4,5]
    S = ArrayStack()
    reverse(S,L)
    print(' '.join(str(e) for e in L))
    # T = ArrayStack()
    # for i in range(10):
    #     S.push(i)
    empty(S)
    print(S.is_empty())
    # transfer(S,T)
    # for i in range(10):
    #     print(T.pop())
