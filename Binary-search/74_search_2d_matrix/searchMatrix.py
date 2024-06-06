def searchMatrix(matrix: list[list[int]], target) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    topPointer, bottomPointer = 0, rows - 1
    while topPointer <= bottomPointer:
        currRow = (topPointer + bottomPointer ) // 2
        if target > matrix[currRow][-1]:
            topPointer = currRow + 1
        elif target < matrix[currRow][0]: 
            bottomPointer = currRow - 1
        else:
            break
    if not (topPointer <= bottomPointer):
        return False
    row = (topPointer + bottomPointer) // 2
    l, r = 0, cols - 1
    while l <= r:
        mid = (l + r) // 2
        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid - 1
        else:
            return True
    return False
print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))