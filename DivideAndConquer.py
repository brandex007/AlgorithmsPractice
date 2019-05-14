def findMaxCrossing(A, low, mid, high):
    leftSum = -100
    rightSum = -100
    sum = 0
    i = mid
    maxLeft = 0
    maxRight = 0
    while i >= low:
        sum += A[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
        i = i - 1

    i = mid + 1
    sum = 0
    while i <= high:
        sum += A[i]
        if sum > rightSum:
            rightSum = sum
            maxRight = i
        i = i + 1

    return maxLeft, maxRight, leftSum + rightSum;


def divideAndConquer(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = (low + high) / 2
        leftLow, leftHigh, leftSum = divideAndConquer(A,low,mid)
        rightLow, rightHigh, rightSum = divideAndConquer(A,mid+1,high)
        crossLow, crossHigh, crossSum = findMaxCrossing(A,low,mid,high)

    if leftSum >= rightSum and leftSum >= crossSum:
        return leftLow, leftHigh, leftSum
    elif rightSum >= leftSum and rightSum >= crossSum:
        return rightLow, rightHigh, rightSum
    else:
        return crossLow, crossHigh, crossSum

A = [1,-3,4,0,2]
result = divideAndConquer(A,0,4)

print result