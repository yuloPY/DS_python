arr = [0,1,2,31,45,62,93,155]

def linerarSearch(array,targetVal):
    for i in range(len(array)):
        if array[i] == targetVal:
            return i
        else:
            return -1

result = linerarSearch(arr,31)

if result != -1:
    print("Value",targetVal,"found at index",result)
else:
    print("Value",targetVal,"not found")