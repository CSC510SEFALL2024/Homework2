import rand


def mergeSort(arr):
    if (len(arr) == 1):
        return arr

    half = len(arr)//2

    return recombine(mergeSort(arr[:half]), mergeSort(arr[half:]))


def recombine(leftArr, rightArr):
    leftIndex = 0
    rightIndex = 0
    mergeArr = [None] * (len(leftArr) + len(rightArr))
    while leftIndex < len(leftArr) and rightIndex < len(rightArr):
        if leftArr[leftIndex] < rightArr[rightIndex]:
            rightIndex += 1
            mergeArr.append(leftArr[leftIndex])
        else:
            leftIndex += 1
            mergeArr.append(rightArr[rightIndex])

    mergeArr.extend(rightArr[rightIndex:])
    mergeArr.extend(leftArr[leftIndex:])

    return mergeArr


arr = rand.random_array([None] * 20)
arr_out = mergeSort(arr)

print(arr_out)
