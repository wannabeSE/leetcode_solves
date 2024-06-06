class Solution {
  bool searchMatrix(List<List<int>> matrix, int target) {
    int rows = matrix.length;
    int cols = matrix[0].length;
    int topPointer = 0;
    int bottomPointer = rows - 1;

    while (topPointer <= bottomPointer) {
      int currRow = (topPointer + bottomPointer) ~/ 2;
      if (target > matrix[currRow].last) {
        topPointer = currRow + 1;
      } else if (target < matrix[currRow].first) {
        bottomPointer = currRow - 1;
      } else {
        break;
      }
    }
    if (!(topPointer <= bottomPointer)) {
      return false;
    }
    
    int row = (topPointer + bottomPointer) ~/ 2;
    int l = 0;
    int r = cols - 1;

    while (l <= r) {
      int mid = (l + r) ~/ 2;
      if (target > matrix[row][mid]) {
        l = mid + 1;
      } else if (target < matrix[row][mid]) {
        r = mid - 1;
      } else {
        return true;
      }
    }
    return false;
  }
}

void main(List<String> args) {
  Solution s = Solution();
  print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3));
}
