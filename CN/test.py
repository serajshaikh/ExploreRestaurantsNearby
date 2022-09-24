""" def sort012(arr,n):
        i=0
        j=0
        while j<n:
            if arr[j]==0:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
                i+=1
                j+=1
            else:
                j+=1
        j=n-1
        i=n-1
        print(arr)
        while j>=0:
            if arr[j]==2:
                arr[i],arr[j]=arr[j],arr[i]
                i-=1
                j-=1
            else:
                j-=1
        return arr

n=int(input())
arr=list(map(int, input().split()))
print(sort012(arr,n)) """

def contInversion(arr,n):
    cnt=0
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            # print(arr[j],end=" ")
            if arr[j]>arr[i]:
                cnt +=1
        # print()
        # print(arr[i],end=" ")
    return cnt


cnt =contInversion([2, 3, 4, 5, 6],5)
print(cnt)