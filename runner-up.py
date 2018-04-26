if __name__ == '__main__':
    n = int(input())
    arr =list( map(int, input().split()))


    arr.sort(reverse=True)
    if arr[0] != arr[1]:
        print(arr[1])
    else:
        for i in range(n):
            if arr[0]!=arr[i]:
                print(arr[i])
                break

