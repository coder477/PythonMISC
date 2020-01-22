''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT


def findLargestSumPair(arr, n): 

    
    print(arr)

    if arr[0] > arr[2]: 
        first = arr[0] 
        second = arr[2] 
    
    else: 
        first = arr[2] 
        second = arr[0] 

    for i in range(2, n): 

        if arr[i] > first and second!=first: 
            second = first 
            first = arr[i] 

        elif arr[i] > second and arr[i] != first and second!=first: 
            second = arr[i] 
    if(max(arr)>(first+second)):
        return max(arr)
    
    if(first<second):
        return (str(first)+" , "+str(second))
    else:
        return (str(second)+" , "+str(first))

    return (str(second)+" , "+str(first))

if __name__ == "__main__":  
    print("Size of cases")  
    cases=int(input())
    arr = []
    i=0
    print("input cases")
    while (i<2*cases):
        line = input()
        arr.append(int(line))
        i=i+1
    print(findLargestSumPair(arr, len(arr)))
        

    


