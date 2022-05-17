def fibNum (n):
    if n <= 1:
        return n
    prev = 0
    current = 1
    sum = 1
    for i in range (n-1):
        prev, current = current%10, (current+prev)%10
        sum = (sum + current)%10
    return sum


if __name__ == '__main__':
    n=int(input())
    print(fibNum(n))