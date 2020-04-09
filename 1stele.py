n = int(input("Enter the number of elements in the array \n"))
arr = []
count = 0

print("Enter the elements in the array:")
for i in range(n):
    ele = int(input())
    arr.append(ele)
print("The list inserted is: ", arr)

for i in arr:
    if count == n-1:
            print("-1")
            break

    if i != arr[count+1]:   
        count = count+1
    else:
        print("The duplicate element in the list is: ",i)
        break
