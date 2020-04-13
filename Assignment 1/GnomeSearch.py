lists=[]
i = 1
flag = True 

def gnome():
    global lists
    global i
    global flag
    i = 1
    while flag:
        if lists[i] < lists[i-1]:
            swap(i)
            # print("Swap-- ", lists)
            if i != 1:
                i = i-1
                # print("DEC--", i)

        elif i != n:
            # print("INC-- ", i) 
            i = i+1   
            
        
        if i == n:
            flag = False
        
    print("Sorted List: ",lists)
           

def swap(i):
    temp = lists[i]
    lists[i] = lists[i-1]
    lists[i-1] = temp
    # print("Swap in ", lists)
    return

n = int(input("\n Enter the number of elements in the array \n"))

print("\n Enter the element \n")
for i in range(n):
    ele = int(input())
    lists.append(ele)
print("Inserted list: ",lists)

gnome()

